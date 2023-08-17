# Intérroger mon PDF



Je vous remercie de l'intérêt que vous portez à ce projet. Veuillez noter qu'il ne s'agit que d'une **preuve de concept** et qu'elle peut contenir des bogues ou des fonctionnalités inachevées. En particulier, les prompts et les appels aux fonctions de la librairie LangChain sont appelées à évoluer.



### Intérroger un PDF  - Système de réponse aux questions sur un PDF basé sur GPT3.5



🎲 Le premier cas d'utilisation de cette application est d'aider les utilisateurs à répondre à des questions sur les règles des jeux de société en se basant sur le manuel d'instructions. Bien que l'application puisse être utilisée pour d'autres tâches, aider les utilisateurs à répondre aux règles des jeux de société est particulièrement important pour moi, car je suis moi-même un fervent amateur de jeux de société. En outre, ce cas d'utilisation est relativement inoffensif, même dans les cas où le modèle peut avoir des hallucinations.



🌐 L'application est accessible sur le Cloud communautaire Streamlit [en cliquant ici](https://interroger-un-pdf-pour-iavenir.streamlit.app/). Toutefois, pour utiliser l'application, vous devez disposer de votre propre [OpenAI's API key](https://platform.openai.com/account/api-keys).



📄 L'application met en œuvre les documents académiques suivants :

- [In-Context Retrieval-Augmented Language Models](https://arxiv.org/abs/2302.00083) aka **RALM**

- [Precise Zero-Shot Dense Retrieval without Relevance Labels](https://arxiv.org/abs/2212.10496) aka **HyDE** (Hypothetical Document Embeddings)

L'application va évoluer avec l'implémentation des [fonctions de résumés de LangChain](https://python.langchain.com/docs/use_cases/summarization).

### Installation



1. Cloner le repo:

   `git clone https://github.com/mobarski/ask-my-pdf`

2. Installer les dependencies:

   `pip install -r ask-my-pdf/requirements.txt`

3. Lancer l'app:

   `cd interroger-mon-pdf/src`
   
   `run.sh` or `run.bat`



### High-level documentation



#### RALM + HyDE

![RALM + HyDE](docs/ralm_hyde.jpg)



#### RALM + HyDE + context

![RALM + HyDE + context](docs/ralm_hyde_wc.jpg)



### Variables d'environnement utilisées pour la configuration



##### General configuration:

- **STORAGE_SALT** - cryptograpic salt used when deriving user/folder name and encryption key from API key, hexadecimal notation, 2-16 characters

- **STORAGE_MODE** - index storage mode:  S3, LOCAL, DICT (default)

- **STATS_MODE** - usage stats storage mode: REDIS, DICT (default)

- **FEEDBACK_MODE** - user feedback storage mode: REDIS, NONE (default)

- **CACHE_MODE** - embeddings cache mode: S3, DISK, NONE (default)

  

##### Local filesystem configuration (storage / cache):

- **STORAGE_PATH** - directory path for index storage

- **CACHE_PATH** - directory path for embeddings cache

  

##### S3 configuration (storage / cache):

- **S3_REGION** - region code

- **S3_BUCKET** - bucket name (storage)

- **S3_SECRET** - secret key

- **S3_KEY** - access key

- **S3_URL** - URL

- **S3_PREFIX** - object name prefix

- **S3_CACHE_BUCKET** - bucket name (cache)

- **S3_CACHE_PREFIX** - object name prefix (cache)

  

##### Redis configuration (for persistent usage statistics / user feedback):

- **REDIS_URL** - Redis DB URL (redis[s]://:password@host:port/[db])

  

##### Community version related options:

- **OPENAI_KEY** - API key used for the default user
- **COMMUNITY_DAILY_USD** - default user's daily budget
- **COMMUNITY_USER** - default user's code

