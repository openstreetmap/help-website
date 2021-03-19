+++
type = "question"
title = "multicast-mac = the virtual MAC address that belongs to the NLB"
description = '''NLB is configured using multicast, on SRX device as follows: set interfaces ge-0/0/1 unit 0 family inet address 1.1.1.1/24 arp 1.1.1.10 multicast-mac 01:00:5e:00:00:04 Where the parameters are as follows: 1.1.1.1 = the JSRX interface IP address arp = the NLB address multicast-mac = the virtual MAC a...'''
date = "2013-11-20T08:19:00Z"
lastmod = "2013-11-21T05:57:00Z"
weight = 27170
keywords = [ "nlb" ]
aliases = [ "/questions/27170" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [multicast-mac = the virtual MAC address that belongs to the NLB](/questions/27170/multicast-mac-the-virtual-mac-address-that-belongs-to-the-nlb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27170-score" class="post-score" title="current number of votes">0</div><span id="post-27170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>NLB is configured using multicast, on SRX device as follows:</p><p>set interfaces ge-0/0/1 unit 0 family inet address 1.1.1.1/24 arp 1.1.1.10 multicast-mac 01:00:5e:00:00:04</p><p>Where the parameters are as follows:</p><pre><code>1.1.1.1 = the JSRX interface IP address
arp = the NLB address
multicast-mac = the virtual MAC address that belongs to the NLB</code></pre><p>So,the packets being captured on Wireshark with target IP 1.1.1.10 originating from the firewall should have target MAC address 01:00:5e:00:00:04 , but they do not.</p><p>Please advise.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nlb" rel="tag" title="see questions tagged &#39;nlb&#39;">nlb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/2e313fa1a63a84718c38122b0f8b732d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MASS&#39;s gravatar image" /><p><span>MASS</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MASS has no accepted answers">0%</span></p></div></div><div id="comments-container-27170" class="comments-container"></div><div id="comment-tools-27170" class="comment-tools"></div><div class="clear"></div><div id="comment-27170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27172"></span>

<div id="answer-container-27172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27172-score" class="post-score" title="current number of votes">0</div><span id="post-27172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The firewall will (most certainly) answer to packets with DESTINATION MAC 01:00:5e:00:00:04 and destination IP 1.1.1.10. So, if another system uses the IP 1.1.1.10 as default gateway you should see that MAC address as the destination address. But if the firewall itself <strong>sends</strong> something into the network, it will (most certainly) use the 'native' MAC address of its interface. At least that's how other systems work I know of.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27172" class="comments-container"><span id="27205"></span><div id="comment-27205" class="comment"><div id="post-27205-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Thanks for looking this.</p><p>As host is not directly connects to the firewall, I have a switch behind the firewall.</p><p>My understanding is Microsoft NLB works by using a virtual IP address (VIP). An ARP for VIP will result in a cluster mac address. The problem is that the cluster mac address is not used to send any traffic, sending traffic by the nodes in the cluster is done from other mac addresses.</p><p>As the switches do not know on which switch port the cluster mac address is found, it will send the packets to all ports in the VLAN. This results in that all cluster members will receive the traffic and the NLB driver on each cluster node will determine which node should handle each request.</p><p>Any thoughts?</p></div><div id="comment-27205-info" class="comment-info"><span class="comment-age">(21 Nov '13, 02:59)</span> <span class="comment-user userinfo">MASS</span></div></div><span id="27206"></span><div id="comment-27206" class="comment"><div id="post-27206-score" class="comment-score"></div><div class="comment-text"><blockquote><p>sending traffic by the nodes in the cluster is done from other mac addresses.</p></blockquote><p>as I said. And that's no problem in most environment. Why is that a problem in your environment?</p><blockquote><p>As the switches do not know on which switch port the cluster mac address is found, it will send the packets to all ports</p></blockquote><p>That's not the case, because the switch will look at the destination MAC and not the source MAC.</p></div><div id="comment-27206-info" class="comment-info"><span class="comment-age">(21 Nov '13, 03:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27211"></span><div id="comment-27211" class="comment"><div id="post-27211-score" class="comment-score"></div><div class="comment-text"><blockquote><p>As the switches do not know on which switch port the cluster mac address is found, it will send the packets to all ports in the VLAN.</p></blockquote><p>Ah, wait you mean: if some other system tries to reach the cluster IP, right? In that case the request will go to the cluster MAC address (destination) and that will indeed be flooded to all ports or all ports in the VLAN (depends on the switch config). That's how it works, if you are using a multicast MAC address (first bit of first octet set).</p><blockquote><p>This results in that all cluster members will receive the traffic and the NLB driver on each cluster node will determine which node should handle each request.</p></blockquote><p>Yes. And that is what you want, right? Otherwise NLB would not make much sense.</p><p>Sounds like you have a standard NLB setup, that works like any other NLB setup.</p><p>But maybe I don't understand your problem. If so, please be more specific in your problem description.</p></div><div id="comment-27211-info" class="comment-info"><span class="comment-age">(21 Nov '13, 05:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27172" class="comment-tools"></div><div class="clear"></div><div id="comment-27172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

