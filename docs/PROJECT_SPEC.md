# AI Blog Generator

## Project Overview

AI Blog Generator is a Django-based web application that allows users to generate rich, SEO-optimized blog posts using Large Language Models (LLMs). The application supports OAuth authentication, AI-powered blog generation, AI image generation, rich content blocks, blog management, and personalized user workspaces.

The frontend is generated using Stitch AI and should remain visually unchanged unless explicitly instructed.

---

# Objectives

- Generate high-quality AI blogs
- Generate contextual images
- Save blogs for authenticated users
- Support blog editing
- Export blogs
- Provide a clean and modern UI
- Keep the project modular and maintainable

---

# Tech Stack

## Backend

- Django
- Python 3.13+

## Authentication

- Supabase Auth
- Google OAuth
- GitHub OAuth (Future)

## Database

- Supabase PostgreSQL

## AI

- Gemini
- OpenRouter
- OpenAI (Optional)

## Image Generation

- FLUX
- Pollinations
- HuggingFace Models

## Frontend

- HTML
- CSS
- JavaScript
- Stitch AI Generated UI

## Deployment

- Render

---

# Current Project Structure

```
AI_Blog_Generator/

apps/
    accounts/
    blogs/
    dashboard/
    generator/
    core/

config/

services/

templates/

static/

media/

tests/

docs/

manage.py
```

This structure should not be changed unless explicitly requested.

---

# Application Modules

## Accounts

Responsibilities

- Login
- Signup
- Logout
- OAuth
- User Profile
- JWT Authentication

---

## Dashboard

Responsibilities

- Home
- Recent Blogs
- Statistics
- User Overview

---

## Blogs

Responsibilities

- Create
- Read
- Update
- Delete
- Search
- Favorites
- History

---

## Generator

Responsibilities

- Blog Generation
- Prompt Building
- Image Generation
- SEO
- Rich Content

---

## Core

Contains shared utilities and reusable functionality.

---

# Authentication Flow

User

↓

Google OAuth

↓

Supabase Authentication

↓

JWT Token

↓

Django Validation

↓

Create/Get User

↓

Dashboard

---

# Blog Generation Flow

Topic

↓

Prompt Builder

↓

LLM

↓

Blog Draft

↓

Rich Content Processing

↓

Image Generation

↓

SEO Optimization

↓

Save Blog

↓

Display Blog

---

# Rich Content

Blogs may contain

- Headings
- Paragraphs
- Lists
- Tables
- Code Blocks
- Images
- Quotes
- Tips
- Warnings
- FAQs
- Summary

---

# User Features

- Register
- Login
- Logout
- Generate Blog
- Save Blog
- Edit Blog
- Delete Blog
- Favorite Blog
- Search Blogs
- View History
- Manage Profile
- Change Settings

---

# Image Generation

Images should be generated based on paragraph context.

Each generated image should be stored with its corresponding blog.

---

# Future Features

- Markdown Import
- PDF Export
- DOCX Export
- Mermaid Diagrams
- AI Rewrite
- AI Summarization
- AI Translation
- Team Workspace

---

# Development Guidelines

- Follow Django best practices.
- Keep views thin.
- Keep business logic modular.
- Reuse components whenever possible.
- Preserve the existing folder structure.
- Write readable, maintainable code.
- Avoid unnecessary complexity.
- Do not change UI unless requested.

---

# Important Rules

- Never break existing functionality.
- Do not rename folders unless instructed.
- Ask before making architectural changes.
- Prefer reusable code over duplication.
- Keep the code production-ready.

---

# Current Development Stage

The project is currently under active development.

Authentication is the first major feature being implemented.

All remaining features will be built incrementally.