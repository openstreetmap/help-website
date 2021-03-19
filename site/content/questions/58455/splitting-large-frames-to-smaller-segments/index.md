+++
type = "question"
title = "splitting large frames to smaller segments"
description = '''I have a trace in which some packets size is greater than 1500; is there any utility that splits these packets to smaller segments (with max size of 1500)?'''
date = "2017-01-01T23:09:00Z"
lastmod = "2017-01-02T12:29:00Z"
weight = 58455
keywords = [ "segment" ]
aliases = [ "/questions/58455" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [splitting large frames to smaller segments](/questions/58455/splitting-large-frames-to-smaller-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58455-score" class="post-score" title="current number of votes">0</div><span id="post-58455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace in which some packets size is greater than 1500; is there any utility that splits these packets to smaller segments (with max size of 1500)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '17, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-58455" class="comments-container"></div><div id="comment-tools-58455" class="comment-tools"></div><div class="clear"></div><div id="comment-58455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58459"></span>

<div id="answer-container-58459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58459-score" class="post-score" title="current number of votes">0</div><span id="post-58459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TCP replay, or more accurately <a href="http://tcpreplay.synfin.net/wiki/tcprewrite">tcprewrite</a> may be helpful here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '17, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58459" class="comments-container"><span id="58466"></span><div id="comment-58466" class="comment"><div id="post-58466-score" class="comment-score"></div><div class="comment-text"><p>hi, you are right. I want to use the tcprewrite command: tcprewrite --fragroute=frag.cfg --infile=input.pcap --outfile=output.pcap but I have no "fragroute" option. it is stated that it is available from v3.3.0 and I am using 4.1.1</p><p>do you have any idea why this is not available?</p></div><div id="comment-58466-info" class="comment-info"><span class="comment-age">(02 Jan '17, 12:21)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="58467"></span><div id="comment-58467" class="comment"><div id="post-58467-score" class="comment-score"></div><div class="comment-text"><p>No, never used it for this. Maybe another forum is more appropriate for that question.</p></div><div id="comment-58467-info" class="comment-info"><span class="comment-age">(02 Jan '17, 12:29)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-58459" class="comment-tools"></div><div class="clear"></div><div id="comment-58459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

