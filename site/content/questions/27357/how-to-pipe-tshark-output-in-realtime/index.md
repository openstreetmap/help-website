+++
type = "question"
title = "How to pipe tshark output in realtime?"
description = '''Hi everyone, I am monitoring wifi traffic and want to process every output line in real time. Monitoring works: sudo tshark -i mon0 subtype probereq  Saving to a file works: sudo tshark -i mon0 subtype probereq &amp;gt; pcap.log  Piping file for processing works: cat pcap.log | while read -r line; do ec...'''
date = "2013-11-25T10:56:00Z"
lastmod = "2013-11-25T11:49:00Z"
weight = 27357
keywords = [ "pipe", "piping", "tshark", "real-time" ]
aliases = [ "/questions/27357" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to pipe tshark output in realtime?](/questions/27357/how-to-pipe-tshark-output-in-realtime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27357-score" class="post-score" title="current number of votes">0</div><span id="post-27357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I am monitoring wifi traffic and want to process every output line in real time.</p><p>Monitoring works:</p><pre><code>sudo tshark -i mon0 subtype probereq</code></pre><p>Saving to a file works:</p><pre><code>sudo tshark -i mon0 subtype probereq &gt; pcap.log</code></pre><p>Piping file for processing works:</p><pre><code>cat pcap.log | while read -r line; do echo &quot;$line&quot;; done</code></pre><p>But piping thark output directly just doesn't work:</p><pre><code>sudo tshark -i mon0 subtype probereq | while read -r line; do echo &quot;$line&quot;; done</code></pre><p>What's the problem? How can I process every line of tshark output in real time?</p><p>Cheers bluepuma</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-piping" rel="tag" title="see questions tagged &#39;piping&#39;">piping</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-real-time" rel="tag" title="see questions tagged &#39;real-time&#39;">real-time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/32c462091397574f96fe6842367dbae5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bluepuma&#39;s gravatar image" /><p><span>bluepuma</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bluepuma has no accepted answers">0%</span></p></div></div><div id="comments-container-27357" class="comments-container"></div><div id="comment-tools-27357" class="comment-tools"></div><div class="clear"></div><div id="comment-27357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27359"></span>

<div id="answer-container-27359" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27359-score" class="post-score" title="current number of votes">1</div><span id="post-27359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bluepuma has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark output is buffered. Please use tshark option -l, if you want tshark to flush STDOUT after every packet.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '13, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27359" class="comments-container"><span id="27360"></span><div id="comment-27360" class="comment"><div id="post-27360-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that was easy</p></div><div id="comment-27360-info" class="comment-info"><span class="comment-age">(25 Nov '13, 11:49)</span> <span class="comment-user userinfo">bluepuma</span></div></div></div><div id="comment-tools-27359" class="comment-tools"></div><div class="clear"></div><div id="comment-27359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

