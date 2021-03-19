+++
type = "question"
title = "Question in regard with TCP Streams."
description = '''Dear All Currently I&#x27;m trying to investigate a &quot;possible&quot; network issue for one of our customers but since I&#x27;ve only just had a course in Wireshark and basic TCP knowledge, I was hoping that one of you guys would be able to help me out. The client is experiencing some performance issues towards one ...'''
date = "2016-01-13T05:57:00Z"
lastmod = "2016-01-13T07:03:00Z"
weight = 49168
keywords = [ "http", "stream", "tcp" ]
aliases = [ "/questions/49168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Question in regard with TCP Streams.](/questions/49168/question-in-regard-with-tcp-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All</p><p>Currently I'm trying to investigate a "possible" network issue for one of our customers but since I've only just had a course in Wireshark and basic TCP knowledge, I was hoping that one of you guys would be able to help me out.</p><p>The client is experiencing some performance issues towards one of their applications. After an initial analysis and following 1 particular TCP stream I've noticed that during the timeframe that these issues were found a TCP 3-Way Handshake was set-up in less than 1 ms. This is good and I expected such. The service on the server is a webserver.</p><p>What I then noticed is that after the 3-way handshake for 53 seconds (TCP Delta) there was no communication and all of a sudden a GET request from the client towards the server. It looks to me that a TCP session was established towards the application and all other queries (GET requests, POST requests) were being sent within 1 TCP stream. Is this normal and even performant? I would expect this to be causing quite some issues if lots of hosts try to connect towards 1 particular server (connection tables being filled up and the like).</p><p>Any information would be greatly appreciated!</p><p>Thanks all!</p></div><div id="question-tags" class="tags-container tags">http stream tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '16, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/5b4d00c75b8f1bb3cac9920591812127?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Herazio&#39;s gravatar image" /><p>Herazio<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Herazio has no accepted answers">0%</span></p></div></div><div id="comments-container-49168" class="comments-container"></div><div id="comment-tools-49168" class="comment-tools"></div><div class="clear"></div><div id="comment-49168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49171"></span>

<div id="answer-container-49171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49171-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Reuse of a single TCP session for several requests in a row is in fact saving resources rather than wasting them.</p><p>Dangerously simplifying: depending on the scenario, the "connection tables" have to contain the data about a session for some time after its closure, so if you establish a new session from the same client to the same server during that time, you occupy two "rows of the connection tables" instead of one. Plus, if you would decide to systematically use a separate session for each request even if some of the previous requests has not been responded yet (and so its respective session would be still active), you could waste even several "rows in the connection tables" for a single client.</p><p>So the usual habit is to establish a tcp session at the occurrence of the first application request and keep it open until some inactivity timer expires or until the related application or e.g. browser window is closed.</p><p>Therefore, to find out whether the gap between setting up the TCP session and using it to deliver the first request ever is logical or suspicious, you have to look at the application behaving like this. For a human-controlled web browser it is surely a strange behaviour, for some automated communication tool using http it may not be.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '16, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49171" class="comments-container"></div><div id="comment-tools-49171" class="comment-tools"></div><div class="clear"></div><div id="comment-49171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

