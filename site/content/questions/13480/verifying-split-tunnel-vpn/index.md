+++
type = "question"
title = "Verifying Split Tunnel VPN"
description = '''I have a site-to-site VPN tunnel with a Cisco ASA connected to an Adtran Netvanta. We think split tunneling is configured properly, but it would be nice to know for sure. Looking for guidance on how to confirm this using Wireshark...if possible. Any assistance would be greatly appreciated!'''
date = "2012-08-08T15:44:00Z"
lastmod = "2012-08-08T21:16:00Z"
weight = 13480
keywords = [ "vpn" ]
aliases = [ "/questions/13480" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Verifying Split Tunnel VPN](/questions/13480/verifying-split-tunnel-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13480-score" class="post-score" title="current number of votes">0</div><span id="post-13480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a site-to-site VPN tunnel with a Cisco ASA connected to an Adtran Netvanta. We think split tunneling is configured properly, but it would be nice to know for sure. Looking for guidance on how to confirm this using Wireshark...if possible. Any assistance would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '12, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/c2c2c9e540ff39762fdbd0320ab98830?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sotelbrad&#39;s gravatar image" /><p><span>sotelbrad</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sotelbrad has no accepted answers">0%</span></p></div></div><div id="comments-container-13480" class="comments-container"></div><div id="comment-tools-13480" class="comment-tools"></div><div class="clear"></div><div id="comment-13480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13481"></span>

<div id="answer-container-13481" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13481-score" class="post-score" title="current number of votes">1</div><span id="post-13481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sotelbrad has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>besides looking at the configuration (which I would prefer), you could capture traffic <strong>between</strong> the two VPN devices and check if there is any <strong>unencrypted traffic</strong> for networks that <strong>should be</strong> encrypted. In your setup, <strong>unencrypted</strong> means to see any traffic for the "protected/Internal" networks on the External side, as that means the traffic is not routed into the VPN tunnel.</p><blockquote><p><code>Internal -- Cisco ASA ---- External ---- Netvanta --- Internal</code><br />
</p></blockquote><p>Capture somewhere in the External Network. Please take a look at the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Capture Setup</a> to learn how to do that.</p><p>Then use this <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a>:</p><blockquote><p><code>net 10.1.0.0/16 or net 192.168.1.0/24</code><br />
</p></blockquote><p>Please replace the networks with whatever network <strong>should</strong> be encrypted (routed into the VPN tunnel).</p><p>Start Wireshark (with the capture filter) and then do some ping/tcp/udp tests to those networks. You should <strong>NOT</strong> see any traffic in Wireshark, if the VPN tunnel works properly.</p><p>Another option would be to <a href="http://www.cisco.com/en/US/products/ps6120/products_tech_note09186a0080a9edd6.shtml">capture on the ASA</a> itself, however that includes the risk to capture traffic before it gets encrypted, if not done properly. I recommend to capture off box, to be really sure!</p><p>Yet another option would be the <a href="https://supportforums.cisco.com/docs/DOC-5796">ASA packet tracer link#1</a> <a href="http://www.networkoc.net/blog/?p=151">/ link#2</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '12, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '12, 16:43</strong> </span></p></div></div><div id="comments-container-13481" class="comments-container"><span id="13482"></span><div id="comment-13482" class="comment"><div id="post-13482-score" class="comment-score"></div><div class="comment-text"><p>Brilliant! I used the packet capture in Cisco ASDM. It appears the split tunnel is working properly since traffic on the egress/outside interface is unencrypted when browsing a web page on the public internet. Thanks for the advice, Kurt!</p></div><div id="comment-13482-info" class="comment-info"><span class="comment-age">(08 Aug '12, 21:16)</span> <span class="comment-user userinfo">sotelbrad</span></div></div></div><div id="comment-tools-13481" class="comment-tools"></div><div class="clear"></div><div id="comment-13481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

