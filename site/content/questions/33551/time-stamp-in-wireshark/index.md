+++
type = "question"
title = "Time stamp in wireshark"
description = '''Hi all, i have a captured file and i want to know the time when a particular packet is captured with respect to the first packet i.e. first packet is captured at 0 seconds. i am using the filter &quot;frame.time_delta&quot; which is giving me the time difference between two adjacent packets, but i need the ab...'''
date = "2014-06-08T10:35:00Z"
lastmod = "2014-06-08T12:53:00Z"
weight = 33551
keywords = [ "timestamp", "time" ]
aliases = [ "/questions/33551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Time stamp in wireshark](/questions/33551/time-stamp-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33551-score" class="post-score" title="current number of votes">0</div><span id="post-33551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, i have a captured file and i want to know the time when a particular packet is captured with respect to the first packet i.e. first packet is captured at 0 seconds. i am using the filter "frame.time_delta" which is giving me the time difference between two adjacent packets, but i need the absolute time. any help please!!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '14, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/f610e4a11992d3a39effbeb0cf10c906?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javeeria%20Jalil&#39;s gravatar image" /><p><span>Javeeria Jalil</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javeeria Jalil has no accepted answers">0%</span></p></div></div><div id="comments-container-33551" class="comments-container"></div><div id="comment-tools-33551" class="comment-tools"></div><div class="clear"></div><div id="comment-33551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33552"></span>

<div id="answer-container-33552" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33552-score" class="post-score" title="current number of votes">2</div><span id="post-33552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Right click the first packet and select "Set Time reference (toggle)", this will set that packet as the time reference, and wireshark will prompt you to select a suitable time format to use that, if not from the menu View | Time Display Format select "Seconds Since Beginning of Capture", and all packet times will now be relative to the previous marked packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '14, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33552" class="comments-container"><span id="33554"></span><div id="comment-33554" class="comment"><div id="post-33554-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot Sir, so nice of u...... actually i was mixing up few things.... ur reply helped me a lot, thanks once again</p></div><div id="comment-33554-info" class="comment-info"><span class="comment-age">(08 Jun '14, 12:01)</span> <span class="comment-user userinfo">Javeeria Jalil</span></div></div><span id="33557"></span><div id="comment-33557" class="comment"><div id="post-33557-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-33557-info" class="comment-info"><span class="comment-age">(08 Jun '14, 12:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33552" class="comment-tools"></div><div class="clear"></div><div id="comment-33552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

