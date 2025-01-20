# YR MCP Server

![YR](YR_blaa_rgb-100.png)

![alt text](Met_RGB_Horisontal-100.jpg)

### Setup environment

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



