+++
type = "question"
title = "Source files&#x27; config.nmake has Debug compiler and link flags"
description = '''Hi, I noticed that in the 1.12.7 source files (https://www.wireshark.org/download/src/) in the config.nmake file, the /Zi debug compiler flag and /DEBUG linker flag are included. I am wondering if this is just for the development version or does the release version of wireshark have these debugging ...'''
date = "2015-08-26T14:25:00Z"
lastmod = "2015-08-27T01:13:00Z"
weight = 45372
keywords = [ "debug", "config.nmake" ]
aliases = [ "/questions/45372" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Source files' config.nmake has Debug compiler and link flags](/questions/45372/source-files-confignmake-has-debug-compiler-and-link-flags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45372-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I noticed that in the 1.12.7 source files (<a href="https://www.wireshark.org/download/src/)">https://www.wireshark.org/download/src/)</a> in the config.nmake file, the /Zi debug compiler flag and /DEBUG linker flag are included. I am wondering if this is just for the development version or does the release version of wireshark have these debugging flags too? I am trying to make a release version of a plugin and an installer for that and am trying to figure out how to do so.</p><p>Thanks for any info,</p></div><div id="question-tags" class="tags-container tags">debug config.nmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '15, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/8f99f97ead483c8f43cf63e9b3d17f7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-demars&#39;s gravatar image" /><p>j-demars<br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-demars has no accepted answers">0%</span></p></div></div><div id="comments-container-45372" class="comments-container"></div><div id="comment-tools-45372" class="comment-tools"></div><div class="clear"></div><div id="comment-45372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45387"></span>

<div id="answer-container-45387" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45387-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Both these flags cause extra info to be inserted into the .pdb files used for debugging release code and shouldn't (AFAIK) affect the produced binary.</p><p>See MSDN <a href="https://msdn.microsoft.com/en-us/library/958x11bc(v=vs.100).aspx">/Zi</a> and <a href="https://msdn.microsoft.com/en-us/library/xe4t6fc1(v=vs.100).aspx">/Debug</a> for more info.</p><p>You can see the actual build flags used by the buildbots when creating the Wireshark releases by examining the buildbot output, e.g. <a href="https://buildbot.wireshark.org/wireshark-1.12/builders/Windows%207%20x64/builds/815/steps/nmake%20all/logs/stdio">here</a>.</p><p>For your plugin just follow the Developers Guide, that will produce a release version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45387" class="comments-container"></div><div id="comment-tools-45387" class="comment-tools"></div><div class="clear"></div><div id="comment-45387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

