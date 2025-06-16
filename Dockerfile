FROM docker.io/hugomods/hugo:debian-base-0.147.8@sha256:9a4344c6db750e7d4114cece2b391c3fa49d213da02d090a9a8f63e30c215cac AS hugo

COPY site /src

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN hugo build \
        --minify \
        --gc \
        --cleanDestinationDir \
        --config /src/config.toml

RUN find /src/public -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.xml' -o -name '*.json' -o -name '*.svg' -o -name '*.txt' \) -print0 | xargs -0 -P4 -n32 gzip --best -kf

# ---------------------------------------------------

# https://github.com/nginxinc/docker-nginx-unprivileged
FROM ghcr.io/nginxinc/nginx-unprivileged:stable-alpine AS webserver

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
