+++
type = "question"
title = "Decapsulation of OpenBSD enc frames"
description = '''I recently upgraded to 2.2.0 on the Mac and noticed that I no longer get OpenBSD ENC Encapsulated captures automatically decapsulated and have not found a manual way to do so either. The ones I routinely use are taken on pfSense&#x27;s IPsec interface. The data is there, but all I see in wireshark now is...'''
date = "2016-10-05T16:14:00Z"
lastmod = "2016-12-31T13:41:00Z"
weight = 56173
keywords = [ "encapsulation", "enc", "openbsd", "decapsulation", "ipsec" ]
aliases = [ "/questions/56173" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decapsulation of OpenBSD enc frames](/questions/56173/decapsulation-of-openbsd-enc-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56173-score" class="post-score" title="current number of votes">0</div><span id="post-56173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently upgraded to 2.2.0 on the Mac and noticed that I no longer get OpenBSD ENC Encapsulated captures automatically decapsulated and have not found a manual way to do so either. The ones I routinely use are taken on pfSense's IPsec interface. The data is there, but all I see in wireshark now is Protocol ENC. Frames show as [Protocols in frame: enc:data] In older versions they would appear as, for example, [Protocols in frame: enc:ip:udp:data] with the data portion decoded and displayed.</p><pre><code>$ capinfos -E packetcapture.cap
File name:           packetcapture.cap
File encapsulation:  OpenBSD enc(4) encapsulating interface</code></pre><p>Is there a way to tell latest Wireshark to decapsulate these captures again?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encapsulation" rel="tag" title="see questions tagged &#39;encapsulation&#39;">encapsulation</span> <span class="post-tag tag-link-enc" rel="tag" title="see questions tagged &#39;enc&#39;">enc</span> <span class="post-tag tag-link-openbsd" rel="tag" title="see questions tagged &#39;openbsd&#39;">openbsd</span> <span class="post-tag tag-link-decapsulation" rel="tag" title="see questions tagged &#39;decapsulation&#39;">decapsulation</span> <span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '16, 16:14</strong></p><img src="https://secure.gravatar.com/avatar/21efa28d71e5f717e77b4e8068430b97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="backsnarf&#39;s gravatar image" /><p><span>backsnarf</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="backsnarf has no accepted answers">0%</span></p></div></div><div id="comments-container-56173" class="comments-container"><span id="58421"></span><div id="comment-58421" class="comment"><div id="post-58421-score" class="comment-score"></div><div class="comment-text"><p>Still an issue on 2.2.3. Anyone know how to trigger automatic decapsulation of the plaintext data in these captures?</p></div><div id="comment-58421-info" class="comment-info"><span class="comment-age">(29 Dec '16, 09:39)</span> <span class="comment-user userinfo">backsnarf</span></div></div><span id="58422"></span><div id="comment-58422" class="comment"><div id="post-58422-score" class="comment-score"></div><div class="comment-text"><p>Either a sample capture of a <a href="http://bugs.wireshark.org">full bug report</a> would be needed to help this along.</p></div><div id="comment-58422-info" class="comment-info"><span class="comment-age">(29 Dec '16, 10:48)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="58423"></span><div id="comment-58423" class="comment"><div id="post-58423-score" class="comment-score">1</div><div class="comment-text"><p>Created bug with a sample capture file. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13279">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13279</a></p></div><div id="comment-58423-info" class="comment-info"><span class="comment-age">(29 Dec '16, 12:52)</span> <span class="comment-user userinfo">labrat</span></div></div></div><div id="comment-tools-56173" class="comment-tools"></div><div class="clear"></div><div id="comment-56173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58438"></span>

<div id="answer-container-58438" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58438-score" class="post-score" title="current number of votes">1</div><span id="post-58438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="backsnarf has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The solution is to upgrade to Wireshark 2.2.4, which contains a fix for this bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '16, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58438" class="comments-container"><span id="58446"></span><div id="comment-58446" class="comment"><div id="post-58446-score" class="comment-score"></div><div class="comment-text"><p>Thank you so very much. Confirmed working again in 2.2.4-RC.</p></div><div id="comment-58446-info" class="comment-info"><span class="comment-age">(31 Dec '16, 13:41)</span> <span class="comment-user userinfo">backsnarf</span></div></div></div><div id="comment-tools-58438" class="comment-tools"></div><div class="clear"></div><div id="comment-58438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

