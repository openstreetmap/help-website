+++
type = "question"
title = "Http failure indicated by the user"
description = '''https://www.cloudshark.org/captures/c80a58e1dccb To start with; the one server is the inside on the network and the others is in DMZ 2 a firewall separates them. I have a user complaining that from time to time they lose connection to and http session,  But there no indication of a http upload disco...'''
date = "2013-05-19T16:18:00Z"
lastmod = "2013-05-19T18:56:00Z"
weight = 21279
keywords = [ "http" ]
aliases = [ "/questions/21279" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Http failure indicated by the user](/questions/21279/http-failure-indicated-by-the-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21279-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://www.cloudshark.org/captures/c80a58e1dccb">https://www.cloudshark.org/captures/c80a58e1dccb</a> To start with; the one server is the inside on the network and the others is in DMZ 2 a firewall separates them. I have a user complaining that from time to time they lose connection to and http session, But there no indication of a http upload disconnection. Is seeing in the three way handshake, but I also see a bunch of NOPS, through the trace, but everything looks good. One retransmission, I read some that the NOPS are like keep-aivers because of the firewall time-out options, but I also have learned that 4 NOPS in a row is options removed by the firewall. Can someone take a look and let me know what you thank. The trace looks good to me from what I can tell.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '13, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/b616f858ccbee3de56d053f1b002a757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ernest%20Johnson&#39;s gravatar image" /><p>Ernest Johnson<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ernest Johnson has no accepted answers">0%</span></p></div></div><div id="comments-container-21279" class="comments-container"></div><div id="comment-tools-21279" class="comment-tools"></div><div class="clear"></div><div id="comment-21279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21280"></span>

<div id="answer-container-21280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21280-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Four NOPs in a row in a SYN packet is not a good thing, because it usually means that a device has removed TCP options by replacing them with NOPs. It would be a good idea to reconfigure the Firewall not to touch the TCP options.</p><p>Also, there seems to be packet loss in frame 132, which is retransmitted in frame 133, but your capture was made before the location where it was lost. As far as I can tell all that lost packet costs you are about 200ms.</p><p>The only reset packet is packet #2 but since there is only an additional FIN packet right before it it looks just like normal session termination. I guess if you can manage to fix the four NOP issue things will run much smoother.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '13, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21280" class="comments-container"><span id="21281"></span><div id="comment-21281" class="comment"><div id="post-21281-score" class="comment-score"></div><div class="comment-text"><p>Thanks you Jasper, what would you recomend we bo to fix the firewall to not touch the NOPS ?</p></div><div id="comment-21281-info" class="comment-info"><span class="comment-age">(19 May '13, 19:20)</span> Ernest Johnson</div></div><span id="21293"></span><div id="comment-21293" class="comment"><div id="post-21293-score" class="comment-score"></div><div class="comment-text"><p>what is your firewall brand?</p></div><div id="comment-21293-info" class="comment-info"><span class="comment-age">(20 May '13, 03:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-21280" class="comment-tools"></div><div class="clear"></div><div id="comment-21280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

