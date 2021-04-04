# create migration repo, creates migrations repository
flask db init
# create migration string
flask db migrate -m "users table"
#
flask db upgrade
