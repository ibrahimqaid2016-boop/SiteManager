[app]

title = Telecom Site Manager
package.name = telecomsitemanager
package.domain = org.telecom

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,db,json,ttf
source.exclude_dirs = .git,.github,__pycache__,bin,.buildozer

version = 1.0.0
requirements = python3,kivy==2.3.1,openpyxl,plyer,pyjnius

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True

p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
