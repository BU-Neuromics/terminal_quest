set -eu

rm -rf dist/*
python setup.py sdist bdist_wheel

# twine_creds.sh mush define TWINE_USERNAME and TWINE_PASSWORD env vars
. twine_creds.sh

echo $TWINE_USERNAME

twine upload --verbose --skip-existing -u $TWINE_USERNAME -p "$TWINE_PASSWORD" dist/*
