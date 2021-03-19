+++
type = "question"
title = "I have a virtual machine with VPN - how can i split traffic in wireshark between my host and VM?"
description = '''So i have a virtual machine and a VPN installed on it. Network is set to NAT. To see that everything works as intended and that my VM with my real IP isn&#x27;t connecting anywhere but VPN, i want to check traffic with in host wireshark, but because there are 2 machines connecting with my IP(host and VM)...'''
date = "2014-01-09T06:49:00Z"
lastmod = "2014-01-09T09:04:00Z"
weight = 28730
keywords = [ "vpn", "packets", "wireshark" ]
aliases = [ "/questions/28730" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I have a virtual machine with VPN - how can i split traffic in wireshark between my host and VM?](/questions/28730/i-have-a-virtual-machine-with-vpn-how-can-i-split-traffic-in-wireshark-between-my-host-and-vm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28730-score" class="post-score" title="current number of votes">0</div><span id="post-28730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So i have a virtual machine and a VPN installed on it. Network is set to NAT. To see that everything works as intended and that my VM with my real IP isn't connecting anywhere but VPN, i want to check traffic with in host wireshark, but because there are 2 machines connecting with my IP(host and VM)source IP is the same. So i wanted to ask is it possible somehow that wireshark would show from where this connection originated? Host or VM?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '14, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/b3baccd41682b4757c68cadc9061a3ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="numsta&#39;s gravatar image" /><p><span>numsta</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="numsta has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jan '14, 06:50</strong> </span></p></div></div><div id="comments-container-28730" class="comments-container"></div><div id="comment-tools-28730" class="comment-tools"></div><div class="clear"></div><div id="comment-28730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28736"></span>

<div id="answer-container-28736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28736-score" class="post-score" title="current number of votes">0</div><span id="post-28736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So i wanted to ask is it possible somehow that wireshark would show from where this connection originated? Host or VM?</p></blockquote><p>There is no reliable way to differentiate traffic of the host and the VM, if you are looking at traffic from the outside. There are however 'indicators' that might be good enough in some cases. Keep in mind, that the NAT implementation of the your Hypervisor might handle things differently (as described below). If that is the case, you can't use some (or all) of those 'indicators'.</p><ul><li><strong>TTL:</strong> The TTL of the packets should be different, -1 for the VM compared to the host. Maybe the TTL <strong>is</strong> a reliable way. It depends on the NAT implementation of the Hypervisor !?!</li><li><strong>IP ID:</strong> the IP ID range will be different between the host and VM</li><li><strong>Source port range:</strong> same as IP ID</li><li><strong>TCP MSS</strong> and <strong>window size:</strong> If the host and the VM use different operating systems, these values might be different as well.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '14, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jan '14, 09:19</strong> </span></p></div></div><div id="comments-container-28736" class="comments-container"></div><div id="comment-tools-28736" class="comment-tools"></div><div class="clear"></div><div id="comment-28736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

