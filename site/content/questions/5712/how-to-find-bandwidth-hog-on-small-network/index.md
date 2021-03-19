+++
type = "question"
title = "How to find bandwidth hog on small network?"
description = '''Hi, Lately having slow internet in the office at random times. This might be network problem or one or more workstations use too much bandwidth. I already tested that I can Wireshark capture between the modem and the router using Windows XP laptop with 2 NICs bridged. I want to keep this capture for...'''
date = "2011-08-16T06:53:00Z"
lastmod = "2011-08-19T13:12:00Z"
weight = 5712
keywords = [ "capture", "analysis" ]
aliases = [ "/questions/5712" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to find bandwidth hog on small network?](/questions/5712/how-to-find-bandwidth-hog-on-small-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5712-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Lately having slow internet in the office at random times. This might be network problem or one or more workstations use too much bandwidth.</p><p>I already tested that I can Wireshark capture between the modem and the router using Windows XP laptop with 2 NICs bridged.</p><p>I want to keep this capture for long time, maybe 1-2 days, and I want to find out what workstation is causing the slowdown.</p><p>Please advice how to prepare my long capture and how to scan it to accomplish what I want. Or maybe there is another tool to do this?</p><p>Thanks, JM</p></div><div id="question-tags" class="tags-container tags">capture analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '11, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/403dd3983dfa695bef59c7fdce982645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joem2&#39;s gravatar image" /><p>joem2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joem2 has no accepted answers">0%</span></p></div></div><div id="comments-container-5712" class="comments-container"></div><div id="comment-tools-5712" class="comment-tools"></div><div class="clear"></div><div id="comment-5712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5713"></span>

<div id="answer-container-5713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5713-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you've already checked your capture setup, you are ready to start capturing and analyzing some traffic. You'll probably want to use <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> directly to avoid an out-of-memory problem during capture (See <a href="http://ask.wireshark.org/questions/1271/dumpcap-syntax?page=1#1272">this answer</a> for an example of using dumpcap).</p><p>Once you've got some capture files, you can use entries in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatistics.html">statistics</a> menu to do what you want, as indicated in this <a href="http://ask.wireshark.org/questions/3880/monitor-network-traffic-by-user?page=1#3882" title="Monitor Network Traffic By User">answer</a> to a similar question. Using that information, you should be able to identify which hosts are consuming the most bandwidth.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '11, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5713" class="comments-container"></div><div id="comment-tools-5713" class="comment-tools"></div><div class="clear"></div><div id="comment-5713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5767"></span>

<div id="answer-container-5767" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5767-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks. I am still learning this stuff.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '11, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/403dd3983dfa695bef59c7fdce982645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joem2&#39;s gravatar image" /><p>joem2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joem2 has no accepted answers">0%</span></p></div></div><div id="comments-container-5767" class="comments-container"></div><div id="comment-tools-5767" class="comment-tools"></div><div class="clear"></div><div id="comment-5767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

