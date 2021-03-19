+++
type = "question"
title = "error on generating build files"
description = '''I have following issue when I used the following command on visual studio cmd window. also I have visual studio 2015 installed on windows 7 Cmd used: cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; C:&#92;Development&#92;wireshark  error displayed:The C compiler identification is unknown  The CXX c...'''
date = "2015-12-01T04:58:00Z"
lastmod = "2015-12-01T13:20:00Z"
weight = 48127
keywords = [ "files", "generating", "build", "error" ]
aliases = [ "/questions/48127" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error on generating build files](/questions/48127/error-on-generating-build-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48127-score" class="post-score" title="current number of votes">0</div><span id="post-48127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have following issue when I used the following command on visual studio cmd window.</p><p>also I have visual studio 2015 installed on windows 7</p><pre><code>Cmd used:  cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; C:\Development\wireshark

error displayed:The C compiler identification is unknown
                The CXX compiler identifcation is unknown

CMake error at CmakeLists.txt:22

No CMAKE_CXX_COMPLIER could be found</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-generating" rel="tag" title="see questions tagged &#39;generating&#39;">generating</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '15, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/5f95711321f840922720016670d7d3b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tony_2013&#39;s gravatar image" /><p><span>Tony_2013</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tony_2013 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Dec '15, 05:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48127" class="comments-container"></div><div id="comment-tools-48127" class="comment-tools"></div><div class="clear"></div><div id="comment-48127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48129"></span>

<div id="answer-container-48129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48129-score" class="post-score" title="current number of votes">0</div><span id="post-48129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have specified Visual Studio 2013 in the CMake generator parameter `-G Visual Studio 12 Win64" and CMake couldn't find it.</p><p>For VS2015, which isn't currently supported by the Wireshark build, you would need to pass the parameter <code>-G Visual Studio 14 Win64</code>.</p><p>You can see all the CMake generators supported by passing a plain <code>-G</code> to CMAKE.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48129" class="comments-container"><span id="48141"></span><div id="comment-48141" class="comment"><div id="post-48141-score" class="comment-score"></div><div class="comment-text"><p>Thanks for coming back</p><p>Now I have following issue after I went through as you have suggested.</p><p>Please kindly advise me.</p><pre><code>C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC&gt;cmake -DENABLE_CHM_GUIDES
=on -G &quot;Visual Studio 14 Win64&quot; C:\Development\wireshark
-- The C compiler identification is MSVC 19.0.23026.0
-- The CXX compiler identification is MSVC 19.0.23026.0
-- Check for working C compiler using: Visual Studio 14 2015 Win64
-- Check for working C compiler using: Visual Studio 14 2015 Win64 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Visual Studio 14 2015 Win64
-- Check for working CXX compiler using: Visual Studio 14 2015 Win64 -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Generating build using CMake 3.4.0
-- Found POWERSHELL: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe

-- Building for win64 using Visual Studio 14 2015 Win64
C:\Development\wireshark\tools\win-setup.ps1 : Cannot validate argument on para
meter &#39;Destination&#39;. The &quot;$_ -like &quot;*\wireshark-*-libs&quot;&quot; validation script for
the argument with value &quot;C:\Development&quot; did not return true. Determine why the
 validation script failed and then try the command again.
At line:1 char:62
+ . &quot;C:\Development\wireshark\tools\win-setup.ps1&quot; -Destination &lt;&lt;&lt;&lt;  C:\Develo
pment \wireshark-win64-libs -Platform win64 -VSVersion 14
    + CategoryInfo          : InvalidData: (:) [win-setup.ps1], ParameterBindi
   ngValidationException
    + FullyQualifiedErrorId : ParameterArgumentValidationError,win-setup.ps1

CMake Error at CMakeLists.txt:133 (message):
  Windows setup (win-setup.ps1) failed.

-- Configuring incomplete, errors occurred!
See also &quot;C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/CMakeFiles/CMak
eOutput.log&quot;.
See also &quot;C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/CMakeFiles/CMak
eError.log&quot;.

C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC&gt;</code></pre></div><div id="comment-48141-info" class="comment-info"><span class="comment-age">(01 Dec '15, 07:22)</span> <span class="comment-user userinfo">Tony_2013</span></div></div><span id="48142"></span><div id="comment-48142" class="comment"><div id="post-48142-score" class="comment-score"></div><div class="comment-text"><p>It appears that you didn't follow the Developers Guide correctly. Section 2.3.2 asks you to:</p><ol><li>Set some environment variables</li><li>Create a build directory, and cd into it.</li></ol><p>From the error you show, it looks like the env vars aren't set, and from the path in the prompt it looks like you haven't created a build directory. Instead you're attempting to run from the VC directory.</p><p>What have you set for the required env vars?</p></div><div id="comment-48142-info" class="comment-info"><span class="comment-age">(01 Dec '15, 08:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48148"></span><div id="comment-48148" class="comment"><div id="post-48148-score" class="comment-score"></div><div class="comment-text"><p>I did set following vars as it shown below.</p><pre><code>&gt;set CYGWIN=nodosfilewarning
&gt;set WIRESHARK_BASE_DIR=C:\Development
&gt;set WIRESHARK_TARGET_PLATFORM=win64
&gt;set QT5_BASE_DIR=C:\Qt\Qt5.5.0\5.5\msvc2015
&gt;set WIRESHARK_VERSION_EXTRA=-YourExtraVersionInfo</code></pre><p>Now i have changed the directory before I execute generate cmd. But I still get the following error.</p><pre><code>C:\Development\wsbuild32&gt;cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 14 Win64&quot; C:\Development\wireshark
-- The C compiler identification is MSVC 19.0.23026.0
-- The CXX compiler identification is MSVC 19.0.23026.0
-- Check for working C compiler using: Visual Studio 14 2015 Win64
-- Check for working C compiler using: Visual Studio 14 2015 Win64 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Visual Studio 14 2015 Win64
-- Check for working CXX compiler using: Visual Studio 14 2015 Win64 -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Generating build using CMake 3.4.0
-- Found POWERSHELL: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe

-- Building for win64 using Visual Studio 14 2015 Win64
C:\Development\wireshark\tools\win-setup.ps1 : Cannot validate argument on parameter &#39;Destination&#39;. The &quot;$_ -like &quot;*\wireshark-*-libs&quot;&quot; validation script for the argument with value &quot;C:\Development&quot; did not return true. Determine why the validation script failed and then try the command again.
At line:1 char:62
+ . &quot;C:\Development\wireshark\tools\win-setup.ps1&quot; -Destination &lt;&lt;&lt;&lt;  C:\Development \wireshark-win64-libs -Platform win64 -VSVersion 14
    + CategoryInfo          : InvalidData: (:) [win-setup.ps1], ParameterBindingValidationException
    + FullyQualifiedErrorId : ParameterArgumentValidationError,win-setup.ps1

CMake Error at CMakeLists.txt:133 (message):
  Windows setup (win-setup.ps1) failed.

-- Configuring incomplete, errors occurred!
See also &quot;C:/Development/wsbuild32/CMakeFiles/CMakeOutput.log&quot;.</code></pre></div><div id="comment-48148-info" class="comment-info"><span class="comment-age">(01 Dec '15, 09:05)</span> <span class="comment-user userinfo">Tony_2013</span></div></div><span id="48160"></span><div id="comment-48160" class="comment"><div id="post-48160-score" class="comment-score"></div><div class="comment-text"><p>The PowerShell script win-setup.ps1 did not like the Destination argument of "C:\Development".</p><p>This argument is generated by CMake from the WIRESHARK_BASE_DIR and WIRESHARK_LIB_DIR env vars. If you have defined WIRESHARK_LIB_DIR that value takes priority and defines the absolute path to the location for the 3rd party libs. If you haven't set WIRESHARK_LIB_DIR, then you must define WIRESHARK_BASE_DIR and CMake will add on the appropriate lib path, in your case <code>wireshark-win64-libs</code>. The win-setup.ps1 script checks the argument to ensure it has the form <code>*\wireshark-*-libs</code>, and as can be seen from your output, it doesn't.</p><p>I suspect you have defined the env var WIRESHARK_LIB_DIR and set it to "C:\Development". If this is the case, then undefine it.</p><p>Arguably win-setup.ps1 is being a bit pernickety in "requiring" the lib path to be of the form"<code>*\wireshark-*-libs</code>, a patch to relax that would be considered.</p></div><div id="comment-48160-info" class="comment-info"><span class="comment-age">(01 Dec '15, 13:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48129" class="comment-tools"></div><div class="clear"></div><div id="comment-48129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

