FROM python:3.7

RUN pip install requests pyyaml aiohttp

COPY . .

ENTRYPOINT ["python", "./src/coding_challenge.py"]