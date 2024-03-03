REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'project.permissions.Isadminreadonly',
    ]
}