docker-compose up -d postgreshost
echo "WAITING FOR DATABASE TO START"
sleep 4 # wait for the database to start up
echo "Running Migrations"
docker-compose run web python manage.py syncdb
echo "Seeding DB"
docker-compose run web python manage.py loaddata waitlist.json accounts.json
docker-compose stop
