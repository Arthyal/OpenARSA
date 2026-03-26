from retriever import get_retriever
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import  HuggingFacePipeline, ChatHuggingFace

def rag(query):

    retriever=get_retriever()

    llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=200
    )
    )  

    model = ChatHuggingFace(llm=llm)

    docs=retriever.invoke(query)

    context="\n\n".join([
        f"source:{doc.metadata.get('source','unkown')}\n"
        f"title:{doc.metadata.get('title',' ')}\n"
        f"{doc.page_content}"
        for doc in docs
    ])

    template=PromptTemplate(
        """You are a helpful assistant.
        Use ONLY the information from the context below , to answer the question which follows it.
        Context:{context}
        Question:{query}""",
        input_variables=['context','query']
    )

    prompt = template.invoke({'context':context,'query':query})

    response= model.invoke(prompt)

    return response