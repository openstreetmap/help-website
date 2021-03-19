+++
type = "question"
title = "Why i receive packets these packets ? ( no mirror port configured )"
description = '''Hi, I&#x27;m running Wireshark on server to see packets from / to this server, but something strange that i see conversations between other sources &amp;amp; destinations, this server is not part of these conversations i&#x27;m sure that there is no mirror port to this server so i&#x27;m wondering ?!! Any help ?'''
date = "2015-08-11T23:26:00Z"
lastmod = "2015-08-11T23:33:00Z"
weight = 44983
keywords = [ "tcp" ]
aliases = [ "/questions/44983" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why i receive packets these packets ? ( no mirror port configured )](/questions/44983/why-i-receive-packets-these-packets-no-mirror-port-configured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44983-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm running Wireshark on server to see packets from / to this server, but something strange that i see conversations between other sources &amp; destinations, this server is not part of these conversations i'm sure that there is no mirror port to this server so i'm wondering ?!!</p><p>Any help ?</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/54eaa9bdc2a24724f43a6722a0fed01a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mahmoud%20Saad&#39;s gravatar image" /><p>Mahmoud Saad<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mahmoud Saad has no accepted answers">0%</span></p></div></div><div id="comments-container-44983" class="comments-container"></div><div id="comment-tools-44983" class="comment-tools"></div><div class="clear"></div><div id="comment-44983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44984"></span>

<div id="answer-container-44984" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44984-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're seeing only single packets at a time that's normal - switches drop MAC addresses after a while and re-learn them. While the MAC is not in the MAC address table the packet is flooded to all ports. That means that Wireshark will also see it. After the flooding of the packet, the MAC is relearned and the flooding stops.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44984" class="comments-container"><span id="44995"></span><div id="comment-44995" class="comment"><div id="post-44995-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper but the extra captured traffic is not broadcast, i see tcp conversations.</p></div><div id="comment-44995-info" class="comment-info"><span class="comment-age">(12 Aug '15, 02:49)</span> Mahmoud Saad</div></div><span id="44996"></span><div id="comment-44996" class="comment"><div id="post-44996-score" class="comment-score">1</div><div class="comment-text"><p>yep, I was talking about unicasts. They get flooded by the switch if the MAC address is unknown. You should only see single packets, not full conversations though. If you see full conversations your switch may have fallen back into "flood all" mode, which usually only happens when it is really overloaded.</p></div><div id="comment-44996-info" class="comment-info"><span class="comment-age">(12 Aug '15, 04:07)</span> Jasper ♦♦</div></div><span id="45008"></span><div id="comment-45008" class="comment"><div id="post-45008-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper</p></div><div id="comment-45008-info" class="comment-info"><span class="comment-age">(12 Aug '15, 08:40)</span> Mahmoud Saad</div></div><span id="45011"></span><div id="comment-45011" class="comment"><div id="post-45011-score" class="comment-score"></div><div class="comment-text"><p>@Mahmoud Saad,</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-45011-info" class="comment-info"><span class="comment-age">(12 Aug '15, 09:42)</span> grahamb ♦</div></div></div><div id="comment-tools-44984" class="comment-tools"></div><div class="clear"></div><div id="comment-44984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

