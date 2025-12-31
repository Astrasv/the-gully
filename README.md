# The Gully 

```
[WORK IN PROGRESS - PITCH IS GETTING READY] 

[THE CORE AGENTS WORK THOUGH]
```

🏏 Ask anything about IPL history in plain English and get answers straight from the ball-by-ball database.

**"How many wides did Pathirana bowl?"**  
**"How many reviews did Nitin Menon give favouring MI?"**  
**"How many sixes did MSD hit in death overs in entire IPL history"**

You name it we answer it

This project turns a single denormalized PostgreSQL table containing IPL ball-by-ball data into a natural-language interface — no SQL knowledge required.

*Fun Fact:*
The most common way of taking wickets in death overs (16–20 overs) is by **caught dismissals**, accounting for **2,671 wickets**. This method dominates wicket-taking in the final five overs of IPL matches.

The dataset is available public curated by me - [Kaggle Link](https://www.kaggle.com/datasets/astrasv247/ipl-dataset-2008-2025-ball-by-ball/data)


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

   For CLI version
    ```bash
    python main.py
   ```

   or 

   For seeing current dummy frontend
   ```bash
    python -m strealit run frontend_dummy/app.py
   ```

## Dummy Frontend Sample Output
![Sample Output](assets\image.png)