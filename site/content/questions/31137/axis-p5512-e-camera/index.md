+++
type = "question"
title = "Axis P5512-e Camera"
description = '''Hello there! I&#x27;m trying to track traffic activity from an Axis p5512-E POE camera after a hard reset to factory default.  Normally it should broadcast dhcp request and get an ip, otherwise if no dhcp is found it should revert to default ip configuration.  Unfortunately this camera sends arp request ...'''
date = "2014-03-24T21:18:00Z"
lastmod = "2014-03-26T08:57:00Z"
weight = 31137
keywords = [ "issue", "axis" ]
aliases = [ "/questions/31137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Axis P5512-e Camera](/questions/31137/axis-p5512-e-camera)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31137-score" class="post-score" title="current number of votes">0</div><span id="post-31137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there!</p><p>I'm trying to track traffic activity from an Axis p5512-E POE camera after a hard reset to factory default. Normally it should broadcast dhcp request and get an ip, otherwise if no dhcp is found it should revert to default ip configuration. Unfortunately this camera sends arp request but it doesn't get any ip address from dhcp (i've tried two different ones) All i get is this message:</p><p>4196 520.124027000 169.254.84.77 224.0.0.251 MDNS 318 Standard query 0x0000 ANY axis-00408cdca1ff.local, "QU" question ANY axis-00408cdca1ff.local, "QU" question ANY AXIS P5512-E - 00408CDCA1FF._http._tcp.local, "QU" question ANY AXIS P5512-E - 00408CDCA1FF._axis-video._tcp.local, "QU" question ANY AXIS P5512-E - 00408CDCA1FF H.264._rtsp._tcp.local, "QU" question</p><p>Hints are appreciated;)</p><p>Cheers</p><p>Alessio</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span> <span class="post-tag tag-link-axis" rel="tag" title="see questions tagged &#39;axis&#39;">axis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '14, 21:18</strong></p><img src="https://secure.gravatar.com/avatar/23552b532d1ee0a38f190a3e5f2602e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alessio&#39;s gravatar image" /><p><span>Alessio</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alessio has no accepted answers">0%</span></p></div></div><div id="comments-container-31137" class="comments-container"><span id="31138"></span><div id="comment-31138" class="comment"><div id="post-31138-score" class="comment-score"></div><div class="comment-text"><p>The packet above is a multicast DNS. If DHCP is configured the camera will send a DHCP Discovery. Use the filter bootp to check for dhcp packets.</p></div><div id="comment-31138-info" class="comment-info"><span class="comment-age">(25 Mar '14, 00:27)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-31137" class="comment-tools"></div><div class="clear"></div><div id="comment-31137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31139"></span>

<div id="answer-container-31139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31139-score" class="post-score" title="current number of votes">0</div><span id="post-31139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently your camera is sending out MDNS requests to detect some services on the network. The IP address it uses is 169.254.84.77, which is an address from a special range (see: <a href="http://packetlife.net/blog/2008/sep/24/169-254-0-0-addresses-explained/">http://packetlife.net/blog/2008/sep/24/169-254-0-0-addresses-explained/</a> ).</p><p>So, apparently your camera is not getting an IP address via DHCP, nor does it fall back to a default IP address in one of the usual ranges (192.168.x.x.).</p><p>You can try to access the camera with a browser on that IP address: <a href="http://169.254.84.77"></a><a href="http://169.254.84.77">http://169.254.84.77</a> . If that works, you can then set the IP address manually. Another option would be to capture the DHCP request (and response) to figure out why DHCP does not work. Maybe the camera is not sending any DHCP requests !?!</p><p>BTW: There is also a tool called <a href="http://www.axis.com/de/techsup/software/iputility/">AXIS IP Utility</a> to identify Axis cameras and their IP address on your network. However that is not necessary in your case, as you already know the address (169.254.84.77).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '14, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '14, 08:54</strong> </span></p></div></div><div id="comments-container-31139" class="comments-container"><span id="31160"></span><div id="comment-31160" class="comment"><div id="post-31160-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt,</p><p>Thank you for your insight! Unfortunately i've tried to browse the camera's configuration page using that IP with no success. I've also used the Axis IP Utility with no result: the camera doesn't even show up locally with it's mac address. Guess i'll have it boxed and sent back as faulty;(</p></div><div id="comment-31160-info" class="comment-info"><span class="comment-age">(25 Mar '14, 22:23)</span> <span class="comment-user userinfo">Alessio</span></div></div><span id="31167"></span><div id="comment-31167" class="comment"><div id="post-31167-score" class="comment-score"></div><div class="comment-text"><p>Not sure about the Axis utility, but for using your browser you should make sure the host machine has a network address configured on the same subnet as the camera is apparently using, e.g. 169.256.0.0/16 or 169.256.84.0/24 as otherwise the NIC in the host will be forwarding packets to the default gateway which is unlikely to know how to route to the camera.</p><p>As the link provided by Kurt above seems to be broken, here is another explaining private (or link-local) IP addresses: <a href="http://en.wikipedia.org/wiki/Private_network">http://en.wikipedia.org/wiki/Private_network</a></p></div><div id="comment-31167-info" class="comment-info"><span class="comment-age">(26 Mar '14, 03:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="31181"></span><div id="comment-31181" class="comment"><div id="post-31181-score" class="comment-score"></div><div class="comment-text"><blockquote><p>As the link provided by Kurt above seems to be broken</p></blockquote><p>that's just the 'dumb' markup language, that does not separate the closing ) after the URL. But maybe that's a Layer 8 problem ;-)</p><p>Anyway: I fixed it. The link works now, as I added a blank between the URL and the )</p></div><div id="comment-31181-info" class="comment-info"><span class="comment-age">(26 Mar '14, 08:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31183"></span><div id="comment-31183" class="comment"><div id="post-31183-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but for using your browser you should make sure the host machine has a network address</p></blockquote><p>Oh, well... I thought that's clear, but you are absolutely right!! Maybe the OP did not think about the necessary steps to access the camera :-))</p></div><div id="comment-31183-info" class="comment-info"><span class="comment-age">(26 Mar '14, 08:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31139" class="comment-tools"></div><div class="clear"></div><div id="comment-31139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

