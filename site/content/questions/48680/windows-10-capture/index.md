+++
type = "question"
title = "Windows 10 Capture"
description = '''Okay i&#x27;m using wireshark for the first time and i need it for my thesis, so i wanted to ask if there is a possibility too use a filter for windows so i can see all connections from windows to windows '''
date = "2015-12-22T23:40:00Z"
lastmod = "2015-12-24T10:36:00Z"
weight = 48680
keywords = [ "windows", "10", "connections" ]
aliases = [ "/questions/48680" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows 10 Capture](/questions/48680/windows-10-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48680-score" class="post-score" title="current number of votes">0</div><span id="post-48680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Okay i'm using wireshark for the first time and i need it for my thesis, so i wanted to ask if there is a possibility too use a filter for windows so i can see all connections from windows to windows</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-10" rel="tag" title="see questions tagged &#39;10&#39;">10</span> <span class="post-tag tag-link-connections" rel="tag" title="see questions tagged &#39;connections&#39;">connections</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '15, 23:40</strong></p><img src="https://secure.gravatar.com/avatar/d88e82c72984517b96ca5c9870db1907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="plonerich&#39;s gravatar image" /><p><span>plonerich</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="plonerich has no accepted answers">0%</span></p></div></div><div id="comments-container-48680" class="comments-container"><span id="48700"></span><div id="comment-48700" class="comment"><div id="post-48700-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "windows to windows". Wireshark has filters for network protocols and endpoints, not host OSs.</p></div><div id="comment-48700-info" class="comment-info"><span class="comment-age">(24 Dec '15, 07:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48680" class="comment-tools"></div><div class="clear"></div><div id="comment-48680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48701"></span>

<div id="answer-container-48701" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48701-score" class="post-score" title="current number of votes">0</div><span id="post-48701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is not possible to see only the traffic for Windows to Windows because there are no filters in wireshark for OSes but if you <strong>capturing from live wire and you are allowed to scan the network</strong> you can use <strong>nmap</strong> first to find out IP address of all windows host and then use capture filter to capture traffic for only windows endpoints.</p><p>with nmap you can find the OS of the machine by using following command</p><pre><code>nmap -v -O --osscan-guess 192.168.1.0/24</code></pre><p>Then you can use the capture or display filters for to display the traffic of windows endpoints</p><p>sorry for my bad English</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '15, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/0032ac169dfa9b4487cca759adaf8097?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muhammad%20Irshad&#39;s gravatar image" /><p><span>Muhammad Irshad</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muhammad Irshad has no accepted answers">0%</span></p></div></div><div id="comments-container-48701" class="comments-container"></div><div id="comment-tools-48701" class="comment-tools"></div><div class="clear"></div><div id="comment-48701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

