# Item Dashboard API

This Django project implements an API for managing items in a dashboard, providing functionalities for retrieving items, adding new items, user authentication, and more.

## Data Models

The project defines the following data models:

### Item Model

- **category**: The category of the item.
- **sku**: Stock Keeping Unit, a unique identifier for the item.
- **name**: The name of the item.
- **inStock**: The total stock of the item.
- **availableStock**: The available stock of the item.
- **tag1** to **tag5**: Boolean flags indicating different attributes of the item.

## API Endpoints

The project exposes the following API endpoints:

- `/login`: User login endpoint.
- `/signup`: User signup endpoint.
- `/test_token`: Endpoint to test user authentication token.
- `/create`: Endpoint to add new items.
- `/getAllItems/`: Endpoint to retrieve all items.
- `/getAllItemsbyParameters/`: Endpoint to retrieve items filtered by parameters.

## Serializers

The project uses Django REST Framework serializers to handle data serialization and deserialization for model instances.

## Query Parameters

The `/getAllItemsbyParameters/` endpoint supports query parameters for filtering items based on SKU, name, category, and other parameters.

## Authentication

Authentication is implemented using token-based authentication provided by Django REST Framework. API endpoints are secure and can only be accessed by authenticated users.

## Testing

Unit tests are written for the API endpoints to validate their functionality. Tests cover user login, signup, token testing, adding items, retrieving items, and filtering items by parameters.

## Bonus Features

- **Caching**: The project implements caching to optimize the performance of the API.
- **Front-end Interface**: A basic front-end interface can be created using a framework of choice to consume the API and display data in a user-friendly format.

## Database

The project uses SQLite as the default database for development purposes. However, for production deployment, you can choose a different database such as PostgreSQL or MySQL based on scalability and performance requirements.

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Configure the database settings in `settings.py`.
4. Run migrations to create the necessary database schema.
5. Start the Django development server using `python manage.py runserver`.
6. Access the API endpoints using a REST client or integrate them into your application.
