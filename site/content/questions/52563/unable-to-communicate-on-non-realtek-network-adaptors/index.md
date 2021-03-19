+++
type = "question"
title = "Unable to communicate on Non RealTek Network Adaptors"
description = '''Hi, I am facing a weird problem...my PC has a RealTek PCIe GBE Family Controller Network card. I am trying to send data over UDP to my target embedded board using my own custom made GUI. Whenever wireshark is open in my PC, I can communicate successfully. However, if Wireshark is off, I cant communi...'''
date = "2016-05-14T06:58:00Z"
lastmod = "2016-05-14T09:51:00Z"
weight = 52563
keywords = [ "nic", "udp", "realtek", "visual-studio" ]
aliases = [ "/questions/52563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to communicate on Non RealTek Network Adaptors](/questions/52563/unable-to-communicate-on-non-realtek-network-adaptors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52563-score" class="post-score" title="current number of votes">0</div><span id="post-52563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am facing a weird problem...my PC has a RealTek PCIe GBE Family Controller Network card. I am trying to send data over UDP to my target embedded board using my own custom made GUI. Whenever wireshark is open in my PC, I can communicate successfully. However, if Wireshark is off, I cant communicate.</p><p>Also, on other PCs having a non-Realtek adaptor, I cant communicate with the target board even if Wireshark is open. Wireshark doesnt show any packets being sent by the GUI to the board. I have tried reinstalling both, Wireshark and Winpcap drivers but the issue still persists. I also have the latest drivers for my network card installed on my PC. For sending data over UDP, the GUI is developed using MS Visual Studio 2008 using winsock library 2.0. I have used standard UDP protocol APIs for performing all the UDP operations.</p><p>Is the issue related to Wireshark or Network card or something else? Please assist.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-realtek" rel="tag" title="see questions tagged &#39;realtek&#39;">realtek</span> <span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '16, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/765dcaee3ca7352430d77f5d8c835771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mihirkarkhane&#39;s gravatar image" /><p><span>mihirkarkhane</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mihirkarkhane has no accepted answers">0%</span></p></div></div><div id="comments-container-52563" class="comments-container"></div><div id="comment-tools-52563" class="comment-tools"></div><div class="clear"></div><div id="comment-52563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52565"></span>

<div id="answer-container-52565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52565-score" class="post-score" title="current number of votes">0</div><span id="post-52565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per your description it may be actually multiple issues combined.</p><p>While a Wireshark capture is running in promiscuous mode (or, in newer versions, also while the Wireshark's idle window shows the traffic graph on individual interfaces), the MAC address filter in the NIC's hardware is disabled. So if your embedded board sends data to proper IP address but to wrong MAC address, use of promiscuous mode hides that issue and the communication works. This scenario would be applicable if your embedded board is connected to the PC directly, using a cable, or there would be a hub (not switch!) between them.</p><p>The fact that Wireshark doesn't show any packets sent to the embedded board may mean that the PC cannot send them because it never gets an answer to its ARP requests from the embedded board (but the fact that it works with Realtek makes this reason questionable), or an issue with the capturing in general caused by some interfering software drivers installed on the capturing PC, as explained several times around here.</p><p>So I would recommend you to test capture on your "realtek" and "non-realtek" PCs while they would communicate over the same Ethernet interface with something else than your embedded board. This should tell you what to concentrate on first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '16, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52565" class="comments-container"></div><div id="comment-tools-52565" class="comment-tools"></div><div class="clear"></div><div id="comment-52565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

