+++
type = "question"
title = "Display packet transitions before capturing"
description = '''Running Wireshark, before selecting the right interface, I can see packet transitions on all interfaces, by means of flashing numbers. Since I use WinPcap library I&#x27;d like to mimic that in my C++ program. Can someone direct me how to do that? Regards I. Lesher'''
date = "2012-09-05T23:42:00Z"
lastmod = "2012-09-06T02:03:00Z"
weight = 14077
keywords = [ "winpcap" ]
aliases = [ "/questions/14077" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display packet transitions before capturing](/questions/14077/display-packet-transitions-before-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14077-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running Wireshark, before selecting the right interface, I can see packet transitions on all interfaces, by means of flashing numbers. Since I use WinPcap library I'd like to mimic that in my C++ program. Can someone direct me how to do that? Regards I. Lesher</p></div><div id="question-tags" class="tags-container tags">winpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '12, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/c46b9d0cf13adb17325f5d9519406546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="triplebit&#39;s gravatar image" /><p>triplebit<br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="triplebit has no accepted answers">0%</span></p></div></div><div id="comments-container-14077" class="comments-container"></div><div id="comment-tools-14077" class="comment-tools"></div><div class="clear"></div><div id="comment-14077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14079"></span>

<div id="answer-container-14079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14079-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's done with <strong><a href="http://www.winpcap.org/docs/docs_40_2/html/group__wpcapfunc.html#gbbd74d8c3ce1bcbccc76129ac38f4549">pcap_stats</a></strong> in <a href="http://anonsvn.wireshark.org/wireshark/trunk/dumpcap.c">dumpcap</a>:print_statistics_loop(). Please check the WinPcap <a href="http://www.winpcap.org/devel.htm">developer docs</a> for more information.</p><p>Google will also help: 'pcap_stats sample code'</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '12, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '12, 02:03</p></div></div><div id="comments-container-14079" class="comments-container"></div><div id="comment-tools-14079" class="comment-tools"></div><div class="clear"></div><div id="comment-14079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

