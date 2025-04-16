
## 💡 Project: **NeuroLogX – Smart Log Intelligence System with Lucene & Deep Learning**

---

### 🧠 Concept

**NeuroLogX** is an intelligent log analysis platform that stores and indexes logs using **Apache Lucene**, then applies **deep learning** models (CNNs, Transformers) to classify, detect anomalies, and extract insights from those logs. The project simulates a real AIOps system with log ingestion, storage, and neural-powered analytics.

---

## 🔧 Key Components

| Component                | Tech Stack                                   |
|--------------------------|----------------------------------------------|
| Log Storage/Search       | Apache Lucene                                |
| Log Generator            | Python + Faker + Simulated Errors            |
| Log Classifier           | CNN / LSTM (Keras)                           |
| Dashboard                | Streamlit for visual insights                |

---

## 📂 Project Structure

```
neurologx/
├── lucene_indexer/          # Java/Python code for indexing/searching logs
│   ├── index                # Index logs
│   └── lib                  # Lucene 10.2.0 jar files
├── data/                    # Logs and model-ready datasets
├── dashboard/               # Visualization tool
│   ├── dashboard.py         
├── utils/
│   ├── log_generator.py     # Python + Faker + Simulated Errors 
│   └── log_classifier.py    # CNN / LSTM (Keras)
└── README.md
```


## ⚙️ How It Works

1. **📝 Simulate Logs**  
   Use Python (`Faker`, `random`, `datetime`) to generate synthetic logs:
   - Log levels: 'INFO', 'DEBUG', 'WARN', 'ERROR', 'CRITICAL'
   - Components: 'AuthService', 'DBService', 'Network', 'Cache', 'APIGateway'
   - Anomaly_phrases = 'Segmentation fault', 'OutOfMemoryError', 'Connection timed out', 'Database locked', 'Permission denied', 'System overheating'
   - Inject random error patterns to create labeled anomalies

2. **📦 Store Logs in Lucene**  
   - Write a simple **Java** script to index logs with Lucene
   - Each log is a document with fields: timestamp, level, component, message, label

3. **🔍 Query Logs with Lucene**
   - Search logs using keywords or time ranges (Default searches all)
   - Extract logs for training/testing to a csv file

4. **🤖 Apply Deep Learning**
   - Preprocess logs (tokenize, pad, embed)
   - Train:
     - **CNN/LSTM classifier** to build a deep learning classifier to predict log categories

5. **📊 Dashboard (Optional)**
   - Show:
     - Sample Predictions
     - Label Distribution
     - Classifier to Predict Logs

---

## 🧠 Example Use Cases

- Predict whether a new log is likely an error or critical issue
- Automatically highlight anomalous logs from thousands of entries
- Search log events related to specific failures
- Visualize log distribution over time and subsystems

---

## 🚀 Stretch Goals

- Use **FAISS or vector DB** to store BERT embeddings of logs for semantic search
- Integrate **OpenAI/LLM** to summarize patterns in recent logs
- Auto-generate incident reports based on clusters of log anomalies

---

## ✅ Why It Matters?

- ✅ Uses **Lucene** (full-text search DB) like in observability tools
- ✅ Demonstrates **deep learning** for NLP/log classification
- ✅ Simulates **anomaly detection**, **root cause**, and **reporting**
- ✅ Involves **data pipelines**, **ML deployment**, and **dashboards**
- ✅ Can integrate with **cloud**, **AIOps**, and **IT ops data**


### 🔧 Project Run Instructions

#### 1. Generate Sample Logs
```bash
python lucene/utils/log_generator.py
```

#### 2. Build and Run the Lucene Indexer
```bash
cd lucene_indexer
javac -cp "lib/*" LuceneLogIndexer.java
java -cp ".;lib/*" LuceneLogIndexer
```

#### 3. Export Indexed Logs
```bash
javac -cp "lib/*" LuceneLogExporter.java
java -cp ".;lib/*" LuceneLogExporter
```

#### 4. Run the Log Classifier
```bash
cd ..
python lucene/utils/log_classifier.py
```

#### 5. Launch the Dashboard
```bash
cd dashboard
python -m streamlit run dashboard.py
```

➡️ Open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

### 📝 Add Your Own Logs

Copy and paste logs in the dashboard input area:

```json
{"timestamp": "2025-04-16 10:34:35", "level": "INFO", "component": "Cache", "message": "Listen current most ok."}
{"timestamp": "2025-04-16 11:03:46", "level": "ERROR", "component": "AuthService", "message": "System overheating"}
```
### Thank you!

Zeliha Ural Merpez