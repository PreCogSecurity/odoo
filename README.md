[![Build Status](http://runbot.odoo.com/runbot/badge/flat/1/9.0.svg)](http://runbot.odoo.com/runbot)
[![Tech Doc](http://img.shields.io/badge/9.0-docs-8f8f8f.svg?style=flat)](http://www.odoo.com/documentation/9.0)
[![Help](http://img.shields.io/badge/9.0-help-8f8f8f.svg?style=flat)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/9.0-nightly-8f8f8f.svg?style=flat)](http://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>, <a href="https://www.odoo.com/page/website-builder">Website Builder</a>, <a href="https://www.odoo.com/page/e-commerce">eCommerce</a>, <a href="https://www.odoo.com/page/project-management">Project Management</a>, <a href="https://www.odoo.com/page/accounting">Billing &amp; Accounting</a>, <a href="https://www.odoo.com/page/point-of-sale">Point of Sale</a>, <a href="https://www.odoo.com/page/employees">Human Resources</a>, Marketing, Manufacturing, Purchase Management, ...  

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.


Getting started with Odoo
-------------------------
For a standard installation please follow the <a href="https://www.odoo.com/documentation/9.0/setup/install.html">Setup instructions</a>
from the documentation.

### Quick Start with Docker & Docker Compose (Recommended)
To run Odoo along with PostgreSQL in an isolated environment without manual dependency management:

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Access the Odoo web interface at `http://localhost:8069`.

### Local Developer Setup
If you are a developer running locally with Python 2.7 and PostgreSQL:

1. Install system requirements (PostgreSQL, libxml2, libxslt, libldap):
   ```bash
   sudo apt-get install libpq-dev libxml2-dev libxslt1-dev libldap2-dev
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your environment variables (see `.env.example`).
4. Run the development server:
   ```bash
   python odoo.py
   ```

### Running Tests
Odoo includes a test suite that can be run against any database using the test runner:
```bash
python odoo.py -d test_db --test-enable --stop-after-init -i base,mass_mailing,lunch
```

### Architecture Overview
- **Core ORM (`openerp/models.py`)**: Object-Relational Mapping engine providing model definitions, fields, security rules, and inheritance.
- **Addons (`addons/`)**: Modular business applications (CRM, Sales, Accounting, Inventory, Website, Mass Mailing, etc.) extending the core framework.
- **View Engine**: QWeb-based rendering engine for dynamic views, forms, and web interfaces.
- **Security & Access Control**: Granular Access Control Lists (`ir.model.access.csv`) and Record Rules enforced at the ORM layer.

