+++
type = "question"
title = "Why do I see network packets with port 443 as the source (unusual), to destination port 4292?"
description = '''Port 443 is usually the destination port if I am not mistaken, however I see it as the source port going to port 4292 and cannot figure out what could be using that. Is it Carbonite maybe? Thank you.'''
date = "2015-04-09T20:20:00Z"
lastmod = "2015-04-09T20:45:00Z"
weight = 41337
keywords = [ "port", "4293" ]
aliases = [ "/questions/41337" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why do I see network packets with port 443 as the source (unusual), to destination port 4292?](/questions/41337/why-do-i-see-network-packets-with-port-443-as-the-source-unusual-to-destination-port-4292)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41337-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Port 443 is usually the destination port if I am not mistaken, however I see it as the source port going to port 4292 and cannot figure out what could be using that.</p><p>Is it Carbonite maybe?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">port 4293</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '15, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/cd2062ccb8489ed12748ff338a5dbd87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pctech&#39;s gravatar image" /><p>pctech<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pctech has no accepted answers">0%</span></p></div></div><div id="comments-container-41337" class="comments-container"></div><div id="comment-tools-41337" class="comment-tools"></div><div class="clear"></div><div id="comment-41337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41338"></span>

<div id="answer-container-41338" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41338-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Port 443 is the well-known server port for SSL (encrypted) web traffic. So, when a client communicates with a server using SSL, the server will use port 443 and the client will use a dynamically selected port, such as 4292.</p><p>Port 443 will be the destination port for packets <em>from</em> the client and <em>to</em> the server, and it will be the source port for packets <em>from</em> the server and <em>to</em> the client.</p><p>GET requests from the client to the server will be from port 4292 on the client (or whatever port was dynamically selected) and to port 443 on the server. Acknowledgments from the server back to the client will be from port 443 and to port 4292.</p><p>When the server sends a web page to the client, the data packets will be from port 443 on the server and to port 4292 on the client. Acknowledgments from the client back to the server will be from port 4292 and to port 443.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '15, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-41338" class="comments-container"><span id="41361"></span><div id="comment-41361" class="comment"><div id="post-41361-score" class="comment-score"></div><div class="comment-text"><p>I.e., it's <em>not</em> usually the destination port; it's a destination port for a client (Web browser), but it's a <em>source</em> port for a server.</p></div><div id="comment-41361-info" class="comment-info"><span class="comment-age">(10 Apr '15, 14:08)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-41338" class="comment-tools"></div><div class="clear"></div><div id="comment-41338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

