![test and lint](https://github.com/patrotom/iso-service/actions/workflows/test.yml/badge.svg)

# ISO Service

The ISO service is a simple web microservice with one `POST /match_country` endpoint. This endpoint takes the ISO code and list of country names (in different languages) as an input. It filters out the country names corresponding to the ISO code and returns them as an output.

The functionality uses [countries data](data/countries.json) provided by mledoze in his [GitHub repository](https://github.com/mledoze/countries). This data contains a lot of information about the different countries, including their ISO codes and translations to the different languages. The service matches the country names based on this data.

## Install & Run

The service is written using `Python 3.9.1` and the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework. The whole functionality is dockerized.

On your local machine, you need to have installed:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

Once you install the required programs, navigate yourself to the root of this repository and run:

``` shell
docker-compose build
```

This will build the image based on the [Dockerfile](Dockerfile). To run the service:

``` shell
docker-compose up
```

This command will build and start our service container and the Redis container. The service is available at the <http://localhost:5000> URL.

`Note:` All required environment variables are automatically set in the [docker-compose.yml](docker-compose.yml) file to ease the process of running the service.

## Example Request and Response

* URL: <http://localhost:5000/match_country>
* Method: `POST`
* Content-Type: `application/json`

---

* **Given valid input data**
  * Request

    ``` json
    {
        "iso": "svk",
        "countries": [
            "Slovakia",
            "Slowakei",
            "Vatikan",
            "Slovačka",
            "Szlovákia",
            "Belgrade",
            "España",
            "Nizozemsko"
        ]
    }
    ```

  * Response

    ``` json
    {
        "data": {
            "iso": "SVK",
            "match_count": 4,
            "matches": [
                "Slovakia",
                "Slowakei",
                "Slovačka",
                "Szlovákia"
            ]
        }
    }
    ```

* **Given invalid input data**
  * Request

    ``` json
    {
        "iso": "svk"
    }
    ```

  * Response

    ``` json
    {
        "errors": [
            "'countries' is a required property"
        ]
    }
    ```

* **Given invalid JSON**
  * Request

    ``` txt
    <>
    ```

  * Response

    ``` json
    {
        "errors": [
            "Payload is not a valid JSON"
        ]
    }
    ```

## Documentation

The documentation of the service is written using the [Open API 3.0 (3.0.3)](https://swagger.io/specification/) standard. The definition can be found in the [docs/iso-service-v1.0.json](docs/iso-service-v1.0.json) file. You can preview this documentation, for example, by using [Swagger Editor](https://editor.swagger.io/). Simply copy the contents of the file and paste it to the editor.

## Tests & Linting

* The [tests](tests/) are written using the [pytest](https://docs.pytest.org/en/6.2.x/) library.
* The linting is enabled by using the [flake8](https://flake8.pycqa.org/en/latest/) library.

Both tests and linting are automatically run on `push` and `pull_request` using the [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions). Navigate yourself to the [Actions tab](https://github.com/patrotom/iso-service/actions) to see the results of the workflows.

## Used Technologies

We already mentioned some of the technologies. Let's summarize them all in the following table:

| Technology     | Description                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------------------|
| Python 3.9.1   | Main development language.                                                                                       |
| Flask          | Web framework enabling the web service functionality.                                                            |
| Redis          | Works with the Flask framework to cache the API responses.                                                       |
| Open API 3.0   | The standard used to create the documentation of the service.                                                    |
| Docker         | Used to build an image from the service.                                                                         |
| Docker Compose | Used to run the service and Redis containers together. We also use it to set the required environment variables. |
| GitHub Actions | CI/CD used for the linting and testing the code.                                                                 |

## Authors

* **Tomáš Patro**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
