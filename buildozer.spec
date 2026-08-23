[app]

# (str) Title of your application
title = Bedrock Sprite Converter

# (str) Package name
package.name = bedrocksprite

# (str) Package domain (needed for android packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,ttf,json

# (str) Application version
version = 0.1

# (list) Application requirements
# ملاحظة: تم استخدام opencv بدلاً من opencv-python لتوافقها مع android
requirements = python3,kivy,opencv,pillow

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Specific build tools version to avoid Aidl missing errors
android.sdk_build_tools_version = 33.0.2

# (bool) Auto-accept SDK licenses
android.accept_sdk_license = True

# (list) The Android archs to build for
# تم تحديد معمارية واحدة لمنع استهلاك الذاكرة وتجاوز الوقت
android.archs = arm64-v8a

# (bool) Enable AndroidX
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
