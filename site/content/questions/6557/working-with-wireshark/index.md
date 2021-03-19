+++
type = "question"
title = "Working with Wireshark"
description = '''Hi, I am a very new user of Wireshark and don&#x27;t have the knowledge on networking. I have, as of now, installed Wireshark 1.2.8 on my laptop (Win-7 pro), and my machine is connected to LAN. Can someone please suggest how can I use Wireshark to monitor any machine connected to LAN? I am able to ping i...'''
date = "2011-09-26T03:15:00Z"
lastmod = "2011-09-26T10:22:00Z"
weight = 6557
keywords = [ "windows", "beginner" ]
aliases = [ "/questions/6557" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Working with Wireshark](/questions/6557/working-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6557-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am a very new user of Wireshark and don't have the knowledge on networking.</p><p>I have, as of now, installed Wireshark 1.2.8 on my laptop (Win-7 pro), and my machine is connected to LAN. Can someone please suggest how can I use Wireshark to monitor any machine connected to LAN? I am able to ping it also. Please share simple steps, and help me.</p><p>Regards, Devender</p></div><div id="question-tags" class="tags-container tags">windows beginner</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '11, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/d46eb6893f11e71bdb457af2c5961c3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dev&#39;s gravatar image" /><p>dev<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '11, 21:49</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6557" class="comments-container"></div><div id="comment-tools-6557" class="comment-tools"></div><div class="clear"></div><div id="comment-6557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6566"></span>

<div id="answer-container-6566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6566-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As said, get a newer version from the <a href="http://www.wireshark.org/download.html">download page</a>. Then explore <a href="http://www.wireshark.org/docs/">the documentation</a>, and <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">the Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '11, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6566" class="comments-container"></div><div id="comment-tools-6566" class="comment-tools"></div><div class="clear"></div><div id="comment-6566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6562"></span>

<div id="answer-container-6562" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6562-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ul><li>1st, I suggest to download a newer version of wireshark as 1.2.8 not supported any more.</li><li>Usually you should check menu Capture -&gt; Capture Options... Select an interface (network connection) you want to capture.</li><li>If everything is ok, start capturing with Capture -&gt; Start</li><li>Capture -&gt; End will stop the capturing.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '11, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/6fe350be1625b29d7944d6ab430e57ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hiftu&#39;s gravatar image" /><p>Hiftu<br />
<span class="score" title="44 reputation points">44</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hiftu has no accepted answers">0%</span></p></div></div><div id="comments-container-6562" class="comments-container"></div><div id="comment-tools-6562" class="comment-tools"></div><div class="clear"></div><div id="comment-6562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

