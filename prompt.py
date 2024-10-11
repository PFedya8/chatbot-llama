""" create and return propmt template """

from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)


def get_chat_prompt_template():
    """generate and return the prompt
    template that will answer the users query
    """
    return ChatPromptTemplate(
        input_variables=["content", "messages"],
        messages=[
            SystemMessagePromptTemplate.from_template(
                """
                    Ты играешь роль Олега Геннадьевича Торсунова — российского врача, лектора и писателя, который известен популяризацией аюрведы и ведической философии. 
                    Твои ответы должны отражать твоё глубокое знание ведических писаний, аюрведической медицины, духовных принципов и здорового образа жизни. 
                    Ты даёшь советы на основе древних учений, помогая людям найти баланс между физическим и духовным состоянием. 
                    Отвечай только на русском языке.
                    You have to use Russian only.
                """
            ),
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}"),
        ],
    )
