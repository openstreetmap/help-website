+++
type = "question"
title = "How to filter data based on the message body?"
description = '''Hi I am trying to use WireShark to capture packets that being transmitted between server 10.0.4.18 to 10.0.4.44 and the respond coming from 10.0.4.44 to 10.0.4.18 to each request. I used the following filter to narrow down the results http &amp;amp;&amp;amp; ( (ip.dst == 10.0.4.44 ) || (ip.dst == 10.0.4.18 ...'''
date = "2015-09-02T16:46:00Z"
lastmod = "2015-09-02T21:59:00Z"
weight = 45607
keywords = [ "filter", "capture", "capture-filter", "wireshark" ]
aliases = [ "/questions/45607" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter data based on the message body?](/questions/45607/how-to-filter-data-based-on-the-message-body)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45607-score" class="post-score" title="current number of votes">0</div><span id="post-45607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am trying to use WireShark to capture packets that being transmitted between server <code>10.0.4.18</code> to <code>10.0.4.44</code> and the respond coming from <code>10.0.4.44</code> to <code>10.0.4.18</code> to each request.</p><p>I used the following filter to narrow down the results</p><pre><code>http &amp;&amp; ( (ip.dst == 10.0.4.44 ) || (ip.dst == 10.0.4.18  ) ) &amp;&amp; frame.time &gt; &quot;2015-09-02 13:00:40.0000&quot;  &amp;&amp; frame.time &lt; &quot;2015-09-02 13:20:50.0000&quot; &amp;&amp; http.response.code !=  200 &amp;&amp; http.response.code !=  201 &amp;&amp; http.response.code !=  202</code></pre><p>All I am looking for is a packet that contains the following string in its respond body</p><blockquote><p>A session cookie was expected in the request, but not found.</p></blockquote><p>But I can't find a way to see the message body unless I right click on each packet and select "Follow TCP Stream."</p><p>How to filter down the results based on a part of the message body?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '15, 16:46</strong></p><img src="https://secure.gravatar.com/avatar/269c87e90f1b9b186fe6b96bf41643bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20A&#39;s gravatar image" /><p><span>Mike A</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike A has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Sep '15, 16:47</strong> </span></p></div></div><div id="comments-container-45607" class="comments-container"></div><div id="comment-tools-45607" class="comment-tools"></div><div class="clear"></div><div id="comment-45607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45609"></span>

<div id="answer-container-45609" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45609-score" class="post-score" title="current number of votes">1</div><span id="post-45609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mike A has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try display filter <code>tcp contains "cookie was expected"</code> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '15, 21:59</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-45609" class="comments-container"></div><div id="comment-tools-45609" class="comment-tools"></div><div class="clear"></div><div id="comment-45609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

