import os
import config
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)
# client.api_key = config.OPENAI_API_KEY*
def generateBlogTopics(prompt1):
    response = client.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages=[{"role": "user", "content":"Generate blog topics on: {}. \n \n 1.  ".format(prompt1)}],
        temperature=0,
    )
    response_message = response.choices[0].message.content
    print(response_message )

    return response_message

def generateBlogSections(prompt1):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":"Expand the blog title into high-level blog sections: {} \n\n- Introduction: ".format(prompt1)}],
        temperature=0,
        top_p=1,
        frequency_penalty=0,    
        presence_penalty=0
    )

    response_message = response.choices[0].message.content
    print(response_message )

    return response_message

def blogSectionExpander(prompt1):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":"Expand the blog section into a detailed professional, witty, and clever explanation.\n\n {}".format(prompt1)}],
        temperature=0,
        top_p=1,
        frequency_penalty=0,    
        presence_penalty=0
    )

    response_message = response.choices[0].message.content
    print(response_message )

    return response_message
