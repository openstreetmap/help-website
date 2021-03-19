+++
type = "question"
title = "Feature request - &quot;previous display filter&quot;?"
description = '''I often use a display filter (e.g. &quot;ssl.record.content_type==21&quot; to get a list of packets for further inspection. If I then use &#x27;Follow TCP Stream&#x27; or the like, I have to go back to the display filter dialog and reselect &quot;ssl.record.content-type==21&quot; again (and hit Apply) to get back to my &#x27;master l...'''
date = "2011-07-26T19:36:00Z"
lastmod = "2012-04-20T00:52:00Z"
weight = 5291
keywords = [ "feature-request", "display-filter" ]
aliases = [ "/questions/5291" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Feature request - "previous display filter"?](/questions/5291/feature-request-previous-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5291-score" class="post-score" title="current number of votes">3</div><span id="post-5291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I often use a display filter (e.g. "ssl.record.content_type==21" to get a list of packets for further inspection. If I then use 'Follow TCP Stream' or the like, I have to go back to the display filter dialog and reselect "ssl.record.content-type==21" again (and hit Apply) to get back to my 'master list' of curious packets.</p><p>How about something like a "back button" that would simply go back to the previous display filter? I don't see anything like that, and it would be VERY handy as I wade through various displays...what do you think?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-feature-request" rel="tag" title="see questions tagged &#39;feature-request&#39;">feature-request</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 19:36</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jul '11, 19:37</strong> </span></p></div></div><div id="comments-container-5291" class="comments-container"><span id="10322"></span><div id="comment-10322" class="comment"><div id="post-10322-score" class="comment-score"></div><div class="comment-text"><p>This is an feature I often missed in daily practice with wireshark: - open wireshark log - watch for tcp connections - open the interested tcp stream - GO-BACK to old view</p><p>And it seems to be a common use - like in browsers. So I'm wondering, why we only have 2 'like it' post (2012/04/12).</p><p>I only found this patch in Bugzilla - which seems to be rejected, but sound dedicated to this feature request: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1869">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1869</a></p><p>Is anybody able to push this patch/feature?</p><p>Ralf</p></div><div id="comment-10322-info" class="comment-info"><span class="comment-age">(19 Apr '12, 23:10)</span> <span class="comment-user userinfo">Ralf S</span></div></div><span id="10328"></span><div id="comment-10328" class="comment"><div id="post-10328-score" class="comment-score"></div><div class="comment-text"><p>you do know about the capture filter history which by default saves the last 10 display filters in the drop down list, right? I agree that a simple "back" button would do the work too - but the history works fine for me</p></div><div id="comment-10328-info" class="comment-info"><span class="comment-age">(20 Apr '12, 00:52)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-5291" class="comment-tools"></div><div class="clear"></div><div id="comment-5291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5292"></span>

<div id="answer-container-5292" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5292-score" class="post-score" title="current number of votes">3</div><span id="post-5292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wesmorgan1 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To submit an RFE (request for enhancement):</p><ol><li><p>Search <a href="http://bugs.wireshark.org">Wireshark Bugzilla</a> for an existing RFE that matches your request. If none exist, file a new "bug", setting the <strong>Severity</strong> to <strong>Enhancement</strong>. If you're a developer, you're encouraged to <a href="http://www.wireshark.org/docs/wsdg_html/#ChSrcSend">submit a patch</a> (attached to the bug report).</p></li><li><p>Vote for the bug by clicking the <strong>vote</strong> link next to <strong>Importance</strong>. You can even vote for your own bug that you just filed in step 1.</p></li><li><p>(OPTIONAL) Take a look at the <a href="http://wiki.wireshark.org/WishList">WishList wiki</a>. You're asked to email the <a href="http://www.wireshark.org/lists/">developer mailing list</a> before adding to the WishList. However, the RFE from step 1 should suffice (and is preferred since it gets tracked).</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jul '11, 20:26</strong> </span></p></div></div><div id="comments-container-5292" class="comments-container"></div><div id="comment-tools-5292" class="comment-tools"></div><div class="clear"></div><div id="comment-5292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

