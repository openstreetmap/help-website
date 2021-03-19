+++
type = "question"
title = "File size limit on TShark?"
description = '''I have been attempting to capture a high volume of multicast traffic for a week now using TShark. The process always unexpectedly terminates. The captures start at various times of the day. Trying to figure out what is going on, I noticed that the capture files almost always are just short of 40GB i...'''
date = "2011-10-10T11:15:00Z"
lastmod = "2015-04-20T06:25:00Z"
weight = 6835
keywords = [ "limit", "tshark", "filesize" ]
aliases = [ "/questions/6835" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [File size limit on TShark?](/questions/6835/file-size-limit-on-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6835-score" class="post-score" title="current number of votes">0</div><span id="post-6835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been attempting to capture a high volume of multicast traffic for a week now using TShark. The process always unexpectedly terminates. The captures start at various times of the day.</p><p>Trying to figure out what is going on, I noticed that the capture files almost always are just short of 40GB in size when TShark terminates. It appears to be the one constant I've found in the problem.</p><p>Is there a file size limit in TShark, or should I be looking elsewhere for the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-filesize" rel="tag" title="see questions tagged &#39;filesize&#39;">filesize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '11, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/bc7ef38c9fb207c34f2903fe2876744d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chuu&#39;s gravatar image" /><p><span>Chuu</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chuu has no accepted answers">0%</span></p></div></div><div id="comments-container-6835" class="comments-container"><span id="41598"></span><div id="comment-41598" class="comment"><div id="post-41598-score" class="comment-score"></div><div class="comment-text"><p>try to limit the size of the trace file - tshark -b filesize:100 - this will close and open a new file after 100 Kb reached</p></div><div id="comment-41598-info" class="comment-info"><span class="comment-age">(20 Apr '15, 05:24)</span> <span class="comment-user userinfo">HiB</span></div></div></div><div id="comment-tools-6835" class="comment-tools"></div><div class="clear"></div><div id="comment-6835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6836"></span>

<div id="answer-container-6836" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6836-score" class="post-score" title="current number of votes">2</div><span id="post-6836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Chuu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think it's not a hard coded limit, but TShark seems to run out of ressources over time.</p><p>You should try to capture using dumpcap instead, and go for a multi capture setup - meaning, write smaller trace files and open a new one when the limit is reached. Usually I go for 32MB or 64MB files, which allows easily opening them in Wireshark afterwards.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '11, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6836" class="comments-container"><span id="41599"></span><div id="comment-41599" class="comment"><div id="post-41599-score" class="comment-score"></div><div class="comment-text"><p>Come on <span>@Jasper</span>, point to the canonical reference on Wireshark\tshark out of memory issues on your blog: <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div id="comment-41599-info" class="comment-info"><span class="comment-age">(20 Apr '15, 05:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41600"></span><div id="comment-41600" class="comment"><div id="post-41600-score" class="comment-score"></div><div class="comment-text"><p>lol <span>@grahamb</span>, this is a really old post from 4 years ago. There was no blog back then :-)</p><p>BTW, most blog hits are for "Spurious retransmission", by far ;-)</p></div><div id="comment-41600-info" class="comment-info"><span class="comment-age">(20 Apr '15, 06:25)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-6836" class="comment-tools"></div><div class="clear"></div><div id="comment-6836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

