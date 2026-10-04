import logging


def configure_logging(log_level: str) -> None:
    """Configure one application console handler while preserving other handlers."""
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    for handler in root_logger.handlers[:]:
        if handler.get_name() == "onhands-console":
            root_logger.removeHandler(handler)
            handler.close()

    console_handler = logging.StreamHandler()
    console_handler.set_name("onhands-console")
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    )
    root_logger.addHandler(console_handler)
