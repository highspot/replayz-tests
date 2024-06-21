import json
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from requests import Session

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    gong_access_key: str
    gong_secret_key: str

    call_ids: list[int]


def main():
    config = Config()

    session = Session()
    session.auth = (config.gong_access_key, config.gong_secret_key)

    host = "https://api.gong.io"
    path = "/v2/calls/transcript"

    cursor = ""

    while True:
        payload = {
            "cursor": cursor,
            "filter": {
                "callIds": config.call_ids,
            },
        }

        logger.info(f"Getting data from Gong API with payload: {payload}")
        response = session.post(host + path, json=payload)

        if response.status_code != 200:
            raise Exception(
                f"Failed to get data from Gong API. Status code: {response.text}"
            )

        data = response.json()

        for call_transcript in data["callTranscripts"]:
            with open(f'output/{call_transcript["callId"]}.json', "w") as f:
                logger.info(
                    f'Writing call transcript to file {call_transcript["callId"]}.json'
                )
                f.write(json.dumps(call_transcript["transcript"]))

        cursor = data["records"].get("cursor")

        if not cursor:
            break

    logger.info("Finished getting transcripts from Gong API")


if __name__ == "__main__":
    main()
