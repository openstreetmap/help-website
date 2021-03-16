# OSQA-Ask Static

This repository contains the tools used for the initial import of the dynamic version of https://osqa-ask.wireshark.org and its subsequent conversion to a static site.

# Import

The site was imported using `tools/import-from-osqa.py`.
This downloaded each question page to `import/question` and file attachments to `import/upfiles`.

What's included in the import:

- Public questions. `import-from-osqa.py` doesn't do any sort of authentication.

- Files attached to public questions.

What's not included in the import:

- The badge and tag lists.

- User profiles.

# Maintenance

The

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

Q: Why Zola?
A: It's a single executable that includes search.