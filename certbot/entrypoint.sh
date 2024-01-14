#!/bin/sh

# Function to renew the certificate every 12 hours
renew_certificate() {
  while true; do
    certbot certonly --standalone -d "$JELLYFIN_URL" -n
    sleep 12h
  done
}

# Start renewing the certificate
renew_certificate

