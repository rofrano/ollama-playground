# ollama-playground

This repo contains some experiments using [Ollama](http://ollama.ai) models. Some of the code are examples from watching the Ollama YouTube channel and not my own work.

## Getting started

Establish a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## The basic test

The basic initial test can be run without any parameters:

```bash
python basic.py
```

## Rag example

To run the RAG example you must give it the URL of a web site to filter.

For example:

```bash
python rag.py --url https://techcrunch.com/
```

## Execution time

Here are the execution times on my 16-inch 2023 MacBook Pro M3 Max with 14 CPUs and 36GB memory.

| Program  | Execution Time |
|----------|----------------|
| basic.py | 6.557268 sec.  |
| rag.py   | 15.280634 sec. |
