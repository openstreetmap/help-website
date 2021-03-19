+++
type = "question"
title = "How to make streaming video suffering serious packet loss"
description = '''hi, everyone Plz, help me solve this tricky problem, making me suffering for almost one week. How to make streaming video suffering packet loss? Switch: Pica8 3290 Computer: core i7 2600, 8GB OS(sever&amp;amp;host): Ubuntu 14.04 Link: 100Mps Streaming video : VLC with RTP Streming(1080P、4K) I&#x27;ve tried &quot;...'''
date = "2015-04-07T10:10:00Z"
lastmod = "2015-04-07T11:06:00Z"
weight = 41257
keywords = [ "test", "video", "rtp", "packet", "packetloss" ]
aliases = [ "/questions/41257" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to make streaming video suffering serious packet loss](/questions/41257/how-to-make-streaming-video-suffering-serious-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41257-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>hi, everyone Plz, help me solve this tricky problem, making me suffering for almost one week.</p><p>How to make streaming video suffering packet loss?</p><p>Switch: Pica8 3290</p><p>Computer: core i7 2600, 8GB</p><p>OS(sever&amp;host): Ubuntu 14.04</p><p>Link: 100Mps</p><p>Streaming video : VLC with RTP Streming(1080P、4K)</p><p>I've tried "iperf", "iperf3" and "Packeth" to generate UDP packets. However, these 3 sofwares seem to measure the residual capacity of the link first and then send the amount of the packets fit the capacity.</p><p>E.g.: (No Video streaming) iperf send almost 100Mps (With video streaming) iperf only send almost 70Mbps Thus, these packet generator won't help me to make the streaming video suffering serious loss. (What I want is make huge traffic and make the streaming suffering terrible loss and delay)</p><p>So, how can I create "congestion" and make the video streaming packets loss ?</p><p>Truly appreciate your help!!</p></div><div id="question-tags" class="tags-container tags">test video rtp packet packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '15, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/549413684fec8a106935e4b97a9d3d18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shine%20Hsu&#39;s gravatar image" /><p>Shine Hsu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shine Hsu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Apr '15, 11:24</p></div></div><div id="comments-container-41257" class="comments-container"></div><div id="comment-tools-41257" class="comment-tools"></div><div class="clear"></div><div id="comment-41257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41260"></span>

<div id="answer-container-41260" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41260-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your source or destination is on linux you can try: "tc" or "tc-ng" . You can create delay or packet loss. It's just little complicated to understand. But just google it and you will find answer....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '15, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/5c59321a66976ba615e1a50b46a4d209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramprasad&#39;s gravatar image" /><p>Ramprasad<br />
<span class="score" title="20 reputation points">20</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramprasad has no accepted answers">0%</span></p></div></div><div id="comments-container-41260" class="comments-container"><span id="41262"></span><div id="comment-41262" class="comment"><div id="post-41262-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. So, what u mean is that Linux limit packet generator(low priority) and the media streaming has the higher priority ? (but, i didn't do any modifications before Linux won't cheat all the traffic the same?)</p></div><div id="comment-41262-info" class="comment-info"><span class="comment-age">(07 Apr '15, 11:31)</span> Shine Hsu</div></div><span id="41263"></span><div id="comment-41263" class="comment"><div id="post-41263-score" class="comment-score"></div><div class="comment-text"><p>btw, i used individual computers, one as host(receiver), one as packet generator to test if the large traffic generated by iperf make the streaming packet loss.</p><p>however, the outcomes didn't look so....</p></div><div id="comment-41263-info" class="comment-info"><span class="comment-age">(07 Apr '15, 11:41)</span> Shine Hsu</div></div></div><div id="comment-tools-41260" class="comment-tools"></div><div class="clear"></div><div id="comment-41260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

