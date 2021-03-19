+++
type = "question"
title = "throughput filter"
description = '''i want to ask about filter wireshark uses to draw throughput graph is it frame.len or tcp.analysis.bytes_in_flight  i want the filter that shows values in throughput graph thank you '''
date = "2015-05-16T07:12:00Z"
lastmod = "2015-05-20T01:22:00Z"
weight = 42437
keywords = [ "throughput" ]
aliases = [ "/questions/42437" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [throughput filter](/questions/42437/throughput-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42437-score" class="post-score" title="current number of votes">0</div><span id="post-42437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to ask about filter wireshark uses to draw throughput graph</p><p>is it frame.len or tcp.analysis.bytes_in_flight</p><p>i want the filter that shows values in throughput graph thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '15, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p><span>shady</span><br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span></p></div></div><div id="comments-container-42437" class="comments-container"><span id="42455"></span><div id="comment-42455" class="comment"><div id="post-42455-score" class="comment-score"></div><div class="comment-text"><p>which throughput graph are you talking about? Statistics -&gt; IO Graph and then Bits/tick?</p></div><div id="comment-42455-info" class="comment-info"><span class="comment-age">(17 May '15, 06:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-42437" class="comment-tools"></div><div class="clear"></div><div id="comment-42437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42439"></span>

<div id="answer-container-42439" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42439-score" class="post-score" title="current number of votes">1</div><span id="post-42439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shady has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not a display filter, it is a function in tcp_graph.C. It uses the TCP segment length and the TCP delta time. You can also look at Statistics &gt; Summary for average bytes/sec.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '15, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-42439" class="comments-container"><span id="42451"></span><div id="comment-42451" class="comment"><div id="post-42451-score" class="comment-score"></div><div class="comment-text"><p>thank you but i wanted a filter gives me the same values appear in throughput graph in order to use it in tshark and extract these numbers in one column in csv file</p><p>i think its frame.len ???</p></div><div id="comment-42451-info" class="comment-info"><span class="comment-age">(17 May '15, 03:50)</span> <span class="comment-user userinfo">shady</span></div></div><span id="42472"></span><div id="comment-42472" class="comment"><div id="post-42472-score" class="comment-score"></div><div class="comment-text"><p>From where do you have the ideea with frame.len? TCP segment length is tcp.len</p></div><div id="comment-42472-info" class="comment-info"><span class="comment-age">(17 May '15, 12:49)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="42570"></span><div id="comment-42570" class="comment"><div id="post-42570-score" class="comment-score"></div><div class="comment-text"><p>i compared values appeared in graph with values in frame.len</p><p>i will confirm this point</p></div><div id="comment-42570-info" class="comment-info"><span class="comment-age">(20 May '15, 01:22)</span> <span class="comment-user userinfo">shady</span></div></div></div><div id="comment-tools-42439" class="comment-tools"></div><div class="clear"></div><div id="comment-42439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

