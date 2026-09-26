# IBM Sentiment Analysis Lab — Local VS Code Starter

This folder prepares the non-exercise setup for the IBM lab.

## Important environment limitation

The official lab states that the Watson sentiment API used in Task 2 is hosted
inside Skills Network and is intended to be called from the Skills Network
Theia environment. The rest of the learning objectives can be practiced locally.

We will first work locally in VS Code. When we reach the actual Watson request,
the tutor will explain the request flow and choose the smallest workaround if
the IBM endpoint is unreachable from your machine.

## Setup

macOS / Linux:

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install -r requirements.txt

Windows PowerShell:

    py -m venv .venv
    .venv\Scripts\Activate.ps1
    py -m pip install -r requirements.txt

## Starter structure

    ibm_sentiment_lab_local_starter/
    ├── sentiment_analysis.py      # Task 2: you implement this
    ├── server.py                  # IBM Flask starter with TODOs
    ├── requirements.txt
    ├── static/
    │   └── mywebscript.js         # IBM-provided; leave as-is
    └── templates/
        └── index.html             # IBM-provided; leave as-is

Later tasks will have you create the SentimentAnalysis package and test file.
Those are intentionally NOT pre-created because they are part of the lab.
