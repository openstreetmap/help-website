+++
type = "question"
title = "Commandline Tools Mac OS X"
description = '''Hi According to the README in the latest Wireshark.dmg image, the installed should install the command line tools in /Library/Wireshark, but this directory is not even created. Is there anything I&#x27;m missing in the setup process?'''
date = "2013-09-30T10:08:00Z"
lastmod = "2013-09-30T18:59:00Z"
weight = 25398
keywords = [ "cli" ]
aliases = [ "/questions/25398" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Commandline Tools Mac OS X](/questions/25398/commandline-tools-mac-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25398-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>According to the README in the latest Wireshark.dmg image, the installed should install the command line tools in /Library/Wireshark, but this directory is not even created.</p><p>Is there anything I'm missing in the setup process?</p></div><div id="question-tags" class="tags-container tags">cli</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '13, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/13861113a7f5f8cc8cba6c4a88e2e91b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f0rd42&#39;s gravatar image" /><p>f0rd42<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f0rd42 has no accepted answers">0%</span></p></div></div><div id="comments-container-25398" class="comments-container"></div><div id="comment-tools-25398" class="comment-tools"></div><div class="clear"></div><div id="comment-25398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25433"></span>

<div id="answer-container-25433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25433-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>According to the README in the latest Wireshark.dmg image, the installed should install the command line tools in /Library/Wireshark</p></blockquote><p>The README is wrong. The binaries are in the app bundle for Wireshark, and the installer should, if you've requested the command-line tools, install wrapper scripts in <code>/usr/local/bin</code> that run those binaries. I've checked in a fix for the README, which should be in the next 1.8 and 1.10 releases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 18:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Oct '13, 15:05</p></div></div><div id="comments-container-25433" class="comments-container"></div><div id="comment-tools-25433" class="comment-tools"></div><div class="clear"></div><div id="comment-25433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

