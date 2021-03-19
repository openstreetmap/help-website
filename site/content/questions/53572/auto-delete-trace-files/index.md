+++
type = "question"
title = "Auto delete trace files"
description = '''We are having an intermittent issue where clients cannot access a config file on the DB server. I would like to set up Wireshark (v2.0.4) to continually capture because of the randomness of the occurrences. Is there a way to set up a capture that will auto delete the trace files so that they don&#x27;t f...'''
date = "2016-06-20T06:32:00Z"
lastmod = "2016-06-20T06:50:00Z"
weight = 53572
keywords = [ "files", "trace", "delete" ]
aliases = [ "/questions/53572" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Auto delete trace files](/questions/53572/auto-delete-trace-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53572-score" class="post-score" title="current number of votes">0</div><span id="post-53572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having an intermittent issue where clients cannot access a config file on the DB server. I would like to set up Wireshark (v2.0.4) to continually capture because of the randomness of the occurrences. Is there a way to set up a capture that will auto delete the trace files so that they don't fill up a drive while continuously capturing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '16, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/185417827ce6b8cf0d178c19ba78fa81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaysack&#39;s gravatar image" /><p><span>jaysack</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaysack has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '16, 08:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-53572" class="comments-container"></div><div id="comment-tools-53572" class="comment-tools"></div><div class="clear"></div><div id="comment-53572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53574"></span>

<div id="answer-container-53574" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53574-score" class="post-score" title="current number of votes">0</div><span id="post-53574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you'll have to look at <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a>, the capture engine, and feeding it '-b' options to setup a ring buffer. Once you've identified a time where problems occurred pick up that capture file and analyze it. So you'll have a tradeoff between storage size needed vs reaction time to retrieve the capture before it's removed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '16, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53574" class="comments-container"></div><div id="comment-tools-53574" class="comment-tools"></div><div class="clear"></div><div id="comment-53574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

