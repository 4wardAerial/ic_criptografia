class CharInvalidoError(Exception):
    def __init__(self, char):
        super().__init__(f"Caractere inválido: {char!r}")
        self.char = char