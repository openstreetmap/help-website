+++
type = "question"
title = "How to capture http 3-way handshake?"
description = '''How to capture the NATed out-bound HTTP syn request and inbound HTTP responses in a 3-way handshake process; identify our public IP address and our device’s private IP address? '''
date = "2014-08-19T19:47:00Z"
lastmod = "2014-08-20T06:29:00Z"
weight = 35601
keywords = [ "ip", "handshake", "3-way", "wirehshark", "wireshark" ]
aliases = [ "/questions/35601" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture http 3-way handshake?](/questions/35601/how-to-capture-http-3-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35601-score" class="post-score" title="current number of votes">0</div><span id="post-35601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to capture the NATed out-bound HTTP syn request and inbound HTTP responses in a 3-way handshake process; identify our public IP address and our device’s private IP address?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-3-way" rel="tag" title="see questions tagged &#39;3-way&#39;">3-way</span> <span class="post-tag tag-link-wirehshark" rel="tag" title="see questions tagged &#39;wirehshark&#39;">wirehshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 19:47</strong></p><img src="https://secure.gravatar.com/avatar/86d57fe7f63a4834a36e898372bf42d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randy%20S&#39;s gravatar image" /><p><span>randy S</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randy S has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '14, 19:49</strong> </span></p></div></div><div id="comments-container-35601" class="comments-container"></div><div id="comment-tools-35601" class="comment-tools"></div><div class="clear"></div><div id="comment-35601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35622"></span>

<div id="answer-container-35622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35622-score" class="post-score" title="current number of votes">0</div><span id="post-35622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Randy,</p><p>One way would be to trace on the inside and the outside interfaces of the firewall. If you can use one PC with two NICs that would be good because both traces will be timestamped by one clock and so pretty closely synchronized. If must use two PCs, try to manually sync the clocks on them as best you can. Capture the traces and the match the packets in each trace using the detsination Internet address (the server the PC is trying to talk to) and the TCP sequence numbers (usually the firewall NAT doesn't change these). Remember to switch off the TCP protocol preference "Relative Sequence Numbers" in Wireshark so that you get distinctive sequence numbers.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35622" class="comments-container"></div><div id="comment-tools-35622" class="comment-tools"></div><div class="clear"></div><div id="comment-35622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

