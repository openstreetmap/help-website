+++
type = "question"
title = "Cannot Access Network Drives through VPN."
description = '''I&#x27;m a little lost, as I&#x27;m not sure what exactly is the issue. Wireshark Snippet &amp;lt;-- Here is a snippet of some of the data I got from my wireshark capture. This capture was from the windows server cluster to a laptop outside our network connected through our VPN. No matter the user (admin privileg...'''
date = "2014-09-12T11:30:00Z"
lastmod = "2014-09-16T11:50:00Z"
weight = 36281
keywords = [ "vpn", "network", "rst+ack", "wireshark" ]
aliases = [ "/questions/36281" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot Access Network Drives through VPN.](/questions/36281/cannot-access-network-drives-through-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36281-score" class="post-score" title="current number of votes">0</div><span id="post-36281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a little lost, as I'm not sure what exactly is the issue. <a href="http://imgur.com/O0u3lE7">Wireshark Snippet</a> &lt;-- Here is a snippet of some of the data I got from my wireshark capture. This capture was from the windows server cluster to a laptop outside our network connected through our VPN. No matter the user (admin privileged or not), or the location, they cannot access these drives remotely. Any ideas? The firewall isn't detecting anything being blocked when I search through the logs.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-rst+ack" rel="tag" title="see questions tagged &#39;rst+ack&#39;">rst+ack</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '14, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/a786575b5e2fbf3a4a8a4441fe7001a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheCarefulOne&#39;s gravatar image" /><p><span>TheCarefulOne</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheCarefulOne has no accepted answers">0%</span></p></div></div><div id="comments-container-36281" class="comments-container"><span id="36306"></span><div id="comment-36306" class="comment"><div id="post-36306-score" class="comment-score"></div><div class="comment-text"><p>After the three way handshake the next packet is usually an SMB Negotiate Protocol message from the pc to the server. Probably the best thing to do is collect matching traces from the pc and the server. Wireshark may not be able to capture traffic along the vpn. If this is the case you can use Microsoft Network Monitor.</p><p>Best regards...Paul</p></div><div id="comment-36306-info" class="comment-info"><span class="comment-age">(14 Sep '14, 01:27)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-36281" class="comment-tools"></div><div class="clear"></div><div id="comment-36281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36365"></span>

<div id="answer-container-36365" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36365-score" class="post-score" title="current number of votes">0</div><span id="post-36365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Paul indicated, the next thing to occur would be some data packets from the client.<br />
As they don't show up at the server they were either not sent or dropped in the network.<br />
Assuming that the client sent the SMB message (which is yet to prove) I think the packet was dropped in the network.<br />
If this only happens over VPN it is probably a MTU-size, Fragmentation, PMTUD problem.</p><p>The inbound SYN shows that the MSS has been reduced to 1360 bytes indicating that the MTU size within the VPN is 1400 bytes and the VPN router adjusted the MSS in the passing SYN packet.<br />
The outbound offering is still at 1460 as the trace was taken at the server.<br />
If the MSS does not get <a href="http://www.cisco.com/c/en/us/support/docs/ip/generic-routing-encapsulation-gre/25885-pmtud-ipfrag.html">tcp adjust-mss</a>'ed on the reverse path you might end up in hung connections for the first full MSS packet that hits the VPN entry point.</p><p>You might want to reduce your server's interface MTU size to 1400 to see if this gets you around this problem.<br />
Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '14, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-36365" class="comments-container"><span id="36374"></span><div id="comment-36374" class="comment"><div id="post-36374-score" class="comment-score"></div><div class="comment-text"><p>Thanks, for the suggestion. MTU size was 1500, 1400 worked when I tested with sending packets of that size. The SMB Packets are indeed getting dropped as well.<br />
</p><p>When I do dcdiags and repadmin /binds. I get RPC errors, so I think it could be related to that as well. However, all the services seem to be running correctly.</p></div><div id="comment-36374-info" class="comment-info"><span class="comment-age">(16 Sep '14, 11:50)</span> <span class="comment-user userinfo">TheCarefulOne</span></div></div></div><div id="comment-tools-36365" class="comment-tools"></div><div class="clear"></div><div id="comment-36365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

