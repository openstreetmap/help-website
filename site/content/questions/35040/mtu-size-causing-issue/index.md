+++
type = "question"
title = "MTU size causing issue"
description = '''Hi guys, I have two capture files, one is when the PC has an MTU of 1300, and the other when I have an MTU of 1500.  There are 2 servers, when accessing via https/rdp it does not work when the MTU is 1500 on the local pc - the page just shows blank white.  But when 1300 MTU is set locally, the page ...'''
date = "2014-07-31T17:50:00Z"
lastmod = "2014-08-04T23:01:00Z"
weight = 35040
keywords = [ "mtu" ]
aliases = [ "/questions/35040" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MTU size causing issue](/questions/35040/mtu-size-causing-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35040-score" class="post-score" title="current number of votes">0</div><span id="post-35040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I have two capture files, one is when the PC has an MTU of 1300, and the other when I have an MTU of 1500.</p><p>There are 2 servers, when accessing via https/rdp it does not work when the MTU is 1500 on the local pc - the page just shows blank white.</p><p>But when 1300 MTU is set locally, the page loads correctly. Looking at the capture, seems like a lot of retransmissions and resets are happening even when its working correctly. any ideas on what this is?? no changes are are made to the servers, just the local PC.</p><p>captures: <a href="http://kdn.co.nz/ftpaccess/mtuof1500.pcapng">http://kdn.co.nz/ftpaccess/mtuof1500.pcapng</a> <a href="http://kdn.co.nz/ftpaccess/mtuof1300.pcapng">http://kdn.co.nz/ftpaccess/mtuof1300.pcapng</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mtu" rel="tag" title="see questions tagged &#39;mtu&#39;">mtu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '14, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/89e3bf56b53123171ef06f47aafd5db5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Flamer&#39;s gravatar image" /><p><span>Flamer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Flamer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Aug '14, 15:20</strong> </span></p></div></div><div id="comments-container-35040" class="comments-container"><span id="35044"></span><div id="comment-35044" class="comment"><div id="post-35044-score" class="comment-score"></div><div class="comment-text"><p>it's not possible to download those file, at least nothing happens on my system. Please use a different file hoster.</p></div><div id="comment-35044-info" class="comment-info"><span class="comment-age">(01 Aug '14, 00:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35126"></span><div id="comment-35126" class="comment"><div id="post-35126-score" class="comment-score"></div><div class="comment-text"><p>apologies about that, updated links!</p></div><div id="comment-35126-info" class="comment-info"><span class="comment-age">(03 Aug '14, 15:21)</span> <span class="comment-user userinfo">Flamer</span></div></div></div><div id="comment-tools-35040" class="comment-tools"></div><div class="clear"></div><div id="comment-35040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35129"></span>

<div id="answer-container-35129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35129-score" class="post-score" title="current number of votes">0</div><span id="post-35129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm sorry, but the file mtuof1500.pcapng does not contain enough data to figure out what's going wrong.</p><p>Furthermore, you would need a capture taken at the client side and at the server side <strong>in parallel</strong> to identify any MTU related problems, which are quite common with VPNs.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '14, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35129" class="comments-container"><span id="35178"></span><div id="comment-35178" class="comment"><div id="post-35178-score" class="comment-score"></div><div class="comment-text"><p>thanks for the reply Kurt. The 1500 capture is actually the whole ssl transaction. I started the capture then tried to load the page, waited a few seconds after it failed to load then stopped the capture. I don't think there is anything more the client can give. However I don't have access to the server to run wireshark on it. I suspect the server may have an issue, because even the 1300 capture looks rather strange doesnt it?</p></div><div id="comment-35178-info" class="comment-info"><span class="comment-age">(04 Aug '14, 16:33)</span> <span class="comment-user userinfo">Flamer</span></div></div><span id="35179"></span><div id="comment-35179" class="comment"><div id="post-35179-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The 1500 capture is actually the <strong>whole ssl transactio</strong></p></blockquote><p>O.K. then I need more information about your setup, because there is only one re-transmission and then the capture file ends. That does not explain what you are describing. BTW: The largest frame in mtuof1500.pcapng is 1286 bytes, so I don't see any relation to the MTU of 1500. Looks like the problem (which is not visible in the capture file!) is caused by something else and it is not related to the MTU size.</p><p>Please add the following details:</p><ul><li>is your VPN a site-2-site VPN (VPN gateways) or a client-2-site (VPN software on one side)</li><li>what kind of VPN is this (IPSEC, SSL, OpenVPN, etc.) and what is the vpn software</li><li>where did you change the MTU</li><li>is there any security software on one of the involved systems, like AV, Firewall, Endpoint Security? That could cause problems as well, although I don't see any relation to the MTU size.</li><li>what happens if you change the MTU size to 1480 and 1450?</li></ul></div><div id="comment-35179-info" class="comment-info"><span class="comment-age">(04 Aug '14, 23:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35129" class="comment-tools"></div><div class="clear"></div><div id="comment-35129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

