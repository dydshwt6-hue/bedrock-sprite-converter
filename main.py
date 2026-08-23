name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          build-essential ccache git libffi-dev libssl-dev libltdl-dev \
          python3-setuptools python3-pip libsqlite3-dev zlib1g-dev \
          openjdk-17-jdk zip unzip
        pip install --upgrade pip
        pip install buildozer cython==0.29.33

    - name: Accept Android SDK Licenses
      run: |
        yes | ~/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager --licenses || true
        yes | ~/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager --update || true

    - name: Build with Buildozer
      run: |
        buildozer android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: bedrocksprite-apk
        path: bin/*.apk 
