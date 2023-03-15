import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, ID):
        try:
            result = self.cursor.execute("SELECT `login` FROM `users` WHERE `tab` = ?", (ID,))
            return bool(len(result.fetchall()))
        except:
            return False

    def get_user_pass(self, ID):
        try:
            result = self.cursor.execute("SELECT `pass` FROM `users` WHERE `tab` = ?", (ID,))
            return result.fetchone()[0]
        except:
            return None

    def get_user_mot(self, ID):
        try:
            result = self.cursor.execute("SELECT `sdep` FROM `users` WHERE `tab` = ?", (ID,))
            return result.fetchone()[0]
        except:
            return None

    def add_log(self, tab, tip):
        self.cursor.execute("INSERT INTO `log` (`tab`, `tip`) VALUES (?,?)", (tab, tip))
        return self.conn.commit()

    def random_tab(self, ID):
        try:
            result = self.cursor.execute("SELECT `tab` FROM `users` WHERE `tab` != ? ORDER BY RANDOM() LIMIT 1", (ID,))
            return result.fetchone()[0]
        except:
            return None

    def close(self):
        self.connection.close()