+++
type = "question"
title = "error wireshark root terminal"
description = '''when I try to run wireshark by using root terminao the following error appears: No protocol specified (wireshark:6951): Gtk-WARNING **: cannot open display: :0.0 Help ?'''
date = "2014-07-03T09:46:00Z"
lastmod = "2014-07-03T10:10:00Z"
weight = 34389
keywords = [ "wireshark" ]
aliases = [ "/questions/34389" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error wireshark root terminal](/questions/34389/error-wireshark-root-terminal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when I try to run wireshark by using root terminao the following error appears: No protocol specified</p><p>(wireshark:6951): Gtk-WARNING **: cannot open display: :0.0</p><p>Help ?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '14, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/fc767447a718110ddbc78942f46e4b2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rpoucas&#39;s gravatar image" /><p>rpoucas<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rpoucas has no accepted answers">0%</span></p></div></div><div id="comments-container-34389" class="comments-container"></div><div id="comment-tools-34389" class="comment-tools"></div><div class="clear"></div><div id="comment-34389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34391"></span>

<div id="answer-container-34391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34391-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should not run Wireshark as root, but as a normal user as untrusted captures can cause so much breakage (security issues!). If you need more privileges for using the capture device, see:</p><ul><li><a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></li><li><a href="http://askubuntu.com/questions/74059/how-do-i-run-wireshark-with-root-privileges">http://askubuntu.com/questions/74059/how-do-i-run-wireshark-with-root-privileges</a></li></ul><p>You get the message "Cannot open display" because your user (root) is not authorized to use the X server (or the X server is not started).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '14, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-34391" class="comments-container"></div><div id="comment-tools-34391" class="comment-tools"></div><div class="clear"></div><div id="comment-34391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

