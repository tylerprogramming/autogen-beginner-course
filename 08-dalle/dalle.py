import autogen


def main():
    # If you have created an OAI_CONFIG_LIST.json file in the current working directory, that file will be used.
    config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json",
        filter_dict={
            "model": ["dall-e-3"]
        }
    )

    # Create the agent that uses the LLM.
    assistant = autogen.AssistantAgent(
        "assistant",
        llm_config={"config_list": config_list}
    )

    # Create the agent that represents the user in the conversation.
    user_proxy = autogen.UserProxyAgent(
        "user_proxy",
        code_execution_config={"work_dir": "coding", "use_docker": False}
    )

    user_proxy.initiate_chat(
        assistant,
        message="Create an image of a robot holding a sign saying 'AutoGen' with the background of wallstreet."
    )


if __name__ == "__main__":
    main()
