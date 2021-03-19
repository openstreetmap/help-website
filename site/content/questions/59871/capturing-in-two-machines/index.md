+++
type = "question"
title = "Capturing in two machines"
description = '''We send a text file from on computer (windows) to another (Linux) and we captured it in each computer. Is there a difference between each capture? My friend says there is a difference but I don&#x27;t see it'''
date = "2017-03-06T15:04:00Z"
lastmod = "2017-03-08T06:50:00Z"
weight = 59871
keywords = [ "windows", "capture", "linux" ]
aliases = [ "/questions/59871" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing in two machines](/questions/59871/capturing-in-two-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59871-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We send a text file from on computer (windows) to another (Linux) and we captured it in each computer. Is there a difference between each capture? My friend says there is a difference but I don't see it</p></div><div id="question-tags" class="tags-container tags">windows capture linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '17, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/bae0312255fee0aafea381dc50ad6faa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martix&#39;s gravatar image" /><p>Martix<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martix has no accepted answers">0%</span></p></div></div><div id="comments-container-59871" class="comments-container"><span id="59872"></span><div id="comment-59872" class="comment"><div id="post-59872-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>Is there a difference between each capture?</p></blockquote></blockquote><p>There might be depending on many factors such as offload settings, network delay, etc.</p><blockquote><blockquote><p>but I don't see it</p></blockquote></blockquote><p>We don't either.</p></div><div id="comment-59872-info" class="comment-info"><span class="comment-age">(06 Mar '17, 16:33)</span> Bob Jones</div></div></div><div id="comment-tools-59871" class="comment-tools"></div><div class="clear"></div><div id="comment-59871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59926"></span>

<div id="answer-container-59926" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59926-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you ask about differences, do you mean in the capture format or in the data itself?<br />
</p><p>As far as the data goes, there will be a few differences:</p><ul><li>The time each frame was seen</li><li>The source and destination MAC addresses (if the two machines are not on the same LAN segment</li><li>There could be more, depending on the network topology between the two machines. For example, the if the connection goes through a NAT'ing device or a proxy server, then the TCP sequence numbers may be different.</li></ul><p>If you don't see any obvious difference, have a look at the timestamps and MAC addresses. Also, make sure you set your configuration to show the actual TCP sequence numbers and not relative ones. If the two machiens are on the same LAN segment, at minimum the timestamps will differ and the source/destination MAC and IP addresses will be swapped.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '17, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p>ryber<br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span> </br></p></div></div><div id="comments-container-59926" class="comments-container"></div><div id="comment-tools-59926" class="comment-tools"></div><div class="clear"></div><div id="comment-59926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

