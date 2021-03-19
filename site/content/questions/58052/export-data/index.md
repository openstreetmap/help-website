+++
type = "question"
title = "export data"
description = '''Hi, I need to export the data from my capture. I am aware of follow the stream, save as. It works fine for small captures. If the capture is big this operation will never end. Can this operation be done as the batch? I hope for better performance.. If yes, can you advise the exact command and parame...'''
date = "2016-12-13T13:23:00Z"
lastmod = "2017-01-04T10:06:00Z"
weight = 58052
keywords = [ "follow", "the", "save", "as", "stream" ]
aliases = [ "/questions/58052" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [export data](/questions/58052/export-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58052-score" class="post-score" title="current number of votes">0</div><span id="post-58052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to export the data from my capture. I am aware of follow the stream, save as. It works fine for small captures. If the capture is big this operation will never end. Can this operation be done as the batch? I hope for better performance.. If yes, can you advise the exact command and parameter? thx Bob</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-the" rel="tag" title="see questions tagged &#39;the&#39;">the</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-as" rel="tag" title="see questions tagged &#39;as&#39;">as</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '16, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/4fd61c766c3399bb02b9b6813dff660b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cz50344&#39;s gravatar image" /><p><span>cz50344</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cz50344 has no accepted answers">0%</span></p></div></div><div id="comments-container-58052" class="comments-container"></div><div id="comment-tools-58052" class="comment-tools"></div><div class="clear"></div><div id="comment-58052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58500"></span>

<div id="answer-container-58500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58500-score" class="post-score" title="current number of votes">1</div><span id="post-58500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may want to check out the <code>tshark</code> option <code>-z follow</code>. For example to follow TCP stream 1 and store the raw data you could run <code>tshark -z follow,tcp,raw,1 [-r /path/to/file]</code>. Check out the <code>tshark</code> <a href="https://www.wireshark.org/docs/man-pages/tshark.html">man page</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58500" class="comments-container"><span id="58503"></span><div id="comment-58503" class="comment"><div id="post-58503-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>it is almost perfect answer. Thanks for it.</p><p>Now - Can we extract only one direction? I have tried this, but it does not work. I am not able to filter for only one direction.</p><pre><code>tshark -z follow,tcp,raw,((ip.src eq 9.138.236.197 and tcp.srcport eq 39647) and (ip.dst eq 9.138.236.247 and tcp.dstport eq 2501)) -r qsysprt.trccnn.cap -w oout.pcl</code></pre><p>Thanks</p><p>Bob</p></div><div id="comment-58503-info" class="comment-info"><span class="comment-age">(04 Jan '17, 09:21)</span> <span class="comment-user userinfo">cz50344</span></div></div><span id="58505"></span><div id="comment-58505" class="comment"><div id="post-58505-score" class="comment-score"></div><div class="comment-text"><p>The filter in this case is there to select the stream not to select the direction. I think you'll need to post-process the data using the fact that, as the man page says: <code>The data sent by the second node is prefixed with a tab to differentiate it from the data sent by the first node.</code></p><p>BTW, don't forget to accept the answer (if it answers your question) by clicking on the checkbox next to it--see the FAQ for details.</p></div><div id="comment-58505-info" class="comment-info"><span class="comment-age">(04 Jan '17, 10:06)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-58500" class="comment-tools"></div><div class="clear"></div><div id="comment-58500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

