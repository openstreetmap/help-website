+++
type = "question"
title = "Not all SYN packets shown"
description = '''Hi, When I start a valid TCP session, I see the expected SYN,SYN/ACK,ACK,PSH/ACK,ACK,FIN/ACK,ACK packets. When I try to start a TCP session to an non-existing IP address, no packets at all are shown. Shouldn&#x27;t there be a SYN packet that is never answered? How can I make sure that I do not miss such ...'''
date = "2010-12-20T06:55:00Z"
lastmod = "2010-12-20T07:24:00Z"
weight = 1404
keywords = [ "syn", "tcp" ]
aliases = [ "/questions/1404" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not all SYN packets shown](/questions/1404/not-all-syn-packets-shown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1404-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When I start a valid TCP session, I see the expected SYN,SYN/ACK,ACK,PSH/ACK,ACK,FIN/ACK,ACK packets. When I try to start a TCP session to an non-existing IP address, no packets at all are shown. Shouldn't there be a SYN packet that is never answered? How can I make sure that I do not miss such a packet?</p><p>Thanks in advance,</p><p>Remco Poelstra</p></div><div id="question-tags" class="tags-container tags">syn tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '10, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/e43e74745903f33eaab0c766cb839069?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Remco%20Poelstra&#39;s gravatar image" /><p>Remco Poelstra<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Remco Poelstra has no accepted answers">0%</span></p></div></div><div id="comments-container-1404" class="comments-container"></div><div id="comment-tools-1404" class="comment-tools"></div><div class="clear"></div><div id="comment-1404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1406"></span>

<div id="answer-container-1406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1406-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you start a TCP session to a non-existing IP address in the locally connected subnet. Your system will do an ARP request to find the mac-address for the requested IP address. However, no system will answer the ARP request, so no SYN packet can be send.</p><p>If you start the TCP session to a non-existing IP address in a remote subnet, you should be able to see the SYN packet. But only if the routing table on your system knows a route to the IP address (the default gateway if no specific route is configured). You will only see the SYN if you capture on the interface to which the (default) route points.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '10, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1406" class="comments-container"><span id="1426"></span><div id="comment-1426" class="comment"><div id="post-1426-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. This makes my problem more interesting. I don't now whether this is the right place to ask, but you people seem to know a lot about TCP :). I've a device (small embedded microcontroller) that sometimes doesn't respond to TCP connections. Given your answer I verified that an ARP request is send and it's answered by the device. For some reason, the answer is not followed by a SYN packet. Why could that be? I also noticed that at the moments that the TCP connections is accepted, there is no preceding ARP, so the system probably already knows where the small device lives. My computer is a Mac running the iPhone simulator, if that might help.</p><p>Many thanks.</p><p>Kind regards,</p><p>Remco Poelstra</p></div><div id="comment-1426-info" class="comment-info"><span class="comment-age">(21 Dec '10, 00:41)</span> Remco Poelstra</div></div><span id="1427"></span><div id="comment-1427" class="comment"><div id="post-1427-score" class="comment-score"></div><div class="comment-text"><p>OK, so you start the TCP session from the iPhone simulator to the embedded micro controller (Hmmm... nice, you must be working on an interesting project :-)).</p><p>Does it work when you immediately try another session after the one that fails? If it fails consistently for a while, does a session from the Mac itself do work?</p><p>Can you check the arp-table on the Iphone simulator to see whether it has received the arp reply?</p><p>Is the iPhone simulator "bridged" to your Mac's ethernet adapter?</p></div><div id="comment-1427-info" class="comment-info"><span class="comment-age">(21 Dec '10, 00:57)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1406" class="comment-tools"></div><div class="clear"></div><div id="comment-1406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

