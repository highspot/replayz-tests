# Gong API tests

## Requisites

- Docker

## Instructions

1. Clone this repository
2. Copy `.env.example` and rename it to `.env`

```ini
GONG_ACCESS_KEY=your_gong_access_key_here
GONG_SECRET_KEY=your_gong_secret_key_here

CALL_IDS=[678901234567890123456,12345678901234567890,9876543210987654321]
```

> Pay attention to call ids list format. It has to be JSON-like array (with square brackets and comma separated values).

3. Open your terminal and navigate to project root directory.
4. Execute `make run` to start the process
5. You should see an `output` folder being created and JSON files being added.

```sh
docker run -v "/home/tests/output:/app/output" tests
INFO:__main__:Getting data from Gong API with payload: {'cursor': '', 'filter': {'callIds': [678901234567890123456,12345678901234567890,9876543210987654321]}}
INFO:__main__:Writing call transcript to file 678901234567890123456.json
INFO:__main__:Writing call transcript to file 12345678901234567890.json
INFO:__main__:Writing call transcript to file 9876543210987654321.json
INFO:__main__:Finished getting transcripts from Gong API
```

# Troubleshooting

If you do not have `make` in your system (e.g. Windows Command Prompt), you can run the commands directly as long as you have docker in your system:

```
docker build -t replayziq-tests .
docker run -v "<YOUR_CURRENT_PATH>/output:/app/output" replayziq-tests
```