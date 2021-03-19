+++
type = "question"
title = "Problem with SMTPS"
description = ''' The Bat! can get mail throught IMAP, but can&#x27;t send messages. Using secure smtp.yandex.ru port is working. '''
date = "2015-08-08T16:30:00Z"
lastmod = "2015-08-11T16:17:00Z"
weight = 44933
keywords = [ "yandex", "smtps" ]
aliases = [ "/questions/44933" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with SMTPS](/questions/44933/problem-with-smtps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44933-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/465_Uo4ks8V.png" alt="tcpport465" /></p><p>The Bat! can get mail throught IMAP, but can't send messages.</p><p>Using secure smtp.yandex.ru</p><p>port is working.<br />
</p></div><div id="question-tags" class="tags-container tags">yandex smtps</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '15, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/73e977acb79f7c74e93399f7996ac0d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrei%20S&#39;s gravatar image" /><p>Andrei S<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrei S has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-44933" class="comments-container"><span id="44934"></span><div id="comment-44934" class="comment"><div id="post-44934-score" class="comment-score"></div><div class="comment-text"><p>From the looks of it: the TCP port is not working.</p></div><div id="comment-44934-info" class="comment-info"><span class="comment-age">(08 Aug '15, 22:53)</span> Jaap ♦</div></div></div><div id="comment-tools-44933" class="comment-tools"></div><div class="clear"></div><div id="comment-44933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44974"></span>

<div id="answer-container-44974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44974-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no SYN-ACK for the SYN.</p><p>As the server does answer to SYN on port 465, I see the following possible reasons for your problem:</p><ul><li>your gateway (firewall) blocks TCP port 465</li><li>your gateway (firewall) does not do source NAT for that traffic</li><li>there is a problem with routing on your gateway (firewall), meaning the gateway does not know how to route traffic to smtp.yandex.ru. Maybe there is a network and/or host route to 213.180.204.xx on your gateway for whatever reason</li><li>somebody (your ISP) on the way between your gateway and the receiver blocks the SYN on port 465</li><li>the receiver side blocks the SYN from your client, maybe due to bad IP reputation or due to TCP flags/options in the SYN frame that it does not like</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 16:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44974" class="comments-container"></div><div id="comment-tools-44974" class="comment-tools"></div><div class="clear"></div><div id="comment-44974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

