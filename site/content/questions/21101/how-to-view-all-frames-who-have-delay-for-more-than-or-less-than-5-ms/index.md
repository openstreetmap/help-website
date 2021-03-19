+++
type = "question"
title = "how to view all frames who have delay for more than or less than 5 ms."
description = '''how to view all frames who have delay for more than or less than 5 ms?'''
date = "2013-05-13T02:28:00Z"
lastmod = "2013-05-13T03:00:00Z"
weight = 21101
keywords = [ "timestamp", "delta" ]
aliases = [ "/questions/21101" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to view all frames who have delay for more than or less than 5 ms.](/questions/21101/how-to-view-all-frames-who-have-delay-for-more-than-or-less-than-5-ms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21101-score" class="post-score" title="current number of votes">0</div><span id="post-21101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to view all frames who have delay for more than or less than 5 ms?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-delta" rel="tag" title="see questions tagged &#39;delta&#39;">delta</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '13, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21101" class="comments-container"></div><div id="comment-tools-21101" class="comment-tools"></div><div class="clear"></div><div id="comment-21101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21102"></span>

<div id="answer-container-21102" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21102-score" class="post-score" title="current number of votes">1</div><span id="post-21102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kishan pandey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try filtering on "frame.time_delta &lt; 0.005" (or "&gt; 0.005" respectively), but very often that is only giving you a list of frames that is too large and not really telling you anything. Especially in cases where one side (the client) is interactive you end up with tons of "long" delays due to user inactivity.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '13, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21102" class="comments-container"><span id="21104"></span><div id="comment-21104" class="comment"><div id="post-21104-score" class="comment-score"></div><div class="comment-text"><p>yes i tried frame.time_delta le 0.005 but the result is not accurate,it still showed some frames with value higher than filtered.</p></div><div id="comment-21104-info" class="comment-info"><span class="comment-age">(13 May '13, 02:37)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="21105"></span><div id="comment-21105" class="comment"><div id="post-21105-score" class="comment-score"></div><div class="comment-text"><p>do you have delta times displayed in one of your columns, and if so, do you use "Seconds since previous captured packet" or "Seconds since previous displayed packet"? If you used "displayed" packet you'll end up with larger delta times because the filter I mentioned works on captured frames. You can verify this by setting your column to "since previous captured frame" instead.</p></div><div id="comment-21105-info" class="comment-info"><span class="comment-age">(13 May '13, 02:44)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="21106"></span><div id="comment-21106" class="comment"><div id="post-21106-score" class="comment-score"></div><div class="comment-text"><p>thankx jasper can we calculate udp latency with this summary details from wireshark which is total packet =201592 , avg packets/sec - 324.132 ,Avg.packet size - 1.47 mbits/s,time between 1st and last packet - 621 second. Thankx</p></div><div id="comment-21106-info" class="comment-info"><span class="comment-age">(13 May '13, 02:44)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="21107"></span><div id="comment-21107" class="comment"><div id="post-21107-score" class="comment-score"></div><div class="comment-text"><p>I would usually determine udp latency by looking at the time from request to response, but that is a tedious process to do that for all packets and the summary won't help with it.</p></div><div id="comment-21107-info" class="comment-info"><span class="comment-age">(13 May '13, 02:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="21108"></span><div id="comment-21108" class="comment"><div id="post-21108-score" class="comment-score"></div><div class="comment-text"><p>but in our case it is just way traffic.</p></div><div id="comment-21108-info" class="comment-info"><span class="comment-age">(13 May '13, 02:58)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="21109"></span><div id="comment-21109" class="comment not_top_scorer"><div id="post-21109-score" class="comment-score"></div><div class="comment-text"><p>great after changing to Seconds since previous captured packet it worked perfectly.Thanks a lot.</p></div><div id="comment-21109-info" class="comment-info"><span class="comment-age">(13 May '13, 03:00)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-21102" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-21102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

