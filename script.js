document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const form = document.getElementById('travelForm');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const travelPlan = document.getElementById('travelPlan');
    const newPlanBtn = document.getElementById('newPlanBtn');
    const interestTags = document.querySelectorAll('.interest-tag');
    const interestsTextarea = document.getElementById('interests');

    // Handle interest tag selection
    let selectedInterests = [];

    interestTags.forEach(tag => {
        tag.addEventListener('click', function() {
            const interest = this.dataset.interest;
            
            if (this.classList.contains('selected')) {
                // Remove interest
                this.classList.remove('selected');
                selectedInterests = selectedInterests.filter(i => i !== interest);
            } else {
                // Add interest
                this.classList.add('selected');
                selectedInterests.push(interest);
            }
            
            // Update textarea
            updateInterestsTextarea();
        });
    });

    function updateInterestsTextarea() {
        const currentText = interestsTextarea.value;
        const tagText = selectedInterests.join(', ');
        
        if (selectedInterests.length > 0) {
            if (currentText && !currentText.includes(tagText)) {
                interestsTextarea.value = tagText + (currentText ? ', ' + currentText : '');
            } else if (!currentText) {
                interestsTextarea.value = tagText;
            }
        }
    }

    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(form);
        const data = {
            source: formData.get('source').trim(),
            destination: formData.get('destination').trim(),
            dates: formData.get('dates').trim(),
            budget: formData.get('budget'),
            travelers: formData.get('travelers'),
            interests: formData.get('interests').trim()
        };

        // Validate form data
        if (!validateFormData(data)) {
            return;
        }

        // Show loading state
        showLoading();

        try {
            // Send request to backend
            const response = await fetch('/api/generate-plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                // Display the travel plan
                displayTravelPlan(result.travel_plan);
            } else {
                throw new Error(result.error || 'Failed to generate travel plan');
            }

        } catch (error) {
            console.error('Error:', error);
            showError('Failed to generate travel plan. Please check your internet connection and try again.');
        }
    });

    // Validate form data
    function validateFormData(data) {
        const requiredFields = ['source', 'destination', 'dates', 'budget', 'travelers', 'interests'];
        
        for (let field of requiredFields) {
            if (!data[field]) {
                showError(`Please fill in the ${field.replace('_', ' ')} field.`);
                return false;
            }
        }

        if (isNaN(data.budget) || data.budget < 100) {
            showError('Please enter a valid budget (minimum $100).');
            return false;
        }

        return true;
    }

    // Show loading state
    function showLoading() {
        form.style.display = 'none';
        results.classList.add('hidden');
        loading.classList.remove('hidden');
    }

    // Display travel plan
    function displayTravelPlan(planText) {
        loading.classList.add('hidden');
        
        // Format the travel plan text
        const formattedPlan = formatTravelPlan(planText);
        travelPlan.innerHTML = formattedPlan;
        
        results.classList.remove('hidden');
        
        // Scroll to results
        results.scrollIntoView({ behavior: 'smooth' });
    }

    // Format travel plan text with better HTML structure
    function formatTravelPlan(text) {
        // Convert markdown-like formatting to HTML
        let formatted = text
            // Convert **bold** to <strong>
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            // Convert *italic* to <em>
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            // Convert line breaks to <br>
            .replace(/\n/g, '<br>')
            // Convert numbered lists
            .replace(/^(\d+\.\s)/gm, '<br><strong>$1</strong>')
            // Convert bullet points
            .replace(/^[-•]\s/gm, '<br>• ')
            // Convert headers (lines that end with :)
            .replace(/^([A-Z][^<]*:)(<br>|$)/gm, '<h3>$1</h3>')
            // Convert section headers
            .replace(/^(\d+\.\s\*\*[^*]+\*\*)/gm, '<h2>$1</h2>')
            // Clean up multiple <br> tags
            .replace(/(<br>\s*){3,}/g, '<br><br>');

        return formatted;
    }

    // Show error message
    function showError(message) {
        alert(message); // Simple alert for now, could be improved with a custom modal
    }

    // Handle new plan button
    newPlanBtn.addEventListener('click', function() {
        // Reset form
        form.reset();
        selectedInterests = [];
        interestTags.forEach(tag => tag.classList.remove('selected'));
        
        // Show form again
        form.style.display = 'block';
        results.classList.add('hidden');
        loading.classList.add('hidden');
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Add some interactive features
    
    // Auto-resize textarea
    interestsTextarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });

    // Add placeholder animation for inputs
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
        });
    });

    // Add smooth scrolling for better UX
    function smoothScrollTo(element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }

    // Check API health on page load
    checkAPIHealth();

    async function checkAPIHealth() {
        try {
            const response = await fetch('/api/health');
            const result = await response.json();
            console.log('API Health:', result);
        } catch (error) {
            console.warn('API health check failed:', error);
        }
    }
});