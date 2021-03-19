+++
type = "question"
title = "Filter With Destination Port"
description = '''Hello, the IP I am connecting to can change, but it always uses 2 destination ports (for example purposes, 00000 and 11111). Let me know what to put in the filter list.'''
date = "2015-04-08T13:47:00Z"
lastmod = "2015-04-09T04:39:00Z"
weight = 41300
keywords = [ "filter", "ip", "destination", "ports" ]
aliases = [ "/questions/41300" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter With Destination Port](/questions/41300/filter-with-destination-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41300-score" class="post-score" title="current number of votes">0</div><span id="post-41300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, the IP I am connecting to can change, but it always uses 2 destination ports (for example purposes, 00000 and 11111).</p><p>Let me know what to put in the filter list.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-ports" rel="tag" title="see questions tagged &#39;ports&#39;">ports</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '15, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/735a10a946b993f50599349073007243?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobTheLawyer&#39;s gravatar image" /><p><span>BobTheLawyer</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobTheLawyer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '15, 14:12</strong> </span></p></div></div><div id="comments-container-41300" class="comments-container"><span id="41301"></span><div id="comment-41301" class="comment"><div id="post-41301-score" class="comment-score"></div><div class="comment-text"><p>What type of filter, capture or display?</p></div><div id="comment-41301-info" class="comment-info"><span class="comment-age">(08 Apr '15, 14:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41302"></span><div id="comment-41302" class="comment"><div id="post-41302-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I'm pretty new. I'm not sure. Here's an image: <a href="http://i.imgur.com/PsT3Eyi.png">http://i.imgur.com/PsT3Eyi.png</a></p></div><div id="comment-41302-info" class="comment-info"><span class="comment-age">(08 Apr '15, 14:26)</span> <span class="comment-user userinfo">BobTheLawyer</span></div></div></div><div id="comment-tools-41300" class="comment-tools"></div><div class="clear"></div><div id="comment-41300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41316"></span>

<div id="answer-container-41316" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41316-score" class="post-score" title="current number of votes">1</div><span id="post-41316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, that's a display filter, it will affect what is displayed, not what is in the capture file. I asked which one because they have different syntax.</p><p>A display filter to filter on certain tcp ports e.g. 1234 and 5678:</p><pre><code>(tcp.port == 1234) or (tcp.port == 5678)</code></pre><p>adjust the port numbers as you require and replace tcp with udp if that's the protocol in use. You can add as many ports as you wish with extra 'or' conditions.</p><p>You can also create a filter by right-clicking on a field in the protocol tree and selecting "Apply as Filter" -&gt; Selected.</p><p>See the wiki page on <a href="https://wiki.wireshark.org/DisplayFilters">Display Filters</a> for more info and links to other sources of information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '15, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41316" class="comments-container"><span id="41320"></span><div id="comment-41320" class="comment"><div id="post-41320-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41320-info" class="comment-info"><span class="comment-age">(09 Apr '15, 04:39)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-41316" class="comment-tools"></div><div class="clear"></div><div id="comment-41316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

