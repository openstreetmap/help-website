+++
type = "question"
title = "Hide partial TCP packets"
description = '''How can I hide all the &quot;TCP segment of a reassembled PDU&quot; in the display? I only want to see the final reassembled ones (as well as non-TCP traffic)'''
date = "2015-10-28T03:43:00Z"
lastmod = "2015-10-28T04:16:00Z"
weight = 47011
keywords = [ "tcp" ]
aliases = [ "/questions/47011" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Hide partial TCP packets](/questions/47011/hide-partial-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47011-score" class="post-score" title="current number of votes">0</div><span id="post-47011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I hide all the "TCP segment of a reassembled PDU" in the display? I only want to see the final reassembled ones (as well as non-TCP traffic)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/5348f77500c08a662088203ef1b4be27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baruch%20Burstein&#39;s gravatar image" /><p><span>Baruch Burstein</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baruch Burstein has no accepted answers">0%</span></p></div></div><div id="comments-container-47011" class="comments-container"></div><div id="comment-tools-47011" class="comment-tools"></div><div class="clear"></div><div id="comment-47011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47012"></span>

<div id="answer-container-47012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47012-score" class="post-score" title="current number of votes">0</div><span id="post-47012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I were you, I would use this filter:<br />
</p><pre><code>tcp.reassembled.data or !tcp or !tcp.segment_data </code></pre><p>It shows all tcp packets, which don´t use reassembling, the reassembled summary Frames and all non tcp traffic.</p><hr /><p>Update:<br />
If you only want to see the reassembled tcp and all non tcp traffic than you can use this filter:<br />
</p><pre><code>tcp.reassembled.data or !tcp </code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '15, 04:20</strong> </span></p></div></div><div id="comments-container-47012" class="comments-container"></div><div id="comment-tools-47012" class="comment-tools"></div><div class="clear"></div><div id="comment-47012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

