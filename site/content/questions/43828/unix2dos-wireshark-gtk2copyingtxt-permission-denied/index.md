+++
type = "question"
title = "unix2dos: wireshark-gtk2/COPYING.txt: Permission denied"
description = '''I ran through the development guide to setup up a wireshark development environment on my windows 7 computer.  I have the wireshark 1.12.6 code on my computer in c:&#92;development&#92;wireshark verify_tools and setup complete fine.  When running make all I get the following error: bash -o igncr tools/texti...'''
date = "2015-07-02T10:41:00Z"
lastmod = "2015-07-02T13:10:00Z"
weight = 43828
keywords = [ "makefile.nmake", "u2d", "unix2dos", "all", "permission" ]
aliases = [ "/questions/43828" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unix2dos: wireshark-gtk2/COPYING.txt: Permission denied](/questions/43828/unix2dos-wireshark-gtk2copyingtxt-permission-denied)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43828-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I ran through the development guide to setup up a wireshark development environment on my windows 7 computer.</p><p>I have the wireshark 1.12.6 code on my computer in c:\development\wireshark</p><p>verify_tools and setup complete fine.</p><p>When running make all I get the following error:</p><pre><code>bash -o igncr tools/textify.sh &quot;./COPYING&quot; wireshark-gtk2
unix2dos: wireshark-gtk2/COPYING.txt: Permission denied
unix2dos: converting file wireshark-gtk2/COPYING.txt to DOS format...
unix2dos: problems converting file wireshark-gtk2/COPYING.txt
NMAKE : fatal error U1077: &#39;C:\cygwin64\bin\bash.EXE&#39; : return code &#39;0xd&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags">makefile.nmake u2d unix2dos all permission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '15, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/fb647bfd9cda0befa12b774fd49e2e6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bigbadbyte&#39;s gravatar image" /><p>bigbadbyte<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bigbadbyte has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '15, 12:14</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-43828" class="comments-container"><span id="43829"></span><div id="comment-43829" class="comment"><div id="post-43829-score" class="comment-score">1</div><div class="comment-text"><p>What is your cygwin version (uname -a in a cygwin bash shell)? I've just run into this after a cygwin update</p></div><div id="comment-43829-info" class="comment-info"><span class="comment-age">(02 Jul '15, 11:00)</span> grahamb ♦</div></div><span id="43830"></span><div id="comment-43830" class="comment"><div id="post-43830-score" class="comment-score"></div><div class="comment-text"><p>CYGWIN_NT-6.1-WOW BIGBADBYTE 2.0.4(0.287/5/3) 2015-06-09 12:20 i686 Cygwin</p></div><div id="comment-43830-info" class="comment-info"><span class="comment-age">(02 Jul '15, 11:04)</span> bigbadbyte</div></div><span id="43832"></span><div id="comment-43832" class="comment"><div id="post-43832-score" class="comment-score">1</div><div class="comment-text"><p>What happens if you remove the COPYING.txt file from the wireshark-gtk2 directory and try to build it again?</p></div><div id="comment-43832-info" class="comment-info"><span class="comment-age">(02 Jul '15, 15:02)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-43828" class="comment-tools"></div><div class="clear"></div><div id="comment-43828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43831"></span>

<div id="answer-container-43831" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43831-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure the command prompt has an admin access?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '15, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/059a334676449782e9d927f2f79351fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="broccollirob&#39;s gravatar image" /><p>broccollirob<br />
<span class="score" title="75 reputation points">75</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="broccollirob has no accepted answers">0%</span></p></div></div><div id="comments-container-43831" class="comments-container"><span id="43892"></span><div id="comment-43892" class="comment"><div id="post-43892-score" class="comment-score"></div><div class="comment-text"><p>Dang it. That was it.</p><p>I had it building previously and then went back and tried to do it again and I forgot to run the command prompt from admin. Thanks.</p></div><div id="comment-43892-info" class="comment-info"><span class="comment-age">(06 Jul '15, 08:47)</span> bigbadbyte</div></div><span id="43893"></span><div id="comment-43893" class="comment"><div id="post-43893-score" class="comment-score"></div><div class="comment-text"><p>Interesting, I've never (intentionally that is) run my command prompts with elevated permissions. Was that intentional originally?</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-43893-info" class="comment-info"><span class="comment-age">(06 Jul '15, 09:25)</span> grahamb ♦</div></div></div><div id="comment-tools-43831" class="comment-tools"></div><div class="clear"></div><div id="comment-43831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

