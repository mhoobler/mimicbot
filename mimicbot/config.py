import configparser
from pathlib import Path
import pdb
import typer
from mimicbot import DIR_ERROR, FILE_ERROR, __app_name__, types
import json

APP_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_DIR_PATH = APP_DIR_PATH / "config.ini"


def init_app(app_path: Path = str(APP_DIR_PATH), data_path: Path = APP_DIR_PATH / "data"):
    try:
        app_path.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    init_config(app_path)
    init_data(data_path)


def init_config(app_path: Path = APP_DIR_PATH):
    try:
        app_path.mkdir(parents=True, exist_ok=True)
        config_file_path = app_path / "config.ini"
        if not config_file_path.exists():
            config_file_path.touch(exist_ok=True)
            config_file_path.write_text(
                "[general]\ndata_path = \nsession = \n\n[discord]\napi_key = \nguild = \ntarget_user = \n\n[huggingface]\napi_key = \nmodel_name = \nmodel_saves = []\n\n[training]\ncontext_window = \ncontext_length = \ntest_perc = ")
    except OSError:
        return FILE_ERROR


def init_data(data_path: Path = APP_DIR_PATH / "data"):
    try:
        data_path.mkdir(parents=True, exist_ok=True)
    except OSError:
        return DIR_ERROR


def general_config(app_path: Path, data_path: Path, session: str):
    config = configparser.ConfigParser()
    try:
        config.read(str(app_path / "config.ini"))
    except:
        pass
    if not config.has_section("general"):
        config.add_section("general")
    config.set("general", "data_path", str(data_path))
    config.set("general", "session", session)
    with open(str(app_path / "config.ini"), "w") as config_file:
        config.write(config_file)


def discord_config(app_path: Path, api_key: str, guild: str, target_user: str):
    config = configparser.ConfigParser()
    try:
        config.read(str(app_path / "config.ini"))
    except:
        pass
    if not config.has_section("discord"):
        config.add_section("discord")
    config.set("discord", "api_key", api_key)
    config.set("discord", "guild", guild)
    config.set("discord", "target_user", target_user)
    with open(str(app_path / "config.ini"), "w") as config_file:
        config.write(config_file)


def huggingface_config(app_path: Path, api_key: str, model_name: str, model_saves: str):
    config = configparser.ConfigParser()
    try:
        config.read(str(app_path / "config.ini"))
    except:
        pass
    if not config.has_section("huggingface"):
        config.add_section("huggingface")
    config.set("huggingface", "api_key", api_key)
    config.set("huggingface", "model_name", model_name)
    config.set("huggingface", "model_saves", model_saves)
    with open(str(app_path / "config.ini"), "w") as config_file:
        config.write(config_file)


def training_config(app_path: Path, context_window: str, context_length: str, test_perc: str):
    config = configparser.ConfigParser()
    try:
        config.read(str(app_path / "config.ini"))
    except:
        pass
    if not config.has_section("training"):
        config.add_section("training")
    config.set("training", "context_window", context_window)
    config.set("training", "context_length", context_length)
    config.set("training", "test_perc", test_perc)
    with open(str(app_path / "config.ini"), "w") as config_file:
        config.write(config_file)
