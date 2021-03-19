+++
type = "question"
title = "Error building Wireshark from source"
description = '''I am trying to build Wireshark from source and I followed all the directions in http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html. When building, I get the following error: Microsoft (R) Program Maintenance Utility Version 10.00.40219.01 Copyright (C) Microsoft Corporation. All right...'''
date = "2013-08-12T09:19:00Z"
lastmod = "2013-08-12T09:47:00Z"
weight = 23713
keywords = [ "bison", "error" ]
aliases = [ "/questions/23713" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Error building Wireshark from source](/questions/23713/error-building-wireshark-from-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23713-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build Wireshark from source and I followed all the directions in <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.">http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.</a> When building, I get the following error:</p><p>Microsoft (R) Program Maintenance Utility Version 10.00.40219.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><pre><code>    bison  -d -p ascend ascend.y -o ascend.c</code></pre><p>/usr/bin/bison: m4 subprocess failed NMAKE : fatal error U1077: 'c:\cygwin64\bin\bison.EXE' : return code '0x1' Stop. NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\Bin\nmake.exe"' : return code '0x2' Stop.</p><p>Any ideas on what the issue might be?</p></div><div id="question-tags" class="tags-container tags">bison error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '13, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/85d45dd493cc06438d31656134874a3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miss_develop&#39;s gravatar image" /><p>miss_develop<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miss_develop has no accepted answers">0%</span></p></div></div><div id="comments-container-23713" class="comments-container"><span id="23717"></span><div id="comment-23717" class="comment"><div id="post-23717-score" class="comment-score"></div><div class="comment-text"><p>I assume from the path to the Cygwin binaries you are using an x64 version of Cygwin.</p><p>While it may work, I'm not aware of anyone successfully using an x64 version of Cygwin to build Wireshark. If problems persist you may want to try a 32 bit version.</p></div><div id="comment-23717-info" class="comment-info"><span class="comment-age">(12 Aug '13, 11:03)</span> grahamb ♦</div></div></div><div id="comment-tools-23713" class="comment-tools"></div><div class="clear"></div><div id="comment-23713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23714"></span>

<div id="answer-container-23714" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23714-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you verify that you have m4 installed, e.g. by running <code>m4 --version</code> and <code>which m4</code> from a Cygwin terminal? It looks like Bison either can't find it or is having trouble running it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '13, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-23714" class="comments-container"><span id="23715"></span><div id="comment-23715" class="comment"><div id="post-23715-score" class="comment-score"></div><div class="comment-text"><p>That worked! I installed m4 explicitly on Cygwin and it worked. However, I now get another error:</p><p>Microsoft (R) Windows (R) Resource Compiler Version 6.1.7600.16385 Copyright (C) Microsoft Corporation. All rights reserved.</p><pre><code>    &quot;C:\Python27\python.exe&quot; tools\rdps.py print.ps ps.c
    rm -f svnversion.h
    perl make-version.pl</code></pre><p>NMAKE : fatal error U1077: 'c:\cygwin64\bin\perl.EXE' : return code '0xc0000135'</p><p>Stop.</p></div><div id="comment-23715-info" class="comment-info"><span class="comment-age">(12 Aug '13, 10:26)</span> miss_develop</div></div><span id="23716"></span><div id="comment-23716" class="comment"><div id="post-23716-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23716-info" class="comment-info"><span class="comment-age">(12 Aug '13, 11:00)</span> grahamb ♦</div></div><span id="23718"></span><div id="comment-23718" class="comment"><div id="post-23718-score" class="comment-score"></div><div class="comment-text"><p>Got it resolved. It was a dependency that was not installed during the Cygwin install.</p></div><div id="comment-23718-info" class="comment-info"><span class="comment-age">(12 Aug '13, 11:11)</span> miss_develop</div></div><span id="27978"></span><div id="comment-27978" class="comment"><div id="post-27978-score" class="comment-score"></div><div class="comment-text"><p>@miss_develop Can you comment on the dependency missing? I'm having the same issue.</p></div><div id="comment-27978-info" class="comment-info"><span class="comment-age">(10 Dec '13, 10:12)</span> tlann</div></div></div><div id="comment-tools-23714" class="comment-tools"></div><div class="clear"></div><div id="comment-23714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

