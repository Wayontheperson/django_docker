# Django DB connection error

>psql: error: could not connect to server: FATAL:  password authentication failed for user

After changing password encryption method this error happend.

## Trials

1. In postgresql.conf **"password_encryption = scram-sha-256"** script updated

2. Remake psql paassword.
    > After change password encryption method, user's password must be changed.

## Solution

error reason was the docker secret option.

In docker-compose.yml
```
  django:
    environment:
      POSTGRES_PASSWORD: /run/secrets/db_password
    secrets:
      - POSTGRES_PASSWORD
```
At first I think docker secrets option encrypted password and my psql password would be saved in *POSTGRES_PASSWORD* but it was totally wrong.

*"/run/secrets/db_password"* was saved in *POSTGRES_PASSWORD* environment valuable literally

so I removed the secrets option and using .env file to conceal my psql password. In the end this solution works well.

