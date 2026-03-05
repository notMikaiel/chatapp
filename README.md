# Chat App

A real-time multi-room chat application built with Django and WebSockets.

## Live Demo
[Link coming soon]

## Features
- Real-time messaging via WebSockets — no polling
- Multiple chat rooms
- User registration and authentication
- Message history persisted to PostgreSQL
- Messages load on room entry, new messages appear instantly

## Tech Stack
- **Backend:** Django 6.0, Django Channels 4.3
- **Database:** PostgreSQL
- **WebSockets:** Daphne ASGI server
- **Auth:** Django built-in authentication
- **Static files:** WhiteNoise
- **Deployment:** Render

## Running Locally

**Requirements:** Python 3.13, PostgreSQL
```bash
# Clone the repo
git clone https://github.com/notMikaiel/chat-app.git
cd chat-app

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create a .env file in the root directory
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/chatapp

# Run migrations
python manage.py migrate

# Start the server
daphne -p 8000 chatapp.asgi:application
```

Visit `http://127.0.0.1:8000/accounts/register/` to create an account.

Rooms are managed via the Django admin panel at `/admin/`.

## What I'd Add Next
- Redis channel layer for multi-process production deployments
- Private messaging between users
- Online presence indicators
- Message pagination beyond 50 messages
- Room creation from the UI instead of admin panel only

## Screenshots
[Coming soon]s