# Static-ized OSQA-Ask

Tweaked version of https://gitlab.com/wireshark/ws-osqa-ask-static used for converting https://help.openstreetmap.org/ to a static site.

Thank you to Wireshark! ❤️

## How do I update the static help.openstreetmap.org site?

1. Edit or Remove as applicable in `./import/questions/`
2. Run `./tools/convert-questions.py` which populates `./site/content/questions/`
3. `cd ./site/; hugo serve` to confirm desired output
4. GitHub Actions will rebuild container on push
5. Chef will update container shortly
6. Live!
