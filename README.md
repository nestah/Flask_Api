# Flask Video API

This project is a simple RESTful API built with Flask and Flask-RESTful. It provides basic CRUD (Create, Read, Update, Delete) functionality for managing a collection of videos, using SQLite for data storage.

## Project Structure

- `main.py`: The main application file where the Flask app and RESTful API are defined.
- `test.py`: A test script to interact with the API, including adding, retrieving, and deleting videos.
- `requirements.txt`: A list of dependencies required for the project.

## API Endpoints

The API provides the following endpoints:

- `GET /video/<int:video_id>`: Retrieve a specific video by its ID.
- `PUT /video/<int:video_id>`: Add a new video or update an existing one by its ID.
- `PATCH /video/<int:video_id>`: Update specific fields of an existing video by its ID.
- `DELETE /video/<int:video_id>`: Delete a specific video by its ID.
- `GET /videos`: Retrieve all videos.

## Setup

To set up and run the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-video-api.git
    cd flask-video-api
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python main.py
    ```

5. Open a new terminal and run the test script to interact with the API:

    ```bash
    python test.py
    ```

## Usage

### Adding Videos

To add videos, uncomment the data list in `test.py` and run the script. This will create three videos with IDs 0, 1, and 2.

### Retrieving All Videos

To retrieve all videos, use the `GET /videos` endpoint. This can be done by running the test script, which includes this request.

### Updating and Deleting Videos

You can update or delete videos by sending `PATCH` or `DELETE` requests to the `video/<int:video_id>` endpoint, respectively. Examples of these requests are provided in the `test.py` script.

## Dependencies

- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- requests

For a complete list of dependencies, see `requirements.txt`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

