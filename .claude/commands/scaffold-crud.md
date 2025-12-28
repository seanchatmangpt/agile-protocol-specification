---
description: Generate CRUD operations for PLAN Pro Stack (Python/Elixir/Nuxt)
---

# CRUD Scaffolding Command

Generate a complete CRUD implementation for the specified entity using the PLAN Pro Stack architecture.

## Arguments

- `$ARGUMENTS` - Entity name and optional layer specification (e.g., "User" or "Product:python,nuxt")

## Task

Parse the entity name and layers from the arguments. If no layers specified, generate for all three layers.

### For Python Layer (if specified or all)

Generate:
1. **Pydantic Model** (`models/{entity}.py`)
   - Base model with fields
   - Create/Update variants
   - Validation rules

2. **FastAPI Router** (`routers/{entity}.py`)
   - GET /items - List all
   - GET /items/{id} - Get by ID
   - POST /items - Create new
   - PUT /items/{id} - Update existing
   - DELETE /items/{id} - Remove

3. **Typer CLI Command** (`commands/{entity}.py`)
   - list, get, create, update, delete subcommands

### For Elixir Layer (if specified or all)

Generate:
1. **Ash Resource** (`lib/app/{entity}.ex`)
   - Attributes with types
   - CRUD actions
   - Validations

2. **Phoenix Controller** (`lib/app_web/controllers/{entity}_controller.ex`)
   - index, show, create, update, delete actions

3. **Ecto Migration** (`priv/repo/migrations/{timestamp}_create_{entity}.exs`)

### For Nuxt Layer (if specified or all)

Generate:
1. **Pinia Store** (`stores/{entity}.ts`)
   - State: items, loading, error
   - Actions: getItems, addItem, updateItem, removeItem

2. **Vue Components**
   - `components/{Entity}List.vue`
   - `components/{Entity}Form.vue`
   - `components/{Entity}Detail.vue`

3. **API Composable** (`composables/use{Entity}Api.ts`)

## Output Format

Create files in appropriate directories following PLAN Pro Stack conventions. Report what was generated.
