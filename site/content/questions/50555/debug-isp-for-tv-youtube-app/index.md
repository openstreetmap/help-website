+++
type = "question"
title = "debug ISP for tv youtube app"
description = '''hi guys, for about a month my tv&#x27;s youtube app stopped working.(thumbs and videos descriptions are loading but video can not start playing). Youtube on PC works good. When I change ISP for my backup one (low speed and transfer) everything works like a charm. The primary ISP says that everything is O...'''
date = "2016-02-26T11:50:00Z"
lastmod = "2016-02-27T05:23:00Z"
weight = 50555
keywords = [ "debug", "isp" ]
aliases = [ "/questions/50555" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [debug ISP for tv youtube app](/questions/50555/debug-isp-for-tv-youtube-app)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50555-score" class="post-score" title="current number of votes">0</div><span id="post-50555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys, for about a month my tv's youtube app stopped working.(thumbs and videos descriptions are loading but video can not start playing). Youtube on PC works good. When I change ISP for my backup one (low speed and transfer) everything works like a charm. The primary ISP says that everything is OK with my connection.</p><p>I think i could run wireshark on primary and backup ISP,and then could see what is the difference, but have no Idea how to do it in wireshark . Any suggestions? I Can have a ubuntu laptop with wireshark as a router , or should I use windows version but windows PC wouldn't be a router then.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-isp" rel="tag" title="see questions tagged &#39;isp&#39;">isp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '16, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/4e8caace54e4f1ba6546f0d9d6d04b6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stanis%C5%82aw%20%C5%81azowy&#39;s gravatar image" /><p><span>Stanisław Ła...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stanisław Łazowy has no accepted answers">0%</span></p></div></div><div id="comments-container-50555" class="comments-container"></div><div id="comment-tools-50555" class="comment-tools"></div><div class="clear"></div><div id="comment-50555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50556"></span>

<div id="answer-container-50556" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50556-score" class="post-score" title="current number of votes">1</div><span id="post-50556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As for "how to capture", a <code>tcpdump -i the_name_of_lan_interface -s 0 -w capture_file_name host your.tv's.local.ipaddress</code> (or <code>dumpcap</code> with the same command line parameters) on the ubuntu laptop used as a router should be fine, you can then use Wireshark on any of the two machines to analyse the captures. Just make sure that you catch all the DNS requests from the TV, so I'd recommend to (switch the TV off, start the capture, and then switch the TV on again and open the video) for both the secondary connection (captured first) and the primary connection (captured second).</p><p>But I'm afraid you'll have a tough time "seeing what is the difference" because if the TV accesses Youtube using https, you'll be unable to get the pre-master TLS key from it, making it impossible for you to see what goes wrong if it goes wrong after the TLS session establishment. If you are "lucky", the TV will attempt to establish a new TCP connection for the video and its SYN packet will not be ever responded due to some routing error between Google's video server and your primary connection's public IP; if you are "not lucky", the issue will be invisible because either an existing TLS session will be re-used or a new one established successfully, and Google will refuse to send the stream requested (possibly based on some IP ranges' blacklist) but you'll be unable to see the request and response as they'll be encrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '16, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '16, 14:08</strong> </span></p></div></div><div id="comments-container-50556" class="comments-container"><span id="50559"></span><div id="comment-50559" class="comment"><div id="post-50559-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your help. I've made a wireshark dump for those 2 scenarios. I would appreciate if you could take a look at those files. <a href="http://we.tl/kIcqcEpjdm">http://we.tl/kIcqcEpjdm</a> Stan</p></div><div id="comment-50559-info" class="comment-info"><span class="comment-age">(27 Feb '16, 03:08)</span> <span class="comment-user userinfo">Stanisław Ła...</span></div></div><span id="50560"></span><div id="comment-50560" class="comment"><div id="post-50560-score" class="comment-score"></div><div class="comment-text"><p>Not much to see there about the reason.</p><p>Try to apply a display filter <code>(tcp and ip.addr == 46.134.194.15)  or (dns.a == 46.134.194.15)</code> in both captures. You shall see that</p><ul><li><p>the TV sends a DNS query for the same fqdn to be resolved to an IP address in both cases, and the DNS answer contains the same IP address in both cases</p></li><li><p>the TV then opens <em>two</em> TLS sessions towards that IP's TCP port 443 simultaneously (don't ask me why it does so, the data volume is approximately similar for both streams so it cannot be that e.g. one is the complete AV stream and the other one is an additional sound track in a different language)</p></li></ul><p>The difference between the two captures is that in the successful one, the TLS handshake in both streams succeeds and the TCP session continues, while in the failing case the seq and ack numbers show that the server has not received the response of the TV to the Change Cipher Spec (btw it has a different size than in the successful case) and since then the server doesn't send anything else (which is quite logical as the cipher negotiation has probably failed).</p><p>There is a difference in the establishment phase of the TCP sessions, though. In the working case, the MSS received in the SYN,ACK packet from the video server says 1220 bytes, while in the failing case, it says 1460 bytes. So there may be an MTU handling issue in the primary providers' network or the CPE you use to connect to it.</p><p>Have a look at <a href="http://people.netfilter.org/kadlec/ipset/iptables.man.html">this link</a> and search for the TCPMSS target (capital letters), read the associated explanation, and then try to <code>--set-mss</code> to set some value like 1000 for the start on the ubuntu machine used as router, so that you could confirm or deny the theory. If it helps, you may talk to your primary ISP about the issue, or replace the ubuntu laptop by some other box as a permanent workaround.</p></div><div id="comment-50560-info" class="comment-info"><span class="comment-age">(27 Feb '16, 05:23)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50556" class="comment-tools"></div><div class="clear"></div><div id="comment-50556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

