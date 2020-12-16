echo Yo pass: 
read PASSWD

echo "root:$PASSWD" | chpasswd

ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

hwclock --systohc

echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
echo "pt_BR.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen

echo "LANG=en_US.UTF-8" > /etc/locale.conf

sed -i "1i\\$SERVER" /etc/pacman.d/mirrorlist

pacman --noconfirm --needed -S networkmanager grub intel-ucode
systemctl enable NetworkManager --now

grub-install --target=i386-pc /dev/sda && grub-mkconfig -o /boot/grub/grub.cfg

useradd -s /bin/zsh -d /home/daniel -m -G wheel daniel
echo "daniel:$PASSWD" | chpasswd

# Base software
pacman -S --noconfirm --needed bat bluez curl dmenu dialog dunst emacs evince feh ffmpeg ffmpegthumbnailer git htop imagemagick intel-ucode ncdu neofetch network-manager-applet nodejs npm php php-apache php-gd php-sqlite python python-pip r ranger ripgrep rofi rsync ruby scrot sqlite sshfs sudo termite tldr tmux vim vlc w3m wget xorg-xev xorg-xinit xorg-xprop xorg-xrandr xsel xorg-server zsh pulseaudio pulseaudio-bluetooth pavucontrol youtube-dl xcape alacritty fish qtile picom

# unattended
visudo

pip install pywal

#The rest
sudo -u daniel bash /home/daniel/.dot/bootstrap/Starter.sh
