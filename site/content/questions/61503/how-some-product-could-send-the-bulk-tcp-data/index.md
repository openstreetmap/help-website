+++
type = "question"
title = "How some product could send the bulk tcp data"
description = '''Hello, We tested a tcp accelation product and found that product could receive the large bulk packets from the server(ftp). (Client -- (WAN) -- Accelation -- FTP Server) When the product work as &#x27;bypass mode&#x27;, I could see around the &#x27;58xx&#x27; length packet received from the server. https://www.cloudsha...'''
date = "2017-05-19T01:53:00Z"
lastmod = "2017-05-21T22:29:00Z"
weight = 61503
keywords = [ "bulk", "packets" ]
aliases = [ "/questions/61503" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How some product could send the bulk tcp data](/questions/61503/how-some-product-could-send-the-bulk-tcp-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61503-score" class="post-score" title="current number of votes">0</div><span id="post-61503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>We tested a tcp accelation product and found that product could receive the large bulk packets from the server(ftp). (Client -- (WAN) -- Accelation -- FTP Server) When the product work as 'bypass mode', I could see around the '58xx' length packet received from the server. <a href="https://www.cloudshark.org/captures/4b2217e6d72e">https://www.cloudshark.org/captures/4b2217e6d72e</a></p><p>When the product work as 'Accelation mode', I could see around the '14xxx~6xxxx' length packets received from the server. <a href="https://www.cloudshark.org/captures/e45cc5ccba29">https://www.cloudshark.org/captures/e45cc5ccba29</a></p><p>I 'd like to know how could receive that large bulk packets from the server.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '17, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/c0ba81b234f6d9018b1d5788e1c47a49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaesung%20kim&#39;s gravatar image" /><p><span>jaesung kim</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaesung kim has no accepted answers">0%</span></p></div></div><div id="comments-container-61503" class="comments-container"><span id="61525"></span><div id="comment-61525" class="comment"><div id="post-61525-score" class="comment-score"></div><div class="comment-text"><p>I edited the trace link option to share mode.</p><p>From my analysis, When the product work as accelation mode, the client send the syn packet with 'ECN','CWR' flags. But i could not found any related reply from the 'Syn-Ack' packets. <img src="https://osqa-ask.wireshark.org/upfiles/accel_ECN_CWR.jpg" alt="alt text" /></p><p>Thank you. Jaesung Kim</p></div><div id="comment-61525-info" class="comment-info"><span class="comment-age">(21 May '17, 19:25)</span> <span class="comment-user userinfo">jaesung kim</span></div></div></div><div id="comment-tools-61503" class="comment-tools"></div><div class="clear"></div><div id="comment-61503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61526"></span>

<div id="answer-container-61526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61526-score" class="post-score" title="current number of votes">0</div><span id="post-61526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The large packets are probably the result of <a href="https://en.wikipedia.org/wiki/Large_receive_offload">large receive offload</a>, where the packets <em>on the wire</em> aren't large, but, when receiving packets, the NIC reassembles multiple TCP segments and hands a fake Ethernet/IP/TCP packet, containing data from multiple over-the-wire TCP segments, to the host. There might also be <a href="https://en.wikipedia.org/wiki/Large_send_offload">large send offload</a>, where the host hands a single large chunk of data for a TCP connection to the NIC, in the form of a very large Ethernet/TCP/IP packet - and also hands that large packet to the packet capture mechanism, so that it shows up in tcpdump/Wireshark/etc. - and the NIC sends it out as multiple segments on the TCP connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '17, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-61526" class="comments-container"><span id="61527"></span><div id="comment-61527" class="comment"><div id="post-61527-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy Harris, Thanks for your reply. The trace captured in Server(Window OS). Does wireshark capture the packet on the NIC level? And is it possible to use ECN/CWR option for the large offload packets?</p><p>Thank you. Jaesung Kim</p></div><div id="comment-61527-info" class="comment-info"><span class="comment-age">(21 May '17, 21:21)</span> <span class="comment-user userinfo">jaesung kim</span></div></div><span id="61528"></span><div id="comment-61528" class="comment"><div id="post-61528-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Does wireshark capture the packet on the NIC level?</p></blockquote><p>Wireshark uses libpcap on UN*X, and WinPcap on Windows, to capture traffic. Libpcap runs atop some OS-dependent mechanism in the OS; WinPcap runs atop NDIS on Windows. None of those mechanisms are guaranteed to capture packets at the level the NIC sees them; at least on Windows, NDIS will provide you with the packets that the NIC provides to you, which may have even reassembled in the fashion I mentioned.</p><blockquote><p>And is it possible to use ECN/CWR option for the large offload packets?</p></blockquote><p>The large offload packets are not sent on the network - they're either split into multiple TCP segments when they're sent or reassembled from multiple TCP segments when they're received; the notion of large offload packets is not part of the TCP protocol, so there's no reason, at the protocol layer, why packets split and sent over the network, or reassembled from packets received over the network, couldn't use that option.</p><p>What the software on the machine, or the firmware in the NIC, that does the splitting-and-transmitting or receiving-and-reassembling, will see those flags in the TCP segments sent over the wire, or will look at those flags in the TCP segments received over the wire and set them in the fake packet it provides after reassembly, is another matter.</p><p>Those flags probably have nothing to do with the segmentation offloading that causes the large packets.</p></div><div id="comment-61528-info" class="comment-info"><span class="comment-age">(21 May '17, 22:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="61529"></span><div id="comment-61529" class="comment"><div id="post-61529-score" class="comment-score"></div><div class="comment-text"><p>ECN/CWR have nothing to do with offloading and they are not used in your session, as your server does not advertise them, too.</p></div><div id="comment-61529-info" class="comment-info"><span class="comment-age">(21 May '17, 22:29)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-61526" class="comment-tools"></div><div class="clear"></div><div id="comment-61526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

