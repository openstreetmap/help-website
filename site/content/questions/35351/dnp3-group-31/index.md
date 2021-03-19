+++
type = "question"
title = "DNP3 group 31"
description = '''Hello, I could be wrong; it appears the dissector does not parse DNP3 group 31 (frozen analog inputs) objects? Is that correct?  I ask before I start the effort of collecting all the data and posting a bug report. I posted a bug report for group 13 variation 2 not being parsed but have seen no respo...'''
date = "2014-08-09T19:08:00Z"
lastmod = "2014-08-10T05:33:00Z"
weight = 35351
keywords = [ "dnp" ]
aliases = [ "/questions/35351" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [DNP3 group 31](/questions/35351/dnp3-group-31)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35351-score" class="post-score" title="current number of votes">0</div><span id="post-35351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I could be wrong; it appears the dissector does not parse DNP3 group 31 (frozen analog inputs) objects? Is that correct?</p><p>I ask before I start the effort of collecting all the data and posting a bug report.</p><p>I posted a bug report for group 13 variation 2 not being parsed but have seen no response.</p><p>Regards,</p><p>Mark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dnp" rel="tag" title="see questions tagged &#39;dnp&#39;">dnp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '14, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/d2fbebbc005d3eba52959bbae9828149?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark-&#39;s gravatar image" /><p><span>Mark-</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark- has no accepted answers">0%</span></p></div></div><div id="comments-container-35351" class="comments-container"></div><div id="comment-tools-35351" class="comment-tools"></div><div class="clear"></div><div id="comment-35351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35355"></span>

<div id="answer-container-35355" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35355-score" class="post-score" title="current number of votes">0</div><span id="post-35355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mark- has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>group 31 isn't currently supported, nor is group 13. Support for object types is added as needed by volunteers when they can, patches gratefully accepted via Gerrit</p><p>Raising the bug report on Bugzilla is the correct approach and adding a capture as you've done for g13 makes life much easier. Again, volunteers will tackle the bug report when they have spare time available, and the pool of folks who have access to the non-free protocol specs is a bit limited.</p><p>Also note from your bug report, you are not using the latest version of Wireshark (even though that won't help in this case), 1.10.2 isn't even the latest version of the old stable release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35355" class="comments-container"><span id="35357"></span><div id="comment-35357" class="comment"><div id="post-35357-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer.</p><p>I will capture a packet, hand dissect the bytes and create a bug report.</p><p>I have the spec and have written a master that supports most groups and all variations for the groups. I am now writing an outstation that supports most groups and all variations. If a volunteer needs an object/variation format, let me know.</p></div><div id="comment-35357-info" class="comment-info"><span class="comment-age">(10 Aug '14, 05:29)</span> <span class="comment-user userinfo">Mark-</span></div></div><span id="35358"></span><div id="comment-35358" class="comment"><div id="post-35358-score" class="comment-score"></div><div class="comment-text"><p>I have the spec and wrote a great deal of the dnp3 dissector, I don't have the time at the moment.</p></div><div id="comment-35358-info" class="comment-info"><span class="comment-age">(10 Aug '14, 05:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-35355" class="comment-tools"></div><div class="clear"></div><div id="comment-35355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

