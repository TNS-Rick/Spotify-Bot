# Implementazione molto semplice di cache in memoria (dizionatio).
class Cache:
    def __init__(self):
        # Memorizzazione interna come dict
        self.cache = {}

    def get(self, key):
        # Recupera valore dalla cache
        return self.cache.get(key)

    def set(self, key, value):
        # Imposta valore nella cache
        self.cache[key] = value

    def clear(self):
        # Svuota la cache
        self.cache.clear()