---
description: Generate CRUD operations for PLAN Pro Stack (Python/Rust/Next.js)
---

# CRUD Scaffolding Command

Generate a complete CRUD implementation for the specified entity using the PLAN Pro Stack architecture.

## Arguments

- `$ARGUMENTS` - Entity name and optional layer specification (e.g., "User" or "Product:python,nextjs")

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

### For Rust Layer (if specified or all)

Generate:
1. **Domain Model** (`src/models/{entity}.rs`)
   - Struct with Serde derive
   - CreateEntity/UpdateEntity variants
   - SQLx FromRow implementation

2. **Axum Handlers** (`src/handlers/{entity}.rs`)
   - get_all, get_by_id, create, update, delete handlers
   - Proper error handling with AppError

3. **SQLx Migration** (`migrations/{timestamp}_create_{entity}.sql`)
   - CREATE TABLE statement
   - Indexes for common queries

4. **Route Registration** (update `src/routes.rs`)
   - Mount handlers on appropriate paths

### For Next.js Layer (if specified or all)

Generate:
1. **Zustand Store** (`stores/{entity}Store.ts`)
   - State: items, loading, error
   - Actions: getItems, addItem, updateItem, removeItem

2. **React Components**
   - `components/{Entity}List.tsx`
   - `components/{Entity}Form.tsx`
   - `components/{Entity}Detail.tsx`

3. **API Routes** (`app/api/{entity}/route.ts`)
   - GET, POST handlers

4. **API Route with ID** (`app/api/{entity}/[id]/route.ts`)
   - GET, PUT, DELETE handlers

5. **Page Component** (`app/{entity}/page.tsx`)
   - Server component with data fetching

## Output Format

Create files in appropriate directories following PLAN Pro Stack conventions. Report what was generated.
