from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)


def load_document(file):
    import os
    name, extension = os.path.splitext(file)

    if extension == '.pdf':
        from langchain_community.document_loaders import PyPDFLoader
        print(f'Loading {file}')
        loader = PyPDFLoader(file)
    elif extension == '.docx':
        from langchain_community.document_loaders import Docx2txtLoader
        print(f'Loading {file}')
        loader = Docx2txtLoader(file)
    else:
        print('Document format is not supported!')
        return None
    data = loader.load()
    return data

def load_from_wikipedia(query, lang='en', load_max_docs=2):
    from langchain_community.document_loaders.wikipedia import WikipediaLoader
    loader = WikipediaLoader(query=query, lang=lang, load_max_docs=load_max_docs)
    data = loader.load()
    return data