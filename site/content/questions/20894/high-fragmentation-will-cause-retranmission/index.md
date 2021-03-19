+++
type = "question"
title = "high fragmentation will cause retranmission"
description = '''Hi,  when i try to stream a video i can see it lagging, when i try to capture using wire-shark. i saw a lot retransmission and duplicate ack?  so my question is , if i have a lot fragment or miss match MTU where by the switch are using Long Frame Size(Bytes) : 9216 while my firewall only using MTU 1...'''
date = "2013-05-02T02:38:00Z"
lastmod = "2013-05-02T02:48:00Z"
weight = 20894
keywords = [ "retransmissions" ]
aliases = [ "/questions/20894" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [high fragmentation will cause retranmission](/questions/20894/high-fragmentation-will-cause-retranmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20894-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, when i try to stream a video i can see it lagging, when i try to capture using wire-shark. i saw a lot retransmission and duplicate ack?</p><p>so my question is , if i have a lot fragment or miss match MTU where by the switch are using Long Frame Size(Bytes) : 9216 while my firewall only using MTU 1500, can this be the cause of the high retransmission? and causing the lagging?</p></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '13, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/ba7415b503be15241d880cab78574700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="splibytes&#39;s gravatar image" /><p>splibytes<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="splibytes has no accepted answers">0%</span></p></div></div><div id="comments-container-20894" class="comments-container"><span id="20905"></span><div id="comment-20905" class="comment"><div id="post-20905-score" class="comment-score"></div><div class="comment-text"><p>can you please post a sample capture file somewhere (google docs, dropbox, cloudshark)?</p></div><div id="comment-20905-info" class="comment-info"><span class="comment-age">(02 May '13, 05:10)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20894" class="comment-tools"></div><div class="clear"></div><div id="comment-20894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20895"></span>

<div id="answer-container-20895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20895-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Every system on the same physical LAN segment MUST use the same MTU size. However, it is allowed to have multiple segments (separated by a router or L3 switch or any other routing device like a loadbalancer or firewall) with different MTU sizes, however, this will result in fragmentation at the IP layer which you will want to avoid.</p><p>In short, unless there is a real need for jumbo frames in a particular part of your network (storage for instance), don't use a MTU other than 1500.</p><p>(I assumed you are on an ethernet network btw :-))</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20895" class="comments-container"><span id="20897"></span><div id="comment-20897" class="comment"><div id="post-20897-score" class="comment-score"></div><div class="comment-text"><p>Hi, i check in one of the switch spec and found this Maximum Frame Size 1553 bytes (10/100 Mbps) 9216 bytes (1/10 Gbps) was frame size same as mtu, what i can found is that my firewall are using mtu1500 and look like the switch are using different mtu (maximum frame size) strangely, i saw a lot retransmission when ever i on video streaming such as you tube.</p></div><div id="comment-20897-info" class="comment-info"><span class="comment-age">(02 May '13, 03:42)</span> splibytes</div></div><span id="20898"></span><div id="comment-20898" class="comment"><div id="post-20898-score" class="comment-score"></div><div class="comment-text"><p>If it is listed in the spec as maximum frame size, it is not necessarily configured to use that maximum.</p><p>I doubt the retransmissions are caused by a MTU size mismatch as I assume your client receiving the video stream is connected to the switch, which is connected to the firewall, which is connected to the Internet.</p><p>So the videostream in coming in from the firewall over the switch to your client. Then every frame sent by the firewall will be small enough to fit your network segment.</p><p>Have you looked at duplex mismatches? Those can be a big source of retransmissions...</p></div><div id="comment-20898-info" class="comment-info"><span class="comment-age">(02 May '13, 03:52)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-20895" class="comment-tools"></div><div class="clear"></div><div id="comment-20895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

