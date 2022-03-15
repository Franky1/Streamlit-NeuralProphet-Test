# Streamlit-NeuralProphet-Test

Streamlit test project for time-series-forecasting library **NeuralProphet**

## Resources

- Website <https://neuralprophet.com/html/index.html>
- GitHub <https://github.com/ourownstory/neural_prophet>

## Issues

## ToDo

- [ ] Add a streamlit example of a time-series-forecasting application with `neuralprophet`.
- [ ] Add a solution that works on Streamlit Cloud.

## Usage

You can build the Docker image for local usage with the following command:

```bash
docker build --progress=plain --tag streamlitneuralprophet:latest .
docker run -ti -p 8501:8501 --rm streamlitneuralprophet:latest
```

### Lokal Docker Streamlit runtime

A Dockerfile is provided for local testing of the Streamlit app.
Here some useful `docker` commands:

```sh
docker build --progress=plain --tag streamlitneuralprophet:latest .
docker run -ti -p 8501:8501 --rm streamlitneuralprophet:latest
docker run -ti -p 8501:8501 --rm streamlitneuralprophet:latest /bin/bash
docker run -ti -p 8501:8501 -v $(pwd):/app --rm streamlitneuralprophet:latest  # linux
docker run -ti -p 8501:8501 -v ${pwd}:/app --rm streamlitneuralprophet:latest  # powershell
docker run -ti -p 8501:8501 -v %cd%:/app --rm streamlitneuralprophet:latest  # cmd.exe
docker run -ti --rm python:3.9-slim /bin/bash  # testing python container
docker builder prune --force  # cleanup dangling images
docker image prune --filter="dangling=true" --force  # cleanup dangling images
```

Open local docker streamlit app site: <http://localhost:8501/>

Port `8501` is the default port for Streamlit.

---

## Status

> Work in progress. Not yet usable.
> Last change: 15.03.2022
