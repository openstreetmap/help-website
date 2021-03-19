+++
type = "question"
title = "Public IP addressed datagram within private IP addressed datagram?"
description = '''We are running an OpenSim server on our network to mess around with - default port is UDP 9000. We are seeing packets that don&#x27;t make a lot of sense to us....even after hours of research. I found that PCLI will automatically show up on anything transmitting from port 9000 (UDPcast). Within that, the...'''
date = "2014-10-29T12:33:00Z"
lastmod = "2014-11-02T04:19:00Z"
weight = 37444
keywords = [ "pcli", "udpcast" ]
aliases = [ "/questions/37444" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Public IP addressed datagram within private IP addressed datagram?](/questions/37444/public-ip-addressed-datagram-within-private-ip-addressed-datagram)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37444-score" class="post-score" title="current number of votes">0</div><span id="post-37444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are running an OpenSim server on our network to mess around with - default port is UDP 9000. We are seeing packets that don't make a lot of sense to us....even after hours of research.</p><p>I found that PCLI will automatically show up on anything transmitting from port 9000 (UDPcast). Within that, there is an IPv4 header that shows two seemingly random public IP addresses well outside of our public range (scr &amp; dst). It contains a typical data segment.</p><p>Above that though, where I would expect to find it, is the typical IP datagram, with the correct private IP addresses and ports (192.168.x.x src &amp; dst).</p><p>The inside (public) IPv4 datagram includes the protocol "Wideband Expak" -- I can't find any literature on what this is....every search just leads me to lists of IP protocols that includes this in the list, nothing more.<br />
</p><p>Also - what gives with the public IP addresses? A lot of the traffic surrounding these particular packets is multicast....and I read some on UDPcast, but this doesn't seem to fit the protocol.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcli" rel="tag" title="see questions tagged &#39;pcli&#39;">pcli</span> <span class="post-tag tag-link-udpcast" rel="tag" title="see questions tagged &#39;udpcast&#39;">udpcast</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '14, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/1841804122cc8042fd77a88bc72b55f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dm123&#39;s gravatar image" /><p><span>dm123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dm123 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37444" class="comments-container"><span id="37458"></span><div id="comment-37458" class="comment"><div id="post-37458-score" class="comment-score"></div><div class="comment-text"><p>It's hard to follow your explanations without a sample capture file. Can you please upload a sample capture file (google drive, dropbox, cloudshark.org) and post the link here?</p></div><div id="comment-37458-info" class="comment-info"><span class="comment-age">(30 Oct '14, 04:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="37463"></span><div id="comment-37463" class="comment"><div id="post-37463-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/221f46219695">https://www.cloudshark.org/captures/221f46219695</a></p><p>Never knew about this site before...thanks!</p></div><div id="comment-37463-info" class="comment-info"><span class="comment-age">(30 Oct '14, 07:28)</span> <span class="comment-user userinfo">dm123</span></div></div><span id="37464"></span><div id="comment-37464" class="comment"><div id="post-37464-score" class="comment-score"></div><div class="comment-text"><p>Wireshark dissects UDP and TCP based protocols on the basis of ports used. In your case the packet is interpreted as PCLI but it's not PCLI so the dissection is completly bogus. Try configure the PCLI port(to zero) or do "decode as" and specify the protocol that is actually carried in the UDP message or dissect as data.</p></div><div id="comment-37464-info" class="comment-info"><span class="comment-age">(30 Oct '14, 07:55)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="37465"></span><div id="comment-37465" class="comment"><div id="post-37465-score" class="comment-score"></div><div class="comment-text"><p><span>@Anders</span> -- I wasn't so concerned with the PCLI as I was the public IP addresses that seemed to be wrapped in the private IPs.... for now I am thinking that is part of the UDPcast protocol....but I can't confirm since I can't find info about it</p></div><div id="comment-37465-info" class="comment-info"><span class="comment-age">(30 Oct '14, 08:00)</span> <span class="comment-user userinfo">dm123</span></div></div></div><div id="comment-tools-37444" class="comment-tools"></div><div class="clear"></div><div id="comment-37444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37488"></span>

<div id="answer-container-37488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37488-score" class="post-score" title="current number of votes">1</div><span id="post-37488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>We are running an OpenSim server on our network to mess around with - default port is UDP 9000.</p></blockquote><p>There is a LUA dissector for the OpenSim UDP protocol.</p><blockquote><p><a href="http://opensimulator.org/wiki/LLUDP_Dissector">http://opensimulator.org/wiki/LLUDP_Dissector</a></p></blockquote><p>Please try that to decode your packets.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '14, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37488" class="comments-container"><span id="37504"></span><div id="comment-37504" class="comment"><div id="post-37504-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt</span> -- that seems to have worked quite well.<br />
</p><p>The dissector completely reframed the packets and there are no longer the dual IP addresses. I assume then, that the LLUDP protocol has a larger header than the norm, and Wireshark read it that the extra binary made it appear that there was another IP datagram encapsulated in each packet.</p><p>Thanks for the help!</p></div><div id="comment-37504-info" class="comment-info"><span class="comment-age">(31 Oct '14, 05:16)</span> <span class="comment-user userinfo">dm123</span></div></div><span id="37534"></span><div id="comment-37534" class="comment"><div id="post-37534-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and Wireshark read it that the extra binary made it appear that there was another IP datagram encapsulated in each packet.</p></blockquote><p>actually the problem is, that Wireshark dissected the frames as PCLI, based on the UDP port 9000, which will give random results, because the data is not structured according to PCLI.</p></div><div id="comment-37534-info" class="comment-info"><span class="comment-age">(02 Nov '14, 04:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37488" class="comment-tools"></div><div class="clear"></div><div id="comment-37488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37469"></span>

<div id="answer-container-37469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37469-score" class="post-score" title="current number of votes">0</div><span id="post-37469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's not much ready made information available, but a little searching reviled this:</p><p>An textual <a href="https://www.udpcast.linux.lu/pipermail/udpcast/2005-December/000436.html">description</a> of the protocol</p><p>The protocol spec (as in <a href="http://anonscm.debian.org/cgit/collab-maint/udpcast.git/tree/udpc-protoc.h">source code</a>)</p><p>A (very) quick glance shows no IP addresses in there other than multicast (obviously). Note that scoping rules for multicast addresses are different than unicast addresses.</p><p>It would be a nice project to create an Wireshark dissector for it. An enhancement request (with ref to this post) would be in order.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '14, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-37469" class="comments-container"></div><div id="comment-tools-37469" class="comment-tools"></div><div class="clear"></div><div id="comment-37469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

