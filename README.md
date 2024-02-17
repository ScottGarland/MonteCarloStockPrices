# MonteCarlo
How to run:
 - Ensure there is a properly generated SECRET_KEY and relational database connection in settings.py.
 - Have Python 3 installed on your machine.
 - Open a powershell in the src directory.
 - Run the command `pip install  -r requirements.txt`.
 - Navigate to django directory `cd django`.
 - Run the command `python manage.py makemigrations`.
 - Then run `python manage.py migrate` to create the required tables.
 - Once migration is complete, run the command `python manage.py runserver` to run the application.
 - You should now be able to browse the site on localhost:8000.

Common error(s)
 - The mpld3 library might show this error when attempting to display the plots: `'XAxis' object has no attribute '_gridOnMajor'`.
 - To fix this error, one can alter the `utils.py` file located in the `Lib\site-packages\mpld3\mplexporter` directory where Python is installed, outlined in the fix here:
 https://github.com/plotly/plotly.py/issues/2913
 https://github.com/carlinmack/mplexporter/commit/739793fdda66809df80bb6b2d19c0605544f8292.
 - change `_gridOnMajor` to `_major_tick_kw['gridOn']` on line 263.
