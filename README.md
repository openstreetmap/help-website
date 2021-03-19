# Static-ized OSQA-Ask

This repository contains the tools used for the initial import of the dynamic version of https://osqa-ask.wireshark.org and its subsequent conversion to a static site.
The static site is generated using the [Hugo](https://gohugo.io/) static site generator.

# Import

The site was imported using `tools/fetch-questions.py` and `tools/fetch-upfiles.py`.
These downloaded each question page to `import/question` and file attachments to `import/upfiles`, respectively.

What's included in the import:

- Public questions. `fetch-questions.py` doesn't do any sort of authentication.

- Files attached to public questions (“upfiles”).

What's *not* included in the import:

- The badge and tag lists.

- User profiles.

After the site was imported the following tasks were completed manually.

- File attachments were moved to `import/upfiles` was manually moved to `site/static/upfiles`

# Directory Layout

Notable directories are:

- `import/`. Imported questions created using `tools/fetch-questions.py`.
- `logs/`. Import script logs.
- `site/`. Hugo configuration, assets, and generated site contents.
  - `config.toml`. Main Hugo configuration.
  - `content/questions/`. Questions converted to CommonMark using `tools/convert-questions.py`.
  - `layouts/_default/baseof.html`. Base page template.
  - `layouts/_default/home.html`. Home page template.
  - `layouts/_default/single.html`. Question page template.
  - `public/`. Generated site contents.
  - `static/images`. OSQA images, copied over manually.
  - `static/upfiles`. Attachments downloaded using `tools/fetch-upfiles.py`.

# Maintenance

You need [Hugo](https://gohugo.io) to generate the site.
You additionally need Python 3, the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) Python module, and [Pandoc](https://pandoc.org/) to regeneate the questions.

To generate the site, run `hugo` in the `site` directory.
Output will be written to `site/public`.

To regenerate the questions, run `tools\convert-questions.py`.
This should only be necessary if you're fixing a conversion bug.

# Questions:

Q: What is osqa-ask?

A: It's the first iteration of our [question and answer site](https://ask.wireshark.org).
It initially ran on software called [OSQA](https://github.com/dzone/osqa), which stopped being maintained in 2015.
In 2017 we migrated to [Askbot](https://github.com/ASKBOT/askbot-devel).

Q: Why not leave the site as-is?

A: As noted in the previous question, OSQA hasn't received updates for years.
It runs on Python 2, which is deprecated.
This makes maintenance and infrastructure upgrades more difficult as time goes on, and any security flaws that might turn up probably won't be fixed.

Q: Why not just get rid of the old site?
A: It's nice to have around as a historical reference.

Q: Why Hugo?
A: It's well-supported, easy to install, doesn't enforce a particular layout, and supports pagination.
