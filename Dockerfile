FROM ghcr.io/hugomods/hugo:debian-base-0.165.0@sha256:cd2763430958b7fa6a88b2206675a5e8199fd1d29fc9f38eed43e53f2bed8514 AS hugo

COPY site /src

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN hugo build \
        --minify \
        --gc \
        --cleanDestinationDir \
        --config /src/config.toml

RUN find /src/public -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.xml' -o -name '*.json' -o -name '*.svg' -o -name '*.txt' \) -print0 | xargs -0 -P4 -n32 --no-run-if-empty gzip -9k --force --no-name

# ---------------------------------------------------

# https://github.com/nginx/docker-nginx-unprivileged
FROM ghcr.io/nginx/nginx-unprivileged:stable AS webserver

RUN echo "absolute_redirect off;" >/etc/nginx/conf.d/no-absolute_redirect.conf
RUN echo "gzip_static on; gzip_proxied any;" >/etc/nginx/conf.d/gzip_static.conf
# brotli_static not yet available in standard nginx distribution
# RUN echo "brotli_static on; brotli_proxied any;" >/etc/nginx/conf.d/brotli_static.conf

# Copy built site from build stage
COPY --from=hugo /src/public /usr/share/nginx/html

# Test configuration during docker build
RUN nginx -t

# Port the container will listen on
EXPOSE 8080
