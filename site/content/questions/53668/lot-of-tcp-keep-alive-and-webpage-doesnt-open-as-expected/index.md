+++
type = "question"
title = "Lot of TCP keep-alive and webpage doesn&#x27;t open as expected"
description = '''We have two servers on different VLANs and both are trying to access a specific http url. The page loads fine on one server, but not on the other one. The wireshark capture from non working server shows lot of TCP-keepalive messages followed by a RST. Can someone advise what could be wrong with the ...'''
date = "2016-06-27T05:40:00Z"
lastmod = "2016-06-27T08:31:00Z"
weight = 53668
keywords = [ "http", "keep-alive", "tcp" ]
aliases = [ "/questions/53668" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lot of TCP keep-alive and webpage doesn't open as expected](/questions/53668/lot-of-tcp-keep-alive-and-webpage-doesnt-open-as-expected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53668-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have two servers on different VLANs and both are trying to access a specific http url. The page loads fine on one server, but not on the other one.</p><p>The wireshark capture from non working server shows lot of TCP-keepalive messages followed by a RST. Can someone advise what could be wrong with the server, which is having issues connecting to the URL</p></div><div id="question-tags" class="tags-container tags">http keep-alive tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '16, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/323d1035e048053b54e413cdedd90b9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krmidhun&#39;s gravatar image" /><p>krmidhun<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krmidhun has no accepted answers">0%</span></p></div></div><div id="comments-container-53668" class="comments-container"></div><div id="comment-tools-53668" class="comment-tools"></div><div class="clear"></div><div id="comment-53668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53675"></span>

<div id="answer-container-53675" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53675-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>One thing you can do is capture a trace on both servers, and compare the two to see the difference.</p><p>If both servers are requesting data from the same URL, and one works while the other doesn't, you should get a trace from both, at the same time if you can, and compare them.</p><p>Second, on the server that doesn't work, I'm assuming the keep-alives are coming from that server and it's also sending the RSTs. Is that correct?</p><p>If so, you should look at your VLAN configuration (since both servers are coming from different VLANs) to see if anything is being blocked. Maybe there's a VACL blocking ports 80/443, if you're using default ports, or maybe even the IP of that server.</p><p>So you compare the VLAN configs for both servers to look for differences that might be impacting the one that doesn't work.</p><p>If you need more assistance, please include a trace file from the nonworking server, at minimum, but preferably from both servers that we can look at.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '16, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/0eafb94fc68881ab754f30924ce504ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeantunis&#39;s gravatar image" /><p>jeantunis<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeantunis has no accepted answers">0%</span></p></div></div><div id="comments-container-53675" class="comments-container"></div><div id="comment-tools-53675" class="comment-tools"></div><div class="clear"></div><div id="comment-53675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

