import autogen


def main():
    phi2 = {
        "config_list": [
            {
                "model": "TheBloke/phi-2-GGUF",
                "base_url": "http://localhost:1234/v1",
                "api_key": "lm-studio",
            },
        ],
        "cache_seed": None,
        "max_tokens": 1024
    }

    phil = autogen.ConversableAgent(
        "Phil (Phi-2)",
        llm_config=phi2,
        system_message="""
        Your name is Phil and you are a comedian.
        """,
    )
    # Create the agent that represents the user in the conversation.
    user_proxy = autogen.UserProxyAgent(
        "user_proxy",
        code_execution_config=False,
        default_auto_reply="...",
        human_input_mode="NEVER"
    )

    user_proxy.initiate_chat(phil, message="Tell me a joke!")


if __name__ == "__main__":
    main()
