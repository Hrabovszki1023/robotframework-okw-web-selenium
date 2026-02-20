# publish.ps1 – Upload dist/ to PyPI
# Usage: .\scripts\publish.ps1

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = Split-Path $PSScriptRoot -Parent
Push-Location $root

Write-Host "=== Publish to PyPI ===" -ForegroundColor Cyan

if (-not (Test-Path dist)) {
    Write-Host "ERROR: dist/ not found. Run build.ps1 first." -ForegroundColor Red
    Pop-Location
    exit 1
}

Write-Host "Uploading via twine ..." -ForegroundColor Yellow
python -m twine upload dist/*

Write-Host ""
Write-Host "Published to PyPI." -ForegroundColor Green

Pop-Location
