
Kudy is an investment platfoim 🙂

## Features
** coming soon


## API Documentation

The full API documentation can be found by following the link below:

{host}/docs
e.g http://localhost:8000/docs

## Requirements and Installation

**Via Cloning The Repository**

```
# Clone the app
git clone https://github.com/vic3king/kudy-backend

# Switch to directory
cd kudy-backend
```

```
# Run with docker
# To run with docker create and setup a .env file according to .env.docker.example and run the following command

docker compose up
```

```
# Run without docker
# To run without docker create and setup a .env file according to .env.example and run the following commands
source .env
bash prestart.sh
uvicorn main:app --reload

Finally visit [http://localhost:8000/docs](http://localhost:8000/docs) to view api docs
```

## Testing

```
Coming soon
```

## Technologies

* Python <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a> backend:
    * **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic).
    * **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
    * **Easy**: Designed to be easy to use and learn. Less time reading docs.
    * **Short**: Minimize code duplication. Multiple features from each parameter declaration.
    * **Robust**: Get production-ready code. With automatic interactive documentation.
    * **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> and <a href="http://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.
    * <a href="https://fastapi.tiangolo.com/features/" class="external-link" target="_blank">**Many other features**</a> including automatic validation, serialization, interactive documentation, authentication with OAuth2 JWT tokens, etc.
* **Secure password** hashing by default.
* **JWT token** authentication.
* **SQLAlchemy** models (independent of Flask extensions, so they can be used with Celery workers directly).
* Basic starting models for users (modify and remove as you need).
* **Alembic** migrations.
* **CORS** (Cross Origin Resource Sharing).
* **Celery** worker that can import and use models and code from the rest of the backend selectively.
* REST backend tests based on **Pytest**, integrated with Docker, so you can test the full API interaction, independent on the database.


#### Linter(s)

Coming soon

### Style Guide

Coming soon


## Authors

- **Akaniru victory** - _Initial work_ - [Vic3king](http://vic3king.io)
