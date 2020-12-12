#!/bin/bash

if [ -f $HOME/.installed ]; then
    echo "You almost destroyed your computer"
    exit 127 
fi

echo Swappie in GBs
read SWAP_PART
echo ROOT in GBs
read ROOT_PART

echo Hostname?
read hohstname
echo $hostname > hostname

timedatectl set-ntp true

cat <<EOF | fdisk /dev/sda
o
n
p


+500M
t
1
ef
n
p


+${SWAP_PART}G
n
p


+${ROOT_PART}G
n
p


p
w
EOF

partprobe

yes | mkfs.ext4 /dev/sda4
yes | mkfs.ext4 /dev/sda3
yes | mkfs.fat -F32 /dev/sda1

# Swap
mkswap /dev/sda2
swapon /dev/sda2

# ROOT
mount /dev/sda3 /mnt
mkdir -p /mnt/boot/efi

# BOOT
mount /dev/sda1 /mnt/boot

# HOME
mkdir -p /mnt/home
mount /dev/sda4 /mnt/home
mkdir /mnt/home/daniel

export SERVER='Server = http://archlinux.c3sl.ufpr.br/$repo/os/$arch'
sed -i "1i\\$SERVER" /etc/pacman.d/mirrorlist

pacstrap /mnt base base-devel vim linux linux-firmware

genfstab -U /mnt >> /mnt/etc/fstab
comp=$(cat hostname)
cat hostname > /mnt/etc/hostname

echo <<EOF > /etc/hosts
127.0.0.1 localhost
::1 localhost
127.0.1.1 ${comp}.localdomain ${comp}
EOF

cp -v *.sh /mnt

touch $HOME/.installed

mv .dot /mnt/home/daniel/.dot

arch-chroot /mnt bash /mnt/home/daniel/.dot/bootstrap/chroot.sh

#reboot
