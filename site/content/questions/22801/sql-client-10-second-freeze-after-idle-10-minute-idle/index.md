+++
type = "question"
title = "sql client 10 second freeze after idle 10 minute idle"
description = '''The scenario is: The situation is this:  i have sql based application client Keep a client &quot;untouched&quot; for 10minutes or more. Come back Do an operation that triggers a dbserver call (This means: write in a socket which is already open to a dbserver instance)  What happens now is the following:  The ...'''
date = "2013-07-10T06:35:00Z"
lastmod = "2013-07-10T07:09:00Z"
weight = 22801
keywords = [ "tcp", "sql" ]
aliases = [ "/questions/22801" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [sql client 10 second freeze after idle 10 minute idle](/questions/22801/sql-client-10-second-freeze-after-idle-10-minute-idle)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22801-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The scenario is: The situation is this:</p><ul><li>i have sql based application client Keep a client "untouched" for 10minutes or more.</li><li>Come back</li><li>Do an operation that triggers a dbserver call (This means: write in a socket which is already open to a dbserver instance)</li></ul><p>What happens now is the following:</p><ul><li>The "write" to the socket gets stuck for 18 seconds.</li><li>Then we get an "error" (connection closed) in the client side (dcl error -209)</li><li>Then the client reconnects - and all works fine.</li></ul><p>The strange thing is this "write" operation that gets "stuck".</p><p>Could a switch config or OS/application decide to close established connections that are not used after some delay? (Apparently set at 10 minutes). Why would this "intermediary" device cause a timeout of 18 seconds when we try to write in the "old connection"?</p><p>Please advice</p></div><div id="question-tags" class="tags-container tags">tcp sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p>tbaror<br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '13, 09:42</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-22801" class="comments-container"></div><div id="comment-tools-22801" class="comment-tools"></div><div class="clear"></div><div id="comment-22801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22807"></span>

<div id="answer-container-22807" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22807-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>could a switch config or os/application can decide to close open connections that are not used after some delay?</p></blockquote><p>sounds like there is a firewall between your client and server. After some time of inactivity in the TCP connection (no packet sent in either direction), it will drop the session in its internal tables.</p><blockquote><p>Why would this "intermediary" device cause a timeout of 18 seconds when we try to write in the "old connection"?</p></blockquote><p>If the client sends a new packet, the firewall will drop that packet, as there is no 'open' session any longer. The client may/will re-try to send the packet for a certain amount of time (18 seconds in your case) and then give up and show the error message.</p><p>So, if there is a firewall involved, please ask the firewall admin to increase the "IDLE timeout" for those sessions. The firewall could be <strong>on</strong> the SQL server as well!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '13, 07:23</p></div></div><div id="comments-container-22807" class="comments-container"></div><div id="comment-tools-22807" class="comment-tools"></div><div class="clear"></div><div id="comment-22807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

