""" create new chain """

from langchain.chains.llm import LLMChain
from threading import Thread
from queue import Queue
from stream import get_streaming_handler
from memory import get_memory


class StreamableChain:
    """modify the streaming of the chain"""

    def stream(self, input):
        queue = Queue()
        streamin_handler = get_streaming_handler(queue)

        def task():
            self.invoke(input, config={"callbacks": [streamin_handler]})

        Thread(target=task).start()

        while True:
            tok = queue.get()
            if not tok:
                yield "\n"
                break
            yield tok


class StreamingChain(StreamableChain, LLMChain):
    pass


def create_chain(llm, prompt):
    """returns a chain instance"""
    return StreamingChain(llm=llm, prompt=prompt, memory=get_memory())
