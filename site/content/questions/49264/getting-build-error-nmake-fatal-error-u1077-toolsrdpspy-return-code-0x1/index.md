+++
type = "question"
title = "Getting build error: &quot;NMAKE: fatal error U1077: &#x27;..&#92;tools&#92;rdps.py&#x27;: return code &#x27;0x1&#x27;"
description = '''I haven&#x27;t made build for awhile and just doing the build which I was able to do successfully in the past, but gotten the above NMAKE error with some &#x27;..&#92;tools&#92;rdps.py&#x27; Please suggest. thank you'''
date = "2016-01-15T14:49:00Z"
lastmod = "2016-01-15T15:19:00Z"
weight = 49264
keywords = [ "build_error", "build", "nmake", "wireshark" ]
aliases = [ "/questions/49264" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting build error: "NMAKE: fatal error U1077: '..\\tools\\rdps.py': return code '0x1'](/questions/49264/getting-build-error-nmake-fatal-error-u1077-toolsrdpspy-return-code-0x1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49264-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I haven't made build for awhile and just doing the build which I was able to do successfully in the past, but gotten the above NMAKE error with some '..\tools\rdps.py' Please suggest. thank you</p></div><div id="question-tags" class="tags-container tags">build_error build nmake wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '16, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/fe7b8b8f82626427d3ae7d5428f2102d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christenmu&#39;s gravatar image" /><p>christenmu<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christenmu has one accepted answer">50%</span></p></div></div><div id="comments-container-49264" class="comments-container"></div><div id="comment-tools-49264" class="comment-tools"></div><div class="clear"></div><div id="comment-49264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49265"></span>

<div id="answer-container-49265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49265-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Firstly, you should move to a CMake build as detailed in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a>, support for Nmake may be dropped in the next release.</p><p>It would help to have a little more context, but rdps.py is a python script that converts the print.ps file to ps.c, and relies on nmake being configured with a valid path to python in the $(PYTHON) variable.</p><p>What version of python do you have installed, and do you have any changes in config.nmake to identify that version of python?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '16, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49265" class="comments-container"><span id="49273"></span><div id="comment-49273" class="comment"><div id="post-49273-score" class="comment-score"></div><div class="comment-text"><p>I verified that the PHYTON is version 2.7 and the config.nmake supposed to support this version and it has the correct path. I did not change the config.nmake. But noticed that while doing nmake -f Makefile.nmake all when it comes to tools\rdps.py print.ps ps.c .. there's a window popped up asking which program to choose to open this file. As if it did not know where this Python is. After manually directing to the correct location, the build seems to continue but at the end still get build error at c1: fatal error C1082: Cannot open source file: 'ps.c': No such file or directory. I re-installed the PYTHON 2.7.8 same version I had before and that seems to resolve the issue. thanks for your help.</p></div><div id="comment-49273-info" class="comment-info"><span class="comment-age">(16 Jan '16, 07:58)</span> christenmu</div></div><span id="49281"></span><div id="comment-49281" class="comment"><div id="post-49281-score" class="comment-score"></div><div class="comment-text"><p>Likely that somehow your original python install was non-functional, and installing the newer version fixed that.</p></div><div id="comment-49281-info" class="comment-info"><span class="comment-age">(16 Jan '16, 14:18)</span> grahamb ♦</div></div></div><div id="comment-tools-49265" class="comment-tools"></div><div class="clear"></div><div id="comment-49265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

