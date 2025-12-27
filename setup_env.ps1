# PowerShell helper: create a virtual environment and install requirements
param(
    [string]$VenvName = "venv"
)

Write-Host "Creating virtual environment: $VenvName"
python -m venv $VenvName

Write-Host "Setting execution policy for this session to allow activation"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

Write-Host "Activating virtual environment"
.\$VenvName\Scripts\Activate.ps1

Write-Host "Upgrading pip and installing requirements"
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Setup complete. To activate the venv in a new session run: .\$VenvName\Scripts\Activate.ps1"
