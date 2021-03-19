+++
type = "question"
title = "ARP Broadcast"
description = '''My main router (66.xxx.xx.x) is sending an arp broadcast to every ip address on my network (66.xxx.xx.1-256) and it repeats this process three times in a second. When the router sends the arp broadcast and repeats three times in a second it throws an alarm stating a possible broadcast storm in a pie...'''
date = "2016-01-08T12:27:00Z"
lastmod = "2016-01-08T15:06:00Z"
weight = 48989
keywords = [ "arp", "broadcast", "storm" ]
aliases = [ "/questions/48989" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ARP Broadcast](/questions/48989/arp-broadcast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48989-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My main router (66.xxx.xx.x) is sending an arp broadcast to every ip address on my network (66.xxx.xx.1-256) and it repeats this process three times in a second. When the router sends the arp broadcast and repeats three times in a second it throws an alarm stating a possible broadcast storm in a piece of equipment attached to the network. Is it normal for a router to send an arp broadcast to every ip three times in a row in one second? And could this be some type of broadcast storm? Any suggestions on how to stop this from happening would be great. Thanks</p></div><div id="question-tags" class="tags-container tags">arp broadcast storm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '16, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/f5111f20cc20d2ccea9ba4f853a6db1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="austinh&#39;s gravatar image" /><p>austinh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="austinh has no accepted answers">0%</span></p></div></div><div id="comments-container-48989" class="comments-container"><span id="49002"></span><div id="comment-49002" class="comment"><div id="post-49002-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is it normal for a router to send an arp broadcast to every ip three times in a row in one second?</p></blockquote><p>I do know one particular type of routing equipment which is cyclically sending arp requests to all individual IPs in the subnet on purpose, but not as frequently as 3 times per second per IP. The declared purpose in that case is to avoid waiting for an arp response when a "real" packet for that IP arrives and needs to be sent.</p><p>But what I do not like about your situation is that the same equipment which sends the arp requests is claiming that there are too many of them.</p><p>Could you please clarify whether</p><ul><li><p>the router behaves like this all the time or only from time to time,</p></li><li><p>the target subnet is 66.xxx.xx.0/24 (i.e. 253 addresses plus network address (.0) plus broadcast address (.255) plus router(.1)</p></li></ul><p>?</p><p>If there is an external cause of that, Wireshark can help you identify it, provided that you can capture at all interfaces of the router.</p><p>But if the arp requests are really sent so frequently also to IP addresses which respond to them, I'm afraid that the root cause is internal to the router and you'll have to claim the issue with its manufacturer.</p></div><div id="comment-49002-info" class="comment-info"><span class="comment-age">(08 Jan '16, 16:40)</span> sindy</div></div><span id="49016"></span><div id="comment-49016" class="comment"><div id="post-49016-score" class="comment-score"></div><div class="comment-text"><p>The router behaves like this from time to time. Some days the event occurs multiple times and some days it does not occur at all. The router has an ip of 66.xxx.xx.1 and the rest of the ip's are from 66.xxx.xx.2-254 plus the broadcast address of 66.xxx.xx.255.</p></div><div id="comment-49016-info" class="comment-info"><span class="comment-age">(09 Jan '16, 08:34)</span> austinh</div></div><span id="49017"></span><div id="comment-49017" class="comment"><div id="post-49017-score" class="comment-score"></div><div class="comment-text"><p>OK, and what about the arp responses from the IPs in the subnet? I mean, how many of the 253 IPs are actually in use, do they respond to the arp requests, and do the arp requests come 3 times per second also to the IPs which respond them?</p></div><div id="comment-49017-info" class="comment-info"><span class="comment-age">(09 Jan '16, 08:45)</span> sindy</div></div></div><div id="comment-tools-48989" class="comment-tools"></div><div class="clear"></div><div id="comment-48989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48993"></span>

<div id="answer-container-48993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48993-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it normal for a router to send an arp broadcast to every ip three times in a row in one second?</p></blockquote><p>it depends. If somebody sends packets to the router with a destination of 66.x.x.0-255 then router has to send ARP requests to be able to forward the frames at L2. If that's the case, then somebody might scan your network (from behind the router), which will cause the ARP "storm".</p><p>Another reason could be a buggy router firmware, or somebody on the network is sending the ARPs with the MAC address of the router (for whatever reason). Hard to tell, without more insight into your network infrastructure.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '16, 11:52</p></div></div><div id="comments-container-48993" class="comments-container"><span id="49001"></span><div id="comment-49001" class="comment"><div id="post-49001-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner, I dare to disagree with</p><blockquote><p>If somebody sends packets to the router with a destination of 66.x.x.0-255 then router has to send ARP requests to be able to forward the frames at L2</p></blockquote><p>as the root cause of 3 arp requests per second.</p><p>Yes, the first packet for a given dst IP after a long period of time (the lifetime of an arp cache record) causes an arp request to be sent, but if it gets responded, the router doesn't need to send further arp requests to the same IP until the record in the cache expires again, which should normally not happen in 1/3 second, as the arp cache lifetime is usually units or tens of seconds.</p><p>So what you wrote is true if the packets from outside are coming with a dst IP which is not assigned in the target subnet, but not if such IP is assigned and responds to arp requests. I think we need @austinh's clarification as the .1-.256 range may be a typo or may mean that the subnet is really larger than 256 addresses and only the lowest 256 ones are affected.</p></div><div id="comment-49001-info" class="comment-info"><span class="comment-age">(08 Jan '16, 16:25)</span> sindy</div></div><span id="49009"></span><div id="comment-49009" class="comment"><div id="post-49009-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So what you wrote is true if the packets from outside are coming with a dst IP which is not assigned in the target subnet, but not if such IP is assigned and responds to arp requests.</p></blockquote><p>I know. As the OP did not tell anything about local clients answering the ARP requests or not, both my and your assumption is only speculation. So let's wait until the OP adds more information ;-)</p></div><div id="comment-49009-info" class="comment-info"><span class="comment-age">(09 Jan '16, 05:13)</span> Kurt Knochner ♦</div></div><span id="49018"></span><div id="comment-49018" class="comment"><div id="post-49018-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The router behaves like this from time to time. Some days the event occurs multiple times and some days it does not occur at all.</p></blockquote><p>So, either it's the router itself who is sending the ARP requests (bug, or an external trigger as I mentioned), or in internal system is simply using the MAC address of the router to send the requests (for whatever reason). A managed switch will tell you on which port it sees the MAC address of the router. If it's only on the port where the router is physically connected, it's the router who is sending the ARP requests. If the switch reports that MAC address on another port as well, it's another system on your network that is "faking" the router MAC.</p></div><div id="comment-49018-info" class="comment-info"><span class="comment-age">(09 Jan '16, 11:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-48993" class="comment-tools"></div><div class="clear"></div><div id="comment-48993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

