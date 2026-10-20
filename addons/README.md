# Add-ons I develop

Each add-on lives in its own repository and is linked here as a git submodule, pinned to a specific commit. Development, issues and releases happen in the add-on's own repository.

| Add-on | Repository | Install |
|---|---|---|
| Ink | [ntfifwyb/ink](https://github.com/ntfifwyb/ink) | Download `ink.ankiaddon` from its [releases](https://github.com/ntfifwyb/ink/releases) |

**Update the pinned version:**

```
git submodule update --remote addons/ink
git commit -am "Update Ink"
```

**Add a new add-on:**

```
git submodule add https://github.com/<owner>/<repo> addons/<name>
```

Then add it to the table above and to the root README.
