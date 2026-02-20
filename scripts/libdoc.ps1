# libdoc.ps1 – Generate Robot Framework Libdoc HTML
# Usage: .\scripts\libdoc.ps1

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = Split-Path $PSScriptRoot -Parent
Push-Location $root

Write-Host "=== Generate Libdoc ===" -ForegroundColor Cyan

$libModule = "okw_web_selenium.library.OkwWebSeleniumLibrary"
$outFile   = "docs/OkwWebSeleniumLibrary.html"

if (-not (Test-Path docs)) { New-Item -ItemType Directory -Path docs | Out-Null }

Write-Host "Generating $outFile ..." -ForegroundColor Yellow
python -m robot.libdoc $libModule $outFile

Write-Host ""
Write-Host "Libdoc written to $outFile" -ForegroundColor Green

Pop-Location
