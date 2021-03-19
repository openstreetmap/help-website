+++
type = "question"
title = "TCP piggybacking effects on RTT measurement with Wireshark"
description = '''i&#x27;m trying to get the RTT samples using tshark, most of the application i observe do not use piggybacking property of the TCP. if it is used is there any considerations/differences for RTT calculation with/without piggybacking? (user think times or any other noises will effect the RTT(?) Thanks.'''
date = "2011-03-23T12:41:00Z"
lastmod = "2011-03-23T12:52:00Z"
weight = 3047
keywords = [ "piggyback", "rtt" ]
aliases = [ "/questions/3047" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP piggybacking effects on RTT measurement with Wireshark](/questions/3047/tcp-piggybacking-effects-on-rtt-measurement-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3047-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'm trying to get the RTT samples using tshark, most of the application i observe do not use piggybacking property of the TCP. if it is used is there any considerations/differences for RTT calculation with/without piggybacking? (user think times or any other noises will effect the RTT(?) Thanks.</p></div><div id="question-tags" class="tags-container tags">piggyback rtt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '11, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/bde1409a68745702a5dd0f41c6a544e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="berkey&#39;s gravatar image" /><p>berkey<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="berkey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '11, 12:42</p></div></div><div id="comments-container-3047" class="comments-container"></div><div id="comment-tools-3047" class="comment-tools"></div><div class="clear"></div><div id="comment-3047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3050"></span>

<div id="answer-container-3050" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3050-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way, IMHO, to get RTT data is just to watch the 3 way handshake at the beginning of a TCP conversation. There's no piggybacking taking place because the conversation is just getting started. This is a <em>slightly</em> better method of RTT calculation than using piggyback packets - though neither are totally reliable. Why, you ask?</p><p>Usually there is no system delay associated with the 3 way handshake - the stack attempts to setup the TCP session as soon as possible. There is very little processing involved, and so this usually takes place very quickly. It's possible that a resource starved server could have delays in packet generation, but it's been my experience that this rarely affects the handshake.</p><p>With piggybacking, however, it's possible that the ACK packet is delayed while new data is being prepared for transmission. There could be significant delays in data bearing packet generation from a server that is resource starved/under burden.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-3050" class="comments-container"><span id="3054"></span><div id="comment-3054" class="comment"><div id="post-3054-score" class="comment-score"></div><div class="comment-text"><p>@GeonJay, thanks for the great post +1. But ACK packets should be delayed how long? who decides ? so my idea is to formulate this effect depending on the application using wireshark.</p></div><div id="comment-3054-info" class="comment-info"><span class="comment-age">(23 Mar '11, 12:56)</span> berkey</div></div><span id="3056"></span><div id="comment-3056" class="comment"><div id="post-3056-score" class="comment-score"></div><div class="comment-text"><p>In a perfect world where there was plenty of available data to transfer and the server was under no burden (SSD harddrives, efficient protocol, nothing SWAP'ed out, etc) there would be no delay..if you grabbed some packets in the middle of a huge file transfer you would be able to watch ACKs and/or piggyback'd ACKs and feel pretty comfortable with the RTT that you derived. If the data is being slowly trickled to the IP stack then it's possible that Nagle's could cause some delay. RTT derivation will always be relative - bandwidth bottlenecks, queue delays, solar flares, etc can cause delays.</p></div><div id="comment-3056-info" class="comment-info"><span class="comment-age">(23 Mar '11, 13:04)</span> GeonJay</div></div><span id="3057"></span><div id="comment-3057" class="comment"><div id="post-3057-score" class="comment-score"></div><div class="comment-text"><p>@GeonJay, i understand, 200ms-500ms delay is possible according to my searches for waiting before sending the pure "ACK". is piggybacking supported for all applications ? my observations show that it is not used that much?</p></div><div id="comment-3057-info" class="comment-info"><span class="comment-age">(23 Mar '11, 13:09)</span> berkey</div></div><span id="3058"></span><div id="comment-3058" class="comment"><div id="post-3058-score" class="comment-score"></div><div class="comment-text"><p>You won't see piggybacking a lot because there aren't a lot of "full duplex" applications. Usually if I'm downloading something from you I won't also be sending data to you at the same time. A lot of the seemingly full duplex applications (video/voice chat, etc) are UDP, so they also won't use any kind of piggybacking.</p><p>200-500ms seems pretty extreme for ACK only packet generation - but it's possible if the server is under load. Good ol' ICMP ping can be a fairly reliable source for RTT as well.</p></div><div id="comment-3058-info" class="comment-info"><span class="comment-age">(23 Mar '11, 13:31)</span> GeonJay</div></div><span id="3059"></span><div id="comment-3059" class="comment"><div id="post-3059-score" class="comment-score"></div><div class="comment-text"><p>@GeonJay, thanks for making me clear.</p></div><div id="comment-3059-info" class="comment-info"><span class="comment-age">(23 Mar '11, 13:32)</span> berkey</div></div></div><div id="comment-tools-3050" class="comment-tools"></div><div class="clear"></div><div id="comment-3050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

