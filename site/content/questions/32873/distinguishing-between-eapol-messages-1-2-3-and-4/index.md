+++
type = "question"
title = "Distinguishing between EAPOL messages (1, 2, 3, and 4)"
description = '''Wireshark presents each of the EAPOL messages with &quot;(Message 1 of 4)&quot; then 2 of 4, 3 of 4, and finally 4 of 4. This information appears in the &quot;Info&quot; column within Wireshark. From the packet data, I&#x27;d like to know how to make the same distinction for each of the 4 EAPOL packets that Wireshark does. ...'''
date = "2014-05-18T17:49:00Z"
lastmod = "2014-05-24T06:43:00Z"
weight = 32873
keywords = [ "eapol", "messages", "wireshark" ]
aliases = [ "/questions/32873" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Distinguishing between EAPOL messages (1, 2, 3, and 4)](/questions/32873/distinguishing-between-eapol-messages-1-2-3-and-4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32873-score" class="post-score" title="current number of votes">0</div><span id="post-32873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark presents each of the EAPOL messages with "(Message 1 of 4)" then 2 of 4, 3 of 4, and finally 4 of 4. This information appears in the "Info" column within Wireshark. From the packet data, I'd like to know how to make the same distinction for each of the 4 EAPOL packets that Wireshark does.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-messages" rel="tag" title="see questions tagged &#39;messages&#39;">messages</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '14, 17:49</strong></p><img src="https://secure.gravatar.com/avatar/f8c9295de767e10e7cfe22381e79cbad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwiftAero&#39;s gravatar image" /><p><span>SwiftAero</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwiftAero has no accepted answers">0%</span></p></div></div><div id="comments-container-32873" class="comments-container"></div><div id="comment-tools-32873" class="comment-tools"></div><div class="clear"></div><div id="comment-32873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33030"></span>

<div id="answer-container-33030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33030-score" class="post-score" title="current number of votes">0</div><span id="post-33030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>These info's come from the WPA key dissection in packet-ieee80211.c. Have a look at <code>dissect_wlan_rsna_eapol_wpa_or_rsn_key()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '14, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-33030" class="comments-container"></div><div id="comment-tools-33030" class="comment-tools"></div><div class="clear"></div><div id="comment-33030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

