+++
type = "question"
title = "How can I set the &#x27;Service Response Time&#x27;"
description = '''There is a pcap file which contains MEGACO packets. I want to know the Service Response Time, but when I Statistics--&amp;gt;Service Response Time--&amp;gt;MEGACO,there is a windows ask me to input the Filter. I don&#x27;t know which filter I should input, and if I put &#x27;ip&#x27; in the Filter and then click &#x27;Create S...'''
date = "2015-07-06T05:58:00Z"
lastmod = "2015-07-06T09:41:00Z"
weight = 43886
keywords = [ "time", "service", "megaco", "response" ]
aliases = [ "/questions/43886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I set the 'Service Response Time'](/questions/43886/how-can-i-set-the-service-response-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43886-score" class="post-score" title="current number of votes">0</div><span id="post-43886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is a pcap file which contains MEGACO packets. I want to know the Service Response Time, but when I Statistics--&gt;Service Response Time--&gt;MEGACO,there is a windows ask me to input the Filter. I don't know which filter I should input, and if I put 'ip' in the Filter and then click 'Create Stat', it says 'Track Context option at Protocols-&gt;MEGACO and Protocols-&gt;H248 preferences has to be set to true to enable measurement of service response times. How should I do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-service" rel="tag" title="see questions tagged &#39;service&#39;">service</span> <span class="post-tag tag-link-megaco" rel="tag" title="see questions tagged &#39;megaco&#39;">megaco</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '15, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/d22c73a5cdc761f2d9bff983a5d8232d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="telnetp&#39;s gravatar image" /><p><span>telnetp</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="telnetp has no accepted answers">0%</span></p></div></div><div id="comments-container-43886" class="comments-container"><span id="43887"></span><div id="comment-43887" class="comment"><div id="post-43887-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/MEGACO.png" alt="alt text" /></p><p>I also attach the screen.</p></div><div id="comment-43887-info" class="comment-info"><span class="comment-age">(06 Jul '15, 05:59)</span> <span class="comment-user userinfo">telnetp</span></div></div></div><div id="comment-tools-43886" class="comment-tools"></div><div class="clear"></div><div id="comment-43886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43894"></span>

<div id="answer-container-43894" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43894-score" class="post-score" title="current number of votes">0</div><span id="post-43894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to Edit &gt; Preferences &gt; Protocols &gt; MEGACO and check "Track Context."</p><p>Go to Edit &gt; Preferences &gt; Protocols &gt; H248 and check "Track Context."</p><p>You can leave the filter field blank, in which case Wireshark will plot the response time for all MEGACO packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></img></div></div><div id="comments-container-43894" class="comments-container"></div><div id="comment-tools-43894" class="comment-tools"></div><div class="clear"></div><div id="comment-43894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

