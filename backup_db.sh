pg_dumpall > $HOME/psql-backups/full-database-backup && echo "success $(date "+%F-%H:%M")" >>  $HOME/cron-logs/daily-log.txt || echo "failed $(date "+%F-%H:%M")" >>  $HOME/run-logs/daily-log.txt
