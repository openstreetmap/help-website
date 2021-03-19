+++
type = "question"
title = "Scanning trafic throught a specific port"
description = '''I&#x27;m using a threat that comunicates with one specific port (for example 55000), I want to scan all the trafic throught this port, so I use the filter  dst port 55000  But it did not appear anything, what I&#x27;m doing wrong? Sorry for my english'''
date = "2016-03-15T02:27:00Z"
lastmod = "2016-03-15T06:14:00Z"
weight = 50913
keywords = [ "ports", "tcp" ]
aliases = [ "/questions/50913" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Scanning trafic throught a specific port](/questions/50913/scanning-trafic-throught-a-specific-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50913-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using a threat that comunicates with one specific port (for example 55000), I want to scan all the trafic throught this port, so I use the filter</p><blockquote><p>dst port 55000</p></blockquote><p>But it did not appear anything, what I'm doing wrong?</p><p>Sorry for my english</p></div><div id="question-tags" class="tags-container tags">ports tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '16, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/175cf1258ac4d0d1c722de91ba31954e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xtapia&#39;s gravatar image" /><p>xtapia<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xtapia has no accepted answers">0%</span></p></div></div><div id="comments-container-50913" class="comments-container"><span id="50916"></span><div id="comment-50916" class="comment"><div id="post-50916-score" class="comment-score"></div><div class="comment-text"><p>Are you using <code>dst port 55000</code> as a <em>capture</em> filter or as a <em>display</em> filter?</p><p>Are you sure that the traffic is leaving/coming through the Ethernet interface on which you are capturing?</p></div><div id="comment-50916-info" class="comment-info"><span class="comment-age">(15 Mar '16, 03:55)</span> sindy</div></div><span id="50924"></span><div id="comment-50924" class="comment"><div id="post-50924-score" class="comment-score"></div><div class="comment-text"><p>Is not leaving or coming through the Ethernet interface because is working on my own PC, so it is an internal package. Is impossible to capture it if this package do not "pass" through the Ethernet intergace?</p></div><div id="comment-50924-info" class="comment-info"><span class="comment-age">(15 Mar '16, 06:00)</span> xtapia</div></div></div><div id="comment-tools-50913" class="comment-tools"></div><div class="clear"></div><div id="comment-50913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50925"></span>

<div id="answer-container-50925" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50925-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is not leaving or coming through the Ethernet interface because is working on my own PC</p></blockquote><p>This is known as a loopback connection as it doesn't leave your machine on an external NIC. See the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Loopback">capturing on loopback interfaces</a> for more info.</p><p>If using Windows you'll need to switch to using npcap instead of WinPcap as mentioned on the page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '16, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '16, 06:14</p></div></div><div id="comments-container-50925" class="comments-container"><span id="50931"></span><div id="comment-50931" class="comment"><div id="post-50931-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks, I ran this thread on another computer of my LAN and Wire Shark captured it perfectly. I'm gonna try to understand hoy to capture it on my own machine.</p><p>Thanks a lot!!</p></div><div id="comment-50931-info" class="comment-info"><span class="comment-age">(15 Mar '16, 09:22)</span> xtapia</div></div></div><div id="comment-tools-50925" class="comment-tools"></div><div class="clear"></div><div id="comment-50925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

