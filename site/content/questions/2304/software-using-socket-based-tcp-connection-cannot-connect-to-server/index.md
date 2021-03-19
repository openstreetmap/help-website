+++
type = "question"
title = "Software using Socket Based TCP connection cannot connect to server."
description = '''Hi, On my computer other network based software are able to connect to servers and I am able to surf the internet as well on this computer however there is a software that uses socket based tcp connection however upon starting that application it reports &quot;No connection&quot;. How can i resolve this. How ...'''
date = "2011-02-13T09:22:00Z"
lastmod = "2011-02-13T16:43:00Z"
weight = 2304
keywords = [ "tcp" ]
aliases = [ "/questions/2304" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Software using Socket Based TCP connection cannot connect to server.](/questions/2304/software-using-socket-based-tcp-connection-cannot-connect-to-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2304-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>On my computer other network based software are able to connect to servers and I am able to surf the internet as well on this computer however there is a software that uses socket based tcp connection however upon starting that application it reports "No connection". How can i resolve this. How to resolve/troubleshoot socket based tcp connections issues.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '11, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/fd1da6cd42b6459e674b1104d81731c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rseni&#39;s gravatar image" /><p>rseni<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rseni has no accepted answers">0%</span></p></div></div><div id="comments-container-2304" class="comments-container"></div><div id="comment-tools-2304" class="comment-tools"></div><div class="clear"></div><div id="comment-2304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2317"></span>

<div id="answer-container-2317" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2317-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could install Wireshark and take a look at all conversations that get started around the time you start the application that has a problem. Go to Statistics -&gt; Conversations for a list (or simply scroll through the packet list).</p><p>If there is a connection that is refused by the server you will see a SYN packet followed by an RST packet - that way you'll know that the server doesn't have any process listening on the TCP port that was accessed. If you don't get anything back on the SYN packet there is most likely a Firewall in between you and the server that blocks the communication.</p><p>BTW it helps to know which IP the server has, because then you can filter on all conversations to that IP by using <code>ip.addr==X.X.X.X</code> where X.X.X.X is the server IP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2317" class="comments-container"></div><div id="comment-tools-2317" class="comment-tools"></div><div class="clear"></div><div id="comment-2317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

