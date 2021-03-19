+++
type = "question"
title = "MAC address and IP on a LAN"
description = '''I&#x27;ve made a capture of a FTP session between my computer and a server. The result of a single packet is as follow: Ethernet II, Src: 00:80:5f:31:d9:7c, Dst: 00:01:f4:96:50:7f Internet Protocol, Src Addr: 164.0.0.130 (164.0.0.130), Dst Addr: 10.0.0.20 (10.0.0.20) Transmission Control Protocol, Src Po...'''
date = "2012-05-08T18:11:00Z"
lastmod = "2012-05-09T06:52:00Z"
weight = 10796
keywords = [ "ip", "mac-address", "router" ]
aliases = [ "/questions/10796" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [MAC address and IP on a LAN](/questions/10796/mac-address-and-ip-on-a-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10796-score" class="post-score" title="current number of votes">0</div><span id="post-10796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've made a capture of a FTP session between my computer and a server. The result of a single packet is as follow:</p><pre><code>Ethernet II, Src: 00:80:5f:31:d9:7c, Dst: 00:01:f4:96:50:7f
Internet Protocol, Src Addr: 164.0.0.130 (164.0.0.130), Dst Addr: 10.0.0.20 (10.0.0.20)
Transmission Control Protocol, Src Port: ftp (21), Dst Port: 32769 (32769), Seq: 81, Ack: 35, Len: 19</code></pre><p>My questions:</p><ul><li>1) Is There a router/switcher between these 2 hosts because they are on different networks?</li><li>2) Are both MAC addresses real (the host MAC address)? Or one of them is from the router/switcher?</li><li>3) The same as above for IP address. Are they real? Both?</li></ul><p>P.S: I don't have information about the LAN, routers, switchers, etc. The capture file is all the information I have.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '12, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/2130b0bae8abeb9030d02981af4bc782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="islon&#39;s gravatar image" /><p><span>islon</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="islon has no accepted answers">0%</span></p></div></div><div id="comments-container-10796" class="comments-container"></div><div id="comment-tools-10796" class="comment-tools"></div><div class="clear"></div><div id="comment-10796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10799"></span>

<div id="answer-container-10799" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10799-score" class="post-score" title="current number of votes">2</div><span id="post-10799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="islon has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1.) Yes, there is a router between the machines. Signs: different subnet and the MAC address of an Enterasys Networks component (00:01:F4 - most certainly the router). Another option would be Proxy ARP (please google that), but even then, there is 'something' between src and dst.</p><p>2.) <strong>00:80:5f</strong> is <strong>HP</strong> which is probably your Client PC: 10.0.0.20. <strong>00:01:F4</strong> is <strong>Enterasys Networks</strong>, which is the next hop router for 10.0.0.20 (see routing table on the client). You won't see the switch mac address, until you talk to one of it's ip addresses (e.g. mgmt interface).</p><p>3.) All IP addresses are just virtual data, made of bits and bytes, so both are "unreal" ;-) Honestly: what do you mean by "real" IP address? If you want to detect if there is IP spoofing in place, then that's hard to detect (often impossible) in a capture file and certainly impossible with just a few bytes one ip packet.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 May '12, 23:45</strong> </span></p></div></div><div id="comments-container-10799" class="comments-container"><span id="10821"></span><div id="comment-10821" class="comment"><div id="post-10821-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer Kurt. About "real" IP addresses, what I was trying to say is: as there's a router between both computers one of the IP addresses is from the router, so maybe the 164... is the server's IP and 10... is my routers IP or the other way arround?</p></div><div id="comment-10821-info" class="comment-info"><span class="comment-age">(09 May '12, 03:54)</span> <span class="comment-user userinfo">islon</span></div></div><span id="10822"></span><div id="comment-10822" class="comment"><div id="post-10822-score" class="comment-score">1</div><div class="comment-text"><p>you won't see the router ip address as routing is just layer-2 forwarding of the original ip packet to the mac of the next hop, hence the enterasys mac. 164.0.0.130 is your ftp server, whereas 10.0.0.20 is your client.</p></div><div id="comment-10822-info" class="comment-info"><span class="comment-age">(09 May '12, 04:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10830"></span><div id="comment-10830" class="comment"><div id="post-10830-score" class="comment-score"></div><div class="comment-text"><p>That's exactly what I wanted to know =)</p></div><div id="comment-10830-info" class="comment-info"><span class="comment-age">(09 May '12, 05:57)</span> <span class="comment-user userinfo">islon</span></div></div><span id="10836"></span><div id="comment-10836" class="comment"><div id="post-10836-score" class="comment-score"></div><div class="comment-text"><p>good :-) ...</p></div><div id="comment-10836-info" class="comment-info"><span class="comment-age">(09 May '12, 06:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-10799" class="comment-tools"></div><div class="clear"></div><div id="comment-10799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

