# Setup — Getting the book's environment running

This is a from-scratch setup guide for the *AI-Powered Search* code
environment, written for a team that may be on a mix of macOS and Windows
machines. Follow this once, and you'll have everything Tutorial 1
(`chapter-5/01_advil_moment.ipynb`) and the rest of the series needs.

> **The good news:** the authors ship the entire stack in Docker. There's
> no Python install, no Java install, no Solr install. You install Docker
> and Git, clone one repo, run one command, and the rest happens inside
> containers.

## What you'll have at the end

Three things running locally:

| Service          | Where               | Why you care                            |
|------------------|---------------------|-----------------------------------------|
| Jupyter Lab      | http://localhost:8888 | Where you run the book's notebooks    |
| Apache Solr      | http://localhost:8983 | The default search engine             |
| Spark + helpers  | (background)        | Used by the book's data-loading code    |

## Time + disk budget

- **Time:** 30–60 min, most of which is Docker pulling images on first run.
- **Disk:** ~15–25 GB total. Most of that is the Docker images. The
  chapter-5 datasets themselves (Stack Exchange dumps) are a few GB.
- **RAM:** Docker Desktop defaults to 2 GB. **Bump it to at least 8 GB**
  before starting — Solr + Spark are hungry. Instructions below.

---

## Step 1 — Install Docker

### macOS

The easiest path is Docker Desktop.

```bash
# Option A: Homebrew (recommended if you have it)
brew install --cask docker

# Option B: download installer
# Visit https://www.docker.com/products/docker-desktop/ and grab the
# .dmg for Apple Silicon (M-series) or Intel.
```

Then launch Docker Desktop from /Applications. Wait until the whale icon
in the menu bar is steady (not animating) before continuing.

**Allocate more RAM:** Docker Desktop → Settings → Resources → Memory.
Set it to **at least 8 GB** (10–12 GB is more comfortable). Click "Apply
& Restart".

### Windows

Docker on Windows runs on top of WSL2 (Windows Subsystem for Linux). The
installer handles most of that for you.

1. Open PowerShell **as Administrator** and enable WSL2:
   ```powershell
   wsl --install
   ```
   This installs WSL2 + Ubuntu. Reboot when it prompts you.
2. Download Docker Desktop for Windows from
   https://www.docker.com/products/docker-desktop/ and run the installer.
3. During install, leave "Use WSL 2 instead of Hyper-V" checked.
4. After install, launch Docker Desktop. It'll ask to start the WSL
   integration — accept.

**Allocate more RAM:** same as macOS — Docker Desktop → Settings →
Resources → Memory → at least 8 GB.

### Verify

In a fresh terminal (macOS Terminal, or Windows PowerShell):

```bash
docker --version
docker compose version
```

You should see version strings, not errors. If `docker compose version`
errors but `docker-compose --version` works, you have the older
standalone tool. Substitute `docker-compose` for `docker compose`
throughout this guide, or upgrade Docker Desktop.

---

## Step 2 — Install Git

### macOS

```bash
# Option A: Homebrew
brew install git

# Option B: it ships with Xcode Command Line Tools
xcode-select --install
```

### Windows

Download from https://git-scm.com/download/win and run the installer.
Accept all defaults. This also installs **Git Bash**, which gives you a
Unix-style shell — recommended for running the rest of the commands in
this guide.

### Verify

```bash
git --version
```

---

## Step 3 — Clone the book's repo

Pick a folder you don't mind a ~20 GB checkout living in (the data files
make the working tree large after you index things). Open a terminal
(or Git Bash on Windows) and run:

```bash
git clone https://github.com/treygrainger/ai-powered-search.git
cd ai-powered-search
```

You should now see folders like `aips/`, `chapters/`, `engines/`, and
a `docker-compose.yml` file.

> **Why we're using the upstream repo unmodified.** Our tutorial series
> (in `tutorials/chapter-5/`) imports the book's `aips` package and
> reuses its Solr setup. So our tutorials need to live inside (or
> alongside) the book's checkout. We'll wire that up in step 6.

---

## Step 4 — Start the Docker stack

From inside the `ai-powered-search` directory:

```bash
docker compose up
```

This will:

1. Pull or build several Docker images (Jupyter, Solr, Spark, helpers).
2. Wire them together on a private Docker network.
3. Stream logs to your terminal.

**On first run this can take 15–30 minutes** depending on your network.
Subsequent starts are fast (seconds).

Leave this terminal window open. The containers run in the foreground.
You'll come back to it later to stop them with `Ctrl+C`.

> **Tip:** If you want it in the background, run `docker compose up -d`
> and use `docker compose logs -f` to follow output.

### When is it ready?

Watch the logs for these signals:

- `aips-notebooks-1  | ...  http://127.0.0.1:8888/lab?token=...`
- `aips-solr-1       | ... o.a.s.c.SolrCore [...] Registered new searcher`

Once you see both, the stack is up.

---

## Step 5 — Open Jupyter and the welcome notebook

In your browser, go to:

> **http://localhost:8888**

You should land in Jupyter Lab with a file tree on the left showing
`chapters/`, `aips/`, etc. Open `chapters/welcome.ipynb` — this is the
authors' table of contents for the whole book. From here, anything in
chapter 5 is reachable under `chapters/ch5/`.

> **If Jupyter asks for a token:** look back at the `docker compose up`
> log for a line like `http://127.0.0.1:8888/lab?token=abc123...`.
> Copy the token. Alternatively, the book's image typically disables
> the token for localhost — try refreshing.

---

## Step 6 — Drop our tutorials into the repo

So that our notebooks can `import aips`, they need to live inside the
checkout you just cloned. From the host (not inside Docker):

### macOS

```bash
# Adjust the source path to wherever you have this tutorials/ folder
cp -R /Users/ericstarr/Documents/Claude/Projects/ai-powered-search-book/tutorials \
      ./tutorials
```

### Windows (Git Bash)

```bash
cp -R "/c/Users/<you>/Documents/Claude/Projects/ai-powered-search-book/tutorials" \
      ./tutorials
```

Because Jupyter is mounting the repo root, the new `tutorials/` folder
will appear in the Jupyter file tree the moment you save the files
(refresh the browser if not).

---

## Step 7 — Index the chapter-5 data

The book's notebooks lazy-load their datasets when first run. For
chapter 5, the relevant notebooks live under `chapters/ch5/`. Open them
in the order suggested by `welcome.ipynb` and **Run All Cells** in each.
The notebooks will:

- Download the Stack Exchange `health` and `scifi` dumps.
- Parse and clean them.
- Index them into the local Solr at `localhost:8983` (from inside the
  Docker network, the engine is reached at `aips-solr:8983`, but the
  notebooks handle that for you).

This takes 5–15 minutes per dataset. You'll know it worked when the
final cell prints a non-zero document count.

> **You can also let our verification notebook tell you exactly which
> datasets are missing.** Skip to step 8 first and let it diagnose.

---

## Step 8 — Run the verification notebook

In Jupyter, open `tutorials/00_verify_setup.ipynb` and **Run All Cells**.

You should see ✅ ✅ ✅ for each check. Any ❌ comes with an action — usually
"open chapters/ch5/foo.ipynb and run all cells".

Once everything is green, you're ready for `tutorials/chapter-5/01_advil_moment.ipynb`.

---

## Troubleshooting

**Port 8888 or 8983 already in use.** Some other app is using the port.
On macOS: `lsof -i :8888` to see what. On Windows: `netstat -ano | findstr :8888`.
Kill the process or change the port mapping in `docker-compose.yml`.

**Docker Desktop refuses to start (Windows).** Make sure WSL2 is fully
installed (`wsl --status` should show "Default Version: 2"). If you see
"Hardware assisted virtualization", enable virtualization in your BIOS.

**Apple Silicon (M1/M2/M3/M4) compatibility.** All the book's images
have arm64 variants. If you ever see "image's platform does not match",
pass `--platform linux/amd64` after `docker compose` — slower but works.

**"No space left on device."** Docker images stack up. Reclaim with:
```bash
docker system prune -a --volumes
```
Note this wipes unused volumes — re-indexing the datasets will take
another 30 min after this.

**Jupyter can't see the new `tutorials/` folder.** It's a mount issue.
Stop the stack (Ctrl+C in the `docker compose up` terminal), then run
`docker compose up` again. The bind mount picks up files dropped into
the repo root.

**`import aips` fails inside our tutorial notebooks.** Confirm the
notebook is being run by the Jupyter inside Docker (URL is
`localhost:8888`), not a host-installed Jupyter. The `aips` package
only exists inside the container.

---

## Shutdown and restart

To stop the stack: in the `docker compose up` terminal, press `Ctrl+C`.
Wait for it to gracefully shut down. The data you've indexed persists
in Docker volumes, so a restart is cheap:

```bash
docker compose up
```

To wipe everything and start clean:

```bash
docker compose down -v   # the -v removes volumes (indexed data)
```

---

## What's next

- Read [`tutorials/chapter-5/README.md`](chapter-5/README.md) for the
  tutorial series overview.
- Open [`tutorials/chapter-5/01_advil_moment.ipynb`](chapter-5/01_advil_moment.ipynb)
  and walk through your first SKG traversal.

If anything in this guide is wrong or out of date, the authoritative
source is [the book repo's README](https://github.com/treygrainger/ai-powered-search)
and Appendix A of *AI-Powered Search*.
