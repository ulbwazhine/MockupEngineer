python setup.py sdist
twine upload dist/*
rm -rf "dist"
rm -rf "MockupEngineer.egg-info"