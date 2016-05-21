FROM nginx:1.10
COPY default.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh

# Script to be run on container
ENTRYPOINT ["/entrypoint.sh"]

# Argument to the entrypoint.sh -- "@"
CMD ["nginx", "-g", "daemon off;"]