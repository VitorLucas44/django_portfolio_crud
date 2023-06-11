import django
django.setup()

from about.seed import run
from contact.seed import contact_run
from services.seed import services_run
from testimonial.seed import testimonial_run
if __name__ == '__main__':
	# run()
	# contact_run()
	# services_run()
	testimonial_run()
	