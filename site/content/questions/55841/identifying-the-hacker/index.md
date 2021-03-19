+++
type = "question"
title = "Identifying the hacker"
description = '''Hello can someone help me and give steps on finding the hacker in this pcap file? https://drive.google.com/open?id=0B94k1Bz5s_fRWTBIdDZRQzhXM2s'''
date = "2016-09-26T06:52:00Z"
lastmod = "2016-10-17T03:34:00Z"
weight = 55841
keywords = [ "wireshark", "help", "homework", "for" ]
aliases = [ "/questions/55841" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Identifying the hacker](/questions/55841/identifying-the-hacker)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55841-score" class="post-score" title="current number of votes">0</div><span id="post-55841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello can someone help me and give steps on finding the hacker in this pcap file?</p><p><a href="https://drive.google.com/open?id=0B94k1Bz5s_fRWTBIdDZRQzhXM2s">https://drive.google.com/open?id=0B94k1Bz5s_fRWTBIdDZRQzhXM2s</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-homework" rel="tag" title="see questions tagged &#39;homework&#39;">homework</span> <span class="post-tag tag-link-for" rel="tag" title="see questions tagged &#39;for&#39;">for</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '16, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/c165ac5b50ce5245e981d75ad5bdf14f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pacbell86&#39;s gravatar image" /><p><span>pacbell86</span><br />
<span class="score" title="2 reputation points">2</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pacbell86 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Oct '16, 04:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span></p></div></div><div id="comments-container-55841" class="comments-container"></div><div id="comment-tools-55841" class="comment-tools"></div><div class="clear"></div><div id="comment-55841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56293"></span>

<div id="answer-container-56293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56293-score" class="post-score" title="current number of votes">1</div><span id="post-56293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This should get you going...<br />
The clue to this challenge is to find two files that were downloaded from the windows machine and to extract those from the pcap file.<br />
</p><pre><code>http and ip.ttl==64</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_420.png" alt="alt text" /></p><p>If you succeed to unzip myfile you see what the hacker's identity is</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_419.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '16, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '16, 22:14</strong> </span></p></div></div><div id="comments-container-56293" class="comments-container"></div><div id="comment-tools-56293" class="comment-tools"></div><div class="clear"></div><div id="comment-56293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56446"></span>

<div id="answer-container-56446" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56446-score" class="post-score" title="current number of votes">0</div><span id="post-56446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The password is also findable in the pcap ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/d945ac48625d4aef83f374f01ffa946c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SynAck&#39;s gravatar image" /><p><span>SynAck</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SynAck has one accepted answer">33%</span></p></img></div></div><div id="comments-container-56446" class="comments-container"></div><div id="comment-tools-56446" class="comment-tools"></div><div class="clear"></div><div id="comment-56446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

