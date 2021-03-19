+++
type = "question"
title = "Wireshark Slow in promiscious mode"
description = '''Using Wireshark 1.6.7 in Ubuntu 12.04 with promiscuous mode makes Wireshark run slow. I have tried reinstalling Wireshark but it still runs slow. When I disable promiscuous mode it runs ok again. Have 8gb of ram.  Is there a way to speed it up ?  Thanks'''
date = "2014-03-15T22:21:00Z"
lastmod = "2014-03-16T05:08:00Z"
weight = 30849
keywords = [ "slow" ]
aliases = [ "/questions/30849" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Slow in promiscious mode](/questions/30849/wireshark-slow-in-promiscious-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark 1.6.7 in Ubuntu 12.04 with promiscuous mode makes Wireshark run slow.</p><p>I have tried reinstalling Wireshark but it still runs slow. When I disable promiscuous mode it runs ok again.</p><p>Have 8gb of ram.</p><p>Is there a way to speed it up ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">slow</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '14, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/24d4985cae281d759cd3fbed6604ed0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kam270&#39;s gravatar image" /><p>kam270<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kam270 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '14, 22:24</p></div></div><div id="comments-container-30849" class="comments-container"></div><div id="comment-tools-30849" class="comment-tools"></div><div class="clear"></div><div id="comment-30849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30855"></span>

<div id="answer-container-30855" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30855-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to speed it up ?</p></blockquote><p>disable name resolution.</p><blockquote><p>Edit -&gt; Preferences -&gt; Name Resolution</p></blockquote><p>disable the options related to name resolution, like '<strong>Resolve network (IP) addresses</strong>' and '<strong>Use an external network name resolver</strong>'</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30855" class="comments-container"><span id="30857"></span><div id="comment-30857" class="comment"><div id="post-30857-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt this done the trick. Thanks.</p></div><div id="comment-30857-info" class="comment-info"><span class="comment-age">(16 Mar '14, 05:25)</span> kam270</div></div></div><div id="comment-tools-30855" class="comment-tools"></div><div class="clear"></div><div id="comment-30855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30852"></span>

<div id="answer-container-30852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30852-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, you are running a quite old version; current is 1.10.6, so you might want to upgrade (if possible; I'm not sure what packages Ubuntu 12.04 has in the repositories).</p><p>Second, what do you mean exactly by "it still runs slow"? What is it doing that should be faster? Wiresharks speed depends largely on the amount of packets that it has to process, so if you're capturing packets on a very busy link you'll notice that it can't keep up with updating the display. If you're loading a trace with lots of packets it may also behave slowly because it has to process lots of data.</p><p>Keep in mind that it is not that important how much data there is (in bytes); the speed of Wireshark depends a lot more on the amount of packets, and what protocols they contain. There are many protocols that are more complex to decode and analyze than others, e.g. an ARP frame doesn't need much processing time while a complex high level protocol might take a lot longer to process.</p><p>If you need a faster capture process try doing it by running dumpcap instead of Wireshark (which in fact uses dumpcap to capture itself).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30852" class="comments-container"><span id="30858"></span><div id="comment-30858" class="comment"><div id="post-30858-score" class="comment-score"></div><div class="comment-text"><p>Yeah it is an old version , cant seem to get a .deb of the latest version. I may have to compile form source.</p><p>The slowness was in the interface. Menus were slow to load 4-7 seconds.</p></div><div id="comment-30858-info" class="comment-info"><span class="comment-age">(16 Mar '14, 05:26)</span> kam270</div></div></div><div id="comment-tools-30852" class="comment-tools"></div><div class="clear"></div><div id="comment-30852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

