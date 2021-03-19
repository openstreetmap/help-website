+++
type = "question"
title = "Can VPN IP visible in a local network?"
description = '''Now I am in a network of 10 devices connected to it and now Device 6 is using VPN. Is it possbile I can see the VPN IP address?'''
date = "2017-08-18T19:02:00Z"
lastmod = "2017-08-22T07:30:00Z"
weight = 63489
keywords = [ "ip", "vpn" ]
aliases = [ "/questions/63489" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can VPN IP visible in a local network?](/questions/63489/can-vpn-ip-visible-in-a-local-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63489-score" class="post-score" title="current number of votes">0</div><span id="post-63489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Now I am in a network of 10 devices connected to it and now Device 6 is using VPN. Is it possbile I can see the VPN IP address?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '17, 19:02</strong></p><img src="https://secure.gravatar.com/avatar/3f53e50244ac6674789173620f09d4cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanielRaj&#39;s gravatar image" /><p><span>DanielRaj</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanielRaj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '17, 01:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-63489" class="comments-container"><span id="63491"></span><div id="comment-63491" class="comment"><div id="post-63491-score" class="comment-score"></div><div class="comment-text"><p>Is that a wired network or a wireless one? Do you have in mind an IP address of a remote VPN server which device 6 is using to anonymize its own traffic or you have in mind device 6's IP address within the VPN?</p></div><div id="comment-63491-info" class="comment-info"><span class="comment-age">(19 Aug '17, 01:06)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="63492"></span><div id="comment-63492" class="comment"><div id="post-63492-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/145/jasper">@Jasper</a> Let me say, I'm considering a wired network (an institutional network). And let us take I am the Device 6 user, and I'm using a VPN Service application like Psiphon or Hotspot shield. Now is there a way that an network admin (for example, with a proxy installed in that network) can see the VPN IP than its original IP address ? .. and I would also want to know considering in a Wireless network.</p></div><div id="comment-63492-info" class="comment-info"><span class="comment-age">(20 Aug '17, 19:02)</span> <span class="comment-user userinfo">DanielRaj</span></div></div></div><div id="comment-tools-63489" class="comment-tools"></div><div class="clear"></div><div id="comment-63489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63495"></span>

<div id="answer-container-63495" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63495-score" class="post-score" title="current number of votes">0</div><span id="post-63495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A usual network administrator can quite easily find out that some of the machines in the network is routing some part of its traffic through a VPN tunnel. It does not depend on whether the network is wired or wireless. A mere user has limited possibilities as compared to the administrator, that's why I've asked what type of network you were using.</p><p>The address part of packets to and from the VPN server is encrypted along with the payload, so in order to find out which particular IP addres the VPN client has been assigned and which remote IP addresses is it actually visiting, the administrator would have to decrypt the VPN communication. This is not easy but I hesitate to say it is totally impossible. At least for Chinese censors it seems simpler to forbid use of VPNs than to decrypt the traffic, but that may be a red herring.</p><p>Who does know for sure is the administrator of the VPN server.</p><p>One funny point noticed by another user here - Windows 10 did, under circumstances which are not fully clear, ignore the IP routing table when routing DNS requests, and were sending them via all routers they could find in the network configuration. That way, it was possible for network administrators to see what fqdns the VPN clients were visiting. It sounded crazy to me but I could reproduce that behaviour.</p><p><strong>EDIT:</strong></p><p>1) By no means it is possible that the network administrator would know the public IP address assigned to the VPN client, i.e. the address which the remote servers see as source one.</p><p>2) It is theoretically possible that if the local network uses private addresses and the VPN by chance assigns addresses from the same private range, the VPN client machine could respond to ARP requests coming to its physical LAN interface and asking for a local IP address of another machine which matches the one assigned by the VPN to the client machine. Some stacks respond to ARP requests regardless the interface through which they come in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '17, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Aug '17, 15:50</strong> </span></p></div></div><div id="comments-container-63495" class="comments-container"><span id="63496"></span><div id="comment-63496" class="comment"><div id="post-63496-score" class="comment-score"></div><div class="comment-text"><p>Alright. How companies and IT security actually manages client VPN usage restrictions ? Do they block VPN clients by ACLs or there is a strategy to trace the VPN Clients ?</p></div><div id="comment-63496-info" class="comment-info"><span class="comment-age">(22 Aug '17, 04:39)</span> <span class="comment-user userinfo">DanielRaj</span></div></div><span id="63497"></span><div id="comment-63497" class="comment"><div id="post-63497-score" class="comment-score"></div><div class="comment-text"><p>Good question. As there are many different VPNs and many obfuscation techniques up to mimicking a regular https session (SSL over TCP port 443), I'm afraid the security device has to work with ACLs of both fqdns and IP addresses and maybe with traffic pattern analysis. However, that's just the very basic, I'm not a network security specialist.</p><p>As this is a different question from your original one, the correct way would be to post it a new one. A properly formulated question is the most important pre-requisite for a useful answer.</p><p>And if you actually seek information how to behave as a VPN client in order to avoid being spotted, I'm afraid you can do little at your side except choosing a provider of an anonymisation VPN which uses the best obfuscation strategy.</p></div><div id="comment-63497-info" class="comment-info"><span class="comment-age">(22 Aug '17, 07:30)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-63495" class="comment-tools"></div><div class="clear"></div><div id="comment-63495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

