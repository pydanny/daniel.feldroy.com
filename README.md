# daniel-blog-air

```
uv run main.py
```

My site


## Adding alembic

```sh
alembic init migrations
```

In `migrations/env.py`, in the "add your model's MetaData object here" section:

```python
from models import SQLModel
target_metadata = SQLModel.metadata
```

Generate first migration

```sh
alembic revision --autogenerate -m "initial migration"
```

---

```sh
alembic init --template pyproject migrations
```

In `alembic.ini`, do:

```ini
sqlalchemy.url = postgresql://drg@localhost/danielblog
```

In `migrations/env.py`, in the "add your model's MetaData object here" section:

```python
from models import SQLModel
target_metadata = SQLModel.metadata
```