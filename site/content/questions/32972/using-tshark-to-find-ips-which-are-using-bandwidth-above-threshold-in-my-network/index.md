+++
type = "question"
title = "Using tshark to find IPs which are using bandwidth above threshold in my network"
description = '''Hi all, how can I log IPs wich are using bandwidth above threshold? For example I want to log computer IPs which are using more than 1Mbps of bandwith at any given point of time. How can I do this using tshark?'''
date = "2014-05-21T23:20:00Z"
lastmod = "2014-05-23T13:26:00Z"
weight = 32972
keywords = [ "bandwidth", "tshark", "utilization" ]
aliases = [ "/questions/32972" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using tshark to find IPs which are using bandwidth above threshold in my network](/questions/32972/using-tshark-to-find-ips-which-are-using-bandwidth-above-threshold-in-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32972-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, how can I log IPs wich are using bandwidth above threshold?</p><p>For example I want to log computer IPs which are using more than 1Mbps of bandwith at any given point of time. How can I do this using tshark?</p></div><div id="question-tags" class="tags-container tags">bandwidth tshark utilization</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/38ab7ece5cfb68aef1a9240019be93fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CJ22&#39;s gravatar image" /><p>CJ22<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CJ22 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '14, 01:51</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32972" class="comments-container"></div><div id="comment-tools-32972" class="comment-tools"></div><div class="clear"></div><div id="comment-32972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33026"></span>

<div id="answer-container-33026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33026-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Only capinfos can show you the average data byte/bit rate similar to the Wireshark -Statistics - Summary. It will not be in real time and the calculations are for the entire packet capture.</p><p>For network statistics look at tools like ntop or darkstat.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '14, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-33026" class="comments-container"></div><div id="comment-tools-33026" class="comment-tools"></div><div class="clear"></div><div id="comment-33026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

