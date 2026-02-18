[app]
# (str) Title of your application
title = SciencePortal

# (str) Package name
package.name = scienceportal

# (str) Package domain (needed for android packaging)
package.domain = org.achiko

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# (list) Application requirements
# შენი აპლიკაციისთვის საჭირო ბიბლიოთეკები
requirements = python3,kivy

# (str) Custom source folders for requirements
# (list) Garden requirements
# (str) Presplash of the application
# (str) Icon of the application

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# თუ ინტერნეტი გჭირდება, ეს ხაზი დატოვე
android.permissions = INTERNET

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Accept SDK license
# ეს აუცილებელია, რომ რობოტი არ გაჩერდეს!
android.accept_sdk_license = True

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Android architecture to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables Android auto backup
android.allow_backup = True

[buildozer]
# (int) log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1
