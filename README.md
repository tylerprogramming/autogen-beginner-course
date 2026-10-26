## AutoGen Beginner Course

> **Legacy code (2024).** This course was recorded on AutoGen 0.2 (`pyautogen==0.2.26`) and the code is kept as it appears in the videos. Several models it uses have since been shut down, so those lessons fail with `model_not_found` until you change the model name. See [Models used in this course were retired](#models-used-in-this-course-were-retired).

- install pycharm community edition ide (if you don't have one)
- install anaconda (if you don't want to use venv)
- Reddit project is bonus, try it out!

Join my [Discord](https://discord.gg/Db6e8KkHww) community for any questions!

To install the requirements, type this in your terminal: <br>
<code>pip install -r requirements.txt</code>

Use Python 3.11 or 3.12: `pyautogen==0.2.26` requires Python below 3.13, and the pinned `numpy==1.26.4` publishes wheels only up to 3.12.

Bonus Project Reddit URL: [Create App](https://old.reddit.com/prefs/apps/)

## Models used in this course were retired

The substitutes are the ones listed on the [OpenAI deprecations page](https://developers.openai.com/api/docs/deprecations):

| Model in this course | Shut down | OpenAI's substitute |
| --- | --- | --- |
| `gpt-3.5-turbo` | 2026-10-23 | `gpt-5.6-terra` |
| `gpt-4` | 2026-10-23 | `gpt-5.6-sol` |
| `gpt-4-vision-preview` | 2024-12-06 | a current vision model, e.g. `gpt-5.6-terra` |
| `dall-e-3` (lesson 08) | 2026-05-12 | `gpt-image-2.5-flare`, called through the Images API (`client.images.generate`), not as a chat model in `llm_config` |

`gpt-5.4-mini` is a cheaper option for these small demos ($0.75 / $4.50 per 1M input/output tokens, against $2 / $12 for `gpt-5.6-terra` and $4 / $20 for `gpt-5.6-sol`).

To run an affected lesson:

1. Change `"model"` in that lesson's `OAI_CONFIG_LIST.json`, and any `filter_dict` model list or `"model":` in its `.py` files (search the folder for `gpt-` and `dall-e`).
2. Delete `"temperature"` and `"max_tokens"` from the `llm_config`. GPT-5 models only accept the default temperature, and use `max_completion_tokens` instead of `max_tokens`.
3. Expect a cost-calculation warning from `pyautogen` 0.2: its price table predates these models. The chat still runs.

Lessons that reference a retired model: 01, 02, 03, 04, 05, 06, 07, 08, 10, 11, 13 and 14. Lessons 09 (LM Studio, local model) and 12 (Hugging Face Inference API) do not use OpenAI models.

For current, maintained AutoGen code (AutoGen 0.7 API), see [tylerprogramming/ai](https://github.com/tylerprogramming/ai/tree/main/frameworks/autogen).
