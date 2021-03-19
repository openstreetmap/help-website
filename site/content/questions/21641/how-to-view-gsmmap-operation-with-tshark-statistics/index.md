+++
type = "question"
title = "how to view GSM/MAP Operation with tshark statistics"
description = '''I want to view statistics with tshark command the same way it&#x27;s done on Wireshark with GSM/MAP Operation Statistics window, which is on Telephony-&amp;gt;GSM-&amp;gt;GSM/MAP Operation. When I view tshark -z help I see only sctp or gsm_a, which are not equal to MAP operation statistics. Can anyone help with ...'''
date = "2013-05-31T01:37:00Z"
lastmod = "2013-05-31T20:06:00Z"
weight = 21641
keywords = [ "statistics", "gsm", "tshark", "gsm_map" ]
aliases = [ "/questions/21641" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to view GSM/MAP Operation with tshark statistics](/questions/21641/how-to-view-gsmmap-operation-with-tshark-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21641-score" class="post-score" title="current number of votes">1</div><span id="post-21641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to view statistics with <em>tshark</em> command the same way it's done on <em>Wireshark</em> with <em>GSM/MAP Operation Statistics</em> window, which is on <em>Telephony-&gt;GSM-&gt;GSM/MAP Operation</em>. When I view <strong>tshark -z help</strong> I see only sctp or gsm_a, which are not equal to MAP operation statistics.</p><p>Can anyone help with this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-gsm_map" rel="tag" title="see questions tagged &#39;gsm_map&#39;">gsm_map</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '13, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Nov '13, 16:02</strong> </span></p></div></div><div id="comments-container-21641" class="comments-container"></div><div id="comment-tools-21641" class="comment-tools"></div><div class="clear"></div><div id="comment-21641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21684"></span>

<div id="answer-container-21684" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21684-score" class="post-score" title="current number of votes">1</div><span id="post-21684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Edmond has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know for certain but I think the answer is going to be that not all statistics functions available in Wireshark are available in Tshark's -z options. When I needed an automated method of grabbing MAP statistics a few months ago, for lack of any other answer my solution was to set up a series of tshark -R queries on gsm_old.localValue, pipe them to a 'grep -c' command and use the output of that as a counter for the number of that operation code found in the trace.</p><p>Since the MAP traffic in that particular case was extremely light that solution worked well and was something I was able to put together in a few dozen lines of a perl script. If tshark itself has a better solution I'd be interested in the other answers here though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '13, 20:06</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '13, 20:07</strong> </span></p></div></div><div id="comments-container-21684" class="comments-container"></div><div id="comment-tools-21684" class="comment-tools"></div><div class="clear"></div><div id="comment-21684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

