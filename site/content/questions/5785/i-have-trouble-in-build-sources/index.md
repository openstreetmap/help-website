+++
type = "question"
title = "i have trouble in build sources"
description = '''I am building sources of wireshark on Windows7, and I can&#x27;t find bash which can execute on the window7.  Although i find the sources of bash offered in http://www.gnu.org/s/bash/ on Windows7, I cannot install it.  The reason that there is no program required for installing in windows7 like gcc and m...'''
date = "2011-08-21T07:35:00Z"
lastmod = "2011-08-22T19:55:00Z"
weight = 5785
keywords = [ "windows7", "build", "install" ]
aliases = [ "/questions/5785" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [i have trouble in build sources](/questions/5785/i-have-trouble-in-build-sources)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5785-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am building sources of wireshark on Windows7, and I can't find bash which can execute on the window7.</p><p>Although i find the sources of bash offered in http://www.gnu.org/s/bash/ on Windows7, I cannot install it.</p><p>The reason that there is no program required for installing in windows7 like gcc and make.</p><p>So I lost direction, Please, give me the direction.</p></div><div id="question-tags" class="tags-container tags">windows7 build install</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '11, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/528f8dd6acb92d7bc6189be06e46c5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="one%20step&#39;s gravatar image" /><p>one step<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="one step has no accepted answers">0%</span></p></div></div><div id="comments-container-5785" class="comments-container"></div><div id="comment-tools-5785" class="comment-tools"></div><div class="clear"></div><div id="comment-5785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5787"></span>

<div id="answer-container-5787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5787-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you read and followed the step-by-step guide for Windows development found <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">HERE</a>?</p><p>Bash (among other required tools) is provided by Cygwin which is a prerequisite for a Windows build.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '11, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5787" class="comments-container"><span id="5790"></span><div id="comment-5790" class="comment"><div id="post-5790-score" class="comment-score"></div><div class="comment-text"><p>They says "do not use cygwin, use cmd.exe". So, I'm confused.</p><p>Thank you for your answer. Have a nice day!</p></div><div id="comment-5790-info" class="comment-info"><span class="comment-age">(21 Aug '11, 19:11)</span> one step</div></div><span id="5792"></span><div id="comment-5792" class="comment"><div id="post-5792-score" class="comment-score"></div><div class="comment-text"><p>Is there other Bash on windows7 which is not cygwin's bash.</p></div><div id="comment-5792-info" class="comment-info"><span class="comment-age">(21 Aug '11, 21:56)</span> one step</div></div><span id="5796"></span><div id="comment-5796" class="comment"><div id="post-5796-score" class="comment-score"></div><div class="comment-text"><p><a href="http://win-bash.sourceforge.net/">There is</a>, but, as far as I know, nobody has tried building Wireshark without Cygwin and with that version of bash; the Wireshark core team does not make any guarantee that it'll work. Note that the Wireshark build process on Windows requires more UNIX-derived tools than just a Bourne-compatible shell, so a Windows port of bash is not sufficient. (That's what "(among other required tools)" means.)</p></div><div id="comment-5796-info" class="comment-info"><span class="comment-age">(21 Aug '11, 22:53)</span> Guy Harris ♦♦</div></div><span id="5797"></span><div id="comment-5797" class="comment"><div id="post-5797-score" class="comment-score">1</div><div class="comment-text"><p>As for "do not use cygwin, use cmd.exe", that means that the command prompt at which you should type the nmake command is the cmd.exe prompt; however, there are Bourne-shell scripts and commands in the build process, so you still need bash.</p></div><div id="comment-5797-info" class="comment-info"><span class="comment-age">(21 Aug '11, 22:55)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5787" class="comment-tools"></div><div class="clear"></div><div id="comment-5787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5815"></span>

<div id="answer-container-5815" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5815-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Solution: The solution is that add the cygwin's bin folder to environmental variables of window</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '11, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/528f8dd6acb92d7bc6189be06e46c5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="one%20step&#39;s gravatar image" /><p>one step<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="one step has no accepted answers">0%</span></p></div></div><div id="comments-container-5815" class="comments-container"><span id="5818"></span><div id="comment-5818" class="comment"><div id="post-5818-score" class="comment-score"></div><div class="comment-text"><p>I think that's normally part of the Cygwin install.</p></div><div id="comment-5818-info" class="comment-info"><span class="comment-age">(22 Aug '11, 23:52)</span> grahamb ♦</div></div><span id="5821"></span><div id="comment-5821" class="comment"><div id="post-5821-score" class="comment-score"></div><div class="comment-text"><p>@grahamb: Actually, it's not.</p></div><div id="comment-5821-info" class="comment-info"><span class="comment-age">(23 Aug '11, 04:47)</span> bstn</div></div><span id="5822"></span><div id="comment-5822" class="comment"><div id="post-5822-score" class="comment-score"></div><div class="comment-text"><p>I was wrong, confirmed with a Cygwin install on XP SP3.</p><p>I can't remember having done this on numerous Wireshark build installations I've done over the years. The dev guide should be updated to mention this step.</p></div><div id="comment-5822-info" class="comment-info"><span class="comment-age">(23 Aug '11, 05:32)</span> grahamb ♦</div></div><span id="5823"></span><div id="comment-5823" class="comment"><div id="post-5823-score" class="comment-score"></div><div class="comment-text"><p>You don't have to, since it's added to PATH from config.nmake. But the size of your environment may be too restricted to expand with the relevant information.</p></div><div id="comment-5823-info" class="comment-info"><span class="comment-age">(23 Aug '11, 05:53)</span> Jaap ♦</div></div><span id="5825"></span><div id="comment-5825" class="comment"><div id="post-5825-score" class="comment-score"></div><div class="comment-text"><p>Duh, not a good day for me. That's why I've never bothered to do it.</p></div><div id="comment-5825-info" class="comment-info"><span class="comment-age">(23 Aug '11, 07:18)</span> grahamb ♦</div></div></div><div id="comment-tools-5815" class="comment-tools"></div><div class="clear"></div><div id="comment-5815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

