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


## Sprint 5: User Registration & JWT Authentication

Status: In Progress

Completed:
- Installed Simple JWT
- Configured JWT authentication
- Created registration serializer
- Created registration API endpoint
- Connected accounts API URLs

---

## Sprint 5: Authentication System
**Status:** ✅ Completed

### Completed Tasks
- Installed Django Simple JWT
- Configured JWT authentication
- Created user registration API
- Created login endpoint
- Created token refresh endpoint
- Added protected profile endpoint
- Tested authenticated requests

### Authentication Flow

User registers → Database → Login → JWT Tokens → Protected APIs

### Next Sprint

- Create Income model
- Create Income API
- Connect income records to authenticated users

---

## Sprint 6: Income Management
**Status:** ✅ Completed

### Completed Tasks
- Created Income model
- Linked income records to users
- Added income source choices
- Created Income serializer
- Built Income CRUD API
- Added JWT protected income endpoints
- Tested API using Postman

### API Endpoints

POST   /api/income/
GET    /api/income/
GET    /api/income/<id>/
PUT    /api/income/<id>/
DELETE /api/income/<id>/

### Next Sprint
- Build Expense Management module

## Sprint 8: Dashboard & Budget Engine
Status: ✅ Completed

Features Added:
- Created dashboard application
- Added financial summary API
- Calculated total income
- Calculated total expenses
- Calculated remaining balance
- Added income and expense record counts
- Secured dashboard endpoint with JWT authentication
- Verified user data isolation

Endpoint:
GET /api/dashboard/summary/

Next Sprint:
Savings Goals Management

## Sprint 9: Savings Goals Management
**Status:** ✅ Completed

### Features Added
- Created Savings Goals module.
- Added SavingsGoal database model.
- Added savings CRUD API.
- Secured endpoints using JWT authentication.
- Implemented user-specific savings goals.
- Added automatic progress calculation.
- Added savings goal status tracking.

### API Endpoint

/api/savings/

### Calculations

Progress:
(current_amount / target_amount) × 100

Progress is capped at 100%.

### Goal Status

0-24%:
Starting

25-74%:
In Progress

75-99%:
Almost There

100%:
Completed

### Security Testing

Verified users can only access their own savings goals.

### Next Sprint

## Sprint 10: Advanced Reports & Analytics
Status: ✅ Completed

Features Added:

- Created Reports API.
- Added financial summary calculations.
- Added total income analysis.
- Added total expense analysis.
- Added savings analysis.
- Added expense category breakdown.
- Added saving rate calculation.
- Added expense ratio calculation.
- Added financial health score.

Reports Endpoint:

GET /api/reports/summary/

Analytics Included:

- Income vs expenses
- Savings performance
- Spending categories
- Financial health classification

## Sprint 11: Budget Limits & Smart Alerts

**Status:** ✅ Completed

### Features Added

* Created Budget Management module.
* Added Budget model for user-defined spending limits.
* Implemented Budget CRUD API.
* Added JWT authentication protection.
* Added user-specific budget filtering.
* Implemented dynamic budget alerts.

### Budget API Endpoints

Create Budget:

POST `/api/budgets/`

View Budgets:

GET `/api/budgets/`

Update Budget:

PUT `/api/budgets/{id}/`

Delete Budget:

DELETE `/api/budgets/{id}/`

### Smart Budget Alerts

Implemented calculated alerts without storing notifications in the database.

Alert system compares:

Budget Limit vs Actual Expenses

Alert Levels:

* Safe: Spending below 80% of budget.
* Warning: Spending between 80% and 100% of budget.
* Exceeded: Spending above the budget limit.

Alert Endpoint:

GET `/api/budgets/alerts/`

### Security Testing

Verified that:

* Users can only access their own budgets.
* Budget alerts are generated based on the authenticated user's expenses.

### Next Sprint

## Sprint 12: Dashboard API Integration
Status: ✅ In Progress

### Completed

- Created dashboard application.
- Implemented dashboard API endpoint.
- Added JWT authentication.
- Integrated financial summary data.
- Added recent expenses retrieval.
- Added savings goal progress information.

Endpoint:

GET /api/dashboard/

Purpose:

Provides a single API endpoint containing the information required by the user dashboard.

## Sprint 12 Part 2: Service Layer Refactor
Status: ✅ Completed

### Completed

- Created reports service layer.
- Moved financial calculations from views.py to services.py.
- Updated FinancialSummaryView to use service functions.
- Updated Dashboard API to use shared financial calculation logic.
- Removed view-to-view dependency.

### Benefits

- Improved code maintainability.
- Reduced duplication.
- Created reusable business logic layer.
