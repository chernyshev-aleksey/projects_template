from dataclasses import dataclass
import os

from loguru import logger
from dotenv import dotenv_values


@dataclass
class Config:
	CONSTANT: str

	def __post_init__(self):
		if isinstance(self.CONSTANT, str):
			self.CONSTANT = eval(self.CONSTANT.replace('', ''))


def only_success(record):
	return record["level"].name == "SUCCESS"


path_log = os.path.dirname(os.path.abspath(__file__)) + "/../logs/"

logger.add(path_log + "errors.log", level="ERROR", rotation='5 MB', retention=0)
logger.add(path_log + "success.log", filter=only_success, rotation='5 MB', retention=0)

config_dict = {
	**dotenv_values(os.path.dirname(os.path.abspath(__file__)) + "/../.env.server"),
	**dotenv_values(os.path.dirname(os.path.abspath(__file__)) + "/../.env.local"),
}

try:
	config = Config(**config_dict)
except Exception as e:
	logger.exception(e)
	exit(1)
# else:
# 	CONNECTION_STRING = f"mongodb://{config.DB_LOGIN}:{config.DB_PASSWORD}@rc1b-okazhb06hqauc9ep.mdb" \
# 						f".yandexcloud.net:27018/?replicaSet=rs01&authSource={config.DB_NAME}"
