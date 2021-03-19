+++
type = "question"
title = "Fragmentation at source why?"
description = '''In my scenario it’s a flat network where couple of host is connected to a switch belonging to same VLAN. The MTU of the link is 1500 and also the Solaris Linux v6 hosts are also configured with this setting. But in fact in traces I could see that they send fragmented IP packets to hosts in the same ...'''
date = "2017-01-24T13:35:00Z"
lastmod = "2017-01-24T14:06:00Z"
weight = 59025
keywords = [ "fragmentation" ]
aliases = [ "/questions/59025" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fragmentation at source why?](/questions/59025/fragmentation-at-source-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59025-score" class="post-score" title="current number of votes">0</div><span id="post-59025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my scenario it’s a flat network where couple of host is connected to a switch belonging to same VLAN. The MTU of the link is 1500 and also the Solaris Linux v6 hosts are also configured with this setting. But in fact in traces I could see that they send fragmented IP packets to hosts in the same LAN.</p><p>From my understanding the upper layer protocols like TCP or UDP send data to IP layer which then creates an IP packet which matches the size of the outgoing link. But in capture I can see that the IP layer instead of building packets which matches the MTU, it fragments. What could be the reason for this?</p><p>Is there any implementation in which the upper layer tells IP to always fragment :(?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '17, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/5de3f05c3183608f6986dd68fa7eb0f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="soochi&#39;s gravatar image" /><p><span>soochi</span><br />
<span class="score" title="57 reputation points">57</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="soochi has no accepted answers">0%</span></p></div></div><div id="comments-container-59025" class="comments-container"><span id="59027"></span><div id="comment-59027" class="comment"><div id="post-59027-score" class="comment-score"></div><div class="comment-text"><p>There might be some reasons. Can you share us a trace?</p></div><div id="comment-59027-info" class="comment-info"><span class="comment-age">(24 Jan '17, 13:41)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="59031"></span><div id="comment-59031" class="comment"><div id="post-59031-score" class="comment-score"></div><div class="comment-text"><p>for example if i ping a host with packet size exceeding the MTU, ip will fragment it (unless DF set). But how/why does the upper layer protocol influence this?</p></div><div id="comment-59031-info" class="comment-info"><span class="comment-age">(24 Jan '17, 13:54)</span> <span class="comment-user userinfo">soochi</span></div></div></div><div id="comment-tools-59025" class="comment-tools"></div><div class="clear"></div><div id="comment-59025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59029"></span>

<div id="answer-container-59029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59029-score" class="post-score" title="current number of votes">0</div><span id="post-59029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Fragmentation occurs when the size of the packet exceeds the MTU. If the upper layer protocol, UDP for example, hands IP a datagram that, combined with the IP header, would result in an IP packet larger than the interface MTU, the packet will be fragmented by the IP layer. How much data is being handed to IP from the upper layers? A capture file might be more helpful to understand what's going on. You can post it to <a href="https://www.cloudshark.org/">cloudshark</a> or some other place and provide the link in your edited question.</p><p>Also, what platform are you running on and is PMTUD enabled or not? On some platforms, <em>"<a href="http://www.cisco.com/c/en/us/support/docs/additional-legacy-protocols/ms-windows-networking/13709-38.html">When PMTU discovery is disabled, a MTU of 576 bytes is used for all non-local destination IP addresses.</a>"</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '17, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '17, 13:52</strong> </span></p></div></div><div id="comments-container-59029" class="comments-container"><span id="59032"></span><div id="comment-59032" class="comment"><div id="post-59032-score" class="comment-score"></div><div class="comment-text"><p>what i basically wanto to know is if ...</p><p>when the upper layer protocol handles a junk of data to IP, which then packetises it as per the link level MTU</p><p>or...</p><p>if the given junk of data is put into one packet and then fragmented as per the link MTU</p></div><div id="comment-59032-info" class="comment-info"><span class="comment-age">(24 Jan '17, 14:00)</span> <span class="comment-user userinfo">soochi</span></div></div><span id="59034"></span><div id="comment-59034" class="comment"><div id="post-59034-score" class="comment-score">1</div><div class="comment-text"><p>When IP receives an upper-layer UDP datagram or TCP segment, if the size of that data exceeds the MTU, then IP will fragment it as needed so that no fragment exceeds the MTU size.</p><p>Perhaps a review of <a href="https://tools.ietf.org/html/rfc791">RFC791</a> would also help?</p></div><div id="comment-59034-info" class="comment-info"><span class="comment-age">(24 Jan '17, 14:06)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-59029" class="comment-tools"></div><div class="clear"></div><div id="comment-59029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

