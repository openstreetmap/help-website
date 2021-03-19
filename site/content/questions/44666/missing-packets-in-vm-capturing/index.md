+++
type = "question"
title = "missing packets in VM capturing"
description = '''Hi all,  In a captured dump I found two warnings: TCP: Previous segment not captured (common at capture start) and TCP: ACKed segment that wasn&#x27;t captured (common at capture start). To avoid missing packets I tried to: recapture in a wired and wIreless LAN, use tcpdump instead of dumpcap and I force...'''
date = "2015-07-30T20:15:00Z"
lastmod = "2015-08-03T08:30:00Z"
weight = 44666
keywords = [ "wireshark", "packets", "missing" ]
aliases = [ "/questions/44666" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [missing packets in VM capturing](/questions/44666/missing-packets-in-vm-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44666-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>In a captured dump I found two warnings: TCP: Previous segment not captured (common at capture start) and TCP: ACKed segment that wasn't captured (common at capture start).</p><p>To avoid missing packets I tried to: recapture in a wired and wIreless LAN, use tcpdump instead of dumpcap and I forced quit all other user processes except the one related to the capturing tool and my VM as I'm doing the capturing within it. I'm still having the same warnings.</p><p>I'm wondering why I have missing packets in my capture and how can I avoid missing packets while capturing?</p></div><div id="question-tags" class="tags-container tags">wireshark packets missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 20:15</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Aug '15, 06:48</p></div></div><div id="comments-container-44666" class="comments-container"><span id="44671"></span><div id="comment-44671" class="comment"><div id="post-44671-score" class="comment-score"></div><div class="comment-text"><p>Your pcap contains SSH packets and not SSL I think they are two different protocols(although they have a similar use).</p><p><a href="https://wiki.wireshark.org/SSH">https://wiki.wireshark.org/SSH</a></p></div><div id="comment-44671-info" class="comment-info"><span class="comment-age">(31 Jul '15, 01:46)</span> koundi</div></div><span id="44675"></span><div id="comment-44675" class="comment"><div id="post-44675-score" class="comment-score"></div><div class="comment-text"><p>Well. you need to decode as SSL. It is an SSL traffic but works on non-standard port so that it looks to you as SSH. Thanks for your comment.</p></div><div id="comment-44675-info" class="comment-info"><span class="comment-age">(31 Jul '15, 04:48)</span> flora</div></div><span id="44677"></span><div id="comment-44677" class="comment"><div id="post-44677-score" class="comment-score"></div><div class="comment-text"><p>We won't be able to test the decryption unless you provide the key.</p></div><div id="comment-44677-info" class="comment-info"><span class="comment-age">(31 Jul '15, 05:31)</span> grahamb ♦</div></div><span id="44678"></span><div id="comment-44678" class="comment"><div id="post-44678-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure the keys will be useful for you as I'm using a master key (DH key exchange) where I implemented an SSL preference to accept it and modify some related code just to load it in the right data structure.However,I haven't changed any code that is related to the decryption process. I noticed the decryption works perfectly until it comes to the packets that have the two mentioned warnings (I get the MAC failed thing!). You can may be help me out by checking my dump and see if you can find any reason why I have some no captured packets or suggest how can I avoid them in my next capture. Thanks.</p></div><div id="comment-44678-info" class="comment-info"><span class="comment-age">(31 Jul '15, 06:12)</span> flora</div></div><span id="44682"></span><div id="comment-44682" class="comment"><div id="post-44682-score" class="comment-score"></div><div class="comment-text"><p>So the real question is "Why do I have missing packets in my capture". Fairly obviously, SSL decryption can't function with missing packets.</p></div><div id="comment-44682-info" class="comment-info"><span class="comment-age">(31 Jul '15, 06:31)</span> grahamb ♦</div></div><span id="44688"></span><div id="comment-44688" class="comment not_top_scorer"><div id="post-44688-score" class="comment-score"></div><div class="comment-text"><p>You are right! I edited my question above. Thank you so much for clarifying this.</p><p>I guess I miss understood the warning messages. as an example, from the Expert Info: packet#233 TCP: Previous segment not captured (common at capture start) from Wireshark's main window: packet#233: [TCP Previous segment not captured] [TCP segment of a reassembled PDU] The previous segment ( the missing one, is the one with sequence#: 127033) and obviously this effects SSL.</p></div><div id="comment-44688-info" class="comment-info"><span class="comment-age">(31 Jul '15, 07:24)</span> flora</div></div><span id="44715"></span><div id="comment-44715" class="comment not_top_scorer"><div id="post-44715-score" class="comment-score"></div><div class="comment-text"><p>Maybe you have somewhere real CRC failures in your network?</p></div><div id="comment-44715-info" class="comment-info"><span class="comment-age">(31 Jul '15, 16:49)</span> Christian_R</div></div><span id="44820"></span><div id="comment-44820" class="comment not_top_scorer"><div id="post-44820-score" class="comment-score"></div><div class="comment-text"><p>not relevant to my situation.. thank you.</p></div><div id="comment-44820-info" class="comment-info"><span class="comment-age">(04 Aug '15, 06:40)</span> flora</div></div></div><div id="comment-tools-44666" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-44666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44787"></span>

<div id="answer-container-44787" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44787-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just out of curiosity how much RAM, and how many processors/cpus have your set for your VM? Is it possible that the VM is getting overloaded due to a lack of memory or processing power? Have you tried capturing from the host machine or even from outside the host machine to see if you are still dropping packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/0a92214fd94d818059f740cdd56be7af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greenfreq&#39;s gravatar image" /><p>greenfreq<br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greenfreq has one accepted answer">33%</span></p></div></div><div id="comments-container-44787" class="comments-container"><span id="44821"></span><div id="comment-44821" class="comment"><div id="post-44821-score" class="comment-score"></div><div class="comment-text"><p>I did use more powerful machine than mine and the problem has been resolved. Thank you.</p></div><div id="comment-44821-info" class="comment-info"><span class="comment-age">(04 Aug '15, 06:42)</span> flora</div></div></div><div id="comment-tools-44787" class="comment-tools"></div><div class="clear"></div><div id="comment-44787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

