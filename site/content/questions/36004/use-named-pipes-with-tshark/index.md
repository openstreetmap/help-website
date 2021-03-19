+++
type = "question"
title = "Use named pipes with tshark"
description = '''According to tshark man page it&#x27;s not possible to use named pipes with tshark&#x27;s -r option, however I tried to use a named pipe with that option before reading the man page and it worked. At least with single-pass filters. Does anybody know if tshark&#x27;s man page is up-to-date? I&#x27;m using 1.12. Thanks'''
date = "2014-09-04T08:07:00Z"
lastmod = "2014-09-04T10:27:00Z"
weight = 36004
keywords = [ "named", "tshark", "pipes" ]
aliases = [ "/questions/36004" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Use named pipes with tshark](/questions/36004/use-named-pipes-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36004-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to tshark man page it's not possible to use named pipes with tshark's -r option, however I tried to use a named pipe with that option before reading the man page and it worked. At least with single-pass filters.</p><p>Does anybody know if tshark's man page is up-to-date?</p><p>I'm using 1.12.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">named tshark pipes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '14, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/1f6bf1f9c1bc56105fed452b59dacb56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andres%20Senac&#39;s gravatar image" /><p>Andres Senac<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andres Senac has no accepted answers">0%</span></p></div></div><div id="comments-container-36004" class="comments-container"></div><div id="comment-tools-36004" class="comment-tools"></div><div class="clear"></div><div id="comment-36004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36007"></span>

<div id="answer-container-36007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36007-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not up to date in version 1.12.0. It was updated in <a href="https://code.wireshark.org/review/2646">master</a> already. I just back-ported the change so it'll show up in 1.12.1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '14, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36007" class="comments-container"></div><div id="comment-tools-36007" class="comment-tools"></div><div class="clear"></div><div id="comment-36007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

