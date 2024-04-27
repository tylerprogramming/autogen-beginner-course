import autogen

config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-3.5-turbo"]
    },
)

llm_config = {
    "config_list": config_list,
    "timeout": 120,
}

assistant_quote1 = autogen.AssistantAgent(
    name="assistant1",
    system_message="You are an assistant agent who gives quotes.  Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,
)

assistant_quote2 = autogen.AssistantAgent(
    name="assistant2",
    system_message="You are another assistant agent who gives quotes.  Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,
    max_consecutive_auto_reply=1
)

assistant_create_new = autogen.AssistantAgent(
    name="assistant3",
    system_message="You will create a new quote based on others.  Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,
    max_consecutive_auto_reply=1
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config=False
)

user_proxy.initiate_chats(
    [
        {
            "recipient": assistant_quote1,
            "message": "give a quote from a famous author",
            "clear_history": True,
            "silent": False,
            "summary_method": "reflection_with_llm"
        },
        {
            "recipient": assistant_quote2,
            "message": "give another quote from a famous author",
            "clear_history": True,
            "silent": False,
            "summary_method": "reflection_with_llm"
        },
        {
            "recipient": assistant_create_new,
            "message": "based on the previous quotes, come up with your own!",
            "clear_history": True,
            "silent": False,
            "summary_method": "reflection_with_llm"
        }
    ]
)
