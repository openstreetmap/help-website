+++
type = "question"
title = "Decode the VSA 3GPP-GPRS-Negotiated-QoS-profile"
description = '''I think there is something wrong when decoding the 3GPP-GPRS-Negotiated-QoS-profile in Access-Request message. According to the 3gpp specification TS 29.061 (v9.6.0), for Release 8 or higher version QoS, the QoS information should contain:   -QCI  -ARP  -GBR QoS Information (MBR, GBR or APN-AMBR) Ho...'''
date = "2011-08-05T07:26:00Z"
lastmod = "2011-08-05T08:02:00Z"
weight = 5528
keywords = [ "vsa", "rel-8", "radius", "qos" ]
aliases = [ "/questions/5528" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode the VSA 3GPP-GPRS-Negotiated-QoS-profile](/questions/5528/decode-the-vsa-3gpp-gprs-negotiated-qos-profile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5528-score" class="post-score" title="current number of votes">0</div><span id="post-5528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I think there is something wrong when decoding the 3GPP-GPRS-Negotiated-QoS-profile in Access-Request message. According to the 3gpp specification TS 29.061 (v9.6.0), for Release 8 or higher version QoS, the QoS information should contain: -QCI -ARP -GBR QoS Information (MBR, GBR or APN-AMBR)</p><p>However the Wireshark decode the Release 8 QoS as: UMTS GTP Qos Profile: -Version -Hyphen separator -Spare -QoS delay -QoS reliability ...</p><p>Could the Wireshark solve this problem?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vsa" rel="tag" title="see questions tagged &#39;vsa&#39;">vsa</span> <span class="post-tag tag-link-rel-8" rel="tag" title="see questions tagged &#39;rel-8&#39;">rel-8</span> <span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '11, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/077cc718c6d3c12b4c9a3e00c3b8a54b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cramfor&#39;s gravatar image" /><p><span>cramfor</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cramfor has no accepted answers">0%</span></p></div></div><div id="comments-container-5528" class="comments-container"></div><div id="comment-tools-5528" class="comment-tools"></div><div class="clear"></div><div id="comment-5528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5529"></span>

<div id="answer-container-5529" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5529-score" class="post-score" title="current number of votes">0</div><span id="post-5529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The best thing to do is to open a <a href="https://bugs.wireshark.org/bugzilla/">bug</a> report, providing a link to the relevant specification and section(s), as well as attaching a small, relevant capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '11, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5529" class="comments-container"></div><div id="comment-tools-5529" class="comment-tools"></div><div class="clear"></div><div id="comment-5529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

