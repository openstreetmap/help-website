+++
type = "question"
title = "A-MPDU Agregation in RadioTap Header (Bytes escaped)"
description = '''Hello, I have the attached photos for a capture for Wifi Frames in Wireshark.   When I was analyzing the frame format for different packets, I found that when I move from the MCS Information field to the A-MPDU status field, three bytes are being escaped by Wireshark. So I checked the Radio Tap head...'''
date = "2015-06-12T11:37:00Z"
lastmod = "2015-06-12T12:01:00Z"
weight = 43098
keywords = [ "wifi", "radiotap", "802.11n" ]
aliases = [ "/questions/43098" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [A-MPDU Agregation in RadioTap Header (Bytes escaped)](/questions/43098/a-mpdu-agregation-in-radiotap-header-bytes-escaped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43098-score" class="post-score" title="current number of votes">0</div><span id="post-43098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have the attached photos for a capture for Wifi Frames in Wireshark.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture.png" alt="alt text" /></p><p>When I was analyzing the frame format for different packets, I found that when I move from the MCS Information field to the A-MPDU status field, three bytes are being escaped by Wireshark. So I checked the Radio Tap header format, and I found nothing is mentioned about these three bytes. So could you please clarify why three bytes are ignored by the parser.</p><p>Additionally according to the A-MPDU Status field definition in the following <a href="http://www.radiotap.org/defined-fields/A-MPDU%20status">Site</a>, the structure should be aligned by 4 bytes. So the subfields should be multiple of 4 bytes i.e. The A-MPDU Status should be 16 Bytes long, correct?</p><p><strong>Notes:</strong></p><ol><li><p>The three Bytes have a value of zero.</p></li><li><p>The original capture file can be found in the following link <a href="https://bugs.wireshark.org/bugzilla/attachment.cgi?id=8912">Capture File</a></p></li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-radiotap" rel="tag" title="see questions tagged &#39;radiotap&#39;">radiotap</span> <span class="post-tag tag-link-802.11n" rel="tag" title="see questions tagged &#39;802.11n&#39;">802.11n</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '15, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/566cfe38b17a31f0dc825c86538cf3d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hany%20Assasa&#39;s gravatar image" /><p><span>Hany Assasa</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hany Assasa has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43098" class="comments-container"></div><div id="comment-tools-43098" class="comment-tools"></div><div class="clear"></div><div id="comment-43098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43099"></span>

<div id="answer-container-43099" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43099-score" class="post-score" title="current number of votes">1</div><span id="post-43099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hany Assasa has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is because the A-MPDU Status field requires a 4 bytes alignment, meaning that the structure must start at a multiple of 4 bytes. The 3 bytes set to 0 are padding between the end of the MCS field and the beginning of the A-MPDU Status field. You can read the "Alignment in Radiotap" paragraph on <a href="http://www.radiotap.org/">http://www.radiotap.org/</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '15, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '15, 12:07</strong> </span></p></div></div><div id="comments-container-43099" class="comments-container"></div><div id="comment-tools-43099" class="comment-tools"></div><div class="clear"></div><div id="comment-43099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

