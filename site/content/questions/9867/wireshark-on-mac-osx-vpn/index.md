+++
type = "question"
title = "Wireshark on MAC OSX VPN"
description = '''I am troubleshooting dns issues with apple products on our corporate network. We are seeing a problem where windows users can resolve short-name dns just fine but users on apple products can not (Iphone, Ipad, Mac). To start I am troubleshooting with a mac, but I am not seeing any packets go across ...'''
date = "2012-03-30T09:10:00Z"
lastmod = "2012-03-30T16:09:00Z"
weight = 9867
keywords = [ "osx", "mac", "vpn", "wireshark" ]
aliases = [ "/questions/9867" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark on MAC OSX VPN](/questions/9867/wireshark-on-mac-osx-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9867-score" class="post-score" title="current number of votes">0</div><span id="post-9867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am troubleshooting dns issues with apple products on our corporate network. We are seeing a problem where windows users can resolve short-name dns just fine but users on apple products can not (Iphone, Ipad, Mac). To start I am troubleshooting with a mac, but I am not seeing any packets go across the VPN when I try to start a wireshark from it..</p><p>From the if config command I've gathered via ip that the tunnel is being generated off of the interface "utun1". When I start a packet capture off of that interface I see no packets, I've generated traffic by pinging devices on the corporate network... etc, I am not seeing anything.</p><p>Similarly, I have tried generating a packet capture off of the en0 interface, which is the interface my ethernet cord is plugged into. I see plenty of traffic go through, but nothing through the VPN. I can see dns queries come into the DNS server on our corporate network from my computer when I am attached to the vpn, but my local wireshark capture does not see packets going out to the DNS server.</p><p>I was wondering if anyone knows exactly how this works on OSX. Is it possible that everything is being encapsulated before it hits en0 or the VPN interface, and thus, no packets are displayed because they are already tunneled?</p><p>I am running Mac OSX Lion version 10.7.3</p><p>Thanks for your help and time!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '12, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/f7fdb608a4c17f8c7242219496ec18d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PhillSimonds&#39;s gravatar image" /><p><span>PhillSimonds</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PhillSimonds has no accepted answers">0%</span></p></div></div><div id="comments-container-9867" class="comments-container"></div><div id="comment-tools-9867" class="comment-tools"></div><div class="clear"></div><div id="comment-9867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9871"></span>

<div id="answer-container-9871" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9871-score" class="post-score" title="current number of votes">0</div><span id="post-9871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>From the if config command I've gathered via ip that the tunnel is being generated off of the interface "utun1".</p></blockquote><p>Are you certain of that? Is there also an interface named, for example, <code>ppp0</code>? If so, what happens if you try to capture on the <code>ppp0</code> interface? Apple's own VPN software sends traffic over a PPP interface such as <code>ppp0</code>; I don't know what other VPN software such as the Cisco VPN software does.</p><blockquote><p>Similarly, I have tried generating a packet capture off of the en0 interface, which is the interface my ethernet cord is plugged into. I see plenty of traffic go through, but nothing through the VPN. I can see dns queries come into the DNS server on our corporate network from my computer when I am attached to the vpn, but my local wireshark capture does not see packets going out to the DNS server.</p></blockquote><p>Again, with Apple's VPN software, the VPN traffic will show up as, for example, ESP traffic on the Ethernet or Airport interface, so it'll already be encapsulated. I don't know what other VPN software does, but it's probably similar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '12, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9871" class="comments-container"><span id="9872"></span><div id="comment-9872" class="comment"><div id="post-9872-score" class="comment-score"></div><div class="comment-text"><p>I am seeing this output from the ifconfig command</p><p>utun1: flags=8051&lt;up,pointopoint,running,multicast&gt; mtu 1280 inet 10.105.135.224 --&gt; 10.105.135.224 netmask 0xffffff00</p><p>This and en0 are the only two interfaces that show IP addresses off of them. I am using Apple's built in VPN Client found under network preferences, but It is conecting to a cisco ASA and using Cisco IPSEC as its tunneling protocol. I don't have a ppp interface being displayed under the ifconfig command or in the interface list under wireshark... I have a p2p0 but as I understand it, that is a completely different tunneling protocol then IPSEC.</p><p>We resolved the DNS issue, so no further troubleshooting is needed. Thank you for all of your input, hopefully this will help someone else.</p><p>Thanks!</p></div><div id="comment-9872-info" class="comment-info"><span class="comment-age">(30 Mar '12, 13:22)</span> <span class="comment-user userinfo">PhillSimonds</span></div></div><span id="9873"></span><div id="comment-9873" class="comment"><div id="post-9873-score" class="comment-score">1</div><div class="comment-text"><p>I seem to remember that somebody once noted that, on OS X, Cisco VPNs don't make the VPN traffic available for sniffing, so it's fortunate that you were able to debug the problem without a traffic capture. I also seem to remember that the <code>utun</code> devices don't carry the decrypted traffic, just some sort of control traffic, and that the decrypted traffic passes to the IP stack without passing through a pseudo-interface, making it un-sniffable.</p></div><div id="comment-9873-info" class="comment-info"><span class="comment-age">(30 Mar '12, 16:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9871" class="comment-tools"></div><div class="clear"></div><div id="comment-9871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

