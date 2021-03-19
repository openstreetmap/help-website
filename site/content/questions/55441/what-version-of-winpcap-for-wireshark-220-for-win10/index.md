+++
type = "question"
title = "what version of winpcap for wireshark 2.2.0 for win10 ?"
description = '''what version of winpcap for wireshark 2.2.0 for win10 should be installed ? or wireshark alone 2.2.0 is enough to run and capture packet on win10 ? http://www.winpcap.org/install/default.htm the above link says winpcap 4.1.3 does not support win 10 . please advice.'''
date = "2016-09-09T11:51:00Z"
lastmod = "2016-09-10T03:37:00Z"
weight = 55441
keywords = [ "winpcap", "10", "win" ]
aliases = [ "/questions/55441" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [what version of winpcap for wireshark 2.2.0 for win10 ?](/questions/55441/what-version-of-winpcap-for-wireshark-220-for-win10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what version of winpcap for wireshark 2.2.0 for win10 should be installed ?</p><p>or wireshark alone 2.2.0 is enough to run and capture packet on win10 ?</p><p><a href="http://www.winpcap.org/install/default.htm">http://www.winpcap.org/install/default.htm</a></p><p>the above link says winpcap 4.1.3 does not support win 10 .</p><p>please advice.</p></div><div id="question-tags" class="tags-container tags">winpcap 10 win</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '16, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/277084326b74dd64bd543405f9838f07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inergi&#39;s gravatar image" /><p>inergi<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inergi has no accepted answers">0%</span></p></div></div><div id="comments-container-55441" class="comments-container"></div><div id="comment-tools-55441" class="comment-tools"></div><div class="clear"></div><div id="comment-55441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55459"></span>

<div id="answer-container-55459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55459-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'll just post this as answer so it's clearer to anyone coming to the question the first time.</p><p>The version of WinPCap (4.1.3) incorporated in the Wireshark 2.2.x installers runs perfectly well on all Windows OS's supported by Wireshark itself, there are no difference in capabilities running on Windows 10 as opposed to Windows Vista.</p><p><a href="https://github.com/nmap/npcap">Npcap</a> is a replacement for WinPcap sponsored and run by the <a href="https://nmap.org/">Nmap</a> project that works at the NDIS 6 level as opposed to the NDIS 5 level of WinPcap, so has different capabilities. Npcap is in the current beta of nmap so is starting to get wider exposure. When it is judged that Npcap has reached sufficient stability, Wireshark is likely to incorporate it in the Wireshark installers, the next opportunity to do so is likely to be in the 2.4.x release.</p><p>Current versions of Wireshark can use Npcap if it's installed in WinPcap "compatibility" mode and the Wireshark installer will detect this and not install WinPcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '16, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Sep '16, 03:39</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55459" class="comments-container"><span id="55463"></span><div id="comment-55463" class="comment"><div id="post-55463-score" class="comment-score"></div><div class="comment-text"><p>Noté that Wireshark 2.2 (just released) also supports Npcap installed without compatibility mode. If both WinPcap and Npcap (without WinPcap compatibility mode) are installed, it will pick WinPcap.</p></div><div id="comment-55463-info" class="comment-info"><span class="comment-age">(10 Sep '16, 05:00)</span> Pascal Quantin</div></div></div><div id="comment-tools-55459" class="comment-tools"></div><div class="clear"></div><div id="comment-55459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55442"></span>

<div id="answer-container-55442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55442-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use <a href="https://github.com/nmap/npcap/releases">npcap</a> instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '16, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55442" class="comments-container"><span id="55443"></span><div id="comment-55443" class="comment"><div id="post-55443-score" class="comment-score"></div><div class="comment-text"><p>Note that Npcap still has some stability issues, that are being resolved when reported. So it cannot be considered as stavle as WinPcap yet. WinPcap is known to work on Windows 10 but Npcap might be more performance (due to the use of NDIS6 versus NDIS5) and for sure allows to capture on some interfaces not seen by WinPcap.</p></div><div id="comment-55443-info" class="comment-info"><span class="comment-age">(09 Sep '16, 13:12)</span> Pascal Quantin</div></div><span id="55444"></span><div id="comment-55444" class="comment"><div id="post-55444-score" class="comment-score"></div><div class="comment-text"><p>Well, I guess my answer was way too brief. There is also the dark side of it: while NPcap can capture on some interfaces not seen by WinPcap, it can not capture on some interfaces on which WinPcap can. In particular, it is possible to set up a software bridge between two NICs on a single machine and capture the transit traffic on one of them using WinPcap, but NPcap stops seeing an interface as soon as it becomes part of a bridge and can capture only on the virtual NIC representing the bridge into the machine, which the transit traffic doesn't reach.</p></div><div id="comment-55444-info" class="comment-info"><span class="comment-age">(09 Sep '16, 13:20)</span> sindy</div></div><span id="55453"></span><div id="comment-55453" class="comment"><div id="post-55453-score" class="comment-score"></div><div class="comment-text"><p>I am curious if Wireshark developers are planning to include npcap into the installer package once it is deemed stable.</p></div><div id="comment-55453-info" class="comment-info"><span class="comment-age">(09 Sep '16, 20:19)</span> Rooster_50</div></div></div><div id="comment-tools-55442" class="comment-tools"></div><div class="clear"></div><div id="comment-55442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

