FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
CMD ["echo", "Hello från Docker image!"]