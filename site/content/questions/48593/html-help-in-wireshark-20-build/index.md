+++
type = "question"
title = "Html Help in Wireshark 2.0 build"
description = '''I setup the Windows build environment for Wireshark 2.0 and I&#x27;m trying to build. I should have all the versions of things from the Win32/Win64 Step-by-Step guide. I downloaded the source tarball from website and have made no modifications to anything not in the guide.  I make it through the cmake pr...'''
date = "2015-12-16T20:11:00Z"
lastmod = "2016-01-22T13:09:00Z"
weight = 48593
keywords = [ "2.0", "help", "html", "wireshark" ]
aliases = [ "/questions/48593" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Html Help in Wireshark 2.0 build](/questions/48593/html-help-in-wireshark-20-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48593-score" class="post-score" title="current number of votes">0</div><span id="post-48593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I setup the Windows build environment for Wireshark 2.0 and I'm trying to build. I should have all the versions of things from the Win32/Win64 Step-by-Step guide. I downloaded the source tarball from website and have made no modifications to anything not in the guide.</p><p>I make it through the cmake process, but it seems to absolutely refuse to find Html Help Workshop. It is installed along with about every docbook module in cygwin.</p><p>I think this is the issue I'm having because the docbook projects fail to build.</p><p>This is the end of the cmake step (didn't include found optional packages, this question is long enough):</p><p>-- The following REQUIRED packages have been found:</p><ul><li>PowerShell</li><li>GLIB2</li><li>GTHREAD2</li><li>LEX</li><li>YACC</li></ul><p>-- The following OPTIONAL packages have not been found:</p><ul><li>CAP</li><li>Gettext</li><li>M</li><li>PkgConfig</li><li>SBC , SBC Codec for Bluetooth A2DP stream playing , &lt;www: &lt;a="" href="http://git.kernel.o"&gt;http://git.kernel.o rg/cgit/bluetooth/sbc.git&gt;</li><li>SETCAP</li><li>YAPP</li><li>HTMLHelp</li></ul><p>-- Configuring done -- Generating done -- Build files have been written to: C:/Development/WiresharkBuild32</p><p>This is the mess I get when I run msbuild: Build FAILED.</p><pre><code>   &quot;C:\Development\WiresharkBuild32\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\WiresharkBuild32\docbook\release_notes_html.vcxproj.meta
   proj&quot; (default target) (59) -&gt;
   &quot;C:\Development\WiresharkBuild32\docbook\release_notes_html.vcxproj&quot; (de
   fault target) (70) -&gt;
   (CustomBuild target) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCo
   mmon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 2. [C:\De
   velopment\WiresharkBuild32\docbook\release_notes_html.vcxproj]

   &quot;C:\Development\WiresharkBuild32\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\WiresharkBuild32\docbook\user_guide_docbook.vcxproj.meta
   proj&quot; (default target) (64) -&gt;
   &quot;C:\Development\WiresharkBuild32\docbook\user_guide_docbook.vcxproj&quot; (de
   fault target) (68) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCo
   mmon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 2. [C:\De
   velopment\WiresharkBuild32\docbook\user_guide_docbook.vcxproj]

   &quot;C:\Development\WiresharkBuild32\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\WiresharkBuild32\docbook\developer_guide_docbook.vcxproj
   .metaproj&quot; (default target) (54) -&gt;
   &quot;C:\Development\WiresharkBuild32\docbook\developer_guide_docbook.vcxproj
   &quot; (default target) (69) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCo
   mmon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 2. [C:\De
   velopment\WiresharkBuild32\docbook\developer_guide_docbook.vcxproj]

0 Warning(s)
3 Error(s)</code></pre><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-2.0" rel="tag" title="see questions tagged &#39;2.0&#39;">2.0</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '15, 20:11</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p><span>brwiese</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-48593" class="comments-container"></div><div id="comment-tools-48593" class="comment-tools"></div><div class="clear"></div><div id="comment-48593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48607"></span>

<div id="answer-container-48607" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48607-score" class="post-score" title="current number of votes">0</div><span id="post-48607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There seems to be a couple of issues here:</p><ol><li>CMake fails to report it finds the HTML Help package, even when it does find the help compiler.</li><li>Your build fails for as yet unknown reasons.</li></ol><p>For (1), this requires an upstream fix by CMake, or a local override of the upstream FindHTMLHelp.cmake to report the package as found.</p><p>For (2), can you look at the CMakeCache.txt file in your build directory for lines with <code>HTML_HELP_</code> in them? These will be the path to the compiler, the path to the includes for the compiler and the path the the library.</p><p>To minimise the output when testing you can just build a single docbook project, e.g.</p><p><code>msbuild /m /p:Configuration=RelWithDebInfo .\docbook\release_notes_html.vcxproj</code></p><p>To turn on more logging, and log to a file append the following to the msbuild command:</p><p><code>/fl /flp:logfile=path\to\log\file;verbosity=diagnostic</code></p><p>You might need to quote some of these parameters depending on the command shell you use. When debugging builds, it's helpful to remove the <code>/m</code> flag to stop parallel building, so nodes are built serially and the output is less difficult to follow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '15, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Dec '15, 03:35</strong> </span></p></div></div><div id="comments-container-48607" class="comments-container"></div><div id="comment-tools-48607" class="comment-tools"></div><div class="clear"></div><div id="comment-48607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49467"></span>

<div id="answer-container-49467" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49467-score" class="post-score" title="current number of votes">0</div><span id="post-49467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So, if I get the source using git this problem goes away. The tar balls for windows are either old, not complete, or just wrong.</p><p>Thanks, Brian</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '16, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p><span>brwiese</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-49467" class="comments-container"></div><div id="comment-tools-49467" class="comment-tools"></div><div class="clear"></div><div id="comment-49467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

