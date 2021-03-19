+++
type = "question"
title = "Wireshark not capturing packets where tpc.src==my.ip.addr"
description = '''I have checked filters and options to resolve the problem. I do not see HTTP URI requests from my system nor do I see ACKs from my machine. When I filter tpc.src==10.72.xxx.xxx where 10.72.xxx.xxx is the IP addr of my system, no packets are listed. I have never experienced this problem before. Does ...'''
date = "2011-11-16T16:19:00Z"
lastmod = "2011-11-16T17:56:00Z"
weight = 7477
keywords = [ "packets", "missing" ]
aliases = [ "/questions/7477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not capturing packets where tpc.src==my.ip.addr](/questions/7477/wireshark-not-capturing-packets-where-tpcsrcmyipaddr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7477-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have checked filters and options to resolve the problem. I do not see HTTP URI requests from my system nor do I see ACKs from my machine. When I filter tpc.src==10.72.xxx.xxx where 10.72.xxx.xxx is the IP addr of my system, no packets are listed. I have never experienced this problem before. Does anyone have any idea what is happening. I am using Windows7. I tried by 32- and 64-bit versions of Wireshark to resolve the problem.</p></div><div id="question-tags" class="tags-container tags">packets missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '11, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/ba92b39bc8491006c049a4b7979aa93b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="b_lane&#39;s gravatar image" /><p>b_lane<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="b_lane has no accepted answers">0%</span></p></div></div><div id="comments-container-7477" class="comments-container"></div><div id="comment-tools-7477" class="comment-tools"></div><div class="clear"></div><div id="comment-7477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7478"></span>

<div id="answer-container-7478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7478-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no display filter called tpc.src. Perhaps you mean ip.src? When you enter a display filter, if the background color is red, it means the filter is invalid. The background should turn green when you have a valid filter.</p><p>But keep in mind that these are only display filters, meaning they don't dictate which packets are captured, only which of the already captured packets are displayed. So, if the valid display filter yields no matching packets, then you may have to modify your capture filter, and <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a> syntax is not the same as <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a> syntax.</p><p>In case your filter was just a typo, there could be other reasons why you have no matching packets, such as capturing on the wrong interface. You might want to read through the <a href="http://wiki.wireshark.org/CaptureSetup">CaptureSetup</a> wiki page for more help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '11, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Nov '11, 18:01</p></div></div><div id="comments-container-7478" class="comments-container"></div><div id="comment-tools-7478" class="comment-tools"></div><div class="clear"></div><div id="comment-7478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

