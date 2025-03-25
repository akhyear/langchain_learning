from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
# ekhaen template1 theke prompt niye model e dei, then model je output then sekhane theke
# string parser sdhu string nei metadata nei na, to oy sting template 2 er sathe lagaiya
# abra model ke dei tarpor ja output ase seta abar parse kore sudhui conent print kore
# tai result.content print kora lage tai 

result = chain.invoke({'topic':'black hole'})

print(result)
