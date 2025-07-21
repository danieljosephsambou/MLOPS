import logging
import logging.config
import yaml
from logger.filters import InfoOnlyFilter

with open('logger/logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)

logger = logging.getLogger('app_logger')

def division(a, b):
    logger.debug(f"Tentative de division {a} / {b}")
    try:
        result = a / b
        logger.info(f"Résultat de {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division par zéro !", exc_info=True)

def main():
    logger.info("Démarrage du programme")
    division(10, 2)
    division(5, 0)
    logger.warning("Fin du programme")

if __name__ == "__main__":
    main()
