+++
type = "question"
title = "trigger the capture"
description = '''Hi there, is it possibe to set a trigger to start the caption? I mean, wireshark is running and waiting for an condition, e.g. a packet to a strange socket, and then starts with captureing in a file (with stop-condition set in the Capture-Interface-Options) or a ringbuffer. Thanks for Your Support, ...'''
date = "2015-12-02T13:33:00Z"
lastmod = "2015-12-02T14:14:00Z"
weight = 48212
keywords = [ "capture", "trigger" ]
aliases = [ "/questions/48212" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [trigger the capture](/questions/48212/trigger-the-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48212-score" class="post-score" title="current number of votes">0</div><span id="post-48212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>is it possibe to set a trigger to start the caption? I mean, wireshark is running and waiting for an condition, e.g. a packet to a strange socket, and then starts with captureing in a file (with stop-condition set in the Capture-Interface-Options) or a ringbuffer.</p><p>Thanks for Your Support, Bernhard Hauser</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-trigger" rel="tag" title="see questions tagged &#39;trigger&#39;">trigger</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/5df15cb7413a11a5897331507b8d9631?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uri&#39;s gravatar image" /><p><span>Uri</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uri has no accepted answers">0%</span></p></div></div><div id="comments-container-48212" class="comments-container"></div><div id="comment-tools-48212" class="comment-tools"></div><div class="clear"></div><div id="comment-48212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48213"></span>

<div id="answer-container-48213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48213-score" class="post-score" title="current number of votes">0</div><span id="post-48213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, that's currently not possible. Wireshark has no "observer" mode where it can look for packet conditions without capturing them, and then start to capture when something happens. It <strong>always</strong> captures packets to inspect them. So what you could try to do is have Wireshark (or better: dumpcap) do a ring buffer capture, read the capture files when they're closed (on move to the next) and then check for the condition you want. If you find it, terminate the dumpcap process.</p><p>See the similar question about that here: <a href="https://ask.wireshark.org/questions/48119/stop-the-trace-from-external-event">https://ask.wireshark.org/questions/48119/stop-the-trace-from-external-event</a></p><p>You'll have to figure out the "process complete capture files and then terminate dumpcap" script yourself though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-48213" class="comments-container"><span id="48214"></span><div id="comment-48214" class="comment"><div id="post-48214-score" class="comment-score"></div><div class="comment-text"><p>OK, I understand. Do You know if the trigger-funktion or "observer" will ever come? Danke Uri!</p></div><div id="comment-48214-info" class="comment-info"><span class="comment-age">(02 Dec '15, 14:14)</span> <span class="comment-user userinfo">Uri</span></div></div></div><div id="comment-tools-48213" class="comment-tools"></div><div class="clear"></div><div id="comment-48213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

