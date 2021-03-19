+++
type = "question"
title = "who is killing connection"
description = '''Maybe easy question, but I dont know how. I need to trace who is killing connection between my PC and Oracle. I have IP address. After some time of using connection is closed and I need to know who/what does it, oracle or firewall? Or anything else? How do I trace it?'''
date = "2015-06-10T04:12:00Z"
lastmod = "2015-06-10T04:16:00Z"
weight = 43035
keywords = [ "closes", "connection", "database" ]
aliases = [ "/questions/43035" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [who is killing connection](/questions/43035/who-is-killing-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43035-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Maybe easy question, but I dont know how. I need to trace who is killing connection between my PC and Oracle. I have IP address. After some time of using connection is closed and I need to know who/what does it, oracle or firewall? Or anything else? How do I trace it?</p></div><div id="question-tags" class="tags-container tags">closes connection database</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '15, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/d8a00fa85d9d15c873768ede74627346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="innspiron&#39;s gravatar image" /><p>innspiron<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="innspiron has no accepted answers">0%</span></p></div></div><div id="comments-container-43035" class="comments-container"></div><div id="comment-tools-43035" class="comment-tools"></div><div class="clear"></div><div id="comment-43035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43037"></span>

<div id="answer-container-43037" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43037-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Best case, with a third PC capturing what the other two do. See the <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Wiki page for capture setup options</a>.</p><p>If SPAN/TAP is not possible, trace on your PC, but that may give you incorrect results. When you have the packets, check connection by connection if there's anything out of the ordinary terminating it, e.g. TCP errors (filter for tcp.analysis.flags) or timeouts. Easier said than done, but if you can upload a capture to e.g. <a href="https://appliance.cloudshark.org/upload/">Cloudshark</a> some of us can take a look (if it's not too many packets).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-43037" class="comments-container"></div><div id="comment-tools-43037" class="comment-tools"></div><div class="clear"></div><div id="comment-43037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

