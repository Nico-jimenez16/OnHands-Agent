import logging

from app.observability.logging.logging_configuration import configure_logging


def test_logging_level_output_and_idempotence(capsys):
    """Central logging emits formatted messages without duplicating handlers."""
    root_logger = logging.getLogger()
    original_handlers = root_logger.handlers[:]
    original_level = root_logger.level
    try:
        configure_logging("WARNING")
        configure_logging("WARNING")
        assert root_logger.level == logging.WARNING
        own_handlers = [handler for handler in root_logger.handlers if handler.get_name() == "onhands-console"]
        assert len(own_handlers) == 1
        logger = logging.getLogger("onhands.foundation")
        logger.info("hidden-foundation-message")
        logger.warning("visible-foundation-message")
        output = capsys.readouterr().err
        assert "WARNING onhands.foundation visible-foundation-message" in output
        assert output.count("visible-foundation-message") == 1
        assert "hidden-foundation-message" not in output
    finally:
        for handler in root_logger.handlers[:]:
            if handler not in original_handlers:
                root_logger.removeHandler(handler)
                handler.close()
        root_logger.handlers = original_handlers
        root_logger.setLevel(original_level)
