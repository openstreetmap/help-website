+++
type = "question"
title = "Problems building a V2 windows installer"
description = '''I&#x27;m trying to build an installer for Windows using the Wireshark 2.0.0rc2 sources and cmake. I have built the main executable using &quot;c:&#92;Program Files (x86)&#92;CMake&#92;bin&#92;cmake.exe&quot; -DENABLE_CHM_GUIDES=on D:&#92;wireshark-2.0.0rc2 msbuild /m /p:Configuration=RelWithDebInfo wireshark.sln This works and I get ...'''
date = "2015-11-05T02:56:00Z"
lastmod = "2015-11-05T03:20:00Z"
weight = 47280
keywords = [ "installer", "cmake" ]
aliases = [ "/questions/47280" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problems building a V2 windows installer](/questions/47280/problems-building-a-v2-windows-installer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47280-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to build an installer for Windows using the Wireshark 2.0.0rc2 sources and cmake.</p><p>I have built the main executable using</p><p>"c:\Program Files (x86)\CMake\bin\cmake.exe" -DENABLE_CHM_GUIDES=on D:\wireshark-2.0.0rc2 msbuild /m /p:Configuration=RelWithDebInfo wireshark.sln</p><p>This works and I get an executable that runs. I now want to build and installer package. So I tried the command</p><p>msbuild /m /p:Configuration=RelWithDebInfo nsis_package.vcxproj</p><p>This stops with the error</p><pre><code>    Section: &quot;-Required&quot;
    SetShellVarContext: all
    SetOutPath: &quot;$INSTDIR&quot;
    File: &quot;D:\wireshark-2.0.0rc2\build-win32\run\RelWithDebInfo\uninstall.exe&quot; -&gt; no files found.
    Usage: File [/nonfatal] [/a] ([/r] [/x filespec [...]] filespec [...] |
       /oname=outfile one_file_only)
    Error in script &quot;wireshark.nsi&quot; on line 349 -- aborting creation process</code></pre><p>And sure enough there is no uninstall.exe in the build directory. So which step am I missing to create one</p><p>I tried commenting out the line 349 in wireshark.nsi to see if it worked and it then fails a bit further on with the error..</p><pre><code>    SetOutPath: &quot;$INSTDIR&quot;
    File: &quot;Wireshark.exe&quot; 6253568 bytes
    !include: could not find: &quot;qt-dll-manifest.nsh&quot;
    Error in script &quot;wireshark.nsi&quot; on line 876 -- aborting creation process</code></pre><p>So is there a step I'm missing to get things ready to build the installer.</p><p>Thanks for any help</p></div><div id="question-tags" class="tags-container tags">installer cmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '15, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/3d25bda262a989924649329d5e0b6b0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Ling&#39;s gravatar image" /><p>Andy Ling<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Ling has no accepted answers">0%</span></p></div></div><div id="comments-container-47280" class="comments-container"></div><div id="comment-tools-47280" class="comment-tools"></div><div class="clear"></div><div id="comment-47280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47281"></span>

<div id="answer-container-47281" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47281-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a missing step from README.cmake (but will be in the planned Dev Guide updates), to build an installer you must first build the uninstall package:</p><pre><code>msbuild /m /p:Configuration=RelWithDebInfo nsis_package_prep.vcxproj</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '15, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47281" class="comments-container"><span id="47286"></span><div id="comment-47286" class="comment"><div id="post-47286-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that seems to have fixed it. I knew it would be something simple.</p></div><div id="comment-47286-info" class="comment-info"><span class="comment-age">(05 Nov '15, 04:22)</span> Andy Ling</div></div><span id="47287"></span><div id="comment-47287" class="comment"><div id="post-47287-score" class="comment-score"></div><div class="comment-text"><p>@Andy Ling</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-47287-info" class="comment-info"><span class="comment-age">(05 Nov '15, 04:29)</span> grahamb ♦</div></div></div><div id="comment-tools-47281" class="comment-tools"></div><div class="clear"></div><div id="comment-47281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

