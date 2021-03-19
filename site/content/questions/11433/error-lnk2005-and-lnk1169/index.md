+++
type = "question"
title = "error LNK2005 and LNK1169"
description = '''Hello guys, I&#x27;ve developped a dissector for a &quot;homemade&quot; protocol. So far, everything went well, it did its job, told all the information I wanted on wireshark. Then, I tried to implement some statistics operation... And it doesn&#x27;t compile anymore ! I followed the developer&#x27;s guide, implemented the ...'''
date = "2012-05-29T01:42:00Z"
lastmod = "2012-05-29T06:28:00Z"
weight = 11433
keywords = [ "development", "statistics", "link", "dissector" ]
aliases = [ "/questions/11433" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error LNK2005 and LNK1169](/questions/11433/error-lnk2005-and-lnk1169)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11433-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>I've developped a dissector for a "homemade" protocol. So far, everything went well, it did its job, told all the information I wanted on wireshark. Then, I tried to implement some statistics operation... And it doesn't compile anymore ! I followed the developer's guide, implemented the tap functions, the statistics functions. But it doesn't work.</p><p>Here are my error messages :</p><p>plugin.obj : error LNK2005: _version already defined in packet-subnet.obj Creating library subnet.lib and objet subnet.exp subnet.dll : fatal error LNK1169: one or more mutliply defined symbols found NMAKE : fatal error U1077 : &lt;path to="" link.exe=""&gt; : return code '0x491' NMAKE : fatal error U1077 : &lt;path to="" nmake.exe=""&gt; : return code '0x2' Stop.</p><p>If you have any idea, or suggestion, that could help getting rid of this problem, this would greatly appreciated !</p><p>Thanks in advance,</p><p>Cheers from France.</p></div><div id="question-tags" class="tags-container tags">development statistics link dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '12, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/c9f1f3b89b389786bd00f0eed02f9928?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cosinuz&#39;s gravatar image" /><p>cosinuz<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cosinuz has no accepted answers">0%</span></p></div></div><div id="comments-container-11433" class="comments-container"></div><div id="comment-tools-11433" class="comment-tools"></div><div class="clear"></div><div id="comment-11433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11441"></span>

<div id="answer-container-11441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11441-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>(This question was answered on the wireshark-dev mailing list. See: <a href="http://www.wireshark.org/lists/wireshark-dev/201205/msg00231.html">wireshark-dev thread</a>).</p><blockquote><p>Do you have some variable called 'version' in packet-subnet.c?<br />
If yes rename it to some subnet_version. hth.</p></blockquote></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '12, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '12, 11:08</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-11441" class="comments-container"></div><div id="comment-tools-11441" class="comment-tools"></div><div class="clear"></div><div id="comment-11441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

