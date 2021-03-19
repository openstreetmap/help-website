+++
type = "question"
title = "cable TV box - slow - DUP ACK"
description = '''I&#x27;ve been having painfully slow downloads on my Cable TV boxes for the last couple of months and I&#x27;ve been trying to solve the problem. using port mirroring, I&#x27;ve managed to create a wireshark port capture of what is happening when I run a speed test on the cable tv box. The cable box IP is 192.168....'''
date = "2015-08-08T23:51:00Z"
lastmod = "2015-08-15T09:00:00Z"
weight = 44935
keywords = [ "box", "dup", "slow", "ack", "cable" ]
aliases = [ "/questions/44935" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [cable TV box - slow - DUP ACK](/questions/44935/cable-tv-box-slow-dup-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been having painfully slow downloads on my Cable TV boxes for the last couple of months and I've been trying to solve the problem.</p><p>using port mirroring, I've managed to create a wireshark port capture of what is happening when I run a speed test on the cable tv box. The cable box IP is 192.168.55.253 in this case.</p><p><a href="http://www.megafileupload.com/97uX/portcapturefoxtelfailing.pcapng">http://www.megafileupload.com/97uX/portcapturefoxtelfailing.pcapng</a></p><p>There seems to be a whole heap of TCP DUP ACK going on, would that have something to do with it?</p></div><div id="question-tags" class="tags-container tags">box dup slow ack cable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '15, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/f378745f78926dbf5f3037c752d62d6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toddfraser88&#39;s gravatar image" /><p>toddfraser88<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toddfraser88 has no accepted answers">0%</span></p></div></div><div id="comments-container-44935" class="comments-container"></div><div id="comment-tools-44935" class="comment-tools"></div><div class="clear"></div><div id="comment-44935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45143"></span>

<div id="answer-container-45143" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45143-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Let me rephrase the question: why does the speed test fail when connecting via a MikroTik router?</p><p>The 'speed-test' consists of an HTTP GET request of a large (10576244) file.<br />
The test fails because the TCP sessions do not recover from packet loss instead the TV box closes the connection prematurely after 6 seconds not waiting long enough for the retransmission to be successful.</p><p>The succeeding speedtests via the netgear router do not show any packet loss.</p><p>So unless you can convince the TV box to wait longer for a successful retransmission,to fix this problem you need to avoid the packet loss.<br />
As the number of segments in flight is not dramatically high due to the low windowsize offering my bet is that you are suffering from the default queue size being too low in your MikroTik router.</p><p>As per <a href="http://wiki.mikrotik.com/wiki/Manual:Queue_Size">http://wiki.mikrotik.com/wiki/Manual:Queue_Size - Default-small queue type</a> "By default most of the queues in RouterOS have queue size of 10. "<br />
</p><p>This is probably not enough to get a seamless packet-flow going .</p><p>Maybe this problem is better addressed to the <a href="http://forum.mikrotik.com/">http://forum.mikrotik.com/</a></p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '15, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-45143" class="comments-container"></div><div id="comment-tools-45143" class="comment-tools"></div><div class="clear"></div><div id="comment-45143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44986"></span>

<div id="answer-container-44986" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44986-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"There seems to be a whole heap of TCP DUP ACK going on, would that have something to do with it?"<br />
</p><p>If you refer to 'it' as the slow downloads the answer is no.<br />
The poor download performance is is more owed to the low windowsize offering of the cable box that does not grow above 17520 bytes.<br />
At an average RTT of more than 50ms this will always be the bottleneck. See the discussions on <a href="https://en.wikipedia.org/wiki/Bandwidth-delay_product">Bandwidth Delay Product</a><br />
</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-44986" class="comments-container"><span id="44993"></span><div id="comment-44993" class="comment"><div id="post-44993-score" class="comment-score"></div><div class="comment-text"><p>I've grabbed a port capture of when it's working.</p><p>it seems window size is identical when it's working properly.</p><p><a href="http://www.megafileupload.com/97vX/portcapturefoxtelworking.pcapng">http://www.megafileupload.com/97vX/portcapturefoxtelworking.pcapng</a></p><p>this is using an old netgear WNDR3700</p><p>the router i've replaced it with is a mikrotik RB951G-2HnD</p><p>Can you see anything in these capture results that might explain why it fails vs when its working?</p></div><div id="comment-44993-info" class="comment-info"><span class="comment-age">(12 Aug '15, 01:51)</span> toddfraser88</div></div><span id="45067"></span><div id="comment-45067" class="comment"><div id="post-45067-score" class="comment-score"></div><div class="comment-text"><p>I still need help with this.</p></div><div id="comment-45067-info" class="comment-info"><span class="comment-age">(13 Aug '15, 11:46)</span> toddfraser88</div></div><span id="45082"></span><div id="comment-45082" class="comment"><div id="post-45082-score" class="comment-score"></div><div class="comment-text"><p>So it seems that in the failling case the server stops sending 6 seconds before the FIN from the client comes. But the reason could not be seen...</p></div><div id="comment-45082-info" class="comment-info"><span class="comment-age">(13 Aug '15, 16:39)</span> Christian_R</div></div><span id="45090"></span><div id="comment-45090" class="comment"><div id="post-45090-score" class="comment-score"></div><div class="comment-text"><p>do you think a port capture from the WAN port would help?</p></div><div id="comment-45090-info" class="comment-info"><span class="comment-age">(13 Aug '15, 23:48)</span> toddfraser88</div></div><span id="45094"></span><div id="comment-45094" class="comment"><div id="post-45094-score" class="comment-score"></div><div class="comment-text"><p>No, not really.</p></div><div id="comment-45094-info" class="comment-info"><span class="comment-age">(14 Aug '15, 00:49)</span> Christian_R</div></div><span id="45102"></span><div id="comment-45102" class="comment not_top_scorer"><div id="post-45102-score" class="comment-score"></div><div class="comment-text"><p>@toddfraser88</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-45102-info" class="comment-info"><span class="comment-age">(14 Aug '15, 01:57)</span> grahamb ♦</div></div><span id="45129"></span><div id="comment-45129" class="comment not_top_scorer"><div id="post-45129-score" class="comment-score"></div><div class="comment-text"><p>So the question you need an answer is: Why does the speed test fail to 192.168.55.253 when it succeeds to 192.168.1.145 ? Those are different TV boxes in different networks?</p></div><div id="comment-45129-info" class="comment-info"><span class="comment-age">(15 Aug '15, 00:17)</span> mrEEde</div></div><span id="45137"></span><div id="comment-45137" class="comment not_top_scorer"><div id="post-45137-score" class="comment-score"></div><div class="comment-text"><p>same modem, same tv box, same Ethernet cable, except in the working i put the mikrotik in switch mode and put the WNDR3700 in between it and the modem.</p><p>so the WNDR3700 does something differently that makes it work properly, I've no idea what though.</p><p>I've even tried reseting the mikrotik with no default configuration and setting it up entirely from scratch, even with the most basic config in place, the problem persists.</p></div><div id="comment-45137-info" class="comment-info"><span class="comment-age">(15 Aug '15, 03:56)</span> toddfraser88</div></div></div><div id="comment-tools-44986" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-44986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

