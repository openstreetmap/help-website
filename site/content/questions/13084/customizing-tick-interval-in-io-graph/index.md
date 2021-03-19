+++
type = "question"
title = "Customizing tick interval in IO Graph"
description = '''In IO Graph I would like to use tick interval value other than 0.001/0/0.01/0.1/1/10 second like 0.025 second. Is there an add-on somewhere that allows us to specify our own value or do I need to perhaps request that?'''
date = "2012-07-27T17:02:00Z"
lastmod = "2012-07-30T13:29:00Z"
weight = 13084
keywords = [ "graph", "tick", "io", "interval" ]
aliases = [ "/questions/13084" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Customizing tick interval in IO Graph](/questions/13084/customizing-tick-interval-in-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13084-score" class="post-score" title="current number of votes">0</div><span id="post-13084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In IO Graph I would like to use tick interval value other than 0.001/0/0.01/0.1/1/10 second like 0.025 second. Is there an add-on somewhere that allows us to specify our own value or do I need to perhaps request that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-tick" rel="tag" title="see questions tagged &#39;tick&#39;">tick</span> <span class="post-tag tag-link-io" rel="tag" title="see questions tagged &#39;io&#39;">io</span> <span class="post-tag tag-link-interval" rel="tag" title="see questions tagged &#39;interval&#39;">interval</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '12, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/327a1e6f77d9d54ab928d1b6327da4b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ntwkeng&#39;s gravatar image" /><p><span>ntwkeng</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ntwkeng has no accepted answers">0%</span></p></div></div><div id="comments-container-13084" class="comments-container"></div><div id="comment-tools-13084" class="comment-tools"></div><div class="clear"></div><div id="comment-13084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13130"></span>

<div id="answer-container-13130" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13130-score" class="post-score" title="current number of votes">2</div><span id="post-13130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ntwkeng has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Those values are hard-coded in <a href="http://anonsvn.wireshark.org/wireshark/trunk/ui/gtk/io_stat.c">io_stat.c</a> (look for <code>tick_interval_values</code>). To modify the values a code change is required. As Wireshark is open source, you can <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html">build your own version</a>, with values that fit better in your environment.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '12, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13130" class="comments-container"></div><div id="comment-tools-13130" class="comment-tools"></div><div class="clear"></div><div id="comment-13130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

