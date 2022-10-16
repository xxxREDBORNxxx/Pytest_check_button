# pytest_check_button

Test task: https://stepik.org/lesson/237240/step/9?unit=209628

The test verifies that the product page on the site
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ 
contains the "add to basket" button.

The browser is launched with the specified user language available on the site,
by default the parameter "language =ru"
The browser must be chrome or firefox, by default the parameter "browser_name=chrome".

Running the test with the "language" parameter :

pytest -language=es test_items.py

Running the test with the "browser_name" parameter:

pytest --language=es --browser_name=firefox test_items.py