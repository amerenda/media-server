# media-server
My media server docker config

## Installation
### Pre-Reqs
1. Install `docker-compose` and `certbot`
2. Create the `CONFIG_BASE` dir found in the `.env` file. Replace with your own path or use the existing path
3. Update the environment variables in `.env`
4. Set the environment variables `source .env`
5. Set ownership `sudo chown -R $(whoami) $CONFIG_BASE`
6. Get your external IP address `curl -s http://ipecho.net/plain; echo`
7. Set your DNS for  `JELLYFIN_URL` to the value of your external IP address found above
8. Open ports 80 and 443 on your firewall
9. Obtain your SSL cert `sudo certbot certonly --standalone -d $JELLYFIN_URL -n`
10. Set your VPN user and password. I'm using `nordvpn` but any vpn that uses `openvpn` will work
    1. echo YOUR_USER > vpn-user.txt
    2. echo YOUR_PASSWORD > vpn-password.txt

### Install
1. Edit the .env file and replace with your configuration options
2. Run `docker-compose --profile=vpn --env-file .env up --build -d`

###
* sudo pacman -S mkvtoolnix-cli
