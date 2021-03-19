+++
type = "question"
title = "Can we do Map remote &amp; map local in wireshark ?"
description = '''As asked above can we do map remote &amp;amp; map local with the feed in wireshark ? these options are available in charles proxy tool &amp;amp; want to check whether same are available here ! If so, Please let me know the way to do it !!'''
date = "2014-11-20T04:09:00Z"
lastmod = "2014-11-21T00:58:00Z"
weight = 38015
keywords = [ "and", "map", "remote", "local" ]
aliases = [ "/questions/38015" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can we do Map remote & map local in wireshark ?](/questions/38015/can-we-do-map-remote-map-local-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38015-score" class="post-score" title="current number of votes">0</div><span id="post-38015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As asked above can we do map remote &amp; map local with the feed in wireshark ? these options are available in charles proxy tool &amp; want to check whether same are available here ! If so, Please let me know the way to do it !!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '14, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/5da36ed019ea1702fa86f32866e1757e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kalsfru&#39;s gravatar image" /><p><span>kalsfru</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kalsfru has no accepted answers">0%</span></p></div></div><div id="comments-container-38015" class="comments-container"></div><div id="comment-tools-38015" class="comment-tools"></div><div class="clear"></div><div id="comment-38015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38028"></span>

<div id="answer-container-38028" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38028-score" class="post-score" title="current number of votes">3</div><span id="post-38028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kalsfru has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <strong><a href="http://www.charlesproxy.com/documentation/tools/map-remote/">Map Remote</a></strong> and <strong><a href="http://www.charlesproxy.com/documentation/tools/map-local/">Map Local</a></strong> tools of Charles Proxy, do either modify requests or feed data into the stream. That's not possible with Wireshark, as it's a <strong>passive</strong> network troubleshooting/analysis tool and as such it does not alter the data or inject traffic.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '14, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38028" class="comments-container"><span id="38033"></span><div id="comment-38033" class="comment"><div id="post-38033-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response !</p></div><div id="comment-38033-info" class="comment-info"><span class="comment-age">(20 Nov '14, 22:54)</span> <span class="comment-user userinfo">kalsfru</span></div></div><span id="38034"></span><div id="comment-38034" class="comment"><div id="post-38034-score" class="comment-score"></div><div class="comment-text"><p><span>@kalsfru</span>,</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38034-info" class="comment-info"><span class="comment-age">(21 Nov '14, 00:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-38028" class="comment-tools"></div><div class="clear"></div><div id="comment-38028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

