+++
type = "question"
title = "How can I deploy Wireshark silently/unattended using Group Policy?"
description = '''I would like to deploy Wireshark to multiple desktops/laptops using Group Policy but need the installer to be in msi format to do this. Could you please advise how I can extract the msi from the Wireshark exe and the commands/properties I should use in order to install it silently/unattended?'''
date = "2012-10-31T03:28:00Z"
lastmod = "2012-10-31T04:26:00Z"
weight = 15414
keywords = [ "policy", "unattended", "group", "silent", "msi" ]
aliases = [ "/questions/15414" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I deploy Wireshark silently/unattended using Group Policy?](/questions/15414/how-can-i-deploy-wireshark-silentlyunattended-using-group-policy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15414-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to deploy Wireshark to multiple desktops/laptops using Group Policy but need the installer to be in msi format to do this. Could you please advise how I can extract the msi from the Wireshark exe and the commands/properties I should use in order to install it silently/unattended?</p></div><div id="question-tags" class="tags-container tags">policy unattended group silent msi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '12, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/fc01e2387332f6fb3d95eef455236e3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="breamer&#39;s gravatar image" /><p>breamer<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="breamer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Oct '12, 03:31</p></div></div><div id="comments-container-15414" class="comments-container"></div><div id="comment-tools-15414" class="comment-tools"></div><div class="clear"></div><div id="comment-15414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15418"></span>

<div id="answer-container-15418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15418-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't use an msi installer, instead it uses <a href="http://nsis.sourceforge.net/Main_Page">NSIS</a>. There is no way to convert the NSIS script that builds the installer to msi format.</p><p>If you Google around a bit you should find utilities and recipes for creating an msi wrapper for .exe installers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '12, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-15418" class="comments-container"></div><div id="comment-tools-15418" class="comment-tools"></div><div class="clear"></div><div id="comment-15418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

