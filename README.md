# URL Shortener

A Django-based URL shortener application with user authentication and link management features.

## Features

- User authentication (email/password and Google OAuth2)
- URL shortening with custom codes
- Link analytics (click tracking)
- User dashboard
- Profile management

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/urlshortener.git
cd urlshortener
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
cp .env.example .env
```

5. Update the `.env` file with your configuration:
- Set DEBUG=True for development
- Add your database credentials
- Configure email settings
- Add Google OAuth2 credentials

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

## Production Deployment

1. Set DEBUG=False in .env
2. Configure your web server (Nginx/Apache)
3. Set up a production database
4. Configure SSL certificates
5. Set up proper static file serving
6. Configure email backend

## Security

- Never commit the `.env` file
- Use strong passwords
- Keep dependencies updated
- Use HTTPS in production
- Set up proper CORS headers if needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django Documentation
- Google OAuth2 Documentation
- Social Auth App Django Documentation

## Contact

Name - [@NsikanEssi68252](https://x.com/NsikanEssi68252)

Project Link: https://github.com/ny-essien/django-url-shortener.git