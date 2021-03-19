+++
type = "question"
title = "All TCP connections end with RST"
description = '''Hi. I&#x27;m doing an analysis on a network and while doing a capture from client&#x27;s end I found out that all TCP connections end with reset packets. The network looks like: Client - Firewall - Load balancer(+SSL acceleration) - Server So when I&#x27;m capturing traffic from a client I see that the TCP traffic...'''
date = "2012-11-12T02:21:00Z"
lastmod = "2012-11-12T02:59:00Z"
weight = 15815
keywords = [ "rst", "reset", "connection", "ack", "tcp" ]
aliases = [ "/questions/15815" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [All TCP connections end with RST](/questions/15815/all-tcp-connections-end-with-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15815-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I'm doing an analysis on a network and while doing a capture from client's end I found out that all TCP connections end with reset packets.</p><p>The network looks like: Client - Firewall - Load balancer(+SSL acceleration) - Server</p><p>So when I'm capturing traffic from a client I see that the TCP traffic is flowing fine and client ACKs packet's normally. After the last segment is ACKed nothing happens for a ~5 seconds and then the rest of the connection <strong>always</strong> goes like this:</p><hr /><p>SERVER sends 'Encrypted alert'-packet</p><p>SERVER sends FIN,ACK</p><p>CLIENT sends ACK</p><p>CLIENT sends 'Encrypted alert'-packet</p><p>CLIENT sends RST,ACK</p><hr /><p>So my questions is: Is this normal behavior or could there be something wrong with the configuration. Any help is appreciated.</p><p>-Rakki</p></div><div id="question-tags" class="tags-container tags">rst reset connection ack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '12, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/387f58c09269aee8709bb3d68f33ea93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakki&#39;s gravatar image" /><p>rakki<br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakki has no accepted answers">0%</span></p></div></div><div id="comments-container-15815" class="comments-container"></div><div id="comment-tools-15815" class="comment-tools"></div><div class="clear"></div><div id="comment-15815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15816"></span>

<div id="answer-container-15816" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15816-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>RST used to be a flag that indicated a session termination due to trouble, but in the last couple of years the RST flag is more and more used to shutdown sessions that had no trouble at all. Mostly because it is faster than FIN-ACK-FIN-ACK, and it releases the stack ressources right away while FIN might lead to a TIME-WAIT state.</p><p>So I'd say seeing reset packets at the end of a conversation is pretty normal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15816" class="comments-container"><span id="15817"></span><div id="comment-15817" class="comment"><div id="post-15817-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jasper for the info. So you would also say that the 5 seconds delay before this happens is also normal?</p><p>Why can't it do this right away after the last ACK is received?</p></div><div id="comment-15817-info" class="comment-info"><span class="comment-age">(12 Nov '12, 03:06)</span> rakki</div></div><span id="15820"></span><div id="comment-15820" class="comment"><div id="post-15820-score" class="comment-score"></div><div class="comment-text"><p>That is usually a result of the systems keeping the connection open in case on of the nodes has another request. After a timeout one (or both) nodes decide to tear down the connection since there doesn't seem to be the need for further data transfers in that session.</p></div><div id="comment-15820-info" class="comment-info"><span class="comment-age">(12 Nov '12, 04:38)</span> Jasper ♦♦</div></div></div><div id="comment-tools-15816" class="comment-tools"></div><div class="clear"></div><div id="comment-15816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

