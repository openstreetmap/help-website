+++
type = "question"
title = "Broken TCP. The acknowledge field is nonzero while the ack flag is not set"
description = '''Hi, My TN3270 printer server sometimes disconnect from IBM communication server. Printer server IP is 10.100.12.105, communication server IP is 10.99.16.22. The server TCP port is 2023. The communication server will sent PSH,ACK to printer server every 20 seconds if no data sent to printer server to...'''
date = "2013-02-26T23:56:00Z"
lastmod = "2013-02-27T15:01:00Z"
weight = 18910
keywords = [ "broken", "tcp" ]
aliases = [ "/questions/18910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Broken TCP. The acknowledge field is nonzero while the ack flag is not set](/questions/18910/broken-tcp-the-acknowledge-field-is-nonzero-while-the-ack-flag-is-not-set)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18910-score" class="post-score" title="current number of votes">0</div><span id="post-18910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>My TN3270 printer server sometimes disconnect from IBM communication server. Printer server IP is 10.100.12.105, communication server IP is 10.99.16.22. The server TCP port is 2023. The communication server will sent PSH,ACK to printer server every 20 seconds if no data sent to printer server to print, and the printer server will sent ACK to communication server.</p><p>I used Wireshark to capture traffic at printer server side and communication server side ( these packet capture not at the same time ). At the printer server side, after the printer server sent ACK to communication server ( No.35865 ), the communication server stop to send PSH,ACK to printer server.</p><p><img src="http://www.imageurlhost.com/images/duhndyx20kv16w03klqb.jpg" alt="alt text" /></p><p>At the communication server side, we can see the last PSH,ACK ( No.98926 ) have sent, but received 2 packets ( No,98932, RST &amp; No.98976, Ack ) <img src="http://www.imageurlhost.com/images/n9xpe37xp0ykmx1kd4j0.jpg" alt="alt text" /></p><p>The packet No.98976 seems normal packets sent from print server, but the packet No.98932 arrived at communication server before No.98976, cause the TCP connection reset, then communication server never sent PSH,ACK to printer server.</p><p>My question is What is the “Broken TCP. The acknowledge field is nonzero while the ack flag is not set” mean? Why the packet No.98932 generated and received by communication server?</p><p>Best Regards,</p><p>Jackson</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broken" rel="tag" title="see questions tagged &#39;broken&#39;">broken</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '13, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/57b5c51e3d55bc37a29f415298ef908f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jackson&#39;s gravatar image" /><p><span>Jackson</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jackson has no accepted answers">0%</span></p></img></div></div><div id="comments-container-18910" class="comments-container"></div><div id="comment-tools-18910" class="comment-tools"></div><div class="clear"></div><div id="comment-18910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18917"></span>

<div id="answer-container-18917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18917-score" class="post-score" title="current number of votes">1</div><span id="post-18917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The message means that although the ACK flag is not set, the ACK field is non-zero. This is a violation on the TCP RFC. It does happen regularly on packets with the RST bit set, so in your case it is not really a problem.</p><p>What is a problem is that you see a RST packet on one side and not on the other side of the connection. So you might want to investigate that further. Have a look at the mac-addresses and the IP TTL to see whether you can determine who is sending the RST. It might be a firewall in between?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '13, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></img></div></div><div id="comments-container-18917" class="comments-container"><span id="18928"></span><div id="comment-18928" class="comment"><div id="post-18928-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>The print server and communication server at 2 different layer 3 VLANs in same Cisco Catalyst 6509, no firewall or ACL in between.</p><p>I found the TTL for the RST packet is 63, and the TTL for normal ACK packet is 127. The source MAC address of both packet are the same ( Cisco Catalyst 6509 MAC address )</p><p>Do you mean maybe someone ( not real printer server ) spoof the IP of print server and sent RST to communication server? I tried to capture traffic for print server's VLAN to analyze it, but this VLAN very big ( almost 2000 devices ). Please advise me how to troubleshooting this problem?</p><p>Best Regards,</p><p>Jackson</p></div><div id="comment-18928-info" class="comment-info"><span class="comment-age">(27 Feb '13, 06:32)</span> <span class="comment-user userinfo">Jackson</span></div></div><span id="18931"></span><div id="comment-18931" class="comment"><div id="post-18931-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Do you mean maybe someone ( not real printer server ) spoof the IP of print server</p></blockquote><p>I would rather say the IP stack implementation of the printer server is buggy. What is the OS of that server?</p><p>Regards<br />
Kurt</p></div><div id="comment-18931-info" class="comment-info"><span class="comment-age">(27 Feb '13, 09:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="18947"></span><div id="comment-18947" class="comment"><div id="post-18947-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>The print server OS is WIN XP, running TN3270 software.</p><p>The communication between print server and communication server was ok before 3 weeks ago, we have not change any network structure or change the print / communication server OS &amp; comfiguration.</p><p>How to verify if the problem is at print server or communication server IP stack and how to solve it?</p><p>Best Regards,</p><p>Jackson</p></div><div id="comment-18947-info" class="comment-info"><span class="comment-age">(27 Feb '13, 15:01)</span> <span class="comment-user userinfo">Jackson</span></div></div></div><div id="comment-tools-18917" class="comment-tools"></div><div class="clear"></div><div id="comment-18917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

