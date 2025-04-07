# Django Blog Application

A full-featured blog application built with Django, featuring a public-facing site and an admin interface.

## Project Structure

- `blog_application/` - Main Django project configuration
- `public_site/` - Public-facing blog application
- `web_admin/` - Admin interface for managing blog content
- `media/` - Directory for uploaded media files

## Installation

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Configuration

1. Copy `.env.example` to `.env`
2. Update the environment variables in `.env` with your specific settings
3. Configure database settings in `blog_application/settings.py`

## Usage

- Access the web admin interface at: `http://localhost:8000/web_admin/`
- Public blog site is available at: `http://localhost:8000/`

## Development Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful commit messages
- Test changes locally before pushing
- Keep the virtual environment updated with `pip install -r requirements.txt`
