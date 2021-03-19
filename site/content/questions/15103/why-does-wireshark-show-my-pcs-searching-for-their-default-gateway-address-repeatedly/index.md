+++
type = "question"
title = "Why Does Wireshark show my pc&#x27;s searching for their default gateway address repeatedly?"
description = '''Why Does Wireshark show my pc&#x27;s searching for their default gateway address repeatedly? It seems that when I do a Traceroute the first hop is going to the vlan address not the default gateway being passed out by the DHCP server. Every PC in the network is ARP broadcasting for it&#x27;s default gateway ad...'''
date = "2012-10-19T05:37:00Z"
lastmod = "2012-10-20T07:53:00Z"
weight = 15103
keywords = [ "default", "arp", "gateway", "wireshark" ]
aliases = [ "/questions/15103" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why Does Wireshark show my pc's searching for their default gateway address repeatedly?](/questions/15103/why-does-wireshark-show-my-pcs-searching-for-their-default-gateway-address-repeatedly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15103-score" class="post-score" title="current number of votes">0</div><span id="post-15103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why Does Wireshark show my pc's searching for their default gateway address repeatedly? It seems that when I do a Traceroute the first hop is going to the vlan address not the default gateway being passed out by the DHCP server. Every PC in the network is ARP broadcasting for it's default gateway address. The VLAN address is on the same physical device as the default gateway. Is this because the default gateway should be the VLAN address not the physical port address? Is this possibly due to redundancy and should these arp broadcasts be going on?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-default" rel="tag" title="see questions tagged &#39;default&#39;">default</span> <span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-gateway" rel="tag" title="see questions tagged &#39;gateway&#39;">gateway</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '12, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/80b9abef2d8e359d95dc696cc500546f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CW30&#39;s gravatar image" /><p><span>CW30</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CW30 has no accepted answers">0%</span></p></div></div><div id="comments-container-15103" class="comments-container"><span id="15116"></span><div id="comment-15116" class="comment"><div id="post-15116-score" class="comment-score"></div><div class="comment-text"><p>You might need to include a more detailed description of your setup. What do you mean by "VLAN address"? VLANs are layer 2 objects that do neither have an IP address nor a MAC address in itself. You can have a system being part of a VLAN and having an address, but that is not what I'd call a "VLAN address".</p><p>Anyway, it is pretty normal for ARP requests to be repeated every once in a while, it just shouldn't be too often. Since you did not say what the frequency of those packets is I can't tell you if it's bad or not.</p></div><div id="comment-15116-info" class="comment-info"><span class="comment-age">(20 Oct '12, 07:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-15103" class="comment-tools"></div><div class="clear"></div><div id="comment-15103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

