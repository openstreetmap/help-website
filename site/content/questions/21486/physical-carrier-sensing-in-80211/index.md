+++
type = "question"
title = "Physical carrier sensing in 802.11?"
description = '''I have two questions about IEEE 802.11 MAC protocol.  1) I want to know that physical carrier sense mechanism is adopted for non-RTS packets (CTS, DATA and ACK) or not? For more clarity please consider following scenario: Suppose that node A sends a RTS packet for node B and node B receives this RTS...'''
date = "2013-05-27T02:01:00Z"
lastmod = "2013-05-27T03:11:00Z"
weight = 21486
keywords = [ "mac", "carrier", "802.11", "sense" ]
aliases = [ "/questions/21486" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Physical carrier sensing in 802.11?](/questions/21486/physical-carrier-sensing-in-80211)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21486-score" class="post-score" title="current number of votes">0</div><span id="post-21486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two questions about IEEE 802.11 MAC protocol.</p><p>1) I want to know that physical carrier sense mechanism is adopted for non-RTS packets (CTS, DATA and ACK) or not? For more clarity please consider following scenario:</p><p>Suppose that node A sends a RTS packet for node B and node B receives this RTS without collision and also node B is not within a pre-established NAV state. So it should respond to node A by a CTS packet after a SIFS interval. Now suppose that node C which is in node B's transmission range and is not in node A's sensing range (and therefor has not heared RTS of node A) sends a RTS packet during this SIFS interval and so channel will be busy physically for node B, before sending its CTS. In this situation if node B transmits its CTS packet independent of channel busy state or not?</p><p>2) Transmission and receiving two packets with time overlap by one node is valid in 802.11 MAC or not? for example in previously described scenario, if node B transmits the CTS, node A can receive it correctly or it will be corrupted because of node C's RTS?<br />
</p><p>If it is possible for you please solve my confusions.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-carrier" rel="tag" title="see questions tagged &#39;carrier&#39;">carrier</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-sense" rel="tag" title="see questions tagged &#39;sense&#39;">sense</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '13, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/554bf8716228ab96d93251845f0d1362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HNM&#39;s gravatar image" /><p><span>HNM</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HNM has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 May '13, 02:03</strong> </span></p></div></div><div id="comments-container-21486" class="comments-container"><span id="21487"></span><div id="comment-21487" class="comment"><div id="post-21487-score" class="comment-score"></div><div class="comment-text"><p>I'm just curious. What kind of problem are you trying to analyze/solve?</p></div><div id="comment-21487-info" class="comment-info"><span class="comment-age">(27 May '13, 03:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21486" class="comment-tools"></div><div class="clear"></div><div id="comment-21486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

