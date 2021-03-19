+++
type = "question"
title = "Tshark - Running multiple instances vs one"
description = '''Hello, In short: tshark dst port 80 -Y http.request -T fields -e http.host -e http.user_agent &amp;gt; http_dumpfile &amp;amp; tshark dst portrange 21-22 -Y &quot;ftp.request.command == LIST || ftp.request.command == PASV&quot; -T fields -e ftp.request.command -e ftp.request.arg &amp;gt; ftp_dumpfile &amp;amp; tshark &quot;dst po...'''
date = "2015-09-04T05:56:00Z"
lastmod = "2015-09-07T16:40:00Z"
weight = 45630
keywords = [ "instances", "efficiency", "tshark", "performance" ]
aliases = [ "/questions/45630" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark - Running multiple instances vs one](/questions/45630/tshark-running-multiple-instances-vs-one)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>In short:</p><p><strong>tshark</strong> dst port 80 -Y http.request -T fields -e http.host -e http.user_agent &gt; http_dumpfile &amp;</p><p><strong>tshark</strong> dst portrange 21-22 -Y "ftp.request.command == LIST || ftp.request.command == PASV" -T fields -e ftp.request.command -e ftp.request.arg &gt; ftp_dumpfile &amp;</p><p><strong>tshark</strong> "dst port 143 or dst port 220" -Y imap.isrequest==1 -T fields -e imap.request.command &gt; imap_dumpfile &amp;</p><p>vs one long:</p><p><strong>tshark</strong> "dst port 80 or dst port 110 or dst port 220 or dst portrange 21-22" -Y "ftp.request.command == LIST || ftp.request.command == PASV || http.request || imap.isrequest==1" &gt; capture_dumpfile</p><h2 id="section">-----</h2><p>Longer version: Writing some program in python that uses tshark to capture and analyze some traffic. Using specific capture filters in a combination of display filters to minimize the output as much as possible.</p><p>Now I have to decide if I'll use several instances of tshark with different capture filters and display filters VS Running unified more complex capture filter and then analyze the traffic programmatically?</p><p>Very important note is that Display Filters ease by work significantly.</p></div><div id="question-tags" class="tags-container tags">instances efficiency tshark performance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '15, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/9da15dcdc7da9530aa269f334d3cf062?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Do5&#39;s gravatar image" /><p>Do5<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Do5 has no accepted answers">0%</span></p></div></div><div id="comments-container-45630" class="comments-container"></div><div id="comment-tools-45630" class="comment-tools"></div><div class="clear"></div><div id="comment-45630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45678"></span>

<div id="answer-container-45678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45678-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Now I have to decide if I'll use several instances of tshark</p></blockquote><p>besides the fact that the sum of the short tshark commands is different than the long tshark command, you can choose whatever method you like better or which causes less work in your script that parses the output. I don't see a direct advantage/disadvantage of having three short tshark commands versus on large.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45678" class="comments-container"></div><div id="comment-tools-45678" class="comment-tools"></div><div class="clear"></div><div id="comment-45678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

