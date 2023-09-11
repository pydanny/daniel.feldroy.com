---

# Robyn - A Python rust framework

Robyn is a fast async Python framework with a Rust runtime

- gh/sansyrox/robyn
- @robyn_oss

# Why do we need another framework?

Comparing frameworks

- Perfomance
- Easy of use
- Scalability
- Built-in features
- Extensibility
- Hacker friendliness / Developer experience
- Community
- End-to-end app creation timeline

# Performance

- Uses a multi-threaded Rust runtime
- Bypasses GIL for increased performance
- Python code converted to Rust objects
- In addition to multi-threads, also does multiple processes and workers

# Easy of use

```
Reverse Proxy => WebServer (*sgi) => Framework (Django, Flask, FastAPI) 
```

Robyn's API is very similar to Flask

Doesn't use *sgi, instead is is the webserver + framework

How Robyn does it

```
Reverse Proxy => WebServer+FrameworkFastAPI) 
```

# Built-in Features

- Supports FBVs, middlewares, application events, etc
- Jinja templates
- Add your own template engine
- Works with Strawberry

# Hacker friendliness / Developer experience

- Const Requests allow you to use consts as psuedo-caching of values
- Easy support for websockets
- Deployment simplicity

# End-to-end app creation timeline

Create new robyn app

```
python -m robyn --create
```

docs

```
python -m robyn --docs
```

# Community

- Discord
- Community growth is constant and stable
- Feature growth comes from community
- gh/sparckles/robyn

# Future Roadmap

- Performance optimization
- OpenAPI docs generation
- Runtime Data Validation (like FastAPI)
- Add ORM support, especially Prisma (why not SQLAlchemy?)
- Improve websockets
-

# Links

- 
