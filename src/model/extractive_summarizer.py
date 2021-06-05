from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import asyncio

class ext_summary:
    def __init__(self, text, model, sentences_count=3) -> None:
        self.text = text
        self.model = model
        self.parser = PlaintextParser.from_string(text,Tokenizer('english'))
        self.sentences_count = sentences_count

    async def get_summary(self) -> str:
        return ''.join(map(str, self.model(self.parser.document, sentences_count=self.sentences_count)))
