FROM python:3.8

RUN pip install yaml pyyaml aiohttp

COPY . .

ENTRYPOINT ["python", "./src/coding_challenge.py"]
