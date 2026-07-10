import sys
import subprocess
import os

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package} module...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure pypdf is installed
install_and_import('pypdf')

from pypdf import PdfWriter

def merge_pdfs():
    merger = PdfWriter()
    
    cv_path = os.path.join("documents", "cv.pdf")
    certs_path = os.path.join("documents", "certs.pdf")
    output_path = "Nyasha_Mapetere_Full_Application.pdf"
    
    # 1. Append CV
    try:
        merger.append(cv_path)
        print(f"[*] Added CV: {cv_path}")
    except FileNotFoundError:
        print(f"\n[ERROR] Could not find {cv_path}!")
        print("-> Please open your cv.html in the browser, click 'Save as PDF', and save it as 'cv.pdf' inside the 'documents' folder.")
        print("-> After doing that, run this script again.\n")
        return
        
    # 2. Append Certificates
    try:
        merger.append(certs_path)
        print(f"[*] Added Certificates: {certs_path}")
    except FileNotFoundError:
        print(f"\n[ERROR] Could not find {certs_path}!")
        return
        
    # 3. Write merged file
    merger.write(output_path)
    merger.close()
    
    print(f"\n[SUCCESS] Successfully merged! Created final PDF at: {os.path.abspath(output_path)}\n")

if __name__ == "__main__":
    merge_pdfs()
