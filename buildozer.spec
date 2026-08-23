[app]

title = Bedrock Sprite Converter
package.name = bedrocksprite
package.domain = org.yourdomain

source.dir = .
source.include_exts = py,png,jpg,ttf,json

version = 0.1
requirements = python3,kivy,opencv,pillow

orientation = portrait
fullscreen = 1

android.archs = arm64-v8a

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.enable_androidx = True

[buildozer] 
log_level = 2
warn_on_root = 1
