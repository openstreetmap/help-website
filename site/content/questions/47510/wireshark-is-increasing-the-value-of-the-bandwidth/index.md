+++
type = "question"
title = "Wireshark is increasing the value of the BandWidth"
description = '''Hello everyone! Currently I am developing a Linux Kernel Module that encrypts (AES) some data on an IPv6 packet. I need to know how the BW (BandWidth) will behave after the module has been inserted. To do that I am using iperf3. Here is my scenario PC1 (windows 8.1) - Iperf client PC2 (windows 8.1) ...'''
date = "2015-11-11T05:16:00Z"
lastmod = "2015-11-11T19:01:00Z"
weight = 47510
keywords = [ "router", "bandwidth", "linux", "iperf" ]
aliases = [ "/questions/47510" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark is increasing the value of the BandWidth](/questions/47510/wireshark-is-increasing-the-value-of-the-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47510-score" class="post-score" title="current number of votes">0</div><span id="post-47510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone!</p><p>Currently I am developing a Linux Kernel Module that encrypts (AES) some data on an IPv6 packet. I need to know how the BW (BandWidth) will behave after the module has been inserted. To do that I am using iperf3. Here is my scenario</p><p>PC1 (windows 8.1) - Iperf client<br />
PC2 (windows 8.1) - Iperf server<br />
R1 (Router, which is actually a PC running Debian wheezy with two ethernet interfaces, one on-board and the other one is an Intel pro PCI express).<br />
PC1 is connected to R1, and R1 is connected to PC2. I wanna know how the BW (between PC1 and PC2) will be affected after my LKM is inserted in R1.</p><p>I have done all the coding and the module is running ok, but the impact on the BW is really severe (I am using Linux crypto API to do the encryption). Anyway, I have run into a very strange situation. Whenever I am running iperf I get a value X of BW, however when I open Wireshark on R1 (to capture the packets going to PC2) the BW becomes 2*X. Exactly the BW shown on iperf is doubled when I open Wireshark on R1. I noticed that Wireshark puts the Ethernet interface in promiscuous mode. So I closed Wireshark and manually set the card to promiscuous, but there was no effect on the BW.</p><p>Has anyone noticed that Wireshark actually caused a better BW value? Am I missing something?</p><p>Thank You very much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-iperf" rel="tag" title="see questions tagged &#39;iperf&#39;">iperf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '15, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/57e1c208779096d19f49a1f40892f8a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Phil%20Lima&#39;s gravatar image" /><p><span>Phil Lima</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Phil Lima has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Nov '15, 08:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></br></p></div></div><div id="comments-container-47510" class="comments-container"><span id="47513"></span><div id="comment-47513" class="comment"><div id="post-47513-score" class="comment-score"></div><div class="comment-text"><p>Try running the capture with promiscuous mode off. It's a setting on the capture interface window.</p></div><div id="comment-47513-info" class="comment-info"><span class="comment-age">(11 Nov '15, 08:18)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="47526"></span><div id="comment-47526" class="comment"><div id="post-47526-score" class="comment-score"></div><div class="comment-text"><p>Can u run Wireshark on PC1 and PC2 and do the same....</p></div><div id="comment-47526-info" class="comment-info"><span class="comment-age">(11 Nov '15, 19:01)</span> <span class="comment-user userinfo">srinu_bel</span></div></div></div><div id="comment-tools-47510" class="comment-tools"></div><div class="clear"></div><div id="comment-47510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47524"></span>

<div id="answer-container-47524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47524-score" class="post-score" title="current number of votes">0</div><span id="post-47524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please check if LRO (large receive offloading) is enabled on R1</p><blockquote><p>ethtool -k eth0 | grep -i offload</p></blockquote><p>If it is enabled, try to disable it with the following command and then repeat the iperf test with and without tcpdump running!</p><blockquote><p>ethtool -K eth0 lro off</p></blockquote><p>If that does not help, you can also try to disable other offloading methods as well.</p><p>BTW: Enabling promiscuous mode 'can' disable LRO, so this might explain what you are seeing. I can't explain why you did not see any difference while you put the interface in promiscuous mode manually, but I don't know how you did it.</p><p>See also here.</p><blockquote><p><a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1027511">http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1027511</a></p></blockquote><p>It's for VMware, but it should apply to a real box as well (depends on the driver).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '15, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Nov '15, 14:33</strong> </span></p></div></div><div id="comments-container-47524" class="comments-container"></div><div id="comment-tools-47524" class="comment-tools"></div><div class="clear"></div><div id="comment-47524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

