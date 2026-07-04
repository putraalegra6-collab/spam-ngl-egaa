pkg update -y && pkg upgrade -y

pkg install python git -y

pip install requests colorama

git clone https://github.com/putraalegra6-collab/spam-ngl-egaa.git

cd spam-ngl-egaa

python spamv2.py
