#!/bin/bash

clear

read -n 1 -s -r -p "Press any key to continue"

clear

echo "Formatting / ... "

while :; do
php <<'EOF' 
<?php for($i = 0; $i < 100; $i++) {
    echo "$i%\r";
    sleep(1);
} ?>
EOF
done
