+++
type = "question"
title = "tshark auto shutdown"
description = '''Hi folks; I am automating some tests that use wireshark. I will switching to tshark so the tests can be batched. Each test will perform a capture, perhaps with a unique capture filter. How do I &quot;terminate&quot; the tshark process once I&#x27;ve captured 1000 packets (just an example), so that I can create a n...'''
date = "2012-02-17T08:23:00Z"
lastmod = "2012-02-17T08:41:00Z"
weight = 9095
keywords = [ "automation" ]
aliases = [ "/questions/9095" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark auto shutdown](/questions/9095/tshark-auto-shutdown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9095-score" class="post-score" title="current number of votes">0</div><span id="post-9095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks;</p><p>I am automating some tests that use wireshark. I will switching to tshark so the tests can be batched.</p><p>Each test will perform a capture, perhaps with a unique capture filter. How do I "terminate" the tshark process once I've captured 1000 packets (just an example), so that I can create a new tshark process for my next test ?? If a set a capture filter to "stop capturing" after 1000 packets, will that terminate the tshark process automagically ??</p><p>thanks wk</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-automation" rel="tag" title="see questions tagged &#39;automation&#39;">automation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '12, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/2b12f1f0687101a1dd8f75db884aed8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakelt&#39;s gravatar image" /><p><span>wakelt</span><br />
<span class="score" title="13 reputation points">13</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakelt has no accepted answers">0%</span></p></div></div><div id="comments-container-9095" class="comments-container"></div><div id="comment-tools-9095" class="comment-tools"></div><div class="clear"></div><div id="comment-9095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9096"></span>

<div id="answer-container-9096" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9096-score" class="post-score" title="current number of votes">2</div><span id="post-9096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes.</p><p>e.g. use -c 1000 to stop after 1000 packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '12, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9096" class="comments-container"></div><div id="comment-tools-9096" class="comment-tools"></div><div class="clear"></div><div id="comment-9096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

