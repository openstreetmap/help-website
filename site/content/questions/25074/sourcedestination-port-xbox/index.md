+++
type = "question"
title = "Source/Destination Port: XBOX"
description = '''I&#x27;ve been trying to figure out why, when playing CoD MW3, via Steam I constantly get server timeouts. So I started up WireShark to try and monitor those packets. I noticed that there were packets being sent with with source and destination port saying Xbox. I don&#x27;t have an XBox on my network, that I...'''
date = "2013-09-22T13:54:00Z"
lastmod = "2013-09-22T15:00:00Z"
weight = 25074
keywords = [ "xbox" ]
aliases = [ "/questions/25074" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Source/Destination Port: XBOX](/questions/25074/sourcedestination-port-xbox)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25074-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to figure out why, when playing CoD MW3, via Steam I constantly get server timeouts. So I started up WireShark to try and monitor those packets. I noticed that there were packets being sent with with source and destination port saying Xbox. I don't have an XBox on my network, that I'm aware of. Any idea why this would be?</p></div><div id="question-tags" class="tags-container tags">xbox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '13, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/a59d9c6cafe1b4c9dbdb4d5c304d5616?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brian%20Barrick&#39;s gravatar image" /><p>Brian Barrick<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brian Barrick has no accepted answers">0%</span></p></div></div><div id="comments-container-25074" class="comments-container"><span id="25075"></span><div id="comment-25075" class="comment"><div id="post-25075-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any idea why this would be?</p></blockquote><p>Maybe, if you share the capture file with us (google docs, dropbox, cloudshark).</p></div><div id="comment-25075-info" class="comment-info"><span class="comment-age">(22 Sep '13, 13:55)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25074" class="comment-tools"></div><div class="clear"></div><div id="comment-25074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25076"></span>

<div id="answer-container-25076" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25076-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the actual port numbers involved, I suspect it will be port 3074, as this is the IANA registered port for xbox. See the IANA list <a href="http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=xbox">here</a>. Although this is the registered port of xbox, it can be freely used by other applications.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '13, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-25076" class="comments-container"><span id="25078"></span><div id="comment-25078" class="comment"><div id="post-25078-score" class="comment-score"></div><div class="comment-text"><p>I kind of thought that was probably it. I was watching it as I shut the game down and brought it back up and sure enough the packets labeled with that port started rolling in. Thank you.</p></div><div id="comment-25078-info" class="comment-info"><span class="comment-age">(22 Sep '13, 15:21)</span> Brian Barrick</div></div></div><div id="comment-tools-25076" class="comment-tools"></div><div class="clear"></div><div id="comment-25076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

