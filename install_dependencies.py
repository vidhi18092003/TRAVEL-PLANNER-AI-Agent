import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        return False

def main():
    print("Installing Travel Planner AI dependencies...")
    print("=" * 50)
    
    packages = [
        "Flask==2.3.3",
        "Flask-CORS==4.0.0", 
        "google-generativeai==0.3.2",
        "python-dotenv==1.0.0",
        "requests==2.31.0"
    ]
    
    failed_packages = []
    
    for package in packages:
        if not install_package(package):
            failed_packages.append(package)
    
    print("\n" + "=" * 50)
    if failed_packages:
        print("❌ Some packages failed to install:")
        for pkg in failed_packages:
            print(f"   - {pkg}")
        print("\nTry installing them manually:")
        for pkg in failed_packages:
            print(f"   pip install {pkg}")
    else:
        print("🎉 All dependencies installed successfully!")
        print("\nYou can now run the application:")
        print("   python backend/app.py")

if __name__ == "__main__":
    main()