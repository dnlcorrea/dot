#!/bin/bash

DIR="/home/daniel/www"

if [ -z "$1" ]; then
    echo "Need host folder" && exit 1;
fi

cat <<EOF >> /etc/httpd/conf/extra/httpd-vhosts.conf

<VirtualHost *:80>
	DocumentRoot "$DIR/$1/public"
	ServerName $1.test
	ErrorLog "$DIR/$1/error.log"
	CustomLog "$DIR/$1/access.log" combined
	Options +FollowSymLinks
</VirtualHost>
EOF

systemctl reload httpd 
