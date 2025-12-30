# The Gully 


The dataset is available public - [Kaggle Link](https://www.kaggle.com/datasets/astrasv247/ipl-dataset-2008-2025-ball-by-ball/data)



## Run the preprocessing pipeline





1. **Clone and navigate to the project:**
   ```bash
   git clone https://github.com/Astrasv/the-gully.git
   cd gully
   ```
    Download the official JSON from [Cricsheet Website for IPL](https://cricsheet.org/matches/) and store it as `ipl_json` in `gully` directory

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

3. **Create Virtual Environment:**
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
   ```
4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
   ```
5. **Run the pipeline**

    ```bash
    python main.py
   ```
This project is based on IPL cricket. Currently this includes data preprocessing steps for a completely denormalized ball by ball IPL data. The projects aims for much more. 



Will be revealed soon

