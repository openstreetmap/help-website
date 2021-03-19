+++
type = "question"
title = "WireShark crashing with C++ errors"
description = '''Running WS 1.6.12(SVN REV 46251 from/Trunk -1.6) on W2K3 server, 4gig ram,  Just doing basic capture from-to an IPAddress, buffer 10 meg, each file 10meg. After around 45 min (6meg file size) Wireshark crashes with C++ error.  Found lots of errors related to C++ crashes when searching Google, but no...'''
date = "2012-12-06T06:47:00Z"
lastmod = "2012-12-06T07:28:00Z"
weight = 16635
keywords = [ "c++" ]
aliases = [ "/questions/16635" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark crashing with C++ errors](/questions/16635/wireshark-crashing-with-c-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running WS 1.6.12(SVN REV 46251 from/Trunk -1.6) on W2K3 server, 4gig ram, Just doing basic capture from-to an IPAddress, buffer 10 meg, each file 10meg. After around 45 min (6meg file size) Wireshark crashes with C++ error. Found lots of errors related to C++ crashes when searching Google, but none matching my configs or even having a resolve for the issue. Any thoughts?</p></div><div id="question-tags" class="tags-container tags">c++</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '12, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/62ea73d800aae5a938742dd7065f34d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raybo73&#39;s gravatar image" /><p>raybo73<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raybo73 has no accepted answers">0%</span></p></div></div><div id="comments-container-16635" class="comments-container"><span id="16639"></span><div id="comment-16639" class="comment"><div id="post-16639-score" class="comment-score"></div><div class="comment-text"><p>do you mind to share the error messages with us?</p></div><div id="comment-16639-info" class="comment-info"><span class="comment-age">(06 Dec '12, 09:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16635" class="comment-tools"></div><div class="clear"></div><div id="comment-16635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16636"></span>

<div id="answer-container-16636" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16636-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try doing the capture with dumpcap instead, since Wireshark might run into trouble with memory management if there's a lot of small packets (even though 6meg doesn't seem that much to cause a crash). Wireshark uses dumpcap to capture the packets anyway, so you could run it without Wireshark to avoid the memory overhead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '12, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16636" class="comments-container"></div><div id="comment-tools-16636" class="comment-tools"></div><div class="clear"></div><div id="comment-16636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

