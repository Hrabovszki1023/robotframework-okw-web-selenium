# build.ps1 – Build distribution packages (wheel + sdist)
# Usage: .\scripts\build.ps1

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = Split-Path $PSScriptRoot -Parent
Push-Location $root

Write-Host "=== Build distribution packages ===" -ForegroundColor Cyan

if (Test-Path dist) {
    Write-Host "Cleaning old dist/ ..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force dist
}

Write-Host "Building wheel + sdist ..." -ForegroundColor Yellow
python -m build

Write-Host ""
Write-Host "Artifacts:" -ForegroundColor Green
Get-ChildItem dist

Pop-Location
