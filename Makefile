all:
	pip install cffi setuptools wheel
	python libheif/libheif_build.py
	python setup.py build bdist_wheel

clean:
	-rm _libheif_*
	find . -type f -name \*pyc -print0 | xargs rm
