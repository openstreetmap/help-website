+++
type = "question"
title = "PC randomly responds to other devices packets with an &quot;ICMP redirect&quot;"
description = '''I have an HP laptop that I use for Wireshark that randomly responds to packets for other devices with ICMP redirects. It only happens when Wireshark is running. I used another Wireshark PC to capture it coming from the HP PC. The redirects even indicate the correct IP and MAC destination in the pack...'''
date = "2013-03-18T21:22:00Z"
lastmod = "2013-03-20T09:39:00Z"
weight = 19629
keywords = [ "redirect", "icmp" ]
aliases = [ "/questions/19629" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [PC randomly responds to other devices packets with an "ICMP redirect"](/questions/19629/pc-randomly-responds-to-other-devices-packets-with-an-icmp-redirect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19629-score" class="post-score" title="current number of votes">0</div><span id="post-19629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an HP laptop that I use for Wireshark that randomly responds to packets for other devices with ICMP redirects. It only happens when Wireshark is running. I used another Wireshark PC to capture it coming from the HP PC. The redirects even indicate the correct IP and MAC destination in the packet. It just feels like telling the originator he was right, but send it again.....</p><p>I am running Win Vista 32 bit on this laptop. It was on an older Wireshark install which I uninstalled as well as WinPcap and installed the latest and still it happens.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-redirect" rel="tag" title="see questions tagged &#39;redirect&#39;">redirect</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '13, 21:22</strong></p><img src="https://secure.gravatar.com/avatar/e8523a26aeab130222d150e02974659c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="azmtnbike&#39;s gravatar image" /><p><span>azmtnbike</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="azmtnbike has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Mar '13, 21:24</strong> </span></p></div></div><div id="comments-container-19629" class="comments-container"><span id="19630"></span><div id="comment-19630" class="comment"><div id="post-19630-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you could upload a capture file to www.cloudshark.org so we could look at what's happening. Be careful that your file doesn't contain confidential data.</p></div><div id="comment-19630-info" class="comment-info"><span class="comment-age">(18 Mar '13, 22:18)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-19629" class="comment-tools"></div><div class="clear"></div><div id="comment-19629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19635"></span>

<div id="answer-container-19635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19635-score" class="post-score" title="current number of votes">1</div><span id="post-19635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess that fact that you capture in promiscuous mode causes packets to be delivered to the network stack that aren't expected there (not the right destination IP address). The network stack assumes the MAC address filter of the hardware would have filtered out frames not destined for this interface, thus decides to help the sender with the information it has on the destination host. I think it's a Vista 'feature' to behave this way regardless of the promiscuous mode of the interface.</p><p>Two things you can do:</p><ol><li>don't capture in promiscuous mode.</li><li>disable the specific ICMP redirect option in the network settings.</li></ol><p>I would go for option 2. A normal host shouldn't be bothered with this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '13, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19635" class="comments-container"></div><div id="comment-tools-19635" class="comment-tools"></div><div class="clear"></div><div id="comment-19635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19641"></span>

<div id="answer-container-19641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19641-score" class="post-score" title="current number of votes">0</div><span id="post-19641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Windows (actually any OS) will/should send an ICMP redirect (only) if <strong>IP Forwarding</strong> is enabled. So I guess, you have two (or more) interfaces in your laptop (e.g. Ethernet and WLAN) and both are active while you capture packets. In that case your OS will send an ICMP redirect if it receives a packet that could be routed differently (according to its own routing table).</p><p>Please check if you have multiple interfaces (ipconfig /all) <strong>and</strong> if IP Forwarding is enabled (please google it). If so, please disable one interface while you capture packets or disable IP Forwarding.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '13, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19641" class="comments-container"><span id="19668"></span><div id="comment-19668" class="comment"><div id="post-19668-score" class="comment-score"></div><div class="comment-text"><p>No luck. I checked and IP forwarding is not enabled. I do have a wired and wireless adapter, but the wireless is turned off.<br />
</p><p>I turned of ICMP redirects in the registry, but still I get them.</p><p>And if I don't capture in promiscuous mode, I can't see the traffic that I need.</p><p>Any other ideas before I make this a Linux or Win 7 machine?</p><p>Thanks for the input so far.</p><p>Jon</p></div><div id="comment-19668-info" class="comment-info"><span class="comment-age">(19 Mar '13, 23:30)</span> <span class="comment-user userinfo">azmtnbike</span></div></div><span id="19689"></span><div id="comment-19689" class="comment"><div id="post-19689-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I turned of ICMP redirects in the registry, but still I get them.</p></blockquote><p>did you reboot the Laptop?</p><blockquote><p>Any other ideas before I make this a Linux or Win 7 machine?</p></blockquote><p>Can you please post the output of the following commands?</p><ul><li><code>ipconfig /all</code><br />
</li><li><code>reg query HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters</code></li></ul></div><div id="comment-19689-info" class="comment-info"><span class="comment-age">(20 Mar '13, 09:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-19641" class="comment-tools"></div><div class="clear"></div><div id="comment-19641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

