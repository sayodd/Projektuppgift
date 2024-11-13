# Använd Ubuntu-basen
FROM ubuntu:latest

# Uppdatera och installera NGINX
RUN apt-get update && apt-get install -y nginx

# Skapa en enkel HTML-fil
RUN echo "<html><body><h1>Hello från Docker image!</h1></body></html>" > /var/www/html/index.html

# Starta NGINX när containern startar
CMD ["nginx", "-g", "daemon off;"]
