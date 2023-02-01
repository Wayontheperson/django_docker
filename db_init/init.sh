set -e
psql -U docker backend<<-EOSQL
CREATE SCHEMA IF NOT EXISTS test
EOSQL