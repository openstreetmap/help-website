+++
type = "question"
title = "Something is downloading @ full bandwidth...."
description = '''Full disclosure: I have no idea how to use Wireshark..  My laptop is pulling full, available, download bandwidth and I have no idea how to use Wireshark to determine what app is doing it.. Task manager is showing the bandwidth under performance (win 8.1) but when I look at processes it does not add ...'''
date = "2014-06-28T19:40:00Z"
lastmod = "2014-06-29T15:10:00Z"
weight = 34264
keywords = [ "toomuchdata" ]
aliases = [ "/questions/34264" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Something is downloading @ full bandwidth....](/questions/34264/something-is-downloading-full-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34264-score" class="post-score" title="current number of votes">0</div><span id="post-34264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Full disclosure: I have no idea how to use Wireshark..</p><p>My laptop is pulling full, available, download bandwidth and I have no idea how to use Wireshark to determine what app is doing it..</p><p>Task manager is showing the bandwidth under performance (win 8.1) but when I look at processes it does not add up.</p><p>The proof is in the pudding though: if I tether the laptop, its pulling insane bandwidth down stream....</p><p>Is there a profile or settings I can use with Wireshark to figure out what app is using all this band with and where the data is going?</p><p>T.I.A</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-toomuchdata" rel="tag" title="see questions tagged &#39;toomuchdata&#39;">toomuchdata</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '14, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/17fbf444449f9ae423ad0c1842a728f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LilRedDog&#39;s gravatar image" /><p><span>LilRedDog</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LilRedDog has no accepted answers">0%</span></p></div></div><div id="comments-container-34264" class="comments-container"></div><div id="comment-tools-34264" class="comment-tools"></div><div class="clear"></div><div id="comment-34264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34273"></span>

<div id="answer-container-34273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34273-score" class="post-score" title="current number of votes">0</div><span id="post-34273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can help you determine what the traffic is and the external source\destination but can't directly tell you which process.</p><p>However Win 8.1 already has the tools to do this, open "Resource Monitor", select the "Network" tab and the process with the most network I/O should be top of the list in the "Processes with Network Activity" list. The next list "Network Activity" then breaks that down by destination address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '14, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '14, 15:10</strong> </span></p></div></div><div id="comments-container-34273" class="comments-container"><span id="34274"></span><div id="comment-34274" class="comment"><div id="post-34274-score" class="comment-score"></div><div class="comment-text"><p>That answered it for me...</p><p>Thank you very much!</p></div><div id="comment-34274-info" class="comment-info"><span class="comment-age">(29 Jun '14, 14:24)</span> <span class="comment-user userinfo">LilRedDog</span></div></div><span id="34275"></span><div id="comment-34275" class="comment"><div id="post-34275-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-34275-info" class="comment-info"><span class="comment-age">(29 Jun '14, 15:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-34273" class="comment-tools"></div><div class="clear"></div><div id="comment-34273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

