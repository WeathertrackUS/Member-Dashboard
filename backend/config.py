import os
import logging

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    DATABASE_PATH = os.getenv('DATABASE_PATH', os.path.join(os.path.dirname(__file__), 'wtus_team_system.db'))
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    ALLOWED_EXTENSIONS = {'psd', 'jpg', 'jpeg', 'png', 'gif'}
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')

    # Logging Configuration
    LOG_FILE = os.getenv('LOG_FILE', 'wtus_team_system.log')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '{program} - %(asctime)s - %(name)s - %(levelname)s - %(message)s'

    @classmethod
    def configure_logging(cls, program_name):
        """Configure logging for the application

        Args:
            program_name (str): Name of the program to be shown in log entries

        Raises:
            ValueError: If LOG_LEVEL is not a valid logging level
        """
        if cls.LOG_LEVEL not in cls.ALLOWED_LOG_LEVELS:
            raise ValueError(f"Invalid log level: {cls.LOG_LEVEL}. Must be one of {cls.ALLOWED_LOG_LEVELS}")

        log_dir = os.path.dirname(cls.LOG_FILE)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        handler = logging.handlers.RotatingFileHandler(
            cls.LOG_FILE,
            maxBytes=cls.LOG_MAX_BYTES,
            backupCount=cls.LOG_BACKUP_COUNT
        )
        handler.setFormatter(logging.Formatter(cls.LOG_FORMAT.format(program=program_name)))

        logging.basicConfig(
            level=getattr(logging, cls.LOG_LEVEL),
            handlers=[handler]
        )
