py:
	pip3 install --user -r requirements-dev.txt
	mypy -i bin/ptr  

install:
	pip3 install --user -r requirements.txt
	pip3 install --user -U .

example:
	python3 bin/ptr who is there
