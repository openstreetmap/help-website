+++
type = "question"
title = "MAKENSIS makensis path"
description = '''Hello, one more time i would like to ask a stupid question : MAKENSIS=&quot;NSIS&#92;makensis.exe&quot;  What is here wrong ;) I have install nsis-2.46-setup.exe at c:&#92;NSIS. I can&#x27;t run the packaging. Every time i try  nmake -f Makefile.nmake packaging  i get an error, that he don&#x27;t find makensis.exe. Please help...'''
date = "2014-03-17T09:26:00Z"
lastmod = "2014-03-17T09:50:00Z"
weight = 30890
keywords = [ "packaging", "makensis" ]
aliases = [ "/questions/30890" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MAKENSIS makensis path](/questions/30890/makensis-makensis-path)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30890-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>one more time i would like to ask a stupid question :</p><pre><code>MAKENSIS=&quot;NSIS\makensis.exe&quot;</code></pre><p>What is here wrong ;) I have install nsis-2.46-setup.exe at c:\NSIS. I can't run the packaging. Every time i try</p><pre><code>nmake -f Makefile.nmake packaging</code></pre><p>i get an error, that he don't find makensis.exe. Please help me. He say :</p><p>? NSIS not available (MAKENSIS not defined in config.nmake)</p><p>NMAKE : fatal error U1077: 'exit' : return code '0x1' Stop. NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\amd64\nmake.exe"' : return code '0x2'</p></div><div id="question-tags" class="tags-container tags">packaging makensis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/3378e4af34b02834b98e8a896efe303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alias_alias&#39;s gravatar image" /><p>Alias_alias<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alias_alias has no accepted answers">0%</span></p></div></div><div id="comments-container-30890" class="comments-container"></div><div id="comment-tools-30890" class="comment-tools"></div><div class="clear"></div><div id="comment-30890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30894"></span>

<div id="answer-container-30894" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30894-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><del>You haven't followed the development guide correctly (see <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChToolsNSIS.html">here</a>):</del></p><del></del><blockquote>To install it, simply download the latest released version (currently 2.46) from <a href="http://nsis.sourceforge.net">http://nsis.sourceforge.net</a> and start the downloaded installer.</blockquote></strike><p><del>After installation is complete. the Wireshark build process will then pick-up the installed version of makensis automatically (as long as it's in a standard location).</del></p><p><strong>Edit:</strong></p><p>The above statements were incorrect, there appears to be an issue with config.nmake and the default NSIS installer location on a 64 bit OS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '14, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Mar '14, 09:14</p></div></div><div id="comments-container-30894" class="comments-container"><span id="30895"></span><div id="comment-30895" class="comment"><div id="post-30895-score" class="comment-score"></div><div class="comment-text"><p>I have try that too. But nothing. Every time i get the same error.</p><p>So i would like to set the path manuel. How can i make that ?</p></div><div id="comment-30895-info" class="comment-info"><span class="comment-age">(17 Mar '14, 11:14)</span> Alias_alias</div></div><span id="30896"></span><div id="comment-30896" class="comment"><div id="post-30896-score" class="comment-score"></div><div class="comment-text"><p>Must i make the Setup again ?</p></div><div id="comment-30896-info" class="comment-info"><span class="comment-age">(17 Mar '14, 11:15)</span> Alias_alias</div></div><span id="30905"></span><div id="comment-30905" class="comment"><div id="post-30905-score" class="comment-score"></div><div class="comment-text"><p>Where is the installed version of nsis in your system, i.e. the path to makensis.exe?</p></div><div id="comment-30905-info" class="comment-info"><span class="comment-age">(17 Mar '14, 14:47)</span> grahamb ♦</div></div><span id="30915"></span><div id="comment-30915" class="comment"><div id="post-30915-score" class="comment-score"></div><div class="comment-text"><p>First it was at :</p><p>C:\Program Files (x86)\NSIS</p><p>Then i have delete NISIS and try :</p><p>C:\NSIS</p><p>But nothing he don't found NSIS.</p><p>When I Install NSIS at : C:\Program Files (x86)\NSIS , I get :</p><pre><code>  C:\Development\wireshark(besser)&gt;nmake -f Makefile.nmake packaging
  Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
  Copyright (C) Microsoft Corporation.  All rights reserved.
  Can&#39;t find Qt. This will become a problem at some point.
  ? NSIS not available (MAKENSIS not defined in config.nmake)
  NMAKE : fatal error U1077: &#39;exit&#39; : return code &#39;0x1&#39;
  Stop.
  C:\Development\wireshark(besser)&gt;</code></pre></div><div id="comment-30915-info" class="comment-info"><span class="comment-age">(18 Mar '14, 01:22)</span> Alias_alias</div></div><span id="30921"></span><div id="comment-30921" class="comment"><div id="post-30921-score" class="comment-score">1</div><div class="comment-text"><p>@Alias_alias,</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>Config.nmake looks for makensis.exe in <code>$(PROGRAM_FILES)\NSIS\makensis.exe</code> and <code>$(PROGRAM_FILES_W6432)\NSIS\makensis.exe</code> and those variables resolve to the env variables <code>ProgramFiles</code> and <code>ProgramW6432</code> respectively, which on my Win 7 machine are both set to <code>C:\Program Files</code>.</p><p>Thus, even though the nsis installer will (by default) install to the ProgramFiles(x86) location, config.nmake isn't looking for it there. Please raise a bug for this on the Wireshark <a href="https://bugs.wireshark.org/">Bugzilla</a>.</p><p>To fix your immediate problem, edit config.nmake and uncomment the line <code>#MAKENSIS="\custom\path\to\NSIS\makensis.exe"</code> by removing the '#' and adding the correct path, e.g. <code>MAKENSIS="C:\Program Files (x86)\NSIS\makensis.exe</code>.</p></div><div id="comment-30921-info" class="comment-info"><span class="comment-age">(18 Mar '14, 02:48)</span> grahamb ♦</div></div><span id="30922"></span><div id="comment-30922" class="comment not_top_scorer"><div id="post-30922-score" class="comment-score"></div><div class="comment-text"><p>Ok next round ;)FIRST THANKS !</p><p>I have add : MAKENSIS="C:\Program Files (x86)\NSIS\makensis.exe" to config.nmake and Makefile.nmake and now it start. Now there is an other error. I try now to fix it. If I have more Problems i post again ;)</p><p>So thanks a lot !</p></div><div id="comment-30922-info" class="comment-info"><span class="comment-age">(18 Mar '14, 03:20)</span> Alias_alias</div></div></div><div id="comment-tools-30894" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-30894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

