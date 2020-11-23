 # For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV ENV_PATH=.env
ENV REPO_PATH=repo

ENV CAPTIONS_REPO=github.com/marosoft/caption-extractor.git
ENV GIT_USERNAME=superroot
ENV GIT_EMAIL=john@example.com
ENV GIT_TOKEN=TOKEN
ENV GOOGLE_API_KEY=key

WORKDIR /app

COPY install-packages.sh .
RUN ./install-packages.sh

# Add pip requirements
ADD requirements.txt .
ADD download_youtube_subtitle.patch .

COPY create-python-env.sh .
RUN ./create-python-env.sh

ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["/app/process-new-videos-main.sh"]
