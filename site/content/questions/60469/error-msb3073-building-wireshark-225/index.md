+++
type = "question"
title = "error MSB3073 building wireshark 2.2.5"
description = ''' 72&amp;gt;Done Building Project &quot;D:&#92;Development&#92;msbuild64&#92;wireshark-gtk.vcxproj.metaproj&quot; (default targets).  140&amp;gt;PostBuildEvent:  setlocal  C:&#92;ProgramData&#92;chocolatey&#92;lib&#92;cmake.portable&#92;tools&#92;cmake-3.7.2-win32-x86&#92;bin&#92;cmake.exe -E copy_if_different D:/Development/WireShark/ipmap.html D:/Development/...'''
date = "2017-03-31T02:32:00Z"
lastmod = "2017-04-07T06:45:00Z"
weight = 60469
keywords = [ "build_error", "msbuild", "wireshark-2.2.5" ]
aliases = [ "/questions/60469" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [error MSB3073 building wireshark 2.2.5](/questions/60469/error-msb3073-building-wireshark-225)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60469-score" class="post-score" title="current number of votes">0</div><span id="post-60469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>    72&gt;Done Building Project &quot;D:\Development\msbuild64\wireshark-gtk.vcxproj.metaproj&quot; (default targets).
   140&gt;PostBuildEvent:
         setlocal
         C:\ProgramData\chocolatey\lib\cmake.portable\tools\cmake-3.7.2-win32-x86\bin\cmake.exe -E copy_if_different D:/Development/WireShark/ipmap.html D:/Development/msbuild64/run/RelWithDebInfo
         if %errorlevel% neq 0 goto :cmEnd
         :cmEnd
         endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
         :cmErrorLevel
         exit /b %1
         :cmDone
         if %errorlevel% neq 0 goto :VCEnd
         :VCEnd
       FinalizeBuildStatus:
         Deleting file &quot;wireshark.dir\RelWithDebInfo\wireshark.tlog\unsuccessfulbuild&quot;.
         Touching &quot;wireshark.dir\RelWithDebInfo\wireshark.tlog\wireshark.lastbuildstate&quot;.
   140&gt;Done Building Project &quot;D:\Development\msbuild64\wireshark.vcxproj&quot; (default targets).
    71&gt;Done Building Project &quot;D:\Development\msbuild64\wireshark.vcxproj.metaproj&quot; (default targets).
     1&gt;Project &quot;D:\Development\msbuild64\Wireshark.sln&quot; (1) is building &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (13) on node 1 (default targets).
    13&gt;Project &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (13) is building &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj&quot; (157) on node 2 (default targets).
   157&gt;InitializeBuildStatus:
         Touching &quot;x64\RelWithDebInfo\copy_qt_dlls\copy_qt_dlls.tlog\unsuccessfulbuild&quot;.
       CustomBuild:
         All outputs are up-to-date.
       PostBuildEvent:
         setlocal
         set PATH=%PATH%;C:/Qt/Qt5.6.2/5.6/msvc2013_64/bin
         if %errorlevel% neq 0 goto :cmEnd
         C:\Qt\Qt5.6.2\5.6\msvc2013_64\bin\windeployqt.exe  --release --no-compiler-runtime --verbose 10 D:/Development/msbuild64/run/RelWithDebInfo/Wireshark.exe
         if %errorlevel% neq 0 goto :cmEnd
         :cmEnd
         endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
         :cmErrorLevel
         exit /b %1
         :cmDone
         if %errorlevel% neq 0 goto :VCEnd
         :VCEnd
   157&gt;EXEC : warning : Unable to read \cygdrive\c\Qt\Qt5.6.2\5.6\msvc2013_64\mkspecs\qconfig.pri: The system cannot find the path specified. [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
         Unsupported platform cygwin-g++
   157&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: The command &quot;setlocal [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: set PATH=%PATH%;C:/Qt/Qt5.6.2/5.6/msvc2013_64/bin [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: C:\Qt\Qt5.6.2\5.6\msvc2013_64\bin\windeployqt.exe  --release --no-compiler-runtime --verbose 10 D:/Development/msbuild64/run/RelWithDebInfo/Wireshark.exe [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :cmEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :cmErrorLevel [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: exit /b %1 [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :cmDone [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: if %errorlevel% neq 0 goto :VCEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :VCEnd&quot; exited with code 1. [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
   157&gt;Done Building Project &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj&quot; (default targets) -- FAILED.
    13&gt;Done Building Project &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (default targets) -- FAILED.
     2&gt;Done Building Project &quot;D:\Development\msbuild64\ALL_BUILD.vcxproj.metaproj&quot; (default targets) -- FAILED.
     1&gt;Done Building Project &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default targets) -- FAILED.

Build FAILED.

       &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (default target) (13) -&gt;
       &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj&quot; (default target) (157) -&gt;
       (PostBuildEvent target) -&gt; 
         EXEC : warning : Unable to read \cygdrive\c\Qt\Qt5.6.2\5.6\msvc2013_64\mkspecs\qconfig.pri: The system cannot find the path specified. [D:\Development\msbuild64\copy_qt_dlls.vcxproj]

       &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (default target) (15) -&gt;
       &quot;D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj&quot; (default target) (100) -&gt;
       (CustomBuild target) -&gt; 
         CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj]

       &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;D:\Development\msbuild64\docbook\release_notes_html.vcxproj.metaproj&quot; (default target) (51) -&gt;
       &quot;D:\Development\msbuild64\docbook\release_notes_html.vcxproj&quot; (default target) (106) -&gt;
         a2x : error : &quot;xmllint&quot; --nonet --noout --valid &quot;/cygdrive/d/Development/msbuild64/docbook/release-notes.xml&quot; returned non-zero exit status 4 [D:\Development\msbuild64\docbook\release_notes_html.vcxproj]

       &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;D:\Development\msbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (default target) (64) -&gt;
       &quot;D:\Development\msbuild64\docbook\user_guide_chm.vcxproj&quot; (default target) (133) -&gt;
         CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\user_guide_chm.vcxproj]

       &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (default target) (13) -&gt;
       &quot;D:\Development\msbuild64\copy_qt_dlls.vcxproj&quot; (default target) (157) -&gt;
       (PostBuildEvent target) -&gt; 
         C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: The command &quot;setlocal [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: set PATH=%PATH%;C:/Qt/Qt5.6.2/5.6/msvc2013_64/bin [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: C:\Qt\Qt5.6.2\5.6\msvc2013_64\bin\windeployqt.exe  --release --no-compiler-runtime --verbose 10 D:/Development/msbuild64/run/RelWithDebInfo/Wireshark.exe [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :cmEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :cmErrorLevel [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: exit /b %1 [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :cmDone [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: if %errorlevel% neq 0 goto :VCEnd [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
       C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(132,5): error MSB3073: :VCEnd&quot; exited with code 1. [D:\Development\msbuild64\copy_qt_dlls.vcxproj]

    1 Warning(s)
    4 Error(s)</code></pre><p><a href="https://drive.google.com/open?id=0B9dMRjnjjypGLWNONW90ci15bEU">msbuilt.txt</a> as the complete Log</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-msbuild" rel="tag" title="see questions tagged &#39;msbuild&#39;">msbuild</span> <span class="post-tag tag-link-wireshark-2.2.5" rel="tag" title="see questions tagged &#39;wireshark-2.2.5&#39;">wireshark-2.2.5</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '17, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p><span>DhanuShalz</span><br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Mar '17, 02:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60469" class="comments-container"></div><div id="comment-tools-60469" class="comment-tools"></div><div class="clear"></div><div id="comment-60469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60471"></span>

<div id="answer-container-60471" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60471-score" class="post-score" title="current number of votes">0</div><span id="post-60471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DhanuShalz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You still have the same errors when building the docs as in your previous question, and you now have a new issue where the Qt tool "windeployqt" returns an odd error:</p><pre><code>157&gt;EXEC : warning : Unable to read \cygdrive\c\Qt\Qt5.6.2\5.6\msvc2013_64\mkspecs\qconfig.pri: The system cannot find the path specified. [D:\Development\msbuild64\copy_qt_dlls.vcxproj]
     Unsupported platform cygwin-g++</code></pre><p>I haven't come accross this error before, can you show the contents of your PATH variable, i.e.</p><pre><code>echo %PATH% &gt; path.txt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '17, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60471" class="comments-container"><span id="60472"></span><div id="comment-60472" class="comment"><div id="post-60472-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/open?id=0B9dMRjnjjypGN0J2SDZocW9vZHc">path.txt</a></p><p><span>@grahamb</span></p></div><div id="comment-60472-info" class="comment-info"><span class="comment-age">(31 Mar '17, 03:06)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60473"></span><div id="comment-60473" class="comment"><div id="post-60473-score" class="comment-score"></div><div class="comment-text"><p>You have quite a few items on your path that are likely to be causing issues. The ones I noticed are:</p><ul><li>C:\Qt_qt531-win32\qtbase\bin - this might be the cause of the windeployqt issue</li><li>C:\cygwin64\bin &amp; C:\cygwin64\lib\qt5\bin - Cygwin and Cygwin QT should NOT be on your path, this also might be the cause of the windeployqt issue.</li></ul><p>and you have elements of VS2008 (Visual Studio 9.0) on the path, those should be removed.</p><p>There is also no need to have the Wireshark win64-libs-2.2 directory on the path although that shouldn't hurt.</p></div><div id="comment-60473-info" class="comment-info"><span class="comment-age">(31 Mar '17, 03:31)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60475"></span><div id="comment-60475" class="comment"><div id="post-60475-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> it didn't work, still getting the same error!</p></div><div id="comment-60475-info" class="comment-info"><span class="comment-age">(31 Mar '17, 05:02)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60477"></span><div id="comment-60477" class="comment"><div id="post-60477-score" class="comment-score"></div><div class="comment-text"><p>Did you delete CMakeCache.txt in your build directory, or the entire build directory, and then in either case rerun the CMake generation step?</p></div><div id="comment-60477-info" class="comment-info"><span class="comment-age">(31 Mar '17, 06:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60479"></span><div id="comment-60479" class="comment"><div id="post-60479-score" class="comment-score"></div><div class="comment-text"><p>i have deleted the directory and re-ran it again, but facing the same ERRORS</p></div><div id="comment-60479-info" class="comment-info"><span class="comment-age">(31 Mar '17, 06:24)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60480"></span><div id="comment-60480" class="comment not_top_scorer"><div id="post-60480-score" class="comment-score"></div><div class="comment-text"><p>As you still seem to have issues with your path, I've backported <a href="https://code.wireshark.org/review/20809">this</a> change to 2.2 to ensure the required Qt bin directory is added to the front of the path. This should fix the windeployqt issue.</p><p>You'll need to update your sources from Git, ensure you have change 959bc4cf (<code>git log 959bc4cf</code>), delete your build dir and re-run cmake and msbuild.</p></div><div id="comment-60480-info" class="comment-info"><span class="comment-age">(31 Mar '17, 07:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60604"></span><div id="comment-60604" class="comment not_top_scorer"><div id="post-60604-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span></p><p>As you mention i just took the latest git revision</p><p>I am facing some new errors on building the fresh source code. the errors are as bleow:</p><p>Build FAILED.</p><pre><code>   &quot;E:\Development\msbuild\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;E:\Development\msbuild\epan\dissectors\dissectors.vcxproj.metaproj&quot; (default target) (20) -&gt;
   &quot;E:\Development\msbuild\epan\dissectors\dissectors.vcxproj&quot; (default target) (118) -&gt;
   (ClCompile target) -&gt;
     E:\Development\wireshark\epan\dissectors\packet-usb-i1d3.c(434): error C2275: &#39;guint32&#39; : illegal use of this type as an expression [E:\Development\
   msbuild\epan\dissectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-usb-i1d3.c(434): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;response_code&#39; [E:\Devel
   opment\msbuild\epan\dissectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-usb-i1d3.c(434): error C2065: &#39;response_code&#39; : undeclared identifier [E:\Development\msbuild\epan\d
   issectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-usb-i1d3.c(436): error C2065: &#39;response_code&#39; : undeclared identifier [E:\Development\msbuild\epan\d
   issectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-usb-i1d3.c(438): error C2065: &#39;response_code&#39; : undeclared identifier [E:\Development\msbuild\epan\d
   issectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-usb-i1d3.c(439): error C2065: &#39;response_code&#39; : undeclared identifier [E:\Development\msbuild\epan\d
   issectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-usb-i1d3.c(442): error C2065: &#39;response_code&#39; : undeclared identifier [E:\Development\msbuild\epan\d
   issectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-ipv6.c(2093): error C2275: &#39;guint16&#39; : illegal use of this type as an expression [E:\Development\msb
   uild\epan\dissectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-ipv6.c(2093): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;mapped_port&#39; [E:\Developmen
   t\msbuild\epan\dissectors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-ipv6.c(2093): error C2065: &#39;mapped_port&#39; : undeclared identifier [E:\Development\msbuild\epan\dissec
   tors\dissectors.vcxproj]
     E:\Development\wireshark\epan\dissectors\packet-ipv6.c(2104): error C2065: &#39;mapped_port&#39; : undeclared identifier [E:\Development\msbuild\epan\dissec
   tors\dissectors.vcxproj]

0 Warning(s)
11 Error(s)</code></pre><p>Time Elapsed 00:00:05.58</p></div><div id="comment-60604-info" class="comment-info"><span class="comment-age">(06 Apr '17, 02:55)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60607"></span><div id="comment-60607" class="comment not_top_scorer"><div id="post-60607-score" class="comment-score"></div><div class="comment-text"><p>Still seems to be issues with the definitions of guint32 and guint16 in a very similar manner to this <a href="https://ask.wireshark.org/questions/59065/updating-custom-dissector-from-16-wireshark-to-22-wireshark">question</a>.</p><p>As I noted there I can't see why that is failing.</p><p>Can you post the earlier errors from the build file where the actual compile commands are of packet-usb-i1d3 and packet-ipv6.c?</p></div><div id="comment-60607-info" class="comment-info"><span class="comment-age">(06 Apr '17, 03:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60614"></span><div id="comment-60614" class="comment not_top_scorer"><div id="post-60614-score" class="comment-score"></div><div class="comment-text"><p>reached till a point were im facing the MSB3073 error:</p><p>the cmake log and msbuild log is below</p><p><a href="https://drive.google.com/file/d/0B9dMRjnjjypGV2xXYmJDVFd0TEE/view?usp=sharing">cmake</a></p><p><a href="https://drive.google.com/open?id=0B9dMRjnjjypGR25Makp6cFR1QkE">msbuild</a></p></div><div id="comment-60614-info" class="comment-info"><span class="comment-age">(06 Apr '17, 06:51)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60615"></span><div id="comment-60615" class="comment not_top_scorer"><div id="post-60615-score" class="comment-score"></div><div class="comment-text"><p>You build is still failing to run windeployqt:</p><pre><code>161&gt;EXEC : warning : Unable to read \Qt\Qt5.6.2\5.6\msvc2013_64\mkspecs\qconfig.pri: The system cannot find the path specified. [F:\Development\msbuild\copy_qt_dlls.vcxproj]
     Unsupported platform cygwin-g++</code></pre><p>And I can see from the build output that you're not using the current source as the setup to run windeployqt is using the older version that adds the Qt bin directory to the end of the path instead of at the front as the latest source does:</p><pre><code>set PATH=%PATH%;C:/Qt/Qt5.6.2/5.6/msvc2013_64/bin</code></pre><p>Please update your source tree to the latest master-2.2, re-run CMake and then rebuild.</p></div><div id="comment-60615-info" class="comment-info"><span class="comment-age">(06 Apr '17, 07:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60651"></span><div id="comment-60651" class="comment not_top_scorer"><div id="post-60651-score" class="comment-score"></div><div class="comment-text"><p>Re-installation of QT resolved the error</p></div><div id="comment-60651-info" class="comment-info"><span class="comment-age">(07 Apr '17, 06:45)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div></div><div id="comment-tools-60471" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-60471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

