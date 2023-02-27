# AI-Translator

Build an online translation and grammar checking APP based on the Transformer model.

APP link: https://junchuanyu-tools.hf.space/

## Model
translation: [Helsinki-NLP](https://github.com/Helsinki-NLP/OPUS-MT-train)
grammar checker: [Gramformer](https://github.com/PrithivirajDamodaran/Gramformer/)
text generator: [DistilGPT2](https://huggingface.co/distilgpt2)

## Interface

The AI-Translator has two interfaces, one for text translation and one for grammar checking and text generation.You can enter sentence through the interface and click the "RUN" button to get the result.

![AI-Translator](./DEMO.gif)

## How to use API

You can realize more functions by calling the API.The api call demo is as follows:

DEMO-1: translation

```python
import requests

response = requests.post("https://junchuanyu-tools.hf.space/run/translate_zh", json={
	"data": [
		"Build an online translation and grammar checking app.",
	]
}).json()

data = response["data"]

print(data)

response2 = requests.post("https://junchuanyu-tools.hf.space/run/translate_en", json={
	"data": [
		"你好吗？代码男",
	]
}).json()

data2 = response2["data"]
print(data2)

```

DEMO-2: grammar checker

```python

import requests

response = requests.post("https://junchuanyu-tools.hf.space/run/gramacorrect", json={
	"data": [
		"I is jack",
	]
}).json()

data = response["data"]
print(data)

```

DEMO-3: text generator

```python
import requests

response = requests.post("https://junchuanyu-tools.hf.space/run/generator", json={
	"data": [
		"hello coding guy, i want",
	]
}).json()

data = response["data"]

print(data)

```