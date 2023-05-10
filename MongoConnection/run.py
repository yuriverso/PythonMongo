from connection.connection import MongoConnectionHandler
from repositories.sessions_repo import SessionsRepository

connection_handler = MongoConnectionHandler()
connection_handler.connect()
connection = connection_handler.get_connection()

sessions_repo = SessionsRepository(connection)

sessions_repo.read_all()
