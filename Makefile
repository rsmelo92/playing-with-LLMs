default:
	make ingest
	make run

ingest:
	python3 ./ingest.py

run:
	python3 privateGPT.py -M
