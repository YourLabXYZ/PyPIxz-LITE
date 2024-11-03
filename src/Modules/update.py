import logging
import requests

from __init__ import forge_api_latest_release


def get_latest_version(current_version):
    url = forge_api_latest_release

    try:
        logging.debug(f"GET request sent to URL: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        latest_version = data.get("tag_name", "undefined")

        logging.debug(f"Latest version retrieved: {latest_version}")

    except requests.exceptions.RequestException as error:
        logging.error(f"HTTP request error: {error}")
        return None

    return get_result_version(current_version, latest_version)


def get_result_version(current_version, latest_version):
    logging.debug(f"Comparing current version ({current_version}) with the latest version ({latest_version})")

    if current_version == latest_version:
        logging.info(f"Current version ({current_version}) is up to date.")
        return False
    else:
        return latest_version


def check_versions(current_version):
    logging.debug(f"Checking version for repository {forge_api_latest_release}")
    result = get_latest_version(current_version)
    return result