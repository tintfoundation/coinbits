test:
	trial coinbits

lint:
	pep8 --ignore=E303,E251,E201,E202 ./coinbits --max-line-length=140
	find ./coinbits -name '*.py' | xargs pyflakes

install:
	python setup.py install
