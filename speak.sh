#run Django server in enable external access
python manage.py runserver 0.0.0.0:8000 &
server_process=$!
sleep 1
python main.py "書斎" "こんにちは。Google Homeです" &
wait $!
kill -TERM ${server_process}
