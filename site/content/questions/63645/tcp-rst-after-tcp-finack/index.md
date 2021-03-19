+++
type = "question"
title = "TCP RST after TCP FIN/ACK"
description = '''Hi  Does anyone know why a Server (10.161.96.228) sends two TCP RST after a successfull termination of the session with FIN/ACK from both the Server and the Client (10.90.32.180? Is this normal, as i see it also in other sessions (X11, etc.) Regards, Patrick '''
date = "2017-09-26T04:23:00Z"
lastmod = "2017-09-26T04:49:00Z"
weight = 63645
keywords = [ "reset" ]
aliases = [ "/questions/63645" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP RST after TCP FIN/ACK](/questions/63645/tcp-rst-after-tcp-finack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63645-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Does anyone know why a Server (10.161.96.228) sends two TCP RST after a successfull termination of the session with FIN/ACK from both the Server and the Client (10.90.32.180?</p><p>Is this normal, as i see it also in other sessions (X11, etc.)</p><p>Regards, Patrick</p><p><img src="https://osqa-ask.wireshark.org/upfiles/RST_Qyi8eGU.jpeg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">reset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '17, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/d316fcd2d12eaac42e4ae584dc4bf386?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kehlpat&#39;s gravatar image" /><p>kehlpat<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kehlpat has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63645" class="comments-container"></div><div id="comment-tools-63645" class="comment-tools"></div><div class="clear"></div><div id="comment-63645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63647"></span>

<div id="answer-container-63647" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63647-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would say there's nothing to worry about, unless there should have been more data - but since both sides already said goodbye via FIN the RSTs won't do no harm. It's hard to say where they come from, but maybe a device between the endpoints created them, e.g. a Firewall. This could be checked by looking at the TTL - if it's the same for the RSTs as for the normal packets from the IP it's the endpoint doing this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '17, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63647" class="comments-container"></div><div id="comment-tools-63647" class="comment-tools"></div><div class="clear"></div><div id="comment-63647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

