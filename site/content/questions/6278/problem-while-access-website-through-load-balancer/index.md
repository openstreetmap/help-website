+++
type = "question"
title = "Problem while access website through load balancer"
description = '''I am facing problem while accessing web site through load balancer but it work fine when i call website directly. After getting traces i found my client is retransmitting TCP packet with PSH+ACK four times and after that load balancer send TCP packet with RST flag. Before that my client send SYN and...'''
date = "2011-09-12T04:53:00Z"
lastmod = "2011-09-12T07:34:00Z"
weight = 6278
keywords = [ "load-balancer" ]
aliases = [ "/questions/6278" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem while access website through load balancer](/questions/6278/problem-while-access-website-through-load-balancer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6278-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am facing problem while accessing web site through load balancer but it work fine when i call website directly.</p><p>After getting traces i found my client is retransmitting TCP packet with PSH+ACK four times and after that load balancer send TCP packet with RST flag.</p><p>Before that my client send SYN and successfully got SYN+ACK.</p><p>Please help me to find out whats wrong with it.</p><p>Regards, imran</p></div><div id="question-tags" class="tags-container tags">load-balancer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/de91466e4164c7f05d9ad2a6b4f9753f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imranrazakhan&#39;s gravatar image" /><p>imranrazakhan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imranrazakhan has no accepted answers">0%</span></p></div></div><div id="comments-container-6278" class="comments-container"></div><div id="comment-tools-6278" class="comment-tools"></div><div class="clear"></div><div id="comment-6278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6284"></span>

<div id="answer-container-6284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6284-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you make the trace on the client or server side of the loadbalancer? Usually a loadbalancer will terminate the TCP session of the client to look into the HTTP request, so that it can make a loadbalancing decision based on the content of the HTTP request (think of cookie persistency as an example why this is needed).</p><p>Then I can think of two things that might be going wrong in your setup.</p><ol><li><p>The loadbalancer is one-armed, but you do not NAT the source address of the client. This means traffic from the server goes back to the client instead of to the loadbalancer to change the real server IP address back to the virtual address.</p></li><li><p>Or the loadbalancer tries to open a connection to the server but for whatever reason does not succeed and therefor gives up after a while. In the mean time the client had retransmitted its request a couple of times.</p></li></ol><p>In loadbalanced scenarios, it is always best to make traces on the client-side as well as the server-side of the loadbalancer to be able to follow its behavior.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6284" class="comments-container"></div><div id="comment-tools-6284" class="comment-tools"></div><div class="clear"></div><div id="comment-6284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

