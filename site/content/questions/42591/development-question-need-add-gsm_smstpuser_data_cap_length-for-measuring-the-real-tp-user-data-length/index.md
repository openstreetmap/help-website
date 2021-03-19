+++
type = "question"
title = "[Development Question] Need add gsm_sms.tp.user_data_cap_length for measuring the real TP-User-Data length"
description = '''Need add gsm_sms.tp.user_data_cap_length for measuring the real TP-User-Data length. As gsm_sms.tp.user_data_length is announced value and gsm_sms.tp.user_data_cap_length needs to measure the TP-User-Data. I think this would be a good enhancement.'''
date = "2015-05-20T12:34:00Z"
lastmod = "2015-05-30T21:55:00Z"
weight = 42591
keywords = [ "gsm_sms" ]
aliases = [ "/questions/42591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[Development Question\] Need add gsm\_sms.tp.user\_data\_cap\_length for measuring the real TP-User-Data length](/questions/42591/development-question-need-add-gsm_smstpuser_data_cap_length-for-measuring-the-real-tp-user-data-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42591-score" class="post-score" title="current number of votes">0</div><span id="post-42591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Need add gsm_sms.tp.user_data_cap_length for measuring the real TP-User-Data length. As gsm_sms.tp.user_data_length is announced value and gsm_sms.tp.user_data_cap_length needs to measure the TP-User-Data. I think this would be a good enhancement.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gsm_sms" rel="tag" title="see questions tagged &#39;gsm_sms&#39;">gsm_sms</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '15, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/c6d2de8ff58f1dc3175ac84d437c5931?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex%20Lu&#39;s gravatar image" /><p><span>Alex Lu</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex Lu has no accepted answers">0%</span></p></div></div><div id="comments-container-42591" class="comments-container"><span id="42592"></span><div id="comment-42592" class="comment"><div id="post-42592-score" class="comment-score"></div><div class="comment-text"><p>gsm_sms.tp.user_data_length is the real TP-User-Data IE length.</p><p>What would you like to get exactly? The number of characters of the text string? The number of bytes corresponding to the gsm_sms.tp.user_data_length value minus the User-Data Header length?</p></div><div id="comment-42592-info" class="comment-info"><span class="comment-age">(20 May '15, 13:13)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="42596"></span><div id="comment-42596" class="comment"><div id="post-42596-score" class="comment-score"></div><div class="comment-text"><p>Pascal, thanks for comments on the question. Yes, ideally the user data length should match the data length, but this is not perfect world and and user data length sometimes not matches the exactly length which will cause issue especially on delivery side.</p></div><div id="comment-42596-info" class="comment-info"><span class="comment-age">(20 May '15, 22:47)</span> <span class="comment-user userinfo">Alex Lu</span></div></div><span id="42604"></span><div id="comment-42604" class="comment"><div id="post-42604-score" class="comment-score"></div><div class="comment-text"><p>Still you have not answered my questions. What are you looking for exactly? A number of bytes? A number of characters? Do you mean that some devices do not compute properly the TP-User-Data length as being the sum of the User-Data Header length + string length, but being longer that what it is in theory?</p></div><div id="comment-42604-info" class="comment-info"><span class="comment-age">(21 May '15, 08:12)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-42591" class="comment-tools"></div><div class="clear"></div><div id="comment-42591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42769"></span>

<div id="answer-container-42769" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42769-score" class="post-score" title="current number of votes">0</div><span id="post-42769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, I'm looking for the number of bytes, and some server doesn't calculate correctly and will cause the recipient to reject the sms.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '15, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/c6d2de8ff58f1dc3175ac84d437c5931?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex%20Lu&#39;s gravatar image" /><p><span>Alex Lu</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex Lu has no accepted answers">0%</span></p></div></div><div id="comments-container-42769" class="comments-container"></div><div id="comment-tools-42769" class="comment-tools"></div><div class="clear"></div><div id="comment-42769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

