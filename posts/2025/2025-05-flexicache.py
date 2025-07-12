import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2025-05-09T08:00:00.00Z"
        title: "Exploring flexicache"
        description: "An exploration of using flexicache for caching in Python."
        published: true
        tags:
          - python
          - fastcore
          - answerdotai
        time_to_read: 2
        type: post
        image: /public/images/exploring-flexicache.png
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When coding in Python I find I really like to use decorators to cache results from functions and methods, often to memory and sometimes to ephemeral stores like memcached. In fact, I've worked on and created several cache decorators, including [one](https://pypi.org/project/cached-property/) that influenced the implementation of the `@cached_property` decorator in Python 3.8. 

        A cache decorator called [flexicache](https://fastcore.fast.ai/xtras.html#flexicache) is part of the [fastcore](https://pypi.org/project/fastcore/) library. `flexicache` allows you to cache in memory results from functions and methods in a flexible way. Besides having an implementation of LRU caching, each use of the decorator can be configured to use one or more cache invalidation policies. 

        Two policies, `time_policy` and `mtime_policy` are used to invalidate the cache based on time and file modification time respectively. The `time_policy` invalidates the cache after a specified number of seconds, while the `mtime_policy` invalidates the cache if the file has been modified since the last time it was cached.

        Let's try it out!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Basic usage
        """
    )
    return


@app.cell
def _():
    # Import necessary libraries
    from fastcore.xtras import flexicache, time_policy, mtime_policy

    # Libraries used in testing cache validity and cache invalidation
    from random import randint
    from pathlib import Path
    from time import sleep
    return Path, flexicache, mtime_policy, randint, sleep, time_policy


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Here's a simple function returning a number between 1 to 1000 that we can show being cached. We'll use this in all our examples.
        """
    )
    return


@app.cell
def _(randint):
    def random_func(v):
        return randint(1, 1000)


    # Assert False as the function is not cached
    assert random_func(1) != random_func(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Time policy

        This is how we use the `time_policy` to cache the function.
        """
    )
    return


@app.cell
def _(flexicache, randint, time_policy):
    @flexicache(time_policy(0.1))
    def random_func_1():
        return randint(1, 1000)
    assert random_func_1() == random_func_1()
    return (random_func_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's use the sleep function to simulate time between calls to `random_func`.
        """
    )
    return


@app.cell
def _(random_func_1, sleep):
    _result = random_func_1()
    assert _result == random_func_1()
    sleep(0.2)
    assert _result != random_func_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### File modification time (mtime_policy)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We'll try with `mtime_policy`, checking to see if touching a file invalidates the cache. We'll use this site's `main.py` file as the file to touch.
        """
    )
    return


@app.cell
def _(flexicache, mtime_policy, randint):
    @flexicache(mtime_policy('../../main.py'))
    def random_func_2():
        return randint(1, 1000)
    assert random_func_2() == random_func_2()
    return (random_func_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now let's use the Path.touch() method to touch the file. This will update the file's modification time to the current time, which should invalidate the cache.
        """
    )
    return


@app.cell
def _(Path, random_func_2):
    _result = random_func_2()
    assert _result == random_func_2()
    Path('../../main.py').touch()
    assert _result != random_func_2()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using multiple policies
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        A unique feature of `flexicache` is that you can use multiple policies at the same time. This allows you to combine the benefits of different caching strategies.
        In this example, we'll use both `time_policy` and `mtime_policy` together. This means that the cache will be invalidated if either the time limit is reached or the file has been modified.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Testing the cache with both policies is identical to the previous examples. We'll call the function, first with the time policy, then with the mtime policy, and finally with both policies. We'll also touch the file to see if it invalidates the cache.
        """
    )
    return


@app.cell
def _(flexicache, mtime_policy, randint, time_policy):
    @flexicache(time_policy(0.1), mtime_policy('../../main.py'))
    def random_func_3():
        return randint(1, 1000)
    assert random_func_3() == random_func_3()
    return (random_func_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Testing time invalidation is the same as before. We'll call the function, wait for the time limit to be reached, and then call it again to see if the cache is invalidated.
        """
    )
    return


@app.cell
def _(random_func_3, sleep):
    _result = random_func_3()
    assert _result == random_func_3()
    sleep(0.2)
    assert _result != random_func_3()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Testing file timestamp is the same as before. We'll call the function, touch the file, and then call it again to see if the cache is invalidated.
        """
    )
    return


@app.cell
def _(Path, random_func_3):
    _result = random_func_3()
    assert _result == random_func_3()
    Path('../../main.py').touch()
    assert _result != random_func_3()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## What about LRU caching?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now let's test out the `flexicache` decorator to see how it behaves as an [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) replacement. For reference, LRU caching is a caching strategy that keeps track of the most recently used items and removes the least recently used items when the cache reaches its maximum size. In other words, it takes out the latest items from the cache first when it runs out of space. It uses the [FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) (first in, first out) strategy to remove the oldest items from the cache.

        We'll use `flexicache` with `maxsize` (of cache) of 2, meaning after 2 saves it starts discarding the oldest cache entries. Entries in cache functions are identified in the cache by arguments (v),so we add an argument to the function. 
        """
    )
    return


@app.cell
def _(flexicache, randint):
    @flexicache(maxsize=2)
    def random_func_4(v):
        return randint(1, 1000)
    return (random_func_4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's see how it works.
        """
    )
    return


@app.cell
def _(random_func_4):
    result1 = random_func_4(1)
    assert result1 == random_func_4(1)
    assert random_func_4(2) == random_func_4(2)
    return (result1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So far so good. The cache is working as expected. Now let's start evicting the first items added to the cache. We'll add a third item to the cache and see if the first one is evicted.
        """
    )
    return


@app.cell
def _(random_func_4, result1):
    assert random_func_4(3) == random_func_4(3)
    assert result1 != random_func_4(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## timed_cache convenience wrapper
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        `lru_cache` is a built-in Python decorator that provides a simple way to cache the results of a function. It uses a Least Recently Used (LRU) caching strategy, which means that it keeps track of the most recently used items as based on arguments and removes the least recently used items when the cache reaches its maximum size. In other words, it takes out the latest items from the cache first when it runs out of space.

        The downside is that it doesn't have a timeout feature, so if you want to cache results for a specific amount of time, you need to implement that yourself.

        `fastcore.xtras.timed_cache` is an implementation of `flexicache` that adds a timeout feature to `functools.lru_cache`.
        """
    )
    return


@app.cell
def _(randint):
    from fastcore.xtras import timed_cache

    @timed_cache(0.1, maxsize=2)
    def random_func_5(v):
        return randint(1, 1000)
    assert random_func_5(1) == random_func_5(1)
    return (random_func_5,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Testing the timeout is the same as before with `flexicache(time_policy(.1), maxsize=2)`. We'll call the function, wait for the timeout to be reached, and then call it again to see if the cache is invalidated.
        """
    )
    return


@app.cell
def _(random_func_5, result1, sleep):
    sleep(0.2)
    assert result1 != random_func_5(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Finally, confirm that the LRU cache is removing the first cached item. This is the same LRU cache set of tests we used in the section above about LRU caching. Again, we'll add a third item to the cache and see if the first one is evicted. 
        """
    )
    return


@app.cell
def _(random_func_5):
    result1_1 = random_func_5(1)
    assert result1_1 == random_func_5(1)
    assert random_func_5(2) == random_func_5(2)
    assert random_func_5(3) == random_func_5(3)
    assert result1_1 != random_func_5(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![/public/images/exploring-flexicache.png](/public/images/exploring-flexicache.png)
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
