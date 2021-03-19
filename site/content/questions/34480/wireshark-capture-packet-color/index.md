+++
type = "question"
title = "Wireshark capture packet color"
description = '''I have a bunch of Apple devices and a TI CC3000 WiFi module. I made the TI device an mDNS advertiser. When I capture packets with Wireshark, I see the mDNS packets from TI are blue color (UDP color code), all other mDNS packets from other devices are Red with white text (TTL low or unexpected).  Usi...'''
date = "2014-07-08T15:29:00Z"
lastmod = "2014-07-09T10:33:00Z"
weight = 34480
keywords = [ "mdns" ]
aliases = [ "/questions/34480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture packet color](/questions/34480/wireshark-capture-packet-color)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34480-score" class="post-score" title="current number of votes">0</div><span id="post-34480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a bunch of Apple devices and a TI CC3000 WiFi module. I made the TI device an mDNS advertiser. When I capture packets with Wireshark, I see the mDNS packets from TI are blue color (UDP color code), all other mDNS packets from other devices are Red with white text (TTL low or unexpected).</p><p>Using mDNS Watcher app, I can see all Bonjour supported devices but not the TI device. Is this color code telling me something that I am missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mdns" rel="tag" title="see questions tagged &#39;mdns&#39;">mdns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '14, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/29ccfac7eaba9eaf208c68b22bb256bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lilyhack&#39;s gravatar image" /><p><span>lilyhack</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lilyhack has no accepted answers">0%</span></p></div></div><div id="comments-container-34480" class="comments-container"></div><div id="comment-tools-34480" class="comment-tools"></div><div class="clear"></div><div id="comment-34480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34483"></span>

<div id="answer-container-34483" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34483-score" class="post-score" title="current number of votes">0</div><span id="post-34483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. the color rule for "TTL low or unexpected" is this</p><blockquote><p>@TTL low or <span class="__cf_email__" data-cfemail="e5908b809d958086918081a5">[email protected]</span>( ! ip.dst == 224.0.0.0/4 &amp;&amp; ip.ttl &lt; 5 &amp;&amp; !pim) || (ip.dst == 224.0.0.0/24 &amp;&amp; ip.dst != 224.0.0.251 &amp;&amp; ip.ttl != 1 &amp;&amp; !(vrrp || carp))@[42148,0,0][60652,61680,60395]</p></blockquote><p>So, the matching rule could be</p><blockquote><p>ip.dst == 224.0.0.0/24 &amp;&amp; <strong>ip.dst != 224.0.0.251</strong> &amp;&amp; ip.ttl != 1 &amp;&amp; !(vrrp || carp)</p></blockquote><p>So, the destination address of the mDNS traffic is probably <strong>not</strong> 224.0.0.251. Is that right? If so, that could explain why you don't see the TI device with your mDNS Watcher app.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '14, 17:44</strong> </span></p></div></div><div id="comments-container-34483" class="comments-container"><span id="34484"></span><div id="comment-34484" class="comment"><div id="post-34484-score" class="comment-score"></div><div class="comment-text"><p>no, the destination address for all the mDNS traffic (including TI) is 224.0.0.251</p></div><div id="comment-34484-info" class="comment-info"><span class="comment-age">(08 Jul '14, 17:45)</span> <span class="comment-user userinfo">lilyhack</span></div></div><span id="34485"></span><div id="comment-34485" class="comment"><div id="post-34485-score" class="comment-score"></div><div class="comment-text"><p>can you post a sample capture file on <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> (or google drive or dropbox)? One frame that is marked like that, should be O.K.</p><p>EDIT: Please also add another frame (marked differently) as well!</p></div><div id="comment-34485-info" class="comment-info"><span class="comment-age">(08 Jul '14, 17:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34488"></span><div id="comment-34488" class="comment"><div id="post-34488-score" class="comment-score"></div><div class="comment-text"><p>Here it is <a href="https://www.cloudshark.org/captures/d72b612860b5">https://www.cloudshark.org/captures/d72b612860b5</a> I have mDNS packets only of those two types (blue &amp; red)</p></div><div id="comment-34488-info" class="comment-info"><span class="comment-age">(08 Jul '14, 18:14)</span> <span class="comment-user userinfo">lilyhack</span></div></div><span id="34493"></span><div id="comment-34493" class="comment"><div id="post-34493-score" class="comment-score"></div><div class="comment-text"><p>Although cloudshark.org shows the red coloring for frames 354, 355, etc. this is <strong>not the case with my installation</strong> of Wireshark, which is the latest development build on Windows 7 x64 (Version 1.12.0-rc2-125-g8a47b3a (v1.12.0-rc2-125-g8a47b3a from master-1.12).</p><p>The only difference between the marked and unmarked frames is the TTL.</p><p>unmarked: 1<br />
marked: 255</p><p>Based on the coloring rule (see my answer) and the TTL in the marked frames (255), they do not deserve the 'Low TTL or unexpected' coloring.</p><p>So, I believe this is a bug of the Wireshark version you are using (and probably also cloudshark.org).</p><p>Pleas upgrade your Wireshark version and the (pseudo) problem should go away.</p></div><div id="comment-34493-info" class="comment-info"><span class="comment-age">(09 Jul '14, 01:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34517"></span><div id="comment-34517" class="comment"><div id="post-34517-score" class="comment-score"></div><div class="comment-text"><p>I am using the latest release build 1.10.8. Upgrade to development version 1.12 resolves the color issue. Thanks.</p></div><div id="comment-34517-info" class="comment-info"><span class="comment-age">(09 Jul '14, 10:27)</span> <span class="comment-user userinfo">lilyhack</span></div></div><span id="34519"></span><div id="comment-34519" class="comment not_top_scorer"><div id="post-34519-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-34519-info" class="comment-info"><span class="comment-age">(09 Jul '14, 10:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34483" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-34483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

