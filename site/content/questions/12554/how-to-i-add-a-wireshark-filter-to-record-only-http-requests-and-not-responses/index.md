+++
type = "question"
title = "How to I add a wireshark filter to record only HTTP requests and not responses?"
description = '''How to I add a filter to record only HTTP requests and not responses?'''
date = "2012-07-10T05:01:00Z"
lastmod = "2012-07-11T07:16:00Z"
weight = 12554
keywords = [ "include" ]
aliases = [ "/questions/12554" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to I add a wireshark filter to record only HTTP requests and not responses?](/questions/12554/how-to-i-add-a-wireshark-filter-to-record-only-http-requests-and-not-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12554-score" class="post-score" title="current number of votes">0</div><span id="post-12554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to I add a filter to record only HTTP requests and not responses?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-include" rel="tag" title="see questions tagged &#39;include&#39;">include</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '12, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/63c50004c4f6eaf3235b9ea836f4b6cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sorin&#39;s gravatar image" /><p><span>sorin</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sorin has no accepted answers">0%</span></p></div></div><div id="comments-container-12554" class="comments-container"></div><div id="comment-tools-12554" class="comment-tools"></div><div class="clear"></div><div id="comment-12554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12633"></span>

<div id="answer-container-12633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12633-score" class="post-score" title="current number of votes">0</div><span id="post-12633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>filter to <strong>RECORD</strong> only HTTP requests</p></blockquote><p>well, that's not easy. One option would be to use tshark</p><blockquote><p><code>tshark -i eth0 (or 1,2,3,4... on windows) -R "http.request"</code><br />
</p></blockquote><p>However that will only print the result to STDOUT. You cannot write a pcap file with -w, at least not with the current releases of tshark/wireshark.</p><p>However, with a little "trick", you can import the tshark output.</p><blockquote><p><code>tshark -i eth0 (or 1,2,3,4... on windows) -R "http.request" -x &gt; http_request.txt</code><br />
</p></blockquote><p>In Wireshark</p><blockquote><p><code>File -&gt; Import</code><br />
</p></blockquote><p>Select <a href="http://http_request.txt">http_request.txt</a> and you will get only the requests in Wireshark.</p><p>HOWEVER: I would rather capture everything and then (later) use a display filter (<code>http.request</code>) in Wireshark to only display the http requests. Maybe you want to know the answer for <strong>some</strong> requests ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '12, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jul '12, 07:39</strong> </span></p></div></div><div id="comments-container-12633" class="comments-container"></div><div id="comment-tools-12633" class="comment-tools"></div><div class="clear"></div><div id="comment-12633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

