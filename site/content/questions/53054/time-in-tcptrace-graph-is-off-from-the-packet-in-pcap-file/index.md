+++
type = "question"
title = "time in tcptrace graph is off from the packet in pcap file"
description = '''Hello, I am trying to understand the tcptrace graph. I noticed that in packet captures if i zoom into a tcp trace graph, time shown in graph is different than what it is in pcap. e.g. when i click on the highlighted tcp segment, in pcap file packet @ 23.3220300 is selected but in graph its showing t...'''
date = "2016-05-30T11:45:00Z"
lastmod = "2016-05-30T11:54:00Z"
weight = 53054
keywords = [ "graphs", "tcptrace" ]
aliases = [ "/questions/53054" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [time in tcptrace graph is off from the packet in pcap file](/questions/53054/time-in-tcptrace-graph-is-off-from-the-packet-in-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53054-score" class="post-score" title="current number of votes">0</div><span id="post-53054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to understand the tcptrace graph. I noticed that in packet captures if i zoom into a tcp trace graph, time shown in graph is different than what it is in pcap. e.g. when i click on the highlighted tcp segment, in pcap file packet @ 23.3220300 is selected but in graph its showing time lower than 23.313. Is this a known issue or am i missing something?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcptrace.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graphs" rel="tag" title="see questions tagged &#39;graphs&#39;">graphs</span> <span class="post-tag tag-link-tcptrace" rel="tag" title="see questions tagged &#39;tcptrace&#39;">tcptrace</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '16, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/39356e003826b924c6b683f177900afb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iWireshark&#39;s gravatar image" /><p><span>iWireshark</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iWireshark has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53054" class="comments-container"></div><div id="comment-tools-53054" class="comment-tools"></div><div class="clear"></div><div id="comment-53054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53055"></span>

<div id="answer-container-53055" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53055-score" class="post-score" title="current number of votes">1</div><span id="post-53055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you may be seeing <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12401">Bug 12401</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '16, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-53055" class="comments-container"></div><div id="comment-tools-53055" class="comment-tools"></div><div class="clear"></div><div id="comment-53055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

