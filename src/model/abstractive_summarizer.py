import asyncio

class abs_summary:
    def __init__(self, text, model, min_length=40, max_length=300, do_sample=False) -> None:
        self.text = text
        self.model = model
        self.min_length = min_length
        self.max_length = max_length
        self.do_sample = do_sample

    async def get_summary(self) -> str:
        return self.model(self.text, 
                          max_length = self.max_length, 
                          min_length = self.min_length, 
                          do_sample = self.do_sample
                         )[0]['summary_text']