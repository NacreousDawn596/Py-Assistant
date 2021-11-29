echo "downloading dependencies"
sleep 1
clear
sudo apt-get install python3 python3-tk mpg123 python3-pip
clear
sudo pacman -S python3-tk python3 python3-pip
clear
sudo dnf install python3 python3-tf mpg123 python3-pip
clear
pip install -r requirements.txt
clear
echo "done!"
