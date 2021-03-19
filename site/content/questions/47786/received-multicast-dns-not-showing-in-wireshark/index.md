+++
type = "question"
title = "received Multicast DNS not showing in Wireshark"
description = '''Hi, I have a windows 7 laptop connected wireless to the network. On this laptop I try to capture Multicast DNS traffic comming from the network, but I never receive any MDNS packets. I do see the MDNS packets send by the laptop. I also monitor with the AirPCAP tool and there I do see that the AP is ...'''
date = "2015-11-20T04:25:00Z"
lastmod = "2015-11-27T08:17:00Z"
weight = 47786
keywords = [ "mdns" ]
aliases = [ "/questions/47786" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [received Multicast DNS not showing in Wireshark](/questions/47786/received-multicast-dns-not-showing-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47786-score" class="post-score" title="current number of votes">0</div><span id="post-47786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a windows 7 laptop connected wireless to the network. On this laptop I try to capture Multicast DNS traffic comming from the network, but I never receive any MDNS packets.</p><p>I do see the MDNS packets send by the laptop.</p><p>I also monitor with the AirPCAP tool and there I do see that the AP is sending out the MDNS packets.</p><p>I hope to find out why this is not showing in the wireshark trace on the laptop?</p><p>Laptop info: Wireshark version:1.12.8 Windows 2007 professional Intel(R) Centrino(R) Advanced-N 6205</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mdns" rel="tag" title="see questions tagged &#39;mdns&#39;">mdns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '15, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/5bdc253dfe511232daf35139347344df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BartS&#39;s gravatar image" /><p><span>BartS</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BartS has no accepted answers">0%</span></p></div></div><div id="comments-container-47786" class="comments-container"><span id="47787"></span><div id="comment-47787" class="comment"><div id="post-47787-score" class="comment-score"></div><div class="comment-text"><p>Do you see other Multicast/Broadcast traffic while you are capturing on your wifi interface on Windows (without using AirPcap)?</p></div><div id="comment-47787-info" class="comment-info"><span class="comment-age">(20 Nov '15, 04:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47951"></span><div id="comment-47951" class="comment"><div id="post-47951-score" class="comment-score"></div><div class="comment-text"><p>I do see other broadcast and multicast traffic arriving at the interface.</p></div><div id="comment-47951-info" class="comment-info"><span class="comment-age">(25 Nov '15, 00:24)</span> <span class="comment-user userinfo">BartS</span></div></div><span id="47952"></span><div id="comment-47952" class="comment"><div id="post-47952-score" class="comment-score"></div><div class="comment-text"><p>Is this an open wifi network or encrypted? Can you provide a capture file (upload to dropbox and post link here).</p></div><div id="comment-47952-info" class="comment-info"><span class="comment-age">(25 Nov '15, 00:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47954"></span><div id="comment-47954" class="comment"><div id="post-47954-score" class="comment-score"></div><div class="comment-text"><p>I also tried the same thing with Tshark, but also there I am not seeing any MDNS packets. Could it be that Windows is filtering those packets out before it can be used by WinPCAP?</p></div><div id="comment-47954-info" class="comment-info"><span class="comment-age">(25 Nov '15, 01:57)</span> <span class="comment-user userinfo">BartS</span></div></div></div><div id="comment-tools-47786" class="comment-tools"></div><div class="clear"></div><div id="comment-47786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47982"></span>

<div id="answer-container-47982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47982-score" class="post-score" title="current number of votes">1</div><span id="post-47982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Could it be that Windows is filtering those packets out before it can be used by WinPCAP?</p></blockquote><p>Could be some kind of security software on the capturing device that filters MDNS traffic. Please disable that kind of software if it's installed on the capturing system, like: AV, IPS/IDS, Endpoint Control, VPN clients, etc.</p><p>See my answer to a similar problem, <strong>although</strong> yours is different.</p><blockquote><p><a href="https://ask.wireshark.org/questions/28909/no-outgoing-packets">https://ask.wireshark.org/questions/28909/no-outgoing-packets</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47982" class="comments-container"><span id="47994"></span><div id="comment-47994" class="comment"><div id="post-47994-score" class="comment-score"></div><div class="comment-text"><p>As a test I also tried the same on a our Lab PC that is also Windows 7 with Firewall and AV disabled. this also gives the same result.</p><p>Still have to test the removal of some vpn adapters that are active on both test system.</p></div><div id="comment-47994-info" class="comment-info"><span class="comment-age">(25 Nov '15, 13:40)</span> <span class="comment-user userinfo">BartS</span></div></div><span id="47995"></span><div id="comment-47995" class="comment"><div id="post-47995-score" class="comment-score"></div><div class="comment-text"><p>Is this an open wifi network or do you have to decrypt it in Wireshark?</p></div><div id="comment-47995-info" class="comment-info"><span class="comment-age">(25 Nov '15, 13:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="48020"></span><div id="comment-48020" class="comment"><div id="post-48020-score" class="comment-score"></div><div class="comment-text"><p>This is a WPA2/AES network I am connected to.</p><p>Done some additional troubleshooting, and removed the vpn interfaces as well. =&gt; still no improvement. Solution=&gt; just installed a Linux laptop with Wireshark on it. Now I see all the MDNS traffic.</p><p>This gives me some trust issues with the captures I am taking on my windows laptop.</p></div><div id="comment-48020-info" class="comment-info"><span class="comment-age">(27 Nov '15, 03:56)</span> <span class="comment-user userinfo">BartS</span></div></div><span id="48027"></span><div id="comment-48027" class="comment"><div id="post-48027-score" class="comment-score"></div><div class="comment-text"><blockquote><p>just installed a Linux laptop with Wireshark on it. Now I see all the MDNS traffic.</p></blockquote><p>O.K. then I guess it's related to some software on your Windows system.</p><blockquote><p>This gives me some trust issues with the captures I am taking on my windows laptop.</p></blockquote><p>Well, yes. Capturing should be done on a 'trusted' system, known to work. What you can do is to run Kali Linux (or any other distribution) from a USB flash drive.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-48027-info" class="comment-info"><span class="comment-age">(27 Nov '15, 08:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47982" class="comment-tools"></div><div class="clear"></div><div id="comment-47982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

