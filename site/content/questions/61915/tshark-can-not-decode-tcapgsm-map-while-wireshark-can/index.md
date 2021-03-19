+++
type = "question"
title = "Tshark CAN NOT decode TCAP/GSM MAP while Wireshark CAN"
description = '''Hello everyone,  Is there any special configuration needed in Tshark so that it can decode TCAP/GSM MAP/GSM SMS packets? Current captures show nothing above SCCP.  Had the same issue with Wireshark but following postings in this forum I was able to resolve it by setting View -&amp;gt; Preferences -&amp;gt; ...'''
date = "2017-06-09T10:07:00Z"
lastmod = "2017-06-13T00:50:00Z"
weight = 61915
keywords = [ "tshark_gsm_map" ]
aliases = [ "/questions/61915" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark CAN NOT decode TCAP/GSM MAP while Wireshark CAN](/questions/61915/tshark-can-not-decode-tcapgsm-map-while-wireshark-can)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61915-score" class="post-score" title="current number of votes">0</div><span id="post-61915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, Is there any special configuration needed in Tshark so that it can decode TCAP/GSM MAP/GSM SMS packets? Current captures show nothing above SCCP. Had the same issue with Wireshark but following postings in this forum I was able to resolve it by setting View -&gt; Preferences -&gt; Protocols -&gt; MTP3=ANSI. How can something similar be done in Tshark?</p><p>Many thanks in advance! Bill</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark_gsm_map" rel="tag" title="see questions tagged &#39;tshark_gsm_map&#39;">tshark_gsm_map</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '17, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/129af39547c3ea7860f0c728131b6238?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pafi84&#39;s gravatar image" /><p><span>pafi84</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pafi84 has no accepted answers">0%</span></p></div></div><div id="comments-container-61915" class="comments-container"></div><div id="comment-tools-61915" class="comment-tools"></div><div class="clear"></div><div id="comment-61915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61933"></span>

<div id="answer-container-61933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61933-score" class="post-score" title="current number of votes">1</div><span id="post-61933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the '-o' option: <code>tshark -o mtp3.standard:ANSI</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '17, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '17, 08:52</strong> </span></p></div></div><div id="comments-container-61933" class="comments-container"><span id="61950"></span><div id="comment-61950" class="comment"><div id="post-61950-score" class="comment-score"></div><div class="comment-text"><p>Uli, Thank you for taking the time to reply. Tshark now displays GSM MAP and GSM SMS messages. Best Regards, Bill</p></div><div id="comment-61950-info" class="comment-info"><span class="comment-age">(12 Jun '17, 08:05)</span> <span class="comment-user userinfo">pafi84</span></div></div><span id="61965"></span><div id="comment-61965" class="comment"><div id="post-61965-score" class="comment-score"></div><div class="comment-text"><p>FYI, a more "permanent" method is to edit your .wireshark/preferences file (assuming Linux), and change the mtp3 parameter within the preferences file. That saves you from adding the -o flag if most of your traces use ANSI-standard for MTP3/M3UA.</p></div><div id="comment-61965-info" class="comment-info"><span class="comment-age">(12 Jun '17, 16:43)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="61977"></span><div id="comment-61977" class="comment"><div id="post-61977-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/34274/pafi84">@pafi84</a></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61977-info" class="comment-info"><span class="comment-age">(13 Jun '17, 00:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61933" class="comment-tools"></div><div class="clear"></div><div id="comment-61933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

