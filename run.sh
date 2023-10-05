export FABRIC=PROD
./env/bin/gunicorn issue_tracker.wsgi --access-logfile access.log --error-logfile error.log --capture-output --bind=127.0.0.1:8002
