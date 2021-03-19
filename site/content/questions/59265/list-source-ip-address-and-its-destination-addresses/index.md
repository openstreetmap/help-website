+++
type = "question"
title = "List Source IP address and its destination addresses"
description = '''Hello, I have a small Internet address space to capture illegitimate incoming packets. I need to list each incoming ip address and its destination addresses.This is to check how many source addresses are sending packets to all ip addresses in my IP address space or Is it targeting only on specific I...'''
date = "2017-02-08T16:48:00Z"
lastmod = "2017-02-08T17:23:00Z"
weight = 59265
keywords = [ "statistics", "list", "tshark", "wireshark" ]
aliases = [ "/questions/59265" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [List Source IP address and its destination addresses](/questions/59265/list-source-ip-address-and-its-destination-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59265-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a small Internet address space to capture illegitimate incoming packets.</p><p>I need to list each incoming ip address and its destination addresses.This is to check how many source addresses are sending packets to all ip addresses in my IP address space or Is it targeting only on specific IP address.</p><p>I have not seen any option in the statistics to do the same. Can I do this with wireshark or tshark?</p><p>Thanks in advance</p><p>Subin</p></div><div id="question-tags" class="tags-container tags">statistics list tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '17, 16:48</strong></p><img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp&#39;s gravatar image" /><p>subinjp<br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp has no accepted answers">0%</span></p></div></div><div id="comments-container-59265" class="comments-container"></div><div id="comment-tools-59265" class="comment-tools"></div><div class="clear"></div><div id="comment-59265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59266"></span>

<div id="answer-container-59266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59266-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Look under STATISTICS --&gt; CONVERSATIONS, then click on the IPv4 tab at the top.</p><p>This will give you a complete list of the communicating endpoints.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '17, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-59266" class="comments-container"></div><div id="comment-tools-59266" class="comment-tools"></div><div class="clear"></div><div id="comment-59266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

