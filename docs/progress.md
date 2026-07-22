# Family Budget Tracker - Development Progress

## Sprint 1: Project Setup
**Status:** ✅ Completed

### Completed Tasks
- Created GitHub repository
- Initialized Git repository
- Created project folder structure
- Added README.md
- Added .gitignore
- Created backend, frontend and docs folders

---

## Sprint 2: Django Backend Setup
**Status:** ✅ Completed

### Completed Tasks
- Created Python virtual environment
- Activated virtual environment
- Installed Django
- Installed Django REST Framework
- Installed psycopg2-binary
- Installed python-decouple
- Created requirements.txt
- Created Django project (config)
- Successfully ran the Django development server
- Created the accounts app
- Created the remaining Django apps
- Registered all apps in settings.py

---

## Current Status

Backend foundation is complete.

Next step:
- Configure PostgreSQL
- Create custom user model
- Design database models

---

## Sprint 3: Project Architecture & Database Design
**Status:** ✅ Completed

### Completed Tasks
- Planned the application architecture
- Identified core entities
- Designed database tables
- Defined relationships between entities
- Created `database-design.md`
- Planned the MVP features
- Created the project roadmap

---

## Sprint 4: Authentication Foundation
**Status:** ✅ Completed

### Completed Tasks
- Created a custom user model (`CustomUser`)
- Added phone number field
- Added profile picture field
- Added preferred currency support
- Added created_at and updated_at timestamps
- Configured Django to use the custom user model
- Installed Pillow for image support
- Successfully created and applied migrations
- Created Django superuser
- Verified Django Admin access

---

## Challenges Encountered

### PowerShell Execution Policy
PowerShell prevented activation of the virtual environment.

**Solution**
Changed the execution policy to `RemoteSigned` for the current user.

### Pillow Dependency
Django raised an error because `ImageField` requires Pillow.

**Solution**
Installed Pillow using:

```bash
python -m pip install Pillow
```

---

## Lessons Learned

- Why virtual environments are important
- How Django's custom authentication works
- Why dependencies like Pillow are required
- How Django migrations create database tables
- Importance of planning before coding

---

## Next Sprint

- Build user registration API
- Build login API
- Configure JWT authentication
- Test authentication endpoints