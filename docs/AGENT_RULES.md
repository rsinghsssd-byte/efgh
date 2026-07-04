# AI Blog Generator - Agent Rules

## Purpose

This document defines how the AI coding agent (Antigravity) should work on this project.

Before starting any task, always read:

1. PROJECT_SPEC.md
2. ARCHITECTURE.md
3. TASKS.md
4. AGENT_RULES.md

These documents together define the project's requirements, architecture, roadmap, and coding guidelines.

---

# Primary Objective

Develop a production-ready Django application while preserving code quality, maintainability, and scalability.

Never optimize for speed at the cost of maintainability.

---

# General Rules

- Complete only the requested task.
- Never implement unrelated features.
- Never modify project architecture unless instructed.
- Never rename folders or applications without approval.
- Preserve existing project structure.
- Keep the project runnable after every task.

---

# Existing Project Structure

The current structure is considered the source of truth.

Do not move or rename folders.

Do not reorganize the project unless explicitly instructed.

---

# UI Rules

The UI has already been designed using Stitch AI.

Do NOT

- redesign pages
- replace layouts
- change styling
- remove components

unless explicitly instructed.

Only connect existing UI with Django.

---

# Django Rules

Follow Django best practices.

Views should

- receive request
- validate input
- call services
- return response

Views must not contain business logic.

Business logic belongs in reusable services.

---

# Models

Create models only when required.

Avoid unnecessary tables.

Use meaningful relationships.

Prefer ForeignKey over duplicated data.

---

# URLs

Keep URLs clean and consistent.

Example

/

accounts/login/

dashboard/

blogs/

generator/

Use lowercase paths.

---

# Templates

Organize templates by application.

Example

templates/

    accounts/

    dashboard/

    blogs/

    generator/

Use template inheritance.

Every page should extend

base.html

when applicable.

---

# Static Files

Use

static/

for CSS, JavaScript, fonts, and images.

Never place generated images inside static.

Generated files belong inside media.

---

# Media

Generated blog images should be stored inside

media/

    blogs/

        user_id/

            blog_id/

Never overwrite existing user files.

---

# Authentication

Authentication provider

Supabase Auth

Support

- Google OAuth

Future support

- GitHub OAuth

Validate JWTs securely.

Never expose secrets.

---

# AI Integration

Supported providers

- Gemini
- OpenRouter
- OpenAI (optional)

The provider should be replaceable without changing the rest of the application.

Avoid tightly coupling code to one provider.

---

# Image Generation

Generate contextual images.

Store

- image
- prompt
- alt text

Associate every image with a blog.

---

# Error Handling

Never crash the application.

Handle

- invalid requests
- API failures
- missing credentials
- authentication failures

Display user-friendly messages.

Log technical details.

---

# Logging

Log

- authentication
- blog generation
- image generation
- API failures
- unexpected exceptions

Never log

- passwords
- JWT tokens
- API keys
- secrets

---

# Code Style

Follow PEP 8.

Write readable code.

Prefer clarity over cleverness.

Keep functions focused.

Avoid duplicated logic.

Use descriptive names.

Use type hints where practical.

---

# Dependencies

Do not introduce new dependencies unless necessary.

Prefer Django's built-in functionality.

If a new package is required, explain why.

---

# Security

Never

- hardcode credentials
- commit secrets
- expose service role keys

Use environment variables for all sensitive data.

---

# Database

Primary database

Supabase PostgreSQL

Design normalized models.

Avoid storing duplicate information.

---

# API Communication

Wrap all external API communication inside reusable service modules.

Do not call external APIs directly from views.

---

# Development Workflow

For every task

1. Read project documentation.
2. Understand the requested feature.
3. Identify affected files.
4. Explain the implementation plan.
5. Implement the feature.
6. Verify imports.
7. Verify URLs.
8. Ensure project runs.
9. Summarize completed work.

---

# Before Creating Files

Check whether a similar file already exists.

Reuse existing code whenever possible.

Avoid creating duplicate utilities.

---

# Before Modifying Files

Understand the existing implementation.

Preserve backward compatibility.

Avoid unnecessary refactoring.

---

# Documentation

When implementing a significant feature

Update

- TASKS.md
- relevant documentation

if necessary.

---

# Git

Every completed feature should represent a logical commit.

Avoid partially completed implementations.

---

# Communication Style

When responding

- Explain what will be changed.
- Mention affected files.
- State assumptions.
- Highlight potential risks.

Do not generate unnecessary explanations.

Focus on implementation.

---

# Completion Criteria

A task is considered complete only if

- code compiles
- imports resolve
- URLs work
- templates render
- no syntax errors exist
- project remains runnable

---

# Guiding Principle

Prioritize correctness, maintainability, readability, and consistency over speed.

Always produce production-ready Django code that fits naturally into the existing project structure.