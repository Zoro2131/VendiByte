# VendiStep — Database Migration & Testing Guide

## Purpose

This document outlines the process for creating, updating, migrating, and verifying PostgreSQL database tables using SQLAlchemy and Alembic.

**Technology Stack**
- Python
- SQLAlchemy 2.x
- Alembic
- PostgreSQL
- pgAdmin 4
- FastAPI

## 1. Create or Update a SQLAlchemy Model

Location: `backend/app/models/`

Each model represents a database table. Attributes represent columns, and model instances represent rows.

Example:

```python
class VendingMachine(Base):
    __tablename__ = "vending_machines"

    vendingMachineName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
```

Verify that the model imports correctly and that all intended columns have been defined.

## 2. Register the Model With Alembic

Location: `backend/alembic/env.py`

```python
from app.database.base import Base
from app.models.vending_machine import VendingMachine

target_metadata = Base.metadata
```

Importing the model registers its table with SQLAlchemy metadata.

Alembic uses this metadata to detect schema changes.

## 3. Verify Model Registration

Open PowerShell in the `backend` directory with the Python virtual environment activated.

```powershell
python -c "from app.database.base import Base; from app.models.vending_machine import VendingMachine; print(list(Base.metadata.tables.keys()))"
```

Expected result:

```text
['vending_machines']
```

If the table does not appear, verify the model import and `Base` inheritance.

## 4. Generate an Alembic Migration

```powershell
alembic revision --autogenerate -m "describe database changes"
```

Example:

```powershell
alembic revision --autogenerate -m "create vending machines table"
```

Alembic compares SQLAlchemy metadata against the existing PostgreSQL schema.

The migration file is generated under:

`backend/alembic/versions/`

**Important:** Generating a migration does not modify the database.

## 5. Review the Generated Migration

Open the new migration file.

Check the `upgrade()` function for:

- Correct table names
- Correct column names and data types
- Primary keys and foreign keys
- Nullable constraints
- Indexes and unique constraints
- Intended database-level defaults

Check `downgrade()` for the appropriate rollback operations.

Do not apply migrations without reviewing them.

Note: SQLAlchemy `default=` values are Python-side defaults and generally do not appear as PostgreSQL server defaults. Use `server_default=` when a database-side default is required.

## 6. Apply the Migration

```powershell
alembic upgrade head
```

This executes pending migrations against PostgreSQL.

Expected output includes a message similar to:

```text
Running upgrade -> 341e5fc80e0a, create vending machines table
```

## 7. Verify the Applied Migration

```powershell
alembic current
```

For our first migration, the expected result is:

```text
341e5fc80e0a (head)
```

This confirms that the database is at the latest migration revision.

## 8. Inspect the Table in pgAdmin 4

Navigate to:

`Servers → PostgreSQL → Databases → vendistep → Schemas → public → Tables`

Refresh the Tables folder if necessary.

To inspect the columns:

`vending_machines → Columns`

To inspect stored rows:

Right-click `vending_machines` → **View/Edit Data → All Rows**

Alternatively, open Query Tool and execute:

```sql
SELECT * FROM public.vending_machines;
```

A newly created table will have no records until data is inserted.

## 9. Test Database Operations

After creating the table, test the following through the application's SQLAlchemy session or API endpoints:

- Create a record
- Retrieve the record
- Update a field
- Delete the record
- Confirm required fields and constraints behave correctly
- Verify the results in pgAdmin

These tests confirm that the database structure and application behavior work together.

## 10. Repeat the Development Loop

Whenever a model's database structure changes:

1. Update the SQLAlchemy model.
2. Verify model registration.
3. Generate a new Alembic migration.
4. Review the generated migration.
5. Apply the migration.
6. Check `alembic current`.
7. Inspect the database in pgAdmin.
8. Test relevant CRUD operations.

**Do not run `alembic init alembic` again.** Initialization is only required once per project.

Do not modify an already-applied migration to introduce new schema changes. Generate a new migration instead.

## 11. Useful Commands

| Command | Purpose |
|---|---|
| `alembic current` | Show the applied database revision |
| `alembic heads` | Show the latest migration head(s) |
| `alembic history` | Show migration history |
| `alembic revision --autogenerate -m "message"` | Generate a migration |
| `alembic upgrade head` | Apply pending migrations |
| `alembic downgrade -1` | Roll back one revision |

**Warning:** Downgrades can delete tables or data. Review the migration before executing a rollback.

## First Completed Migration

**Date:** October 9, 2026

**Model:** VendingMachine

**Table:** `vending_machines`

**Migration revision:** `341e5fc80e0a`

**Status:** Successfully generated and applied.

**Next development tasks:**
- Define allowed `vendingMachineAccessType` values.
- Implement CRUD operations.
- Test inserting and retrieving vending machines.
- Connect the FastAPI endpoints to PostgreSQL.