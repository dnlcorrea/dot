fc-cache -rv

emacs -l $HOME/Dropbox/emacs/emacs_packs.el &

# sudo cp $HOME/Dropbox/Geekery/checkupdates /usr/bin/checkupdates

# PHP
mkdir /home/daniel/www

sudo chown daniel:http $HOME/www

sudo cp $HOME/Dropbox/Geekery/httpd.conf /etc/httpd/conf/
sudo cp $HOME/Dropbox/Geekery/httpd-vhosts.conf /etc/httpd/conf/extra/

sudo chmod o+x /home/daniel

sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
sudo systemctl enable mysqld --now
sudo mysql_secure_installation

wal -i $HOME/Dropbox/wallpaper

cd

wget https://getcomposer.org/installer
sudo php installer --install-dir=/usr/bin --filename=composer

composer global require hirak/prestissimo

cd 

# Symlinks
ln -s Dropbox/bin bin 
ln -s Dropbox/emacs/.dnl-emacs .dnl-emacs 
ln -s Dropbox/emacs/.emacs .emacs 
ln -s Dropbox/fonts .fonts 
ln -s Dropbox/Geekery/.oh-my-zsh .oh-my-zsh 
ln -s Dropbox/Org org 
ln -s Dropbox/config/.tmux.conf .tmux.conf 
ln -s Dropbox/config/.Xresources .Xdefaults 
ln -s Dropbox/config/.Xresources .Xresources 
ln -s Dropbox/Geekery/zsh .zsh 
ln -s Dropbox/Geekery/zsh/.zshrc .zshrc 
