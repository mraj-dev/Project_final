# IOT Insighter

A brief description of IOT Insighter that get the metrics data from IOT device via MQTT and display in Web UI.

## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Fast-Api

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Initlize the project

```bash
 python initlizer.py
```

Start the API server

```bash
  fastapi dev app.py
```

Start the pub-sub server

```bash
  python subscriber.py

  python publisher.py
```

Start the CSV generator

```bash
  python csv_generator_bw.py
```
