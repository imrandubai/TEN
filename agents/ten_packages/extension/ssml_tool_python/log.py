
import logging

logger = logging.getLogger("ssml_tool_python")
logger.setLevel(logging.INFO)

formatter_str = (
    "%(asctime)s - %(name)s - %(levelname)s - %(process)d - "
    "[%(filename)s:%(lineno)d] - %(message)s"
)
formatter = logging.Formatter(formatter_str)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
