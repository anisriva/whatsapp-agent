import csv
import json
import logging
import os
from datetime import datetime
from typing import Any

import yaml


def mkdir(path: str) -> None:
    """
    Takes a valid path and creates directories
    recursively.
        params:
            - path : /pathto/file.js [it will create pathto folder]
    """
    directory = os.path.dirname(path)
    try:
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created dir [{directory}]")
    except Exception as e:
        logging.error(f"Issue occurred while creating dir [{directory}] : {e}")
        raise Exception(e)


def write_json_file(data: str, filename: str) -> None:
    """
    Takes a json input and dumps to a file
        params:
            - data : Data to write
            - filename : File where data is to be written
    """
    mkdir(filename)
    try:
        logging.info(f"Writing json data to [{filename}]")
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Issue occurred while writing to [{filename}] : {e}")
        raise Exception(e)


def write_json_to_csv(data: dict, csv_filename: str) -> None:
    """
    Dumps json to csv (Assumes a falttened out json) ex-> {"key1":"value1", "key2":"value2"}
        params:
            - data: Json data
            - csv_filename : target file
    """
    try:
        if data:
            mkdir(csv_filename)
            with open(csv_filename, "w", newline="") as csv_file:
                logging.info(f"Writing data to [{csv_filename}]")
                fieldnames = data[0].keys()
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(data)
    except Exception as e:
        logging.error(f"Issue occurred while writing to [{csv_filename}] : {e}")
        raise Exception(e)


def write_result_output(
    data: str, output_format: str, dir: str, query_name: str, env: str
) -> None:
    if data == "":
        logging.warning(
            f"No results found for query [{query_name}]. File will not be created"
        )
        return

    file_name = f"{dir}/{query_name}-{env}-{int(datetime.now().timestamp())}"

    if output_format == "json":
        write_json_file(data, f"{file_name}.json")
    elif output_format == "csv":
        write_json_to_csv(data, f"{file_name}.csv")
    else:
        logging.warning("Unsupported file type. Valid options are json or csv")


def read_yaml(path: str) -> Any:
    """
    Loads the yaml and returns the data
        params:
            - path : path to yaml
    """
    logging.info(f"Reading [{path}]...")
    try:
        with open(path, "r") as f:
            file = yaml.safe_load(f)
        return file
    except Exception as e:
        logging.error(f"Issue occurred while reading [{path}] : {e}")
        raise Exception(e)
