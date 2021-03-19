+++
type = "question"
title = "Data filter by byte not string"
description = '''Hello All, I want to search on the Data field of a TCP packet where I can search on a data byte pattern not a data string, Is this possible, if so how? Regards B'''
date = "2011-09-13T09:14:00Z"
lastmod = "2011-09-13T10:15:00Z"
weight = 6324
keywords = [ "display-filter" ]
aliases = [ "/questions/6324" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Data filter by byte not string](/questions/6324/data-filter-by-byte-not-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6324-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I want to search on the Data field of a TCP packet where I can search on a data byte pattern not a data string, Is this possible, if so how?</p><p>Regards</p><p>B</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '11, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/8fbeff627fe9082da131384ae21a5d85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baz&#39;s gravatar image" /><p>Baz<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Sep '11, 10:16</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6324" class="comments-container"></div><div id="comment-tools-6324" class="comment-tools"></div><div class="clear"></div><div id="comment-6324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6326"></span>

<div id="answer-container-6326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6326-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can use <a href="http://wiki.wireshark.org/DisplayFilters">display filter syntax</a> to search for a particular byte sequence. Here's an example display filter to find <code>{A1,B2,C3,D4}</code> anywhere in <code>tcp.data</code>:</p><pre><code>tcp.data contains A1:B2:C3:D4</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '11, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-6326" class="comments-container"></div><div id="comment-tools-6326" class="comment-tools"></div><div class="clear"></div><div id="comment-6326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

