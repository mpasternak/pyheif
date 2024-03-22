all:
	rm -rf build dist
	python libheif/libheif_build.py
	python setup.py build bdist_wheel
