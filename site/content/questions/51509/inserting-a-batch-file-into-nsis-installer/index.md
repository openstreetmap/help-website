+++
type = "question"
title = "Inserting a batch file into nsis installer"
description = '''Hello, I would like to add a batch file to be executed at the end of a successful Wireshark installation. The goal is to have a single setup.exe file which will include this batch script and it&#x27;s functionality. I made the installation exe file following the guide on the Development documentation for...'''
date = "2016-04-08T06:19:00Z"
lastmod = "2016-04-08T07:11:00Z"
weight = 51509
keywords = [ "nsis", "installation", "batch" ]
aliases = [ "/questions/51509" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Inserting a batch file into nsis installer](/questions/51509/inserting-a-batch-file-into-nsis-installer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51509-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I would like to add a batch file to be executed at the end of a successful Wireshark installation. The goal is to have a single setup.exe file which will include this batch script and it's functionality. I made the installation exe file following the guide on the Development documentation for Win32/Win64. The batch file is setting up a file in %APPDATA%\Wireshark. I've never written a nsi script so I have no idea how to do it.</p><p>Thanks ahead!</p></div><div id="question-tags" class="tags-container tags">nsis installation batch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '16, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/a03fa5b340afab78d2e44b63e8dcf3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aliniel&#39;s gravatar image" /><p>Aliniel<br />
<span class="score" title="30 reputation points">30</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aliniel has 2 accepted answers">100%</span></p></div></div><div id="comments-container-51509" class="comments-container"></div><div id="comment-tools-51509" class="comment-tools"></div><div class="clear"></div><div id="comment-51509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51512"></span>

<div id="answer-container-51512" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51512-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's nothing currently to include a general NSIS custom script section, although there is support for custom scripts for various other things, e.g. plugins, mibs etc.</p><p>You'll have to modify wireshark.nsi to do what you want. Basically use a <code>File "path\to\file"</code> statement to add your batch file to the installer and then use <code>ExecWait ...</code> to execute it. There are nsis plugins, e.g. <a href="http://nsis.sourceforge.net/Docs/nsExec/nsExec.txt">nsExec</a> that will hide the DOS command prompt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '16, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51512" class="comments-container"><span id="51552"></span><div id="comment-51552" class="comment"><div id="post-51552-score" class="comment-score"></div><div class="comment-text"><p>Thanks. It was enough to put <code>ExecWait "$PATH\script.cmd"</code>. It had to be .cmd, .bat wasn't executing for some reason.</p></div><div id="comment-51552-info" class="comment-info"><span class="comment-age">(11 Apr '16, 06:31)</span> Aliniel</div></div></div><div id="comment-tools-51512" class="comment-tools"></div><div class="clear"></div><div id="comment-51512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

