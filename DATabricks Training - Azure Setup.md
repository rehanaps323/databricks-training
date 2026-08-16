# Databricks Training - Azure Setup

This workspace contains Databricks training material. Start with **Intro to Python for Databricks** and keep answer keys separate from exercises.

## 1. Create the workspace folders

In Azure Databricks, create this folder under your user area:

```text
Databricks-Training/
  Intro to Python/
  Labs/
  Solutions/
  ML/
  DevOps/
```

## 2. Import the Python course

Import this local archive into `Databricks-Training/Intro to Python/`:

```text
Intro to Python for Databricks/DBC Archive/introduction-to-python-for-data-science-and-data-engineering-1.2.1 (1).dbc
```

Do not import the local HTML files as runnable notebooks. They are exported reading/reference pages. The `.dbc` archive and raw Databricks notebook-source files are the execution material.

## 3. Compute

Use the smallest available personal compute option:

- Single node
- Single user, assigned to your own account
- Auto-termination enabled, preferably 15-30 minutes
- Runtime compatible with the course; the course lesson documents DBR 13.3 LTS / Scala 2.12

If DBR 13.3 LTS is unavailable, use the closest supported LTS runtime and record any compatibility error before changing course files. Stop compute after each practice session to control Azure cost.

## 4. First validation

1. Open and attach `ITP 00 - Databricks Environment` to compute.
2. Run the simple Python cell that prints a message.
3. Open one lesson, such as `ITP 01 - Data Types and Variables`.
4. Complete its matching lab from the local `Labs/` material or imported lab folder.
5. Run the lab check/assertion cells.

Keep `Solutions/` closed until the lab is complete.

## 5. Setup scripts

`Includes/Classroom-Setup.py` may be required if a lesson reports that course state or datasets are not initialized.

Do **not** run `Includes/Workspace-Setup.py` for this personal learner workspace. It is instructor/admin automation that creates instance pools, cluster policies, and workspace entitlements.

## 6. Reading workflow

Use these local files for reading and navigation:

- `Intro to Python for Databricks/index.html`
- `Intro to Python for Databricks/AGENDA.html`
- The lesson HTML files

Run code in the imported Databricks notebooks. The exported HTML pages depend on external Databricks JavaScript and CSS, so they may not render fully offline.

## Information needed to continue

Provide these details after checking the workspace:

- Azure Databricks workspace URL
- Whether you can create folders and import `.dbc` files
- Whether you can create compute, or the name of an existing compute resource
- Which runtime versions are available
- The exact error text if import, compute creation, or notebook execution fails

Never send passwords, access tokens, client secrets, or other credentials.
