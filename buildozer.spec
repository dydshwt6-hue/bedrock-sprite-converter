[app]

title = Bedrock Sprite Converter
package.name = bedrocksprite
package.domain = org.yourdomain

source.dir = .
source.include_exts = py,png,jpg,ttf,json

version = 0.1
requirements = python3,kivy,opencv-python,pillow,plyer

orientation = portrait
fullscreen = 1

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.sdk_version = 33
android.ndk_version = 23b
android.build_tools_version = 33.0.0
android.gradle_dependencies = 
android.enable_androidx = True
android.openssl = True

[buildozer]
log_level = 2
warn_on_root = 1 
