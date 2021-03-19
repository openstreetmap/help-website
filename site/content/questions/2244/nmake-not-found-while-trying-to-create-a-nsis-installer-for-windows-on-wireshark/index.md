+++
type = "question"
title = "nmake not found while trying to create a NSIS installer for windows on wireshark?"
description = '''Hello, I am trying to create a NSIS installer for my wireshark which I have compiled from source code. I have changed the config.nmake file to include the path where nsis.exe is installed.  Now when I try to create the installer using &#x27;nmake -f Makefile.nmake packaging&#x27; I get this error. &#x27;nmake&#x27; is ...'''
date = "2011-02-08T21:45:00Z"
lastmod = "2011-02-08T22:19:00Z"
weight = 2244
keywords = [ "wireshark" ]
aliases = [ "/questions/2244" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [nmake not found while trying to create a NSIS installer for windows on wireshark?](/questions/2244/nmake-not-found-while-trying-to-create-a-nsis-installer-for-windows-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to create a NSIS installer for my wireshark which I have compiled from source code. I have changed the config.nmake file to include the path where nsis.exe is installed.</p><p>Now when I try to create the installer using 'nmake -f Makefile.nmake packaging' I get this error.</p><p><strong>'nmake' is not recognized as an internal or external command, operable program or batch file.</strong></p><p>However, before creating the installer, I compiled using nmake -f Makefile.nmake make all'. I did not face any problems with nmake then. What should be done??</p><p>Thanks,</p><p>Sid</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '11, 21:45</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2244" class="comments-container"></div><div id="comment-tools-2244" class="comment-tools"></div><div class="clear"></div><div id="comment-2244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2246"></span>

<div id="answer-container-2246" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2246-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found the answer..</p><p>The path needed to be set. Refer Wireshark Developers Guide, incase anyone ever again stumbles at the same juncture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2246" class="comments-container"></div><div id="comment-tools-2246" class="comment-tools"></div><div class="clear"></div><div id="comment-2246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

