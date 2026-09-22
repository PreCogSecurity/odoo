FROM python:2.7-slim

# Install system dependencies required for Odoo 9.0 (lxml, psycopg2, ldap, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8069 8071

ENV PGHOST=db \
    PGPORT=5432 \
    PGUSER=odoo \
    PGPASSWORD=odoo

CMD ["python", "odoo.py"]
