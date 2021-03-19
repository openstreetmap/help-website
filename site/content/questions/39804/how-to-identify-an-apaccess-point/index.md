+++
type = "question"
title = "How to identify an ap(access point)?"
description = '''Hello, How would one go about identifying an access point when looking at packets through wireshark? From what I understand, it&#x27;s the source mac adresss of a Beacon frame(which would also be the BSSID), is that right? Thanks for any answers in advance.'''
date = "2015-02-11T12:58:00Z"
lastmod = "2015-02-12T12:26:00Z"
weight = 39804
keywords = [ "access", "ap", "wireshark", "packet", "point" ]
aliases = [ "/questions/39804" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify an ap(access point)?](/questions/39804/how-to-identify-an-apaccess-point)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39804-score" class="post-score" title="current number of votes">0</div><span id="post-39804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>How would one go about identifying an access point when looking at packets through wireshark? From what I understand, it's the source mac adresss of a Beacon frame(which would also be the BSSID), is that right?</p><p>Thanks for any answers in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-ap" rel="tag" title="see questions tagged &#39;ap&#39;">ap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '15, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/bac381a7780bf481fac8b9c7a4419a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rokas%20Mackevi%C4%8Dius&#39;s gravatar image" /><p><span>Rokas Mackev...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rokas Mackevičius has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '15, 13:19</strong> </span></p></div></div><div id="comments-container-39804" class="comments-container"></div><div id="comment-tools-39804" class="comment-tools"></div><div class="clear"></div><div id="comment-39804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39814"></span>

<div id="answer-container-39814" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39814-score" class="post-score" title="current number of votes">2</div><span id="post-39814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are several methods:</p><ul><li>look for beacon frames (wlan.fc.type_subtype == 0x0008). The sender is an AP</li><li>look for <strong>association requests</strong> (wlan.fc.type_subtype == 0x0000). The destination is the AP</li><li>if the traffic is not encrypted: find a frame with a SYN and then look at the destination address (wlan.da) in the 802.11 header. That's the MAC of the AP.</li><li>if the traffic is encrypted, filter for EAPOL frames. The first Key messages comes from an AP</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39814" class="comments-container"><span id="39819"></span><div id="comment-39819" class="comment"><div id="post-39819-score" class="comment-score"></div><div class="comment-text"><p>Thanks!</p><p>Just to be completely clear, in terms of beacon frames, by sender are you referring to the Transmitter adress or Source adress from the IEEE 802.11 Beacon frame packet header?</p></div><div id="comment-39819-info" class="comment-info"><span class="comment-age">(11 Feb '15, 15:22)</span> <span class="comment-user userinfo">Rokas Mackev...</span></div></div><span id="39820"></span><div id="comment-39820" class="comment"><div id="post-39820-score" class="comment-score"></div><div class="comment-text"><p>correct .</p></div><div id="comment-39820-info" class="comment-info"><span class="comment-age">(11 Feb '15, 15:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="39822"></span><div id="comment-39822" class="comment"><div id="post-39822-score" class="comment-score"></div><div class="comment-text"><p>So Transmitter adress and Source adress are identical in this situation? My question was which one was it, source or transmitter heh.</p></div><div id="comment-39822-info" class="comment-info"><span class="comment-age">(11 Feb '15, 16:40)</span> <span class="comment-user userinfo">Rokas Mackev...</span></div></div><span id="39839"></span><div id="comment-39839" class="comment"><div id="post-39839-score" class="comment-score"></div><div class="comment-text"><p>For a beacon frame in 802.11, the transmitter address and the Source address are the same.</p></div><div id="comment-39839-info" class="comment-info"><span class="comment-age">(12 Feb '15, 12:26)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-39814" class="comment-tools"></div><div class="clear"></div><div id="comment-39814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

