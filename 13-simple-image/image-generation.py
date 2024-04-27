import requests
import random
import io
import autogen
from PIL import Image
from typing import Annotated

# api and headers
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer your_token"}


# the function to take in prompt and convert to image and save to a file
def create_image(message: Annotated[str, "The response from the LLM"]) -> str:
    response = requests.post(API_URL, headers=headers, json=message)
    image_bytes = response.content

    random_number = random.randint(1, 1000000)
    file_name = "filename_" + str(random_number) + ".png"

    Image.open(io.BytesIO(image_bytes)).save(file_name)
    return message


# the llm_config
llm_config = {
    "config_list": autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json",
    ),
    "temperature": 0.5,
    "seed": 41
}

# Create the agent workflow
assistant = autogen.AssistantAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
                   "Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,

)
user_proxy = autogen.UserProxyAgent(
    name="User",
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
    code_execution_config={
        "use_docker": False
    }
)


assistant.register_for_llm(name="create_image", description="Create an image from a text description")(create_image)
user_proxy.register_for_execution(name="create_image")(create_image)


user_proxy.initiate_chat(
    assistant, message="""
        Create an image of a professional futbol player.
    """
)
