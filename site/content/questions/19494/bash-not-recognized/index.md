+++
type = "question"
title = "bash not recognized"
description = '''hi,while following the step by step guide for build environment,i get this error: c:&#92;wireshark&amp;gt; nmake -f Makefile.nmake verify_tools  Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation. All rights reserved.  &#x27;bash&#x27; is not recognized as an internal...'''
date = "2013-03-14T04:59:00Z"
lastmod = "2013-03-14T05:23:00Z"
weight = 19494
keywords = [ "cygwin", "bash" ]
aliases = [ "/questions/19494" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [bash not recognized](/questions/19494/bash-not-recognized)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19494-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,while following the step by step guide for build environment,i get this error:</p><pre><code>c:\wireshark&gt; nmake -f Makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

&#39;bash&#39; is not recognized as an internal or external command,
operable program or batch file.
&#39;bash&#39; is not recognized as an internal or external command,
operable program or batch file.
NMAKE : fatal error U1077: &#39;bash&#39; : return code &#39;0x1&#39;
Stop.</code></pre><p>what is the error about?</p></div><div id="question-tags" class="tags-container tags">cygwin bash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/f48b4f4f35dc1e8a66425e223c958173?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chin12&#39;s gravatar image" /><p>chin12<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chin12 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '13, 05:08</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19494" class="comments-container"></div><div id="comment-tools-19494" class="comment-tools"></div><div class="clear"></div><div id="comment-19494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19498"></span>

<div id="answer-container-19498" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19498-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Config.nmake sets the path to Cygwin to be <code>C:\cygwin\bin</code>. I suspect you've installed it elsewhere. If this is the case, adjust the entry in config.nmake.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '13, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19498" class="comments-container"><span id="19500"></span><div id="comment-19500" class="comment"><div id="post-19500-score" class="comment-score"></div><div class="comment-text"><p>i checked it.cygwin binaries are in c:\cygwin\bin.i assume i have to add some path in system environment variable 'path'?</p></div><div id="comment-19500-info" class="comment-info"><span class="comment-age">(14 Mar '13, 06:04)</span> chin12</div></div><span id="19502"></span><div id="comment-19502" class="comment"><div id="post-19502-score" class="comment-score"></div><div class="comment-text"><p>Nope, config.nmake sets that for you. What is the result of <code>dir c:\cygwin\bin\bash.exe</code>?</p></div><div id="comment-19502-info" class="comment-info"><span class="comment-age">(14 Mar '13, 06:28)</span> grahamb ♦</div></div><span id="19503"></span><div id="comment-19503" class="comment"><div id="post-19503-score" class="comment-score"></div><div class="comment-text"><p>ah..i don't see bash.exe in cygwin\bin or anywhere in cygwin.though i see a bashbug file in this directory.have i missed anything here..cygwin's size is 20mb and i downloaded it from one of mirror sites provided on running cygwin's setup.exe.</p></div><div id="comment-19503-info" class="comment-info"><span class="comment-age">(14 Mar '13, 06:44)</span> chin12</div></div><span id="19506"></span><div id="comment-19506" class="comment"><div id="post-19506-score" class="comment-score"></div><div class="comment-text"><p>Odd, I thought bash was an integral part of Cygwin. You should be able to run the setup again and choose the package that contains bash.</p></div><div id="comment-19506-info" class="comment-info"><span class="comment-age">(14 Mar '13, 07:17)</span> grahamb ♦</div></div><span id="19508"></span><div id="comment-19508" class="comment"><div id="post-19508-score" class="comment-score"></div><div class="comment-text"><p>The only thing I can see that would cause that sort of error message is the SetEnv.cmd script uses reg.exe in query mode to obtain some install paths from the registry.</p><p>I guess someone (admin) has disabled that command for some reason on your machine. What output do you get with <code>reg query /?</code>?</p><p>Note that the version of Wireshark you build will no run on OS's earlier than Win7. If you need to run on earlier versions set the target OS as a parameter to SetEnv.cmd, e.g. <code>/xp</code> to target xp. Look at the top of SetEnv.cmd for more info.</p></div><div id="comment-19508-info" class="comment-info"><span class="comment-age">(14 Mar '13, 07:43)</span> grahamb ♦</div></div><span id="19513"></span><div id="comment-19513" class="comment not_top_scorer"><div id="post-19513-score" class="comment-score"></div><div class="comment-text"><p>Any cmd.exe shortcut will do as you should call SetEnv.Cmd as soon as you open it which will set the path to nmake.</p><p>If you look in the Start Menu entry for the SDK, you should find an entry for "Windows SDK 7.1 Command Prompt". Using that gets you a cmd.exe already set up with SetEnv. I've copied that shortcut to my desktop and edited the properties to include <code>/xp /debug</code> at the end.</p></div><div id="comment-19513-info" class="comment-info"><span class="comment-age">(14 Mar '13, 10:03)</span> grahamb ♦</div></div><span id="19514"></span><div id="comment-19514" class="comment not_top_scorer"><div id="post-19514-score" class="comment-score"></div><div class="comment-text"><p>I can't think of anything further to add regarding the "registry editing disabled" issue. I've never seen that before.</p></div><div id="comment-19514-info" class="comment-info"><span class="comment-age">(14 Mar '13, 10:05)</span> grahamb ♦</div></div><span id="19612"></span><div id="comment-19612" class="comment not_top_scorer"><div id="post-19612-score" class="comment-score"></div><div class="comment-text"><p>If your build requires winsparkle then your source is from trunk, therefore you need the packages from trunk, not trunk-1.8.</p></div><div id="comment-19612-info" class="comment-info"><span class="comment-age">(18 Mar '13, 03:36)</span> grahamb ♦</div></div><span id="19631"></span><div id="comment-19631" class="comment not_top_scorer"><div id="post-19631-score" class="comment-score"></div><div class="comment-text"><p>grahamb,thanx a ton..able to build wireshark.But,when i run the wireshark solution in vc++,i get error as win32.mak not found and "nmake -f Makefile.nmake packaging_papps" exited with code 2.i understand its because vc++ has to set env var path for sdk.but how to do that?also,i've to start coding dissector.plz provide links to materials (i'am reading readme.dev now)which contain sample examples of dissectors with concise explanations.thanx.</p></div><div id="comment-19631-info" class="comment-info"><span class="comment-age">(18 Mar '13, 23:20)</span> chin12</div></div><span id="19638"></span><div id="comment-19638" class="comment not_top_scorer"><div id="post-19638-score" class="comment-score"></div><div class="comment-text"><p>AFAIK the Visual Studio solution is old and should not be used. The only supported method of building Wireshark on Windows is via a command line nmake. You can open the executable in Visual Studio for debugging though.</p><p>For dissector writing, README.developer is essential. Read it all thoroughly several times and then again looking at the source code for a dissector for a protocol that you know about. For help and advice the <a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">dev mailing list</a> is a better place to post queries.</p></div><div id="comment-19638-info" class="comment-info"><span class="comment-age">(19 Mar '13, 03:50)</span> grahamb ♦</div></div><span id="19830"></span><div id="comment-19830" class="comment not_top_scorer"><div id="post-19830-score" class="comment-score"></div><div class="comment-text"><p>so,if my dissector has errors..only way for compiling is to do nmake thing?i can't compile my dissector in visual c++.</p></div><div id="comment-19830-info" class="comment-info"><span class="comment-age">(26 Mar '13, 00:37)</span> chin12</div></div><span id="19831"></span><div id="comment-19831" class="comment not_top_scorer"><div id="post-19831-score" class="comment-score"></div><div class="comment-text"><blockquote><p>only way for compiling is to do nmake thing?i</p></blockquote><p>Your only alternatives for building with MSVC++ on Windows are nmake or CMake. It's painful enough to support those two mechanisms, along with automake for UN*X systems; supporting a Windows-only build system not oriented towards allowing manual editing of the build files is probably not likely to happen, given that many of the Wireshark developers are running on UN*X systems and can't run MSVC++ to add new source files, so, unless you can build in VC++ with nmake, building with VC++ will probably never be well supported.</p></div><div id="comment-19831-info" class="comment-info"><span class="comment-age">(26 Mar '13, 00:42)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-19498" class="comment-tools"><span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a></div><div class="clear"></div><div id="comment-19498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

