+++
type = "question"
title = "Some stats questions"
description = '''I&#x27;m trying to do the following but having some problems. Could someone give me some hints:  How do I graph the total number of http 200 response codes compared to http 500 response codes in the trace? Same as above but only if those responses were for GET requests? Actually is there a way to display...'''
date = "2013-06-29T01:13:00Z"
lastmod = "2013-06-30T00:04:00Z"
weight = 22464
keywords = [ "statistics" ]
aliases = [ "/questions/22464" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Some stats questions](/questions/22464/some-stats-questions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22464-score" class="post-score" title="current number of votes">0</div><span id="post-22464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to do the following but having some problems. Could someone give me some hints:</p><ul><li>How do I graph the total number of http 200 response codes compared to http 500 response codes in the trace?</li><li>Same as above but only if those responses were for GET requests? Actually is there a way to display complete streams in the trace which had a GET request?</li><li>in the stats io graphs - can it filter a particular tcp stream? what I see is it applies on the whole trace.</li></ul><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '13, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/3e7d3a929b8db7c975caea8dfe94feac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brumik&#39;s gravatar image" /><p><span>brumik</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brumik has no accepted answers">0%</span></p></div></div><div id="comments-container-22464" class="comments-container"></div><div id="comment-tools-22464" class="comment-tools"></div><div class="clear"></div><div id="comment-22464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22474"></span>

<div id="answer-container-22474" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22474-score" class="post-score" title="current number of votes">0</div><span id="post-22474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For the questions in your first bullet point, for one line in the IO graph, use the following display filter to catch all response codes in the 5xx range:</p><p>http.response.code &gt;499 &amp;&amp; http.response.code &lt; 600</p><p>Then for a second line, apply this to get all 200-range codes:</p><p>http.response.code &gt;199 &amp;&amp; http.response.code &lt; 300</p><p>For your second bullet point, take the above display filters, contain them within brackets and add a "&amp;&amp;" followed by whatever else you want to use to uniquely identify one type of server response compared to others. It's really quite flexible.</p><p>For the third bullet point, you can filter on TCP streams by adding the filter statement " &amp;&amp; tcp.stream==x" where "x" is the stream number for that particular stream. Again, you can combine display filters in that IO graph in an and/or fashion to filter on just what you want it to display.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '13, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-22474" class="comments-container"><span id="22480"></span><div id="comment-22480" class="comment"><div id="post-22480-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response. The IO graphs work on the streams as you mentioned I realized that I was not seeing anything as I had to unselect the default graph1 otherwise the scale is wrong. I also wanted just a summary count of the total responses in the trace. In the http packet counter feature I see similar stats but they cannot be customized for GET requests only.</p><p>I think it may be a bit tricky to filter on the response but only if the request for that response was a GET packet as it would require to look at the previous request packet in the stream was a GET requests only (as opposed to a POST or other http request method) Not sure if there is another feature/method to do this. Perhaps another way would be to remove all TCP streams/sessions which do not have http GET method, can you do this in wireshark?</p></div><div id="comment-22480-info" class="comment-info"><span class="comment-age">(30 Jun '13, 00:04)</span> <span class="comment-user userinfo">brumik</span></div></div></div><div id="comment-tools-22474" class="comment-tools"></div><div class="clear"></div><div id="comment-22474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

