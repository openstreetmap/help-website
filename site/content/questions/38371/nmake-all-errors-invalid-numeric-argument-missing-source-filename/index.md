+++
type = "question"
title = "Nmake All Errors - Invalid Numeric Argument / Missing Source Filename."
description = '''I&#x27;m trying to build Wireshark from source for x64, and am running into some problems. Currently, after following all the setup instructions, when I try to do a full make on it I get these messages: cl : Command line error d8021 : invalid numeric argument &#x27;/FS&#x27; NMAKE : fatal error U1077: &#x27;&quot;c:&#92;Program...'''
date = "2014-12-05T11:22:00Z"
lastmod = "2014-12-05T11:33:00Z"
weight = 38371
keywords = [ "makefile.nmake", "commandline", "nmake" ]
aliases = [ "/questions/38371" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nmake All Errors - Invalid Numeric Argument / Missing Source Filename.](/questions/38371/nmake-all-errors-invalid-numeric-argument-missing-source-filename)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to build Wireshark from source for x64, and am running into some problems. Currently, after following all the setup instructions, when I try to do a full make on it I get these messages:</p><p>cl : Command line error d8021 : invalid numeric argument '/FS' NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64\nmake.EXE"' : return code '0x2' Stop. NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64\nmake.EXE"' : return code '0x2' Stop.</p><p>when I try to run that command myself from the command line, I get the following message:</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 16.00.40219.01 for x64 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl : Command line error D8003 : missing source filename</p><p>Any idea what might be causing this?</p></div><div id="question-tags" class="tags-container tags">makefile.nmake commandline nmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '14, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p>mehubb985<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div></div><div id="comments-container-38371" class="comments-container"></div><div id="comment-tools-38371" class="comment-tools"></div><div class="clear"></div><div id="comment-38371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38372"></span>

<div id="answer-container-38372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38372-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As seen on <a href="http://stackoverflow.com/questions/24494251/deploying-a-qt-5-3-app-on-windows">stackoverflow</a>, this probably happens because you are trying to compile the Qt GUI with MSVC2010 (there is no x64 Qt package for MSVC2010). So you need either to switch MSVC2013 (the Community Edition is available for free) or build only the GTK based GUI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '14, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-38372" class="comments-container"></div><div id="comment-tools-38372" class="comment-tools"></div><div class="clear"></div><div id="comment-38372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

