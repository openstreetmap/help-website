+++
type = "question"
title = "How do I diagnose a slow WLAN guest network?"
description = '''I have Laura&#x27;s newest Wireshark Analysis book (2010, anyway) and have been reading through it to try and solve a problem. Our guest WLAN is slow at times. Each user is capped via the wireless distribution system at 1mb/s download, and capped uploading and downloading at the DMZ to 8mb/s, but that is...'''
date = "2011-09-27T12:20:00Z"
lastmod = "2011-09-29T01:44:00Z"
weight = 6599
keywords = [ "overloaded", "internet" ]
aliases = [ "/questions/6599" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I diagnose a slow WLAN guest network?](/questions/6599/how-do-i-diagnose-a-slow-wlan-guest-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Laura's newest Wireshark Analysis book (2010, anyway) and have been reading through it to try and solve a problem.</p><p>Our guest WLAN is slow at times. Each user is capped via the wireless distribution system at 1mb/s download, and capped uploading and downloading at the DMZ to 8mb/s, but that is the entire pipe, not per user.</p><p>I have eliminated the RF side of the house, which is what I thought it was. Not congested or experiencing interference. We put a copper port in the same network (also eliminating the WLAN) and we still experience the problem.</p><p>Put Wireshark on my laptop and associated to guest WLAN. Every now and then when I browse the Internet, it gets super slow and pages timeout.</p><p>I would like to snag a capture of when the network is slow and go from there. I was thinking this was the best angle since I want to see what's happening from the user's experience.</p><p>Can anyone give me some things to look for? I suspect there are too many users trying to use the guest network's 8mb/s pipe. All I have to do is prove it.</p></div><div id="question-tags" class="tags-container tags">overloaded internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '11, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/1f77b298350afb4f1220c504f110de93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tdennehy&#39;s gravatar image" /><p>tdennehy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tdennehy has no accepted answers">0%</span></p></div></div><div id="comments-container-6599" class="comments-container"></div><div id="comment-tools-6599" class="comment-tools"></div><div class="clear"></div><div id="comment-6599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6633"></span>

<div id="answer-container-6633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6633-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From what you've written I conclude two main facts:</p><ol><li>You said that even using a copper port you experience the problem</li><li>You already know that there is a throttle in your Wireless distribution system</li></ol><p>So a good way to go from my perspective would be to take a trace at the uplinks of the wireless distribution system connecting your guest WLANs and look at the traffic there. Maybe you can even just recover something from the logs if your controller is capable and configured to monitor bandwidth usage.</p><p>Sniffing from a wireless client you can only tell that there <em>IS</em> a problem, but not if thats connected to too many users on the guest network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '11, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Sep '11, 01:45</p></div></div><div id="comments-container-6633" class="comments-container"></div><div id="comment-tools-6633" class="comment-tools"></div><div class="clear"></div><div id="comment-6633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

