+++
type = "question"
title = "Wireshark Git Rev Unknown from unknown"
description = '''Hi all, I read following link: https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin And also I read README.Cmake file at the source code. Finally I create a Visual Studio 2010 solution for Wireshark and now I can build it moreover debug it.  However, I cannot understand f...'''
date = "2014-11-07T03:35:00Z"
lastmod = "2014-11-07T03:44:00Z"
weight = 37642
keywords = [ "visual", "revision", "cmake", "visual-studio", "wireshark" ]
aliases = [ "/questions/37642" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Git Rev Unknown from unknown](/questions/37642/wireshark-git-rev-unknown-from-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37642-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I read following link:</p><p><a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin</a></p><p>And also I read README.Cmake file at the source code.</p><p>Finally I create a Visual Studio 2010 solution for Wireshark and now I can build it moreover debug it.</p><p>However, I cannot understand following issue: When I click Help -&gt; About, I see following line for the Wireshark revision: Wireshark Git Rev Unknown from unknown</p><p>I understand that a solution which locates at</p><p>Solutioon -&gt; Auxiliary -&gt; gitversion.vcxproj causes this, because when I build it it gives following output:</p><p>1&gt;------ Build started: Project: gitversion, Configuration: Debug x64 ------</p><p>1&gt;CUSTOMBUİLD : cygwin warning :</p><p>1&gt; MS-DOS style path detected: C:/Development/trunk/wireshark/make-version.pl</p><p>1&gt; Preferred POSIX equivalent is: /cygdrive/c/Development/trunk/wireshark/make-version.pl</p><p>1&gt; CYGWIN environment variable option "nodosfilewarning" turns off this warning.</p><p>1&gt; Consult the user's guide for more details about POSIX paths:</p><p>1&gt; <a href="http://cygwin.com/cygwin-ug-net/using.html#using-pathnames">http://cygwin.com/cygwin-ug-net/using.html#using-pathnames</a></p><p>1&gt; Version configuration file version.conf not found. Using defaults.</p><p>1&gt; sh: git: command not found</p><p>1&gt; sh: git: command not found</p><p>1&gt; version.h unchanged.</p><p>I can solve this issue by using c files but I do not want to break down the automaci cmake process.</p><p>Can you help me about this issue?</p></div><div id="question-tags" class="tags-container tags">visual revision cmake visual-studio wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/6257a856e7271c04dd39469c7a5332ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BirolCapa&#39;s gravatar image" /><p>BirolCapa<br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BirolCapa has no accepted answers">0%</span></p></div></div><div id="comments-container-37642" class="comments-container"></div><div id="comment-tools-37642" class="comment-tools"></div><div class="clear"></div><div id="comment-37642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37643"></span>

<div id="answer-container-37643" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37643-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You must ensure that the folder containing the git executable is part of your PATH environment variable because here the Perl script fails to find it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-37643" class="comments-container"><span id="37644"></span><div id="comment-37644" class="comment"><div id="post-37644-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your answer. It works, now I do not get any error from the git version. A little question is again about the About window. Why I always get the default version 1.99.1 - here it is now: Version 1.99.1 (v1.99.1rc0-466-gbb05124 from master) - even if I change the config.nmake file?</p></div><div id="comment-37644-info" class="comment-info"><span class="comment-age">(07 Nov '14, 04:05)</span> BirolCapa</div></div><span id="37647"></span><div id="comment-37647" class="comment"><div id="post-37647-score" class="comment-score"></div><div class="comment-text"><p>version.h contains the version info string and that is produced by make-version.pl which fetches the version string from git via the command:</p><p><code> git describe --long --always --match "v*"</code></p><p>Which on my system gives me the string similar to that which you have.</p><p>If you want to change the version string, you can tack on extra info via the environment variable WIRESHARK_VERSION_EXTRA (or VERSION_EXTRA in config.nmake).</p></div><div id="comment-37647-info" class="comment-info"><span class="comment-age">(07 Nov '14, 05:23)</span> grahamb ♦</div></div></div><div id="comment-tools-37643" class="comment-tools"></div><div class="clear"></div><div id="comment-37643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

