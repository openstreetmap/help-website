# Static-ized OSQA-Ask

Tweaked version of https://gitlab.com/wireshark/ws-osqa-ask-static used for converting https://help.openstreetmap.org/ to a static site.

Thank you to Wireshark! ❤️

## How do I update the static help.openstreetmap.org site?

1. Edit or Remove as applicable in `./import/questions/`
2. Run `./tools/convert-questions.py` which populates `./site/content/questions/`
3. Note the manually edited out questions in https://github.com/openstreetmap/help-website/commit/5b0088538073086f41530cfed88f2c2c987e590d (Tip: do not `git add` them)
4. `cd ./site/; hugo serve` to confirm desired output
5. GitHub Actions will rebuild container on push
6. Chef will update container shortly
7. Live!
