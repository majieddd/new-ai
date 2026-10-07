# New AI

An open research project aiming at a hybrid energy-based model: a frozen cortical core, learned scalar-energy candidate refinement, bounded residual growth, retention checks and conditional promotion. Ternary computation and tiered memory are planned, not measured capabilities.

**This release foundation is not a working integrated model.** E20 and E21 have separate synthetic development fixtures; their pretrained language studies remain **NOT RUN**. Historical E19 failed its timing/acquisition acceptance. A passing website build is not a scientific result.

- Original code: [Apache-2.0](LICENSE); exceptions and dependency rights: [third-party notices](THIRD_PARTY_NOTICES.md).
- Existing dashboard and historical links remain intact: https://majieddd.github.io/new-ai-dashboard/
- Release interface and integration ownership: [docs/RELEASE_INTERFACE.md](docs/RELEASE_INTERFACE.md).
- Reproducibility and review: [CONTRIBUTING.md](CONTRIBUTING.md).

## CPU-only publication tools

Python 3.11+; no GPU, model weights, corpus or final evaluation material required.

```sh
python -m venv .venv
# POSIX: . .venv/bin/activate
# Windows PowerShell: .venv/Scripts/Activate.ps1
python -m pip install -r requirements.lock
python -m pip install --no-build-isolation --no-deps -e .
new-ai status
python -m unittest discover -s tests -v
```

Model execution is reserved to the model lead. The agreed public interface will use `src/new_ai/model/`, `examples/` and safe developmental receipts, after review; no substitute model or fake checkpoint is packaged here.
