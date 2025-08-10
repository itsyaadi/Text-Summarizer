import os
from box.exceptions import BoxValueError
import yaml
from text_summarization.logging import logger
from ensure import ensure_annotations
from box import Box, ConfigBox
from pathlib import Path
from typing import Any, Union

@ensure_annotations
def read_yaml(path_to_yaml: Union[str, Path]) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox.
    
    Args:
        path_to_yaml (Union[str, Path]): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"YAML file not found: {e}")
        raise
    except BoxValueError as e:
        logger.error(f"Error reading YAML file: {e}")
        raise 
@ensure_annotations
def create_directories(paths: Union[str, Path, list]) -> None:
    """
    Creates directories if they do not exist.
    
    Args:
        paths (Union[str, Path, list]): Single path or list of paths to create.
    """
    if isinstance(paths, (str, Path)):
        paths = [paths]
    
    for path in paths:
        path = Path(path)
        try:
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Directory {path} created successfully.")
        except Exception as e:
            logger.error(f"Error creating directory {path}: {e}")
            raise
    
