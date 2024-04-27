import autogen


config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json",
)

llm_config = {
    "cache_seed": 47,
    "temperature": 0,
    "config_list": config_list,
    "timeout": 120,
}
user_proxy = autogen.UserProxyAgent(
    name="User",
    system_message="Executor. Execute the code written by the coder and suggest updates if there are errors.",
    human_input_mode="NEVER",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "code",
        "use_docker": False,
    },
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
    system_message="""
    If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line.
    Coder. Your job is to write complete code. You primarily are a game programmer.  Make sure to save the code to disk.
    """,
)

pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Help plan out to create games.",
    llm_config=llm_config,
)

group_chat = autogen.GroupChat(
    agents=[user_proxy, coder, pm], messages=[], max_round=15
)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=llm_config)

user_proxy.initiate_chat(
    manager,
    message=
    """
    I would like to create a snake game in Python!  Make sure the game ends when the player hits the side of the screen.
    """,
)
