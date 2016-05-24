#!/bin/bash
set -e

sed -i "s|{{NGINX_HOST}}|$NGINX_HOST|;s|{{NGINX_PROXY}}|$NGINX_PROXY|;s|{{STATIC_VOLUME}}|$STATIC_VOLUME|;s|{{MEDIA_VOLUME}}|$MEDIA_VOLUME|" \
/etc/nginx/conf.d/default.conf

#cat /etc/nginx/conf.d/default.conf
exec "$@"