+++
type = "question"
title = "Identify the IP addresses called by an application"
description = '''I need to identify the IP addresses called by an application. Is it possible to configure WireShark to filter for this, and how?'''
date = "2015-10-20T08:15:00Z"
lastmod = "2015-10-20T10:12:00Z"
weight = 46763
keywords = [ "ip", "wireshark" ]
aliases = [ "/questions/46763" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Identify the IP addresses called by an application](/questions/46763/identify-the-ip-addresses-called-by-an-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46763-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to identify the IP addresses called by an application. Is it possible to configure WireShark to filter for this, and how?</p></div><div id="question-tags" class="tags-container tags">ip wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '15, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/ce0e846b906e210c533268e000364e61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jared&#39;s gravatar image" /><p>Jared<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jared has no accepted answers">0%</span></p></div></div><div id="comments-container-46763" class="comments-container"></div><div id="comment-tools-46763" class="comment-tools"></div><div class="clear"></div><div id="comment-46763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46766"></span>

<div id="answer-container-46766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46766-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if you know the IP addresses, you can do that</p><p>As you seem to be new to Wireshark, please read the Wirshark docs first to understand how it (basically) works.</p><blockquote><p><a href="https://www.wireshark.org/docs/">https://www.wireshark.org/docs/</a></p></blockquote><p>You can also watch some videos.</p><blockquote><p><a href="https://www.youtube.com/results?search_query=wireshark+tutorial">https://www.youtube.com/results?search_query=wireshark+tutorial</a></p></blockquote><p>Then, capture the traffic and filter for the IP addresses like this</p><blockquote><p>ip.addr == a.a.a.a or ip.addr b.b.b.b or ip.addr c.c.c.c</p></blockquote><p>Please replace a.a.a.a, b.b.b.b, etc. with the IP addresses you are looking for.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Oct '15, 10:13</p></div></div><div id="comments-container-46766" class="comments-container"></div><div id="comment-tools-46766" class="comment-tools"></div><div class="clear"></div><div id="comment-46766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

