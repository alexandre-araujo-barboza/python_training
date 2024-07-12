#!/bin/sh
python manage.py collectstatic --noinput
  15 changes: 4 additions & 11 deletions15  
scripts/commands.sh
Original file line number	Diff line number	Diff line change
@@ -3,14 +3,7 @@
# O shell irá encerrar a execução do script quando um comando falhar
set -e

wait_psql.sh
collectstatic.sh
migrate.sh
runserver.sh