+++
type = "question"
title = "keep alive packets at the end of the session"
description = '''Hi, I have captured a TCP session which has TCP keep alive packet at the end. machine A has sent the keep alive packet to machine B and machine B has acknowledged this keep alive packet. But there is no communication after that between them. Does this mean the connection is still open between the tw...'''
date = "2013-09-23T03:21:00Z"
lastmod = "2013-09-23T05:20:00Z"
weight = 25108
keywords = [ "tcp", "keepalive" ]
aliases = [ "/questions/25108" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [keep alive packets at the end of the session](/questions/25108/keep-alive-packets-at-the-end-of-the-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25108-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have captured a TCP session which has TCP keep alive packet at the end. machine A has sent the keep alive packet to machine B and machine B has acknowledged this keep alive packet. But there is no communication after that between them. Does this mean the connection is still open between the two machines? If connection is closed then how to decide when the connection is closed between them?</p><p>The TCP session I captured looks like this: <a href="https://docs.google.com/file/d/0B0MoCNH_0Z5NcGVUV2ttWUZQa00/edit?usp=sharing">link text</a></p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">tcp keepalive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '13, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/57e272f8bacf9005a5cf2ebcd62dcde7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Swamy&#39;s gravatar image" /><p>Swamy<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Swamy has no accepted answers">0%</span></p></div></div><div id="comments-container-25108" class="comments-container"></div><div id="comment-tools-25108" class="comment-tools"></div><div class="clear"></div><div id="comment-25108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25109"></span>

<div id="answer-container-25109" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25109-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the connection is still open between the machines in your capture. Usually, one of the two machines will terminate the session after a global timeout is reached, but sometimes you'll see Keep-Alives for long long times, e.g. for SSH sessions.</p><p>The closing of the connection will be performed either gracefully (using FIN flags) or brutally (using a Reset flag). Unless you see then, the connection is still alive.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '13, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25109" class="comments-container"><span id="25113"></span><div id="comment-25113" class="comment"><div id="post-25113-score" class="comment-score"></div><div class="comment-text"><p>One more clarification though. The Dump file i have has similar kind of TCP sessions and none of them are closed like the dump file i have attached. So according to you all the connections are still opened.One or two sessions like that i would understand that connection is still opened but i have around 25-30 sessions like that.what might be the reason for that?</p></div><div id="comment-25113-info" class="comment-info"><span class="comment-age">(23 Sep '13, 05:56)</span> Swamy</div></div><span id="25114"></span><div id="comment-25114" class="comment"><div id="post-25114-score" class="comment-score"></div><div class="comment-text"><p>Usually a connection is terminated with a Reset flag if the application shuts down that has used the port. So if the application on both ends is still alive, the connection can stay open for a long time.</p><p>E.g users often start database applications in the morning and keep them open even while not using them for hours, so the TCP connection stays open, too. In those cases Keep Alives are very useful to prevent session termination by a Firewall or ACL, but if there aren't such devices in the network the connection doesn't even have to use Keep Alives to keep going.</p></div><div id="comment-25114-info" class="comment-info"><span class="comment-age">(23 Sep '13, 06:07)</span> Jasper ♦♦</div></div></div><div id="comment-tools-25109" class="comment-tools"></div><div class="clear"></div><div id="comment-25109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

