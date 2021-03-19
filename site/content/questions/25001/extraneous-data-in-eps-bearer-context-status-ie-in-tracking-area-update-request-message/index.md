+++
type = "question"
title = "Extraneous data in EPS bearer context status IE in Tracking Area update request message"
description = '''why EPS bearer context status IE is decoded successfully but with a tag Extraneous data in tracking area update request message including TA/LA updating and bearer establishment requested.'''
date = "2013-09-20T04:16:00Z"
lastmod = "2013-09-20T11:46:00Z"
weight = 25001
keywords = [ "extraneous" ]
aliases = [ "/questions/25001" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extraneous data in EPS bearer context status IE in Tracking Area update request message](/questions/25001/extraneous-data-in-eps-bearer-context-status-ie-in-tracking-area-update-request-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25001-score" class="post-score" title="current number of votes">0</div><span id="post-25001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>why EPS bearer context status IE is decoded successfully but with a tag Extraneous data in tracking area update request message including TA/LA updating and bearer establishment requested.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-extraneous" rel="tag" title="see questions tagged &#39;extraneous&#39;">extraneous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/97e0a5093cca0d174b984d2ef9566eaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheMan%20Catch&#39;s gravatar image" /><p><span>TheMan Catch</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheMan Catch has no accepted answers">0%</span></p></div></div><div id="comments-container-25001" class="comments-container"><span id="25018"></span><div id="comment-25018" class="comment"><div id="post-25018-score" class="comment-score"></div><div class="comment-text"><p>"Extraneous data" means that there was data left in the message when wireshark finished dissection dye to: - New IE added to message which wireshark does not dissect. - Bug in Wireshark - Bug in application, wrong length or? We need to see the capture to tell which of the above applies.</p></div><div id="comment-25018-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:55)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="25052"></span><div id="comment-25052" class="comment"><div id="post-25052-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.10 supports all the known IEs (up to R12) for a Tracking Area Update Request message. So either you are using an older release, or the message contains extra data not specified in 3GPP 24.301 (or it could be a Wireshark bug but it seems unlikely). As Anders stated, sharing the capture would allow to confirm which case it is.</p></div><div id="comment-25052-info" class="comment-info"><span class="comment-age">(20 Sep '13, 11:46)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-25001" class="comment-tools"></div><div class="clear"></div><div id="comment-25001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

