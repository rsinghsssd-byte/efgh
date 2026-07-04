# AI Blog Generator - Project Context

## Purpose

This document provides the background, reasoning, and long-term vision for the AI Blog Generator project.

Unlike PROJECT_SPEC.md, this document explains **why** decisions were made, not just **what** should be built.

Read this document before implementing any feature.

---

# Project Vision

The goal is to build an AI-powered blog generation platform that produces high-quality, editable, SEO-friendly blogs with contextual AI-generated images.

The application should feel like a modern SaaS product rather than a simple text generator.

Users should be able to generate, edit, manage, and export blogs from one place.

---

# Why Django?

Django was selected because it provides:

- Mature architecture
- Excellent ORM
- Built-in admin
- Authentication support
- Scalability
- Large ecosystem
- Easy deployment

The backend should remain Django-centric.

---

# Why Supabase?

Supabase is used because it provides:

- PostgreSQL
- OAuth Authentication
- JWT Support
- Storage
- Row-Level Security
- Easy scalability

Instead of replacing Django's authentication system, Supabase should act as the authentication provider while Django manages the application logic.

---

# Why Stitch AI?

The frontend was designed using Stitch AI.

The generated UI should be considered the design source of truth.

The objective is to integrate it into Django rather than redesign it.

Only modify the UI when explicitly requested.

---

# Why Antigravity?

This project is also a learning exercise.

The goal is not only to build the application but to understand how AI coding agents can contribute to real-world software development.

The AI agent acts as a software engineer.

The human acts as the software architect.

Architecture and technical decisions remain under human control.

---

# AI Philosophy

The project should support multiple AI providers.

Examples include:

- Gemini
- OpenRouter
- OpenAI
- Future providers

The application should never depend on a single LLM.

Changing the model should require minimal code changes.

---

# Image Generation Philosophy

Images should be generated based on the content of the corresponding blog section.

The system should support multiple image providers.

Possible providers include:

- FLUX
- Pollinations
- Hugging Face models

The image generation implementation should be replaceable.

---

# Rich Content Philosophy

The application should generate more than plain text.

Blogs may include:

- Headings
- Lists
- Tables
- Code blocks
- Quotes
- Tips
- Warnings
- Images
- FAQs
- Summaries

The application should be capable of rendering structured content cleanly.

---

# Storage Philosophy

Generated blogs belong to authenticated users.

Users should only access their own content unless explicit sharing features are added.

Generated images should remain linked to their corresponding blog.

---

# Scalability

The architecture should support future features without major restructuring.

Examples:

- Additional AI models
- Team workspaces
- Public blogs
- Scheduled publishing
- Analytics
- AI assistants
- Mobile application
- Public API

---

# Development Philosophy

Build one complete feature at a time.

Each feature should be:

- implemented
- tested
- reviewed
- committed

before moving to the next.

Avoid partially completed features.

---

# UI Philosophy

Backend functionality should adapt to the existing UI.

Avoid redesigning pages.

If new UI elements are required, they should match the existing design language.

---

# Code Philosophy

The project should prioritize:

- readability
- maintainability
- modularity
- production readiness

Avoid unnecessary abstractions.

Prefer simple, understandable solutions.

---

# Security Philosophy

Never expose:

- API keys
- JWT secrets
- service role keys

Always use environment variables.

Validate authentication on the server.

Never trust client-side data.

---

# Error Handling Philosophy

Applications should fail gracefully.

Users should receive clear error messages.

Developers should receive useful logs.

Unexpected failures should never expose internal implementation details.

---

# Performance Philosophy

Optimize only when necessary.

Correctness is more important than premature optimization.

When optimization is required, prefer improvements that preserve readability.

---

# Documentation Philosophy

Documentation is part of the project.

When architecture changes significantly, update the documentation before implementing additional features.

The documentation should always reflect the current state of the project.

---

# Long-Term Goal

The final product should be a production-ready AI blogging platform that demonstrates:

- Modern Django architecture
- AI-assisted development
- Multiple AI integrations
- Maintainable software design
- Professional code quality

This project should serve both as a usable application and as a reference implementation for building AI-powered web applications.