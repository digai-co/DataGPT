clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf data

dep:
	pip freeze > requirements.txt

fmt:
	python -m black .