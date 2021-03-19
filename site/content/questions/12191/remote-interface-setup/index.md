+++
type = "question"
title = "Remote Interface setup"
description = '''Under Capture Options Interface remote - after completing the dialog I get the following error: Microsoft Visual C++ runtime library. This application has requested the runtime to terminate it in an unusual way. Please contact the application&#x27;s support team for more information. I can repeat this ov...'''
date = "2012-06-26T11:28:00Z"
lastmod = "2012-06-26T15:11:00Z"
weight = 12191
keywords = [ "interfaces", "remote" ]
aliases = [ "/questions/12191" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Interface setup](/questions/12191/remote-interface-setup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12191-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Under Capture Options Interface remote - after completing the dialog I get the following error:</p><p>Microsoft Visual C++ runtime library. This application has requested the runtime to terminate it in an unusual way. Please contact the application's support team for more information. I can repeat this over and over again.</p><p>Running Wireshark 1.6.6 (SVN Rev 41803 from /trunk-1.6) on Windows 7 64 bit workstation. WinPcap 4.1.2 on a Windows Server 2003,standard Edition</p></div><div id="question-tags" class="tags-container tags">interfaces remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/83c69d524461783cda243d849afdb656?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spizzuto&#39;s gravatar image" /><p>spizzuto<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spizzuto has no accepted answers">0%</span></p></div></div><div id="comments-container-12191" class="comments-container"></div><div id="comment-tools-12191" class="comment-tools"></div><div class="clear"></div><div id="comment-12191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12213"></span>

<div id="answer-container-12213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12213-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7021">bug 7021</a>, which is a bit confusing as the <em>original</em> bug he reported (the crash) is apparently fixed in 1.6.8, but he's seeing <em>another</em> problem which may be a Wireshark bug in code to work around a bug in WinPcap. Try using 1.6.8, which shouldn't crash but which might pop up a warning(?) dialog that it shouldn't be popping up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '12, 15:13</p></div></div><div id="comments-container-12213" class="comments-container"></div><div id="comment-tools-12213" class="comment-tools"></div><div class="clear"></div><div id="comment-12213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

