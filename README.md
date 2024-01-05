# ollama-playground

This repo contains some experiments using [Ollama](http://ollama.ai) models. Some of the code are examples from watching the Ollama YouTube channel and not my own work.

## Getting started

Establish a Python virtual environment with `pip`.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Establish a Python virtual environment with Poetry

```bash
poetry shell
poetry install --no-root
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

## Execution times

Just for fun, I did some tests to determine the execution times on the 3 computers that I had available to me:

1. Apple Silicon 2023 16-inch MacBook Pro M3 Max w/ 14-core CPU, 30-core GPU, and 36GB Unified Memory
2. Apple Silicon 2020 Mac mini M1 w/ 8-core CPU 8-core GPU, and 8GB Unified Memory
3. Apple Intel 2019 16-inch MacBook Pro with Intel 2.3Ghz 8-Core i9 CPU, AMD Radeon Pro 5500M GPU, and 64GB memory

I ran these after an initial run to prime the model so that all subsequent runs would have the same advantage. The initial run of `basic.py` took `12` seconds on my M3 Max, while all subsequent runs took `6` seconds which suggest that there is a 50% startup overhead the first time you load the model. My Intel had similar results. Basic took 73 seconds the first time and 52.6 seconds every other time suggesting about a 33% overhead to initially load the model.

Here are the results:

| Program  | Apple M3 Max   | Apple M1 8GB    | Intel 8-Core i9 |
|----------|----------------|-----------------|-----------------|
| basic.py | 6.557268 sec.  | 28.559059 sec.  | 52.613833 sec.  |
| rag.py   | 15.280634 sec. | 77.175288 sec.  | 279.106837 sec. |

As you can see, the original 2020 Mac mini with 8GB memory is 3.6x faster than the Intel 8-Core i9 with 64GB memory, and the M3 Max is 18x faster!!! That's almost two orders of magnitude with the Intel Mac taking 4 minutes and 39 seconds compared to 15 seconds on the M3 Max. Wow!
