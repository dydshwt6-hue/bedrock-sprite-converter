[app]

title = Bedrock Sprite Converter
package.name = bedrocksprite
package.domain = org.yourdomain

source.dir = .
source.include_exts = py,png,jpg,ttf,json

version = 0.1
requirements = python3,kivy,opencv-python,pillow

orientation = portrait
fullscreen = 1

# أذونات هواوي
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.gradle_dependencies = 
android.enable_androidx = True
android.openssl = True

# إضافات خاصة بهواوي
android.extra_manifest = 
    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
    <uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />

[buildozer]
log_level = 2
warn_on_root = 1 
