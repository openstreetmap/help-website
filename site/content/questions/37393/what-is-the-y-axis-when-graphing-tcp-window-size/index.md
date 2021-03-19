+++
type = "question"
title = "What is the Y axis when graphing TCP window size?"
description = '''I would like to know what the Y axis represents when I build an I/0 graph based upon TCP window size. When I graph the window size for the Y axis the unit I select is advance. Then for Graph 1 the filter I use filter:ip.src==ServerIP Calc:AVG()tcp.window_size then for graph 2 filter:ip.src==ClientIP...'''
date = "2014-10-28T06:49:00Z"
lastmod = "2014-10-28T10:36:00Z"
weight = 37393
keywords = [ "y", "graph", "io", "axis" ]
aliases = [ "/questions/37393" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the Y axis when graphing TCP window size?](/questions/37393/what-is-the-y-axis-when-graphing-tcp-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37393-score" class="post-score" title="current number of votes">0</div><span id="post-37393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://i59.tinypic.com/2r57myr.png" alt="alt text" />I would like to know what the Y axis represents when I build an I/0 graph based upon TCP window size. When I graph the window size for the Y axis the unit I select is advance. Then for Graph 1 the filter I use filter:ip.src==ServerIP Calc:AVG(<em>)tcp.window_size then for graph 2 filter:ip.src==ClientIP Calc:AVG(</em>)tcp.window_size.</p><p>Secondly shouldn't both the server and the client be fairly close to one another?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-y" rel="tag" title="see questions tagged &#39;y&#39;">y</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-io" rel="tag" title="see questions tagged &#39;io&#39;">io</span> <span class="post-tag tag-link-axis" rel="tag" title="see questions tagged &#39;axis&#39;">axis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '14, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/5b20990cd21bd091665e684410ebe9fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdJ&#39;s gravatar image" /><p><span>EdJ</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdJ has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '14, 08:14</strong> </span></p></div></div><div id="comments-container-37393" class="comments-container"></div><div id="comment-tools-37393" class="comment-tools"></div><div class="clear"></div><div id="comment-37393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37413"></span>

<div id="answer-container-37413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37413-score" class="post-score" title="current number of votes">1</div><span id="post-37413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, it is not necessary for the server and client window sizes to be close to each other. The TCP Window Size is the amount of space currently available in the receive buffer. The receive buffer sizes can differ quite a bit, depending on what the two systems do.</p><p>For example, if the server is a web server, then data will flow primarily <em>from</em> the server <em>to</em> the client. The server only needs a receive buffer large enough for GET requests from the client, but the client needs a receive buffer large enough for the actual web pages that will be downloaded.</p><p>On the other hand, if the server is an FTP server, then it needs a much larger receive buffer in order to handle uploads.</p><p>As long as the window sizes never get so small that communication pauses (usually less than one Maximum Segment Size), then the windows are large enough.</p><p>Maybe it would make more sense to graph the minimum window size, rather than the average.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '14, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-37413" class="comments-container"></div><div id="comment-tools-37413" class="comment-tools"></div><div class="clear"></div><div id="comment-37413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37405"></span>

<div id="answer-container-37405" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37405-score" class="post-score" title="current number of votes">0</div><span id="post-37405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>like to know what the Y axis represents when I build an I/0 graph based upon TCP window size.</p></blockquote><p>That's the average (AVG) <strong>value of the field</strong> you are reporting on, in your example tcp.window_size.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '14, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37405" class="comments-container"></div><div id="comment-tools-37405" class="comment-tools"></div><div class="clear"></div><div id="comment-37405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

