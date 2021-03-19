+++
type = "question"
title = "Capturing Over a Long Period of Time"
description = '''Hi Folks I am investigating an issue of intermittent connectivity between two applications on seperate server, and want to set up Wireshark to capture packets between the two. The period of time I am looking to capture for is about 3 days - As the problem is intermittent and seems totally random, we...'''
date = "2012-08-26T21:10:00Z"
lastmod = "2012-08-27T14:49:00Z"
weight = 13900
keywords = [ "save", "capture", "capture-filter", "filter", "time" ]
aliases = [ "/questions/13900" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Over a Long Period of Time](/questions/13900/capturing-over-a-long-period-of-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13900-score" class="post-score" title="current number of votes">0</div><span id="post-13900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks</p><p>I am investigating an issue of intermittent connectivity between two applications on seperate server, and want to set up Wireshark to capture packets between the two. The period of time I am looking to capture for is about 3 days - As the problem is intermittent and seems totally random, we have to leave the capture running the whole time to ensure that we are capturing when connectivity is interrupted.</p><p>However, the capture file gets really big really fast so I need to know if you can apply filters to the file before the capture begins, resulting in only the filtered packets being saved, and the rest discarded.</p><p>Does anyone know of a way to do this?</p><p>Many Thanks</p><p>Jon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '12, 21:10</strong></p><img src="https://secure.gravatar.com/avatar/95ac01766c9a9fadf08ceab1613c609b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Holty&#39;s gravatar image" /><p><span>Holty</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Holty has no accepted answers">0%</span></p></div></div><div id="comments-container-13900" class="comments-container"></div><div id="comment-tools-13900" class="comment-tools"></div><div class="clear"></div><div id="comment-13900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13906"></span>

<div id="answer-container-13906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13906-score" class="post-score" title="current number of votes">2</div><span id="post-13906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can certainly apply capture filters to limit what is captured but the expressiveness of the filters is limited compared to Wireshark display filters. See <a href="http://wiki.wireshark.org/CaptureFilters">Capture Filters</a> page on the Wiki for more info.</p><p>For long-term captures you should use dumpcap rather Wireshark (or tshark) as that program doesn't do reassembly and thus maintain state and you can also use multiple capture files over the period of time so that no file is too large (-b option). If appropriate you can also limit the packet length captured (-s) if you don't require the full frame for your analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '12, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13906" class="comments-container"><span id="13917"></span><div id="comment-13917" class="comment"><div id="post-13917-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham, thanks for coming back to me so quickly. I think I can get what I need using Windump, I've tested a couple of time using simple HTTP traffic and the output is appearing Wireshark as expected, so we are all good to go. Really appreciate your response here!</p></div><div id="comment-13917-info" class="comment-info"><span class="comment-age">(27 Aug '12, 14:49)</span> <span class="comment-user userinfo">Holty</span></div></div></div><div id="comment-tools-13906" class="comment-tools"></div><div class="clear"></div><div id="comment-13906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

