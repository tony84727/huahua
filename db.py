import os


def get_dsn(*,
            host=os.environ.get('DB_HOST', 'localhost'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', ''),
            name=os.environ.get('DB_NAME', 'huahua'),
            ) -> str:
    """
        Return database connection string.
        The connection parameters are figured out by the following order:
        1. Parameters written directly in code
        2. Environment variables: DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
        3. Hardcoded default
    """
    return f'mysql+pymysql://{user}:{password}@{host}/{name}'
