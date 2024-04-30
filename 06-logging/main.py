import json
import autogen
import pandas as pd
import sqlite3

# set up the llm_configuration
llm_config = {
    "config_list": autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json",
    ),
    "temperature": 0
}

# Start logging
logging_session_id = autogen.runtime_logging.start(config={"dbname": "logs.db"})
print("Started Logging session ID: " + str(logging_session_id))

# Create an agent workflow and run it
assistant = autogen.AssistantAgent(name="assistant", llm_config=llm_config)
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config=False,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
)

user_proxy.initiate_chat(
    assistant, message="What is the height of the Sears Tower? Only respond with the answer and terminate"
)

# Stop logging
autogen.runtime_logging.stop()


# create function to get log
def get_log(dbname="logs.db", table="chat_completions"):
    con = sqlite3.connect(dbname)
    query = f"SELECT request, response, cost, start_time, end_time from {table}"
    cursor = con.execute(query)
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    data = [dict(zip(column_names, row)) for row in rows]

    con.close()

    return data


def str_to_dict(s):
    return json.loads(s)


# use pandas to get extra information and print out to terminal
def get_log(dbname="logs.db", table="chat_completions"):
    import sqlite3

    con = sqlite3.connect(dbname)
    query = f"SELECT request, response, cost, start_time, end_time from {table}"
    cursor = con.execute(query)
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    data = [dict(zip(column_names, row)) for row in rows]
    con.close()
    return data

def str_to_dict(s):
    return json.loads(s)


log_data = get_log()
log_data_df = pd.DataFrame(log_data)

log_data_df["total_tokens"] = log_data_df.apply(
    lambda row: str_to_dict(row["response"])["usage"]["total_tokens"], axis=1
)

log_data_df["request"] = log_data_df.apply(lambda row: str_to_dict(row["request"])["messages"][0]["content"], axis=1)

log_data_df["response"] = log_data_df.apply(
    lambda row: str_to_dict(row["response"])["choices"][0]["message"]["content"], axis=1
)

print(log_data_df)
