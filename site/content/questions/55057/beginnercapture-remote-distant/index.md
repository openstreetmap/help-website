+++
type = "question"
title = "[beginner]capture remote distant"
description = '''Hi, I work on WireShark on Windows 7 Pro. How do I make precisely to capture all the packages passing in transit of a distant machine A of ip v4 XXX.XXX.XXX.XXX towards a distant machine B of ip v4 YYY.YYY.YYY.YYY, knowing that these 2 machines do not belong to the local area network but are very di...'''
date = "2016-08-22T15:50:00Z"
lastmod = "2016-08-23T06:32:00Z"
weight = 55057
keywords = [ "#velvet" ]
aliases = [ "/questions/55057" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[beginner\]capture remote distant](/questions/55057/beginnercapture-remote-distant)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55057-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I work on WireShark on Windows 7 Pro.</p><p>How do I make precisely to capture all the packages passing in transit of a distant machine A of ip v4 XXX.XXX.XXX.XXX towards a distant machine B of ip v4 YYY.YYY.YYY.YYY, knowing that these 2 machines do not belong to the local area network but are very distant on the internet network?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">#velvet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '16, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/56d94591c91e28d29d99fb214a880aff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tercyanos&#39;s gravatar image" /><p>Tercyanos<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tercyanos has no accepted answers">0%</span></p></div></div><div id="comments-container-55057" class="comments-container"></div><div id="comment-tools-55057" class="comment-tools"></div><div class="clear"></div><div id="comment-55057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55072"></span>

<div id="answer-container-55072" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55072-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have in mind that the traffic between A and B transits through your machine, and you want to <strong>capture</strong> only that traffic, use a <strong>capture</strong> filter <code>host XXX.XXX.XXX.XXX and host YYY.YYY.YYY.YYY</code>. If you want to capture all traffic and only <strong>show</strong> just the traffic between the A and B, use no capture filter and apply a <strong>display</strong> filter <code>ip.addr == XXX.XXX.XXX.XXX and ip.addr == YYY.YYY.YYY.YYY</code>.</p><p>If there is a NAT between the machine on which you capture and the internet, you'll need to change the capture filter to <code>host XXX.XXX.XXX.XXX or host YYY.YYY.YYY.YYY</code>, meaning that you would capture also traffic running between your machine and A or B which is not transited between them.</p><p>If the machines A and B have private addresses and there is a NAT in front of each of them, you'll need to use the public side addresses of the NATs in the capture filter.</p><p>If the traffic between them doesn't transit through your PC, and you don't have access to a machine on the path between then (including any of the two machines themselves), you are out of luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '16, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55072" class="comments-container"></div><div id="comment-tools-55072" class="comment-tools"></div><div class="clear"></div><div id="comment-55072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

