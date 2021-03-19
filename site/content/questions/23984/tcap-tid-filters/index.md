+++
type = "question"
title = "tcap tid filters"
description = '''Hi  what is meaning tcap.tid == 2f:00:57:21 , so what is meaning 2f:00:57:21 please thanks'''
date = "2013-08-23T12:13:00Z"
lastmod = "2013-08-23T13:54:00Z"
weight = 23984
keywords = [ "sin73an" ]
aliases = [ "/questions/23984" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcap tid filters](/questions/23984/tcap-tid-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi what is meaning tcap.tid == 2f:00:57:21 , so what is meaning 2f:00:57:21 please thanks</p></div><div id="question-tags" class="tags-container tags">sin73an</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '13, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/da3e09c56522fbeeb554c9edd8f6b817?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sin73an&#39;s gravatar image" /><p>sin73an<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sin73an has no accepted answers">0%</span></p></div></div><div id="comments-container-23984" class="comments-container"></div><div id="comment-tools-23984" class="comment-tools"></div><div class="clear"></div><div id="comment-23984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23985"></span>

<div id="answer-container-23985" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23985-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The tid is the Transaction ID and 2f:00:57:21 is the filter matching criteria for the 4 bytes that comprise it. The notation used is hexadecimal since this field happens to be an FT_BYTES type, as can be seen using:</p><pre><code>tshark -G | grep &quot;tcap\.tid&quot;</code></pre><p>or by visiting the Wireshark "<a href="http://www.wireshark.org/docs/dfref/t/tcap.html">Display Filter Reference: Transaction Capabilities Application Part</a>" page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '13, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-23985" class="comments-container"></div><div id="comment-tools-23985" class="comment-tools"></div><div class="clear"></div><div id="comment-23985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

