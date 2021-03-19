+++
type = "question"
title = "how to detect nmap connections?"
description = '''HI can anyone help with an issue I am having using wireshark to detect nmap scans I have managed to filter the amount of SYN/ACK packets for the 3 way with ip.proto == 6 and tcp.flags == 18. I have also filtered for a SYN scan only with ip.proto == 6 and tcp.flags == 2 and have identified areas with...'''
date = "2012-04-06T08:50:00Z"
lastmod = "2012-04-06T11:00:00Z"
weight = 9986
keywords = [ "nmap" ]
aliases = [ "/questions/9986" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to detect nmap connections?](/questions/9986/how-to-detect-nmap-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9986-score" class="post-score" title="current number of votes">0</div><span id="post-9986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI can anyone help with an issue I am having using wireshark to detect nmap scans I have managed to filter the amount of SYN/ACK packets for the 3 way with ip.proto == 6 and tcp.flags == 18. I have also filtered for a SYN scan only with ip.proto == 6 and tcp.flags == 2 and have identified areas with large amounts of these in a small space of time which prob proves a SYN scan happening. I have also filtered for ACK as well. I wanted to try to find what successful ports have been connected too and what ones have not. Im using a pre set up pcap given to me at university. any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nmap" rel="tag" title="see questions tagged &#39;nmap&#39;">nmap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '12, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/d2f98b846180b91135a4f3683b4436b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aikiscotsman&#39;s gravatar image" /><p><span>aikiscotsman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aikiscotsman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '12, 10:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9986" class="comments-container"></div><div id="comment-tools-9986" class="comment-tools"></div><div class="clear"></div><div id="comment-9986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9993"></span>

<div id="answer-container-9993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9993-score" class="post-score" title="current number of votes">2</div><span id="post-9993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nmap has many options, so an nmap scan can take many forms. You would need to create a filter for each type of scan behavior you want to detect.</p><p>As a starting point, you might want to go to the <a href="http://www.wiresharkbook.com/downloads.html">download page</a> of Laura Chappell's "Wireshark Network Analysis" book web site and download her Wireshark profiles and sample filters. She has one profile called "Nmap detection" that contains a color filter designed to highlight some possible nmap scans.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '12, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9993" class="comments-container"></div><div id="comment-tools-9993" class="comment-tools"></div><div class="clear"></div><div id="comment-9993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

