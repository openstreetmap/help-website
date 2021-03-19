+++
type = "question"
title = "LLMNR Query has blank name"
description = '''I am looking at the following capture and the first thing I notice is that the LLMNR query doesn&#x27;t specify a name that it is trying to locally resolve. Is this a bug? See frame 1-12 (excluding 7) http://www.cloudshark.org/captures/3bfe4764f3f4'''
date = "2013-08-21T22:44:00Z"
lastmod = "2013-08-21T23:15:00Z"
weight = 23940
keywords = [ "llmnr" ]
aliases = [ "/questions/23940" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [LLMNR Query has blank name](/questions/23940/llmnr-query-has-blank-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23940-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking at the following capture and the first thing I notice is that the LLMNR query doesn't specify a name that it is trying to locally resolve. Is this a bug? See frame 1-12 (excluding 7)</p><p><a href="http://www.cloudshark.org/captures/3bfe4764f3f4">http://www.cloudshark.org/captures/3bfe4764f3f4</a></p></div><div id="question-tags" class="tags-container tags">llmnr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/3e8f9f4373a1fe12ae4be7f9b995707c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark12&#39;s gravatar image" /><p>wireshark12<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark12 has no accepted answers">0%</span></p></div></div><div id="comments-container-23940" class="comments-container"></div><div id="comment-tools-23940" class="comment-tools"></div><div class="clear"></div><div id="comment-23940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23941"></span>

<div id="answer-container-23941" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23941-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, the query <strong>DOES</strong> specify a name: 'blank' is probably not what you are intending to resolve but I don't see anything wrong with it - protocol-wise <img src="https://osqa-ask.wireshark.org/upfiles/Selection_047.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-23941" class="comments-container"><span id="23946"></span><div id="comment-23946" class="comment"><div id="post-23946-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I just saw that the query was trying to find a resource called "blank". This was very misleading but like you said was following the protocol correctly!</p></div><div id="comment-23946-info" class="comment-info"><span class="comment-age">(22 Aug '13, 04:21)</span> wireshark12</div></div></div><div id="comment-tools-23941" class="comment-tools"></div><div class="clear"></div><div id="comment-23941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

