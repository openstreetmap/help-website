+++
type = "question"
title = "Authentication failure"
description = '''I have two domain controllers serving up a NLB VIP for ADFS authentication. The client is able to ping and RDP to both servers but it is unable to get an ack bit from either server. When I take a capture I see the SYN bit sent and re-transmitted,then crickets. I have confirmed that the firewall isn&#x27;...'''
date = "2016-05-16T07:32:00Z"
lastmod = "2016-05-19T07:43:00Z"
weight = 52621
keywords = [ "syn+ack", "syn", "authetication" ]
aliases = [ "/questions/52621" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Authentication failure](/questions/52621/authentication-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52621-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two domain controllers serving up a NLB VIP for ADFS authentication. The client is able to ping and RDP to both servers but it is unable to get an ack bit from either server. When I take a capture I see the SYN bit sent and re-transmitted,then crickets. I have confirmed that the firewall isn't dropping packets and tracetoutes and DNS resolution are successful. This one is a head scratcher so I was hoping for some insight. Thanks in advance!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_rYITtt2.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">syn+ack syn authetication</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '16, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/d930a81ddfe6e0818f854634ad160652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="it_ninja&#39;s gravatar image" /><p>it_ninja<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="it_ninja has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52621" class="comments-container"><span id="52637"></span><div id="comment-52637" class="comment"><div id="post-52637-score" class="comment-score"></div><div class="comment-text"><p>Presumably the client was taken at the client, what do you see if you capture at the server?</p><p>As ever, analysis by screenshot is hopeless, as a) we can't use the Wireshark tools for analysis and b) you may have cut out the frames in the capture that reveal the issue.</p></div><div id="comment-52637-info" class="comment-info"><span class="comment-age">(16 May '16, 12:00)</span> grahamb ♦</div></div><span id="52642"></span><div id="comment-52642" class="comment"><div id="post-52642-score" class="comment-score"></div><div class="comment-text"><p>Correct, Gramb. The capture was taken from the client. When I do a capture from the server I don't see anything coming from the source IP. The client is connected to a remote SOHO router that provides access via an IP Sec tunnel. Please forgive me for the screen-shot, this is my first post on the wireshark forum. I didn't want to give out my private IPs to the world. Thanks again.<br />
</p></div><div id="comment-52642-info" class="comment-info"><span class="comment-age">(16 May '16, 12:37)</span> it_ninja</div></div></div><div id="comment-tools-52621" class="comment-tools"></div><div class="clear"></div><div id="comment-52621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="52663"></span>

<div id="answer-container-52663" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52663-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't see the SYN packets at the server, then it's likely your IPSEC tunnel is dropping them. You'll have to check the tunnel ingress and egress settings.</p><p>Does the tunnel also NAT the client IP, so it's presented as something on the server's local network?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '16, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-52663" class="comments-container"><span id="52771"></span><div id="comment-52771" class="comment"><div id="post-52771-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I was actually able to confirm that the issue was a limitation from the vendor’s equipment. I have submitted a ticket to their QA department and they are in the process of resolving the problem. This was my first post and I would like to thank everyone for their insight. I am learning that Wireshark is an INVALUABLE tool that I look forward to mastering (with the help of this forum) .<br />
</p></div><div id="comment-52771-info" class="comment-info"><span class="comment-age">(19 May '16, 07:49)</span> it_ninja</div></div><span id="52772"></span><div id="comment-52772" class="comment"><div id="post-52772-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-52772-info" class="comment-info"><span class="comment-age">(19 May '16, 07:53)</span> Jaap ♦</div></div></div><div id="comment-tools-52663" class="comment-tools"></div><div class="clear"></div><div id="comment-52663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52631"></span>

<div id="answer-container-52631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52631-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you say you confirmed that the firewall isn't dropping packets, I assume you are talking about a different device. Have you checked that the Windows Firewall on the servers is allowing incoming traffic on those ports?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '16, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p>ryber<br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span> </br></p></div></div><div id="comments-container-52631" class="comments-container"><span id="52634"></span><div id="comment-52634" class="comment"><div id="post-52634-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, Ryber. Yes, I confirmed that Windows Firewall is off and the servers are allowing incoming traffic on that port. This is only affecting users with an Ethernet connection on a SOHO router via an IPSEC tunnel and the logs don't indicate any traffic being dropped.</p></div><div id="comment-52634-info" class="comment-info"><span class="comment-age">(16 May '16, 11:43)</span> it_ninja</div></div><span id="52666"></span><div id="comment-52666" class="comment"><div id="post-52666-score" class="comment-score"></div><div class="comment-text"><p>The statements</p><blockquote><p>I have confirmed that the firewall isn't dropping packets</p></blockquote><p>and</p><blockquote><p>the logs don't indicate any traffic being dropped</p></blockquote><p>are not the same, are they? The only way to be sure that a box is not dropping packets is to capture at both its ends simultaneously and see the packets at the input of the box and not see them at its output.</p><p>Plus it may not actually drop them, it may just misroute them somewhere else if it has several interfaces.</p></div><div id="comment-52666-info" class="comment-info"><span class="comment-age">(17 May '16, 05:17)</span> sindy</div></div></div><div id="comment-tools-52631" class="comment-tools"></div><div class="clear"></div><div id="comment-52631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52769"></span>

<div id="answer-container-52769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52769-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You mentioned that the client can ping and connect via RDP to either server. Can you see the TCP handshake completing for the RDP connections? If RDP works but HTTPS does not, then you may need to adjust the crypto map being used by your IPSEC tunnel (as grahamb suggested), or any other ACLs that might be along the way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '16, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p>ryber<br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span></p></div></div><div id="comments-container-52769" class="comments-container"></div><div id="comment-tools-52769" class="comment-tools"></div><div class="clear"></div><div id="comment-52769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

