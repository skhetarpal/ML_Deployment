import osimport loggingimport logging.configimport yamlimport sysfrom house_price_predictor.config import configwith open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as version_file:    __version__ = version_file.read().strip()#with open(os.path.join(config.PACKAGE_ROOT, 'config/logging_config.yaml'), 'r') as f:#    conf = yaml.safe_load(f)##logging.config.dictConfig(conf)#logger = logging.getLogger(name=config.LOGGER_NAME)FORMATTER = logging.Formatter("LOG: %(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s")console_handler = logging.StreamHandler(sys.stdout)console_handler.setFormatter(FORMATTER)logger = logging.getLogger(name=config.LOGGER_NAME)logger.setLevel(logging.DEBUG)logger.addHandler(console_handler)logger.propagate = False#from house_price_predictor.config import logging_config#logger = logging_config.basic_logger(name=__name__)