# AI Blog Generator - Architecture Guide

## Purpose

This document defines the software architecture, coding standards, project organization, and development rules for the AI Blog Generator project.

All implementations should follow this document unless explicitly instructed otherwise.

---

# Architecture

The project follows Django's MTV architecture with clear separation of responsibilities.

```
Browser
    │
    ▼
URLs
    │
    ▼
Views
    │
    ▼
Services
    │
    ▼
Models
    │
    ▼
Supabase PostgreSQL
```

Views should never contain business logic.

Business logic should be delegated to services.

---

# Project Structure

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

docs/

tests/
```

Do not change this structure without approval.

---

# App Responsibilities

## accounts

Responsible for

- Login
- Signup
- Logout
- OAuth
- JWT Validation
- User Profile

No blog logic belongs here.

---

## dashboard

Responsible for

- Dashboard
- Statistics
- User Home
- Navigation

---

## blogs

Responsible for

- Blog CRUD
- Search
- History
- Favorites
- Export

No AI generation logic belongs here.

---

## generator

Responsible for

- Prompt Builder
- LLM Communication
- Image Generation
- Rich Content
- SEO

---

## core

Contains reusable utilities shared across multiple apps.

---

# Services Layer

The services folder contains integrations with external systems.

Examples

```
services/

    auth/

    ai/

    image/

    storage/

    seo/
```

Services should

- communicate with APIs
- process data
- contain reusable business logic

Views should call services instead of implementing API calls directly.

---

# URL Structure

```
/

accounts/

accounts/login/

accounts/signup/

/dashboard/

/blogs/

/blogs/<slug>/

/generator/

/profile/

/settings/
```

Use lowercase URLs.

Use hyphens instead of underscores where appropriate.

---

# Template Structure

```
templates/

    base.html

    accounts/

    dashboard/

    blogs/

    generator/

    partials/

    errors/
```

Every page should extend

```
base.html
```

Reusable UI components belong inside

```
partials/
```

---

# Static Files

```
static/

    css/

    js/

    images/

    fonts/
```

Keep application assets organized.

Avoid inline CSS and JavaScript whenever possible.

---

# Media

Generated images should be stored inside

```
media/

    blogs/

        user_id/

            blog_id/
```

Never mix uploaded assets with static assets.

---

# Models

Each Django app owns its own models.

Examples

accounts

- User Profile

blogs

- Blog
- Blog Section
- Image

generator

No persistent models unless required.

---

# Database

Primary database

Supabase PostgreSQL

Relationships

User

↓

Blogs

↓

Sections

↓

Images

Avoid unnecessary table duplication.

---

# Authentication

Authentication provider

Supabase

OAuth Providers

- Google

Future

- GitHub

Django should validate JWTs issued by Supabase.

---

# AI Architecture

```
User Prompt

↓

Prompt Builder

↓

LLM

↓

Raw Blog

↓

Rich Content Processor

↓

Image Prompt Builder

↓

Image Generator

↓

Save Blog
```

Every stage should be independent and replaceable.

---

# Image Generation

Generate one contextual image for each relevant section.

Each image should

- have alt text
- store prompt
- belong to a blog

---

# Rich Content

Supported content blocks

- Heading
- Paragraph
- List
- Table
- Code
- Quote
- Image
- Warning
- Tip
- FAQ
- Summary

Avoid storing blog content as a single large HTML string.

Prefer structured content.

---

# Coding Standards

Follow PEP 8.

Use meaningful names.

Keep functions small.

Avoid duplicated code.

Prefer composition over inheritance.

Use type hints where appropriate.

Document complex functions.

---

# Views

Views should only

- validate request
- call services
- render template
- return response

Views should NOT

- generate AI responses
- call external APIs directly
- contain large business logic

---

# Error Handling

Gracefully handle

- API failures
- Invalid input
- Missing authentication
- Missing images

Show user-friendly error messages.

Never expose stack traces.

---

# Logging

Log

- Authentication events
- AI generation
- Image generation
- API failures
- Unexpected exceptions

Do not log secrets or tokens.

---

# Security

Never expose

- API Keys
- JWT Secrets
- Service Role Keys

All secrets must come from

```
.env
```

Never hardcode credentials.

---

# Performance

Avoid duplicate API requests.

Cache reusable data where appropriate.

Optimize images before storing.

Paginate large result sets.

---

# Future Expansion

The architecture should allow future support for

- Multiple AI Providers
- Multiple Image Models
- Team Workspaces
- Public Blog Sharing
- AI Agents
- API Access

without major restructuring.

---

# Development Rules

Before implementing a feature

1. Read PROJECT_SPEC.md

2. Read TASKS.md

3. Read ARCHITECTURE.md

Only implement the requested task.

Do not implement unrelated features.

Do not change architecture without approval.

Preserve compatibility with existing code.

Always produce production-ready, maintainable Django code.