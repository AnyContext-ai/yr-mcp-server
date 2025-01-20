# YR MCP Server

![YR](YR_blaa_rgb-100.png)

![alt text](Met_RGB_Horisontal-100.jpg)

## Setup environment using uv

#### Windows
```
# Install uv
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment
uv venv

# Activate virtual environment
.venv\Scripts\activate
```

#### Linux

```
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate
```

### Install dependencies
```
uv pip install -r pyproject.toml
```

### Run server
```
uv run yr.py
```


## Setup environment using pip

### Create requirements.txt for installing dependencies via pip
```
uv pip freeze > requirements.txt
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run server
```
python yr.py
```



