all:
	pip install cffi setuptools wheel
	python libheif/libheif_build.py
	python setup.py build bdist_wheel

clean:
	-rm -rf _libheif_* build dist
	find . -type f -name \*pyc -print0 | xargs rm
