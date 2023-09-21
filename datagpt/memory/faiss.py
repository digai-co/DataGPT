import os
import pickle

import faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from datagpt.config import config
from datagpt.util import root


class FaissStore:
    def __init__(self, dir: str, name: str):
        self.name = name
        if not os.path.exists(root / dir):
            os.mkdir(root / dir)

        self.store_file = root / dir / f"{name}.pkl"
        self.index_file = root / dir / f"{name}.index"

        if not (self.index_file.exists() and self.store_file.exists()):
            self.store = None
        else:
            with open(str(self.store_file), "rb") as f:
                self.store = pickle.load(f)
            self.store.index = faiss.read_index(str(self.index_file))

    def _persist(self):
        faiss.write_index(self.store.index, str(self.index_file))
        index = self.store.index
        self.store.index = None
        with open(self.store_file, "wb") as f:
            pickle.dump(self.store, f)
        self.store.index = index

    def write(self, schemas: dict):
        """batch writing all table schemas into long-term memory
        schemas should be
          {
            'table description': 'table schema',
            'table description': 'table schema'
          }
        """
        if config.get("llm.openai.azure") is not None:
            embeddings = OpenAIEmbeddings(
                deployment=config.get("llm.openai.azure.embedding_deployment"),
                openai_api_base=config.get(
                    "llm.openai.api_base", default="https://api.openai.com/v1"
                ),
                openai_api_key=config.get("llm.openai.api_key"),
                openai_api_type="azure",
                chunk_size=16,
            )
        else:
            embeddings = OpenAIEmbeddings(
                openai_api_key=config.get("llm.openai.api_key"), chunk_size=16
            )

        self.store = FAISS.from_texts(
            list(schemas.keys()),
            embeddings,
            metadatas=[{k: schemas[k]} for k in schemas],
        )
        self._persist()

    def search(self, query, k=10):
        """search top k tables that most relating to the query"""
        r = self.store.similarity_search(query, k=k)
        return str("\n".join([f"{x.metadata}" for x in r]))
