+++
type = "question"
title = "HTTP 408 Timeout from particular IP"
description = '''I&#x27;ve uploaded my first Wireshark session to CloudShark, I don&#x27;t have sslkeylog from client, I guess I can walk them through configuring if it comes to that (I assume that will work with an imported snoop log, just as it does &#x27;real time&#x27; in Wireshark?). https://www.cloudshark.org/captures/00f74e9e979...'''
date = "2015-08-03T09:10:00Z"
lastmod = "2015-08-03T22:53:00Z"
weight = 44791
keywords = [ "not", "segment", "captured", "tcp", "previous" ]
aliases = [ "/questions/44791" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP 408 Timeout from particular IP](/questions/44791/http-408-timeout-from-particular-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44791-score" class="post-score" title="current number of votes">0</div><span id="post-44791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've uploaded my first Wireshark session to CloudShark, I don't have sslkeylog from client, I guess I can walk them through configuring if it comes to that (I assume that will work with an imported snoop log, just as it does 'real time' in Wireshark?).</p><p><a href="https://www.cloudshark.org/captures/00f74e9e979d">https://www.cloudshark.org/captures/00f74e9e979d</a></p><p>64.114.102.2 is client 10.1.4.61 is host/receiver, where snoop was running</p><p>The client is ultimately getting an HTTP 408 from Apache, POST'ing a SAML request. Everything works dandy, except from a block of this particular clients IP's.</p><p>I've read that 'TCP Previous segment not captured' can be result of packet loss, or snoop not keeping up. But does the TCP Dup ACK tell a different story?</p><p>Is there anything here which would suggest there's an issue with the client/and/or a proxy between us?</p><p>I'm not really a 'network guy', so still trying to understand some of this, but was hoping if there were anything definitive here, someone might share it.</p><p>Thanks for any insights, Jeff</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span> <span class="post-tag tag-link-captured" rel="tag" title="see questions tagged &#39;captured&#39;">captured</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-previous" rel="tag" title="see questions tagged &#39;previous&#39;">previous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '15, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/23a87a325996d0f2a159c183a95eb759?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JHuston&#39;s gravatar image" /><p><span>JHuston</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JHuston has no accepted answers">0%</span></p></div></div><div id="comments-container-44791" class="comments-container"></div><div id="comment-tools-44791" class="comment-tools"></div><div class="clear"></div><div id="comment-44791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44795"></span>

<div id="answer-container-44795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44795-score" class="post-score" title="current number of votes">1</div><span id="post-44795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that none of the client's full-MSS (1368 bytes) sized segments make it to your server even though the server's full-MSS segments reach the client.<br />
Unless you have control over the VPN routers and their <a href="https://learningnetwork.cisco.com/thread/40703">ip adjust-mss</a> configuration towards these IP addresses the circumvention will likely be to add a static route in Solaris and reduce the MTU size towards the IP subnet to something less than 1420 bytes (1400 may already do)</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-44795" class="comments-container"><span id="44801"></span><div id="comment-44801" class="comment"><div id="post-44801-score" class="comment-score"></div><div class="comment-text"><p>Okay Matthias, this makes some sense to me. Although am I mistaken, or shouldn't my server be limiting it's MSS to that in the initial client packet? (1380) I'm reading something to that effect elsewhere, or doesn't it work that way?</p><p>Thanks for the quick response, good information.</p><p>Jeff</p></div><div id="comment-44801-info" class="comment-info"><span class="comment-age">(03 Aug '15, 13:42)</span> <span class="comment-user userinfo">JHuston</span></div></div><span id="44803"></span><div id="comment-44803" class="comment"><div id="post-44803-score" class="comment-score"></div><div class="comment-text"><p>The server will offer its MSS based on the MTU size of the interface, it is up to intelligent network devices to reduce the MSS if the net MTU size is shrinking... . The client actually sees 'your' MSS of 1380 bytes when the SYN_ACK reaches the client. As TCP timestamps are also negotiated the net MSS is further reduced by 12 bytes so the maximum remaining tcp.len IS 1368 bytes.</p><p>However somehow this is still too high to pass the VPN infrastructure along the path without requiring IP fragmentation.</p></div><div id="comment-44803-info" class="comment-info"><span class="comment-age">(03 Aug '15, 13:48)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="44805"></span><div id="comment-44805" class="comment"><div id="post-44805-score" class="comment-score"></div><div class="comment-text"><p>The VPN infrastruture should ideally be reducing the client MSS in the initial SYN as well then, correct? and if so, is this a common issue? Does ip adjust-mss actually set the max MSS? or does it tell the device to make the adjustment as well?</p><p>Thanks so much,</p><p>Jeff</p></div><div id="comment-44805-info" class="comment-info"><span class="comment-age">(03 Aug '15, 13:57)</span> <span class="comment-user userinfo">JHuston</span></div></div><span id="44809"></span><div id="comment-44809" class="comment"><div id="post-44809-score" class="comment-score"></div><div class="comment-text"><p>"The VPN infrastruture should ideally be reducing the client MSS in the initial SYN as well then, correct?" Yes, and this is what happened: The SYN packet's MSS option is arriving as 1380, certainly not what the linux client initially sent.<br />
So the we can assume that the VPN infrastructure reduced it to adapt to the believed net MTU size of 1420 bytes in the tunnel.<br />
The largest segment the server sent contained 1368 and was acknowledged so we can deduct it made it to the client successfully.</p><p>However, in the reverse direction all 1368 bytes segments are reported missing by the server.</p><p>"is this a common issue?"<br />
This is not really common as usually both directions should have the same MTU size - if forward and backward route follow the same path.</p><p>"Does ip adjust-mss actually set the max MSS? or does it tell the device to make the adjustment as well?"</p><p>The SYN and SYN_ACK packets are intercepted and the MSS option gets modified in flight. As a result receiver TCP will not be sending segments larger than the offered MSS ( in fact 12 bytes less of what was offered if tcp timestamps are negotiated).</p></div><div id="comment-44809-info" class="comment-info"><span class="comment-age">(03 Aug '15, 22:53)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-44795" class="comment-tools"></div><div class="clear"></div><div id="comment-44795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

