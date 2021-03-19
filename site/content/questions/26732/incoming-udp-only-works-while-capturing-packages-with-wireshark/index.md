+++
type = "question"
title = "Incoming UDP only works while capturing packages with Wireshark"
description = '''I was transmitting UDP packets from an Arduino with out being able to detect them. When I used Wireshark to capture the packages, they started coming into my receiving program they way they should. As soon as I closed Wireshark the packages were no longer received. Any ideas on why this is and what ...'''
date = "2013-11-07T13:39:00Z"
lastmod = "2013-11-07T17:03:00Z"
weight = 26732
keywords = [ "connection", "problem", "arduino", "udp", "wireshark" ]
aliases = [ "/questions/26732" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Incoming UDP only works while capturing packages with Wireshark](/questions/26732/incoming-udp-only-works-while-capturing-packages-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26732-score" class="post-score" title="current number of votes">0</div><span id="post-26732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was transmitting UDP packets from an Arduino with out being able to detect them. When I used Wireshark to capture the packages, they started coming into my receiving program they way they should.</p><p>As soon as I closed Wireshark the packages were no longer received.</p><p>Any ideas on why this is and what I need to change to my settings?</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-arduino" rel="tag" title="see questions tagged &#39;arduino&#39;">arduino</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/4c10b5413bcec59512c2f86cc68e2736?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bartp&#39;s gravatar image" /><p><span>Bartp</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bartp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Nov '13, 16:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-26732" class="comments-container"></div><div id="comment-tools-26732" class="comment-tools"></div><div class="clear"></div><div id="comment-26732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26736"></span>

<div id="answer-container-26736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26736-score" class="post-score" title="current number of votes">0</div><span id="post-26736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are several reports about similar behavior. However there is no common reason for all cases. The most plausible reason is:</p><ul><li>Your UDP frame is somehow 'malformed' and thus the receiving OS drops the frame (bad checksum) or does not even receive it (wrong MAC address, like <code>0:0:0:0:0:0</code>) until you enable promiscuous mode, by running Wireshark.</li></ul><p>If you post a sample capture file (one packet should be enough) somewhere (google drive, dropbox, cloudshark.org) we may be able to find the reason.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Nov '13, 16:30</strong> </span></p></div></div><div id="comments-container-26736" class="comments-container"><span id="26740"></span><div id="comment-26740" class="comment"><div id="post-26740-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply</p><p>Here is a screen dump: <a href="https://dyp.im/oKcPi1S9Eh">https://dyp.im/oKcPi1S9Eh</a></p><p>I can already see that there is no mac adress defined for the packet to go to, that might cause problems. However, i cannot influence what mac adress to send the packet too. Only IP and port. I'm using an arduino ethernet library that does not support this.</p><p>I can not find good instructions for windows to set the card into promiscuous mode. Do you have any suggestions?</p></div><div id="comment-26740-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:33)</span> <span class="comment-user userinfo">Bartp</span></div></div><span id="26743"></span><div id="comment-26743" class="comment"><div id="post-26743-score" class="comment-score"></div><div class="comment-text"><p>well, the <strong>destination address is 0:0:0:0:0:0</strong>. The NIC of your PC will not react upon that frame as it is not its own MAC address. As soon as you start Wireshark, the interface goes into promiscuous mode and then the NIC reacts on all MAC addresses. As soon as the NIC receives the packet, your OS (and Wireshark) will also see it.</p><blockquote><p>However, i cannot influence what mac adress to send the packet too.</p></blockquote><p>That's bad.</p><blockquote><p>Only IP and port. I'm using an arduino ethernet library that does not support this.</p></blockquote><p>Well, then it will never work.</p><p>I rather guess you missed something, as that would be a huge problem for all Arduino users. A library that works like that, would be totally useless.</p><blockquote><p>I can not find good instructions for windows to set the card into promiscuous mode. Do you have any suggestions?</p></blockquote><p>That's not the solution. The solution is to fix the code on Arduino and I'm sure there are qualified people on an Arduino forum that can help you with the ethernet library. Please check the following example:</p><blockquote><p><a href="http://arduino.cc/de/Reference/EthernetClient">http://arduino.cc/de/Reference/EthernetClient</a></p></blockquote></div><div id="comment-26743-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26750"></span><div id="comment-26750" class="comment"><div id="post-26750-score" class="comment-score"></div><div class="comment-text"><p>Maybe ARP requests are not working well in a local network with Arduino. Try to call <a href="http://arduino.cc/de/Reference/EthernetBegin">EthernetBegin()</a> with the IP address of your server (192.168.0.150) as <strong>gateway</strong></p><blockquote><p>Ethernet.begin(mac, ip, dns, <strong>gateway</strong>, subnet);</p></blockquote><p>mac: Arduino MAC address<br />
IP: Arduino IP address<br />
DNS: Network DNS server (set it to your target server)<br />
<strong>gateway</strong>: Usually the router in the local network. However, try to set it to your target server (192.168.0.150)</p></div><div id="comment-26750-info" class="comment-info"><span class="comment-age">(07 Nov '13, 16:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26753"></span><div id="comment-26753" class="comment"><div id="post-26753-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your suggestions. This does not work. I can still receive OK though.</p></div><div id="comment-26753-info" class="comment-info"><span class="comment-age">(07 Nov '13, 16:55)</span> <span class="comment-user userinfo">Bartp</span></div></div><span id="26755"></span><div id="comment-26755" class="comment"><div id="post-26755-score" class="comment-score"></div><div class="comment-text"><p>well, then I suggest to talk to Arduino gurus or open a support ticket (if that is possible). Maybe a firmware update will help !?!</p><p>At least you know, why it does not work: wrong/missing destination MAC address. If there is a solution to that problem (except promiscuous mode on the receiver), please update here for the benefit of others.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-26755-info" class="comment-info"><span class="comment-age">(07 Nov '13, 17:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26736" class="comment-tools"></div><div class="clear"></div><div id="comment-26736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

