+++
type = "question"
title = "What does ICMP | Redirect | (redirect for host) mean?"
description = '''I&#x27;m trying to troubleshoot a strange problem with some of my switches dropping pings. When the problem happens I get these black/green lines that read ICMP | Redirect | (redirect for host) in Wireshark. I don&#x27;t see these when the network is running normally. In the screenshot below:  172.16.1.1 (me)...'''
date = "2014-08-27T21:13:00Z"
lastmod = "2014-08-28T17:26:00Z"
weight = 35826
keywords = [ "redirect", "icmp", "wireshark" ]
aliases = [ "/questions/35826" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What does ICMP | Redirect | (redirect for host) mean?](/questions/35826/what-does-icmp-redirect-redirect-for-host-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35826-score" class="post-score" title="current number of votes">0</div><span id="post-35826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to troubleshoot a strange problem with some of my switches dropping pings. When the problem happens I get these black/green lines that read ICMP | Redirect | (redirect for host) in Wireshark. I don't see these when the network is running normally.</p><p>In the screenshot below:</p><ul><li>172.16.1.1 (me) Wireshark Laptop</li><li>172.16.0.2 Internet Gateway</li><li>172.16.7.254 Core switch gateway for 172 subnet/vlan</li><li>10.236.67.12 Suspect switch</li></ul><p><img src="http://i58.tinypic.com/10s9feu.jpg" title="screenshot" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-redirect" rel="tag" title="see questions tagged &#39;redirect&#39;">redirect</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '14, 21:13</strong></p><img src="https://secure.gravatar.com/avatar/9728165378c367e74698331381869dbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aj-admin&#39;s gravatar image" /><p><span>aj-admin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aj-admin has no accepted answers">0%</span></p></img></div></div><div id="comments-container-35826" class="comments-container"></div><div id="comment-tools-35826" class="comment-tools"></div><div class="clear"></div><div id="comment-35826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35827"></span>

<div id="answer-container-35827" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35827-score" class="post-score" title="current number of votes">1</div><span id="post-35827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aj-admin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://tools.ietf.org/html/rfc792">RFC 792</a>, "Internet Control Message Protocol" says:</p><pre><code>Redirect Message

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Type      |     Code      |          Checksum             |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                 Gateway Internet Address                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |      Internet Header + 64 bits of Original Data Datagram      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   IP Fields:

   Destination Address

      The source network and address of the original datagram&#39;s data.

   ICMP Fields:

   Type

      5

   Code

      0 = Redirect datagrams for the Network.

      1 = Redirect datagrams for the Host.

      2 = Redirect datagrams for the Type of Service and Network.

      3 = Redirect datagrams for the Type of Service and Host.

   Checksum

      The checksum is the 16-bit ones&#39;s complement of the one&#39;s
      complement sum of the ICMP message starting with the ICMP Type.
      For computing the checksum , the checksum field should be zero.
      This checksum may be replaced in the future.

   Gateway Internet Address

      Address of the gateway to which traffic for the network specified
      in the internet destination network field of the original
      datagram&#39;s data should be sent.

   Internet Header + 64 bits of Data Datagram

      The internet header plus the first 64 bits of the original
      datagram&#39;s data.  This data is used by the host to match the
      message to the appropriate process.  If a higher level protocol
      uses port numbers, they are assumed to be in the first 64 data
      bits of the original datagram&#39;s data.

   Description

      The gateway sends a redirect message to a host in the following
      situation.  A gateway, G1, receives an internet datagram from a
      host on a network to which the gateway is attached.  The gateway,
      G1, checks its routing table and obtains the address of the next
      gateway, G2, on the route to the datagram&#39;s internet destination
      network, X.  If G2 and the host identified by the internet source
      address of the datagram are on the same network, a redirect
      message is sent to the host.  The redirect message advises the
      host to send its traffic for network X directly to gateway G2 as
      this is a shorter path to the destination.  The gateway forwards
      the original datagram&#39;s data to its internet destination.

      For datagrams with the IP source route options and the gateway
      address in the destination address field, a redirect message is
      not sent even if there is a better route to the ultimate
      destination than the next address in the source route.

      Codes 0, 1, 2, and 3 may be received from a gateway.</code></pre><p>So the ICMP Redirect packet should contain the "Internet Header + 64 bits of Data Datagram" of a packet that was sent to a router in order to get it one routing hop closer to the host whose IP address appears as the destination address in the "Internet Header". However, the router to which it was sent thinks it isn't the right router, and thinks that some <em>other</em> router provides a better route to that particular host, so it's saying "pick another route" ("redirect") "for packets to that particular host ("for host"), and provides the IP address of the router to which the packet <em>should</em> have been sent in order to get it to the host in question.</p><p>I.e., the host that sent the packet <em>should</em> have routed it to 172.16.7.254 rather than to the host with the MAC address of 00:26?b9:68:4f:52.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '14, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35827" class="comments-container"></div><div id="comment-tools-35827" class="comment-tools"></div><div class="clear"></div><div id="comment-35827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35830"></span>

<div id="answer-container-35830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35830-score" class="post-score" title="current number of votes">1</div><span id="post-35830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ICMP redirects are messages telling a host to deliver the next packet for the same destination IP address to a different router. This can happen for two reasons:</p><ol><li>There are two routers in the subnet, the first being the default gateway. The host sends a packet to a remote network which is only reachable through the second router. Instead of sending it to that router the host sends it to its default gateway, which forwards it to the correct (second) router, and tells the client to sent it to that router the next time.</li></ol><p>Solution: add static route to host to tell it to use the second router for that specific destination</p><ol><li>The host has a bad subnet mask configured, so when trying to send a packet to a node in the same subnet it sends the packet to the default gateway instead. That happens when the subnet mask is too narrow, forcing the host to think that it cannot reach the target directly.</li></ol><p>Solution: fix the bad subnet mask setting on the host</p><p>By the way, ICMP Redirects are usually not accepted by modern operating systems, because if they would it would be easy to do a man-in-the-middle attack (at least for one packet direction). An attacker could tell hosts to send packets over his own system next time, and reading whats in the packet before passing it on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '14, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35830" class="comments-container"><span id="35854"></span><div id="comment-35854" class="comment"><div id="post-35854-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much for the information - it has been helpful. Problem is not fixed yet so I'll update with more info when it is.</p></div><div id="comment-35854-info" class="comment-info"><span class="comment-age">(28 Aug '14, 17:26)</span> <span class="comment-user userinfo">aj-admin</span></div></div></div><div id="comment-tools-35830" class="comment-tools"></div><div class="clear"></div><div id="comment-35830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

