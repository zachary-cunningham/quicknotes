Makes sense. Rebuilding now.

---

# Django REST Framework — Study Guide & Homework

## The bigger picture

Web apps traditionally serve **HTML pages**. Django handles a request, queries the database, stuffs data into a template, and returns a webpage. That's fine when a browser is the only consumer.

But what if a mobile app needs your data? Or a React frontend? Or another service? They don't want HTML — they want raw data, usually JSON, so they can decide how to display it themselves. That's what an API is: your app exposing its data in a format any client can consume.

The problem is doing this in raw Django is tedious. For every endpoint you'd manually:
- parse the incoming request body
- validate the data yourself
- convert your model objects to JSON by hand
- handle every HTTP method (GET, POST, PUT, DELETE) with if/else logic
- write every URL pattern manually

Django REST Framework (DRF) is a library that handles all of that boilerplate. It gives you a set of building blocks that slot together into a repeatable pattern. Once you know the pattern, building a new API is mostly filling in the blanks.

---

## The pattern — how the pieces connect

Every DRF API follows this loop:

```
HTTP Request
    ↓
urls.py  →  routes the request to the right ViewSet
    ↓
ViewSet  →  decides what action to take (list, create, update, delete)
    ↓
Serializer  →  validates incoming data / converts outgoing data to JSON
    ↓
Model  →  reads or writes to the database
    ↓
HTTP Response (JSON)
```

Think of building a DRF API as a checklist:
- [ ] Define your **Model** (what data you're storing)
- [ ] Write a **Serializer** (how that data becomes JSON)
- [ ] Write a **ViewSet** (what actions are available)
- [ ] Register it with a **Router** (what URLs map to those actions)

That's it. Every DRF API you ever build follows this same four-step checklist.

---

## Each component explained

### Model
This is plain Django — nothing DRF-specific. It's just the database table. DRF sits on top of whatever models you already have.

---

### Serializer
Your database stores Python objects. HTTP speaks JSON. A Serializer is the translator between them — it works in both directions:

- **Outgoing:** takes a model object from the database and converts it to a JSON-friendly dictionary
- **Incoming:** takes raw JSON from a request, validates it (are all required fields present? are the types correct?), and prepares it to be saved

Without a serializer you'd be writing `json.loads()`, manually checking every field, then manually calling `.save()`. The serializer wraps all of that into one reusable class.

`ModelSerializer` specifically is a shortcut — it reads your model's field definitions and generates the serializer fields automatically, so you don't have to redeclare every field by hand.

---

### ViewSet
A ViewSet is a class that groups all the actions for one resource in one place. Instead of writing six separate view functions (one for listing, one for creating, one for retrieving a single item, etc.), you write one ViewSet and DRF generates all six.

`ModelViewSet` is the fully-loaded version — it gives you list, create, retrieve, update, partial update, and delete out of the box. You can override any of them if you need custom behaviour, or remove ones you don't want.

---

### Router
The Router connects your ViewSet to URLs automatically. You register your ViewSet once:

```python
router.register(r'notes', NoteViewSet)
```

And it generates all the URL patterns for you — the collection endpoint (`/api/notes/`) and the single-item endpoint (`/api/notes/1/`), wired to the correct ViewSet actions.

Without a router you'd write each URL pattern manually and map it to a specific action yourself.

---

## Learning more — reading & resources

The course gives you a working example but skips the why behind most decisions. To actually understand what you're doing:

**Start here:** Work through the official DRF tutorial in order — all six parts. It's well-written and covers everything from this module plus the next several steps (authentication, permissions). Don't skip parts.
→ https://www.django-rest-framework.org/tutorial/quickstart/

**Particularly useful reference:** Classy DRF shows you the full inheritance tree of every DRF class — what methods a ModelViewSet has, where they come from, what you can override. Bookmark it.
→ https://www.cdrf.co/

**For serializers specifically**, this article goes deeper than the docs and explains the parts the docs assume you already know:
→ https://testdriven.io/blog/drf-serializers/

---

**Bonus — not essential yet:** Once you're comfortable with the basics, skim the FastAPI getting-started docs. FastAPI is a different Python framework that also builds APIs, but approaches it completely differently. You don't need to learn it now — but seeing the contrast will sharpen your understanding of the choices DRF makes and why.
→ https://fastapi.tiangolo.com/tutorial/

---

## Exercises — each component

These are deliberately repetitive. The goal is that connecting the four pieces becomes automatic.

**Serializer**
- Add a new field to your Note model (e.g. `created_at`, auto-populated). Add it to the serializer and confirm it appears in the API response.
- Make one field optional with a default value. POST without that field and confirm it still saves.
- Add a computed field that doesn't exist on the model (e.g. `word_count` derived from the content). It should appear in GET responses but be ignored on POST.

**ViewSet**
- Override `list()` to return notes in reverse creation order.
- Override `destroy()` so instead of deleting the record, it sets an `is_archived` boolean to True. Confirm the note still exists in the database after a DELETE request.
- Add a custom endpoint `GET /api/notes/count/` that returns just the total number of notes. (Look up the `@action` decorator in the DRF docs.)

**Router/URLs**
- Print out every URL pattern the router generates (you can do this in the Django shell: `print(router.urls)`). Map each one to the ViewSet action it calls.
- Manually write the URL patterns without the router to produce the same result. Then switch back to the router.

---

## Consolidation project

Build a basic **Book collection API** from scratch without referencing the quicknotes code. Use the docs.

- [ ] Model: `Book` with title, author, year published, and read status (boolean)
- [ ] Serializer: all four fields exposed, year validated to be a reasonable value (not in the future), computed field `display_name` that returns `"Title by Author"`
- [ ] ViewSet: full CRUD, plus a custom action `GET /api/books/unread/` that returns only books where read is False
- [ ] Router: register and confirm all URLs work
- [ ] Test every endpoint manually: create a book, list all books, retrieve one, update it, mark it as read, delete it

Nothing outside what's been covered above. The point is connecting the four pieces yourself, not building a feature-complete app.