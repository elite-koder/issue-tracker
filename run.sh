export FABRIC=PROD
./env/bin/gunicorn easy_todo.wsgi --access-logfile access.log --error-logfile error.log --capture-output
