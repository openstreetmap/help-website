+++
type = "question"
title = "Source code main file of wireshark"
description = '''I am trying to build and run Wireshark from source code on Ubuntu. I would like to know the main file in the source code which launches the application  The documentation says that i can execute the source code after build by running:  $ WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark But i also ne...'''
date = "2014-08-25T11:41:00Z"
lastmod = "2014-08-26T12:14:00Z"
weight = 35715
keywords = [ "source-code", "build", "wireshark" ]
aliases = [ "/questions/35715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Source code main file of wireshark](/questions/35715/source-code-main-file-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build and run Wireshark from source code on Ubuntu. I would like to know the main file in the source code which launches the application</p><p>The documentation says that i can execute the source code after build by running: $ WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark</p><p>But i also need to know the file which is launching the application.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">source-code build wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '14, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/6faea3eba9bf10d1e5dd9cc5b58e4fcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssayed1&#39;s gravatar image" /><p>ssayed1<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssayed1 has no accepted answers">0%</span></p></div></div><div id="comments-container-35715" class="comments-container"><span id="35774"></span><div id="comment-35774" class="comment"><div id="post-35774-score" class="comment-score"></div><div class="comment-text"><p>Please refrain from asking the <a href="https://ask.wireshark.org/questions/35712/what-source-code-launches-wireshark">same question</a> more than once.</p></div><div id="comment-35774-info" class="comment-info"><span class="comment-age">(26 Aug '14, 13:04)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-35715" class="comment-tools"></div><div class="clear"></div><div id="comment-35715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35769"></span>

<div id="answer-container-35769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35769-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For the gtk version, program execution begins with <code>ui/gtk/main.c:main()</code>, and for the Qt version, program execution begins with <code>ui/qt/main.cpp:main()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35769" class="comments-container"></div><div id="comment-tools-35769" class="comment-tools"></div><div class="clear"></div><div id="comment-35769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

