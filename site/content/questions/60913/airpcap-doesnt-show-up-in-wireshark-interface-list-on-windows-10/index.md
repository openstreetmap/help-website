+++
type = "question"
title = "Airpcap doesn&#x27;t show up in Wireshark interface list on Windows 10"
description = '''I installed AirPcap driver 4.1.3 on Windows 10 Pro. The AirPcap Nx adapter works fine according to AirpcapConf and Cain&amp;amp;Abel. However the AirPcap interface doesn&#x27;t show up in Wireshark&#x27;s (version 2.2.5) interface list. I run Wireshark with admin privileges. Is this a known issue? Is it no longer...'''
date = "2017-04-20T02:42:00Z"
lastmod = "2017-04-20T03:57:00Z"
weight = 60913
keywords = [ "interface", "problem", "airpcap", "windows10" ]
aliases = [ "/questions/60913" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Airpcap doesn't show up in Wireshark interface list on Windows 10](/questions/60913/airpcap-doesnt-show-up-in-wireshark-interface-list-on-windows-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60913-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed AirPcap driver 4.1.3 on Windows 10 Pro. The AirPcap Nx adapter works fine according to AirpcapConf and Cain&amp;Abel. However the AirPcap interface doesn't show up in Wireshark's (version 2.2.5) interface list. I run Wireshark with admin privileges. Is this a known issue? Is it no longer possible to use the AirPcap adapter with Wireshark?</p></div><div id="question-tags" class="tags-container tags">interface problem airpcap windows10</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '17, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/9ca4c6b0f41a26ab63e8868e6975f48b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terentius&#39;s gravatar image" /><p>Terentius<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terentius has no accepted answers">0%</span></p></div></div><div id="comments-container-60913" class="comments-container"></div><div id="comment-tools-60913" class="comment-tools"></div><div class="clear"></div><div id="comment-60913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60917"></span>

<div id="answer-container-60917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60917-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have npcap installed? If so, you'll need to remove it, and install WinPcap 4.1.3 if you don't have that already, to display the AirPcap adaptor in the interface list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '17, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Apr '17, 03:59</p></div></div><div id="comments-container-60917" class="comments-container"><span id="60920"></span><div id="comment-60920" class="comment"><div id="post-60920-score" class="comment-score"></div><div class="comment-text"><p>Worked perfectly - thanks!</p></div><div id="comment-60920-info" class="comment-info"><span class="comment-age">(20 Apr '17, 05:40)</span> Terentius</div></div><span id="60922"></span><div id="comment-60922" class="comment"><div id="post-60922-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-60922-info" class="comment-info"><span class="comment-age">(20 Apr '17, 07:45)</span> grahamb ♦</div></div></div><div id="comment-tools-60917" class="comment-tools"></div><div class="clear"></div><div id="comment-60917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

