+++
type = "question"
title = "Isolating the Subnet"
description = '''I&#x27;ve gone ahead and created the filter [ip.addr == 192.168.0.1/24], with the hope of only monitoring my local subnet in the Endpoints/ IPv4 window, but am still getting all the other IP addresses popping up. Any suggestions on only capturing my local network (192.168.0.1-254)?'''
date = "2013-12-17T20:21:00Z"
lastmod = "2013-12-17T21:51:00Z"
weight = 28227
keywords = [ "ipv4", "filters" ]
aliases = [ "/questions/28227" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Isolating the Subnet](/questions/28227/isolating-the-subnet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28227-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've gone ahead and created the filter [ip.addr == 192.168.0.1/24], with the hope of only monitoring my local subnet in the Endpoints/ IPv4 window, but am still getting all the other IP addresses popping up. Any suggestions on only capturing my local network (192.168.0.1-254)?</p></div><div id="question-tags" class="tags-container tags">ipv4 filters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '13, 20:21</strong></p><img src="https://secure.gravatar.com/avatar/5bd09bb4f476844a60673843799a33e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johncalvinhall&#39;s gravatar image" /><p>johncalvinhall<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johncalvinhall has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 17 Dec '13, 20:30</p></div></div><div id="comments-container-28227" class="comments-container"></div><div id="comment-tools-28227" class="comment-tools"></div><div class="clear"></div><div id="comment-28227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28229"></span>

<div id="answer-container-28229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28229-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>With your filter, only one communication parter must be in your local subnet. Try this one to match only when both IP hosts are in your IP subnet:</p><pre><code>ip.src==192.168.0.0/24 and ip.dst==192.168.0.0/24</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '13, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28229" class="comments-container"><span id="28230"></span><div id="comment-28230" class="comment"><div id="post-28230-score" class="comment-score"></div><div class="comment-text"><p>That is fantastic! TYVM!</p></div><div id="comment-28230-info" class="comment-info"><span class="comment-age">(17 Dec '13, 21:59)</span> johncalvinhall</div></div><span id="28232"></span><div id="comment-28232" class="comment"><div id="post-28232-score" class="comment-score"></div><div class="comment-text"><p>You're welcome - Don't forget to 'accept' the answer to mark it as closed, thanks</p></div><div id="comment-28232-info" class="comment-info"><span class="comment-age">(17 Dec '13, 22:10)</span> mrEEde</div></div></div><div id="comment-tools-28229" class="comment-tools"></div><div class="clear"></div><div id="comment-28229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

