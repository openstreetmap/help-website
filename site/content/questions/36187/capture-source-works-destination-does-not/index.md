+++
type = "question"
title = "capture source works, destination does not"
description = '''just dl&#x27;ed and installed wireshark onto a Toshiba Portege R705 Laptop running W8.1 Pro. When i put in a filter of ip.address == 192.168.1.101  I only see traffic where 192.168.1.101 is the source, never when it is the destination. And at that, the only traffic that seems to be captured are Broadcast...'''
date = "2014-09-10T17:59:00Z"
lastmod = "2014-09-11T06:57:00Z"
weight = 36187
keywords = [ "ip4", "tcp" ]
aliases = [ "/questions/36187" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture source works, destination does not](/questions/36187/capture-source-works-destination-does-not)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36187-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>just dl'ed and installed wireshark onto a Toshiba Portege R705 Laptop running W8.1 Pro.</p><p>When i put in a filter of ip.address == 192.168.1.101 I only see traffic where 192.168.1.101 is the source, never when it is the destination. And at that, the only traffic that seems to be captured are Broadcast type packets. I don't see any TCP/UDP.</p><p>Both devices are attached to a DLink DGS-1008G switch.</p></div><div id="question-tags" class="tags-container tags">ip4 tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 17:59</strong></p><img src="https://secure.gravatar.com/avatar/ce623175ed886355a40be00c7a7e7ed1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PacNW-cp&#39;s gravatar image" /><p>PacNW-cp<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PacNW-cp has no accepted answers">0%</span></p></div></div><div id="comments-container-36187" class="comments-container"></div><div id="comment-tools-36187" class="comment-tools"></div><div class="clear"></div><div id="comment-36187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36203"></span>

<div id="answer-container-36203" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36203-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unless you configure your switch to send copies of the traffic of 192.168.1.101 to your laptop (also known as SPAN port/mirror port), you'll only see Broadcasts.</p><p>Take a look here: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '14, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36203" class="comments-container"><span id="36208"></span><div id="comment-36208" class="comment"><div id="post-36208-score" class="comment-score"></div><div class="comment-text"><p>hmmm, well unfortunately lots of dead links at the wiki page <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>the DGS-1008G is a "dumb" switch, it has no interfacing. Though looking at the description it does do QoS , tagging and MAC learning. So maybe better to call it "smart but unmanageable"? Even so, the 2 machines are on the same switch, traffic still can't be seen??</p><p>Anyway, from what I've read it seems ARP hacking (with Cain and Able) is required. I am not eager to hack the network , so not sure what I will do now.</p><p>Be nice if there was a bundling option somewhere ...</p></div><div id="comment-36208-info" class="comment-info"><span class="comment-age">(11 Sep '14, 11:41)</span> PacNW-cp</div></div><span id="36255"></span><div id="comment-36255" class="comment"><div id="post-36255-score" class="comment-score"></div><div class="comment-text"><p>The "partitioning" of traffic is pretty much the entire reason for a switch, traffic is only directed to the ports that "need" to see it. Unless the switch provides a means to span or mirror port traffic, you won't be able to capture non-broadcast traffic on ports other than the port you're connected to.</p></div><div id="comment-36255-info" class="comment-info"><span class="comment-age">(12 Sep '14, 00:56)</span> grahamb ♦</div></div></div><div id="comment-tools-36203" class="comment-tools"></div><div class="clear"></div><div id="comment-36203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

