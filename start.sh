echo "Cloning Repo, Please Wait..."
git clone -b main https://github.com/RSR-TG-Info/mizomv1.git /mizomv1
cd /mizomv1
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
