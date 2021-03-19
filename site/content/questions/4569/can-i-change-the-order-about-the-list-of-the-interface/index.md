+++
type = "question"
title = "Can i change the order about the list of the interface?"
description = '''Can i change the order of interface number, by the way, the number is get by command &quot;tshark -D&quot;?'''
date = "2011-06-15T05:19:00Z"
lastmod = "2011-06-16T11:42:00Z"
weight = 4569
keywords = [ "interface", "list" ]
aliases = [ "/questions/4569" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can i change the order about the list of the interface?](/questions/4569/can-i-change-the-order-about-the-list-of-the-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4569-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can i change the order of interface number, by the way, the number is get by command "tshark -D"?</p></div><div id="question-tags" class="tags-container tags">interface list</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '11, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/5e0b401d2cc313f3a83d96e0595b586a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phoenix&#39;s gravatar image" /><p>phoenix<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phoenix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jun '11, 05:22</p></div></div><div id="comments-container-4569" class="comments-container"><span id="4570"></span><div id="comment-4570" class="comment"><div id="post-4570-score" class="comment-score"></div><div class="comment-text"><p>Why would you want to do that? the list is usually pretty short anyway...</p></div><div id="comment-4570-info" class="comment-info"><span class="comment-age">(15 Jun '11, 06:32)</span> Jasper ♦♦</div></div></div><div id="comment-tools-4569" class="comment-tools"></div><div class="clear"></div><div id="comment-4569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4601"></span>

<div id="answer-container-4601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4601-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't change the order of the interfaces; they're supplied in the order in which libpcap gets them from the OS (with interfaces that libpcap can identify as "loopback" interfaces sorted to the end) or in which WinPcap gets them from wherever it gets them.</p><p>The number printed by "tshark -D" (and "tcpdump -D" and...) is just the ordinal number of the interface in the list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '11, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4601" class="comments-container"></div><div id="comment-tools-4601" class="comment-tools"></div><div class="clear"></div><div id="comment-4601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

