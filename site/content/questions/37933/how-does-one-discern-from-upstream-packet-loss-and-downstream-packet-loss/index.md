+++
type = "question"
title = "How does one Discern from Upstream Packet Loss and Downstream Packet Loss"
description = '''I&#x27;m just curious to know how does one differentiate between upstream and downstream packet loss? I do know how to filter out for packet loss, but I don&#x27;t know how to differentiate between upstream and downstream packet loss. Thanks!'''
date = "2014-11-17T22:49:00Z"
lastmod = "2014-11-17T23:33:00Z"
weight = 37933
keywords = [ "packetloss" ]
aliases = [ "/questions/37933" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does one Discern from Upstream Packet Loss and Downstream Packet Loss](/questions/37933/how-does-one-discern-from-upstream-packet-loss-and-downstream-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37933-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm just curious to know how does one differentiate between upstream and downstream packet loss? I do know how to filter out for packet loss, but I don't know how to differentiate between upstream and downstream packet loss. Thanks!</p></div><div id="question-tags" class="tags-container tags">packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></div></div><div id="comments-container-37933" class="comments-container"></div><div id="comment-tools-37933" class="comment-tools"></div><div class="clear"></div><div id="comment-37933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37936"></span>

<div id="answer-container-37936" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37936-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can usually tell by the fact if you see a retransmission and the original (meaning, loss occurs after your capture location) or just the retransmission (loss occuring before your capture location).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37936" class="comments-container"><span id="37955"></span><div id="comment-37955" class="comment"><div id="post-37955-score" class="comment-score"></div><div class="comment-text"><p>So when you see a retransmission and the original packet, is that downstream packet loss? And if you don't see an original packet that is upstream packet loss..? How does one check for that in wireshark?</p></div><div id="comment-37955-info" class="comment-info"><span class="comment-age">(18 Nov '14, 16:27)</span> Beldum</div></div><span id="37957"></span><div id="comment-37957" class="comment"><div id="post-37957-score" class="comment-score"></div><div class="comment-text"><p>There's the question of what upstream/downstream means for you exactly... everybody may have a different idea of which is which.</p><p>Let's say you're capturing in the middle between client and server, and you see packet and its retransmission coming from the server towards the client - that means that the packet loss is closer to the client from your capture location. If you only see the retransmission, it's closer to the server from your capture location.</p><p>Determining if there is an original and its retransmission is simple: if you see a retransmission, check if you can find an earlier packet with the same sequence number containing a non zero payload - if you do, you have the original (payload size may vary, but must not be empty).</p></div><div id="comment-37957-info" class="comment-info"><span class="comment-age">(18 Nov '14, 23:57)</span> Jasper ♦♦</div></div></div><div id="comment-tools-37936" class="comment-tools"></div><div class="clear"></div><div id="comment-37936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

