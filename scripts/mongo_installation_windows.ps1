# Specify installation directory
$installDir = "C:\MongoDB"
$zipFile = "$installDir\mongodb.zip"

# Check if the zip file already exists
if (-Not (Test-Path -Path $zipFile)) {
    # Download MongoDB
    Invoke-WebRequest -Uri "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.27.zip" -OutFile $zipFile
}

# Extract MongoDB directly into the installation directory
Expand-Archive -Path $zipFile -DestinationPath $installDir -Force

# Create data directory
New-Item -ItemType Directory -Path "$installDir\data" -Force

# Create config file
@"
systemLog:
  destination: file
  path: $installDir\mongod.log
storage:
  dbPath: $installDir\data
"@ | Out-File "$installDir\mongod.cfg" -Force

# Install MongoDB as a service
& "$installDir\bin\mongod.exe" --config "$installDir\mongod.cfg" --install

# Set service to autostart
Set-Service MongoDB -StartupType Automatic

# Start MongoDB service
Start-Service MongoDB

# Verify installation
mongo --eval "db.version()"

# Clean up
# Remove-Item "$zipFile" -Force
