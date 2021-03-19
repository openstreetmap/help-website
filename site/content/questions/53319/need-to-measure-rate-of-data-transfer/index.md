+++
type = "question"
title = "Need to measure rate of data transfer"
description = '''Hello and thanks for your time. I am operating a system drawing data from a server to generate simulated terrain for a flight simulator. I have been getting odd results though lately, and I suspect that the data being sent from the server is not being sent at a constant rate, or is being sent asynch...'''
date = "2016-06-08T08:38:00Z"
lastmod = "2016-06-10T23:07:00Z"
weight = 53319
keywords = [ "transfer", "datarate" ]
aliases = [ "/questions/53319" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need to measure rate of data transfer](/questions/53319/need-to-measure-rate-of-data-transfer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53319-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello and thanks for your time.</p><p>I am operating a system drawing data from a server to generate simulated terrain for a flight simulator. I have been getting odd results though lately, and I suspect that the data being sent from the server is not being sent at a constant rate, or is being sent asynchronously. The server's manufacturer is unable to assist, so I am looking to use Wireshark to measure the rate of data transfer.</p><p>Unfortunately I've never USED Wireshark before, so I am a little in the woods. Any suggestions would be much appreciated!</p><p>Brian</p></div><div id="question-tags" class="tags-container tags">transfer datarate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/a4058441909c1592875459d147bc47f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BrianKarasek&#39;s gravatar image" /><p>BrianKarasek<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BrianKarasek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 15:43</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-53319" class="comments-container"><span id="53352"></span><div id="comment-53352" class="comment"><div id="post-53352-score" class="comment-score"></div><div class="comment-text"><p>How far did you get in using Wireshark (i.e. have you found out how to capture traffic and just don't know what to look for in the result or you even don't know what to do next after starting Wireshark)?, and do you have any theoretical knowledge of TCP/IP?</p><p>Why would you expect the terrain data to be delivered at constant rate? I would rather suspect the issue to be that they arrive slower than required for smooth rendering, but the data arrival speed sufficient for smooth rendering depends on flight speed - the faster you fly the faster you need to get the tiles of the terrain ahead of you.</p><p>I mention that because it may be difficult to spot anything at all from the capture if the only issue is that the server is lazy. If the slow delivery of data is caused by packet loss causing retransmissions rather than slow sending, then yes, Wireshark would visualise that to you. But unless you control the network path between the server and your flight simulator machine, there is little you can do to fix the network problems causing the loss.</p></div><div id="comment-53352-info" class="comment-info"><span class="comment-age">(10 Jun '16, 15:20)</span> sindy</div></div></div><div id="comment-tools-53319" class="comment-tools"></div><div class="clear"></div><div id="comment-53319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53355"></span>

<div id="answer-container-53355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53355-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>If it is only about data rate of transfer, what would be more simply is just only use a tool which can tell you , even in real-time, the bandwidth used to/from an IP adress. A tool like "iftop" would be more than enough. You will get the total bandwidth and real-time bandwidth..</p><p>Otherwise a filter in wireshare like : ip.addr == REMOTE_IP/24 would be usefull, then just export the packet, and check the length field, and you will get what you want...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '16, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/daee239c2db6b37205dd35ab72ec7f29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spoown&#39;s gravatar image" /><p>spoown<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spoown has no accepted answers">0%</span></p></div></div><div id="comments-container-53355" class="comments-container"></div><div id="comment-tools-53355" class="comment-tools"></div><div class="clear"></div><div id="comment-53355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

