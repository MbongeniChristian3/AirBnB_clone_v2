python -m unittest discover tests 2>&1 /dev/null | tail -n 1

python -m unittest discover tests.test_models

python -m unittest discover tests.test_console

python -m unittest discover tests

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2  max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
