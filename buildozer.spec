[app]
title = JokesApp
package.name = jokesapp
package.domain = org.example
source.include_exts = py,kv,json
source.dir = .
entrypoint = main.py
requirements = python3,kivy
version = 1.0.0
# استخدم نسخة Build-Tools ثابتة لتجنب مشاكل الترخيص
android.build_tools_version = 33.0.2
