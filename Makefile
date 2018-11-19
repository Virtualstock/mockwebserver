help:
	@echo "Usage:"
	@echo "		make help: 	    print this message"
	@echo "		make test:	    run the tests"
	@echo "		make dist:	    build the distribution files"
	@echo "		make upload:	upload distributions in dist directory"

test:
	tox

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
