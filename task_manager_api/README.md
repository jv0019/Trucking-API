# Task Manager API Documentation

## Table of Contents
1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [API Endpoints](#api-endpoints)
   - [Create Load](#create-load)
   - [Retrieve Loads](#retrieve-loads)
   - [Retrieve Single Load](#retrieve-single-load)
   - [Update Load](#update-load)
   - [Delete Load](#delete-load)
6. [Database](#database)
   - [Database Configuration](#database-configuration)
   - [Database Models](#database-models)
7. [Schemas](#schemas)
8. [Error Handling](#error-handling)
9. [Testing](#testing)
10. [Contributing](#contributing)
11. [License](#license)

## Getting Started

Instructions for getting started with the project.

## Prerequisites

You need to have the following software installed before running the application:
- Python 3.8 or higher
- PostgreSQL

## Installation

Follow these steps to install and set up the application:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task_manager_api.git

2. Navigate to the project directory:
   cd task_manager_api

3. Install the required Python packages:
   pip install -r requirements.txt

## Running the Application

To run the application locally, use the following command:
    python -m flask run

The application will be accessible at http://127.0.0.1:5000.

## API Endpoints

Create Load:

Endpoint: /load
Method: POST
Description: Creates a new load.

Example Request:
   {
     "shipperId": "123456789",
     "description": "Sample load"
   }

Retrieve Loads:

Endpoint: /load
Method: GET
Description: Retrieves all loads.

Retrieve Single Load:

Endpoint: /load/<load_id>
Method: GET
Description: Retrieves a specific load by its ID.

Update Load:

Endpoint: /load/<load_id>
Method: PUT
Description: Updates a specific load.

Delete Load:

Endpoint: /load/<load_id>
Method: DELETE
Description: Deletes a specific load.

## Database

Database Configuration:

The application uses PostgreSQL for data storage. Ensure that your PostgreSQL server is running and that you have created a database for the application.

Database Models

The database consists of the following models:
-Load: Represents the load data.

Schemas

The API uses JSON schemas for request validation.

Error Handling

Errors are handled gracefully and return appropriate HTTP status codes.

Testing

To test the application, you can use tools like Postman or run unit tests provided in the tests directory.

Contributing

Contributions are welcome! Please follow these steps to contribute:
-Fork the repository.
-Create a new branch.
-Make your changes and commit them.
-Submit a pull request.

License
This project is licensed under the MIT License.