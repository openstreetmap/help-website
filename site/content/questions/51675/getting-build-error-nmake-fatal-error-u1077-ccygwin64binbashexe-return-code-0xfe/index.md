+++
type = "question"
title = "Getting build error: NMAKE: fatal error U1077: &#x27;C:&#92;cygwin64&#92;bin&#92;bash.EXE&#x27; : return code &#x27;0xfe&#x27;"
description = '''NMAKE: fatal error U1077: &#x27;C:&#92;cygwin64&#92;bin&#92;bash.EXE&#x27; : return code &#x27;0xfe&#x27; When I tried to do &#x27;nmake -f Makefile.nmake verify_tools&#x27;. The strange thing is that I was able to build with no issue last week, but this week, I am encountering this error. Please suggest.'''
date = "2016-04-14T12:09:00Z"
lastmod = "2016-04-14T13:36:00Z"
weight = 51675
keywords = [ "build_error", "wireshark" ]
aliases = [ "/questions/51675" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting build error: NMAKE: fatal error U1077: 'C:\\cygwin64\\bin\\bash.EXE' : return code '0xfe'](/questions/51675/getting-build-error-nmake-fatal-error-u1077-ccygwin64binbashexe-return-code-0xfe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51675-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>NMAKE: fatal error U1077: 'C:\cygwin64\bin\bash.EXE' : return code '0xfe' When I tried to do 'nmake -f Makefile.nmake verify_tools'. The strange thing is that I was able to build with no issue last week, but this week, I am encountering this error. Please suggest.</p></div><div id="question-tags" class="tags-container tags">build_error wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '16, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/fe7b8b8f82626427d3ae7d5428f2102d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christenmu&#39;s gravatar image" /><p>christenmu<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christenmu has one accepted answer">50%</span></p></div></div><div id="comments-container-51675" class="comments-container"><span id="51676"></span><div id="comment-51676" class="comment"><div id="post-51676-score" class="comment-score"></div><div class="comment-text"><p>What version of the source? Please append the full output from your nmake command to your question.</p></div><div id="comment-51676-info" class="comment-info"><span class="comment-age">(14 Apr '16, 12:18)</span> grahamb ♦</div></div><span id="51681"></span><div id="comment-51681" class="comment"><div id="post-51681-score" class="comment-score"></div><div class="comment-text"><p>I had this source code downloaded quite sometime ago. It's master_1.12.</p><pre><code>C:\Development\wireshark&gt;&quot;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Vcvarsall.bat&quot;
Setting environment for using Microsoft Visual Studio 2010 x86 tools.

C:\Development\wireshark&gt;set WIRESHARK_TARGET_PLATFORM=win64

C:\Development\wireshark&gt;cd C:\Development\wireshark

C:\Development\wireshark&gt;nmake -f Makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

Checking for required applications:
        cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/link
        nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/nmake
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        /usr/bin/find: /usr/bin/find
   2088 [main] bash 680608 fork: child -1 - CreateProcessW failed for &#39;C:\cygwin64\bin\bash.exe&#39;, errno 12
/cygdrive/c/Development/wireshark/tools/win-setup.sh: fork: Cannot allocate memory
NMAKE : fatal error U1077: &#39;C:\cygwin64\bin\bash.EXE&#39; : return code &#39;0xfe&#39;</code></pre><p>Stop.</p><pre><code>C:\Development\wireshark&gt;</code></pre></div><div id="comment-51681-info" class="comment-info"><span class="comment-age">(14 Apr '16, 12:27)</span> christenmu</div></div></div><div id="comment-tools-51675" class="comment-tools"></div><div class="clear"></div><div id="comment-51675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51685"></span>

<div id="answer-container-51685" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51685-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess rebooting the machine resolved the issue. thanks for your time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/fe7b8b8f82626427d3ae7d5428f2102d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christenmu&#39;s gravatar image" /><p>christenmu<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christenmu has one accepted answer">50%</span></p></div></div><div id="comments-container-51685" class="comments-container"></div><div id="comment-tools-51685" class="comment-tools"></div><div class="clear"></div><div id="comment-51685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51682"></span>

<div id="answer-container-51682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51682-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's an issue with your Cygwin installation. Have you updated it since your last successful build?</p><p>You also seem to be wanting to make an x64 build with <code>set WIRESHARK_TARGET_PLATFORM=win64</code> but have started Visual Studio in x86 mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51682" class="comments-container"><span id="51684"></span><div id="comment-51684" class="comment"><div id="post-51684-score" class="comment-score"></div><div class="comment-text"><p>No, I did not install a new cygwin, I don't believe our IT will push a new cygwin on this machine either. I was able to make a build on the visual studio window last week. I just tried it on windows prompt and got the same error. I have just sent an email inquiry to our IT to see whether they changed the cygwin. Do I need to re-install a new cygwin?</p></div><div id="comment-51684-info" class="comment-info"><span class="comment-age">(14 Apr '16, 13:13)</span> christenmu</div></div></div><div id="comment-tools-51682" class="comment-tools"></div><div class="clear"></div><div id="comment-51682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

