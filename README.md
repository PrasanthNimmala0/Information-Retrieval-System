# Information-Retrieval-System

# How to run?
#### Steps:

clone the repository

```bash
Project repo : https://github.com/
```

### Step - 1 Create a conda environment after opening the repository

```bash
conda create -n llmapp python= 3.8 -y
```

```bash
conda activate llmapp
```

#### Step -2 - install the requirements

```bash
pip install -r requirements.txt
```

#### Create a `.env` file in the root directory and add your GOOGLE_API_KEY as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
streamlit run app.py
```

Now
```bash
open up : https://localhost:8501
```

#### Techstack Used:
- Python
- LangChain
- Streamlit
- PaLM2
- FAISS