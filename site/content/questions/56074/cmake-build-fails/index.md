+++
type = "question"
title = "CMake build fails"
description = '''Got this when building Wireshark: The PLATFORM environment variable ([undefined]) doesn&#x27;t match the generator On AMD64 machine. Any resolution to that that does not involve modification to the cmake file?'''
date = "2016-10-02T10:51:00Z"
lastmod = "2016-10-05T03:26:00Z"
weight = 56074
keywords = [ "win64", "cmake", "amd64" ]
aliases = [ "/questions/56074" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [CMake build fails](/questions/56074/cmake-build-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56074-score" class="post-score" title="current number of votes">1</div><span id="post-56074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Got this when building Wireshark:</p><pre><code>The PLATFORM environment variable ([undefined]) doesn&#39;t match the generator</code></pre>On AMD64 machine. Any resolution to that that does not involve modification to the cmake file?</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-win64" rel="tag" title="see questions tagged &#39;win64&#39;">win64</span> <span class="post-tag tag-link-cmake" rel="tag" title="see questions tagged &#39;cmake&#39;">cmake</span> <span class="post-tag tag-link-amd64" rel="tag" title="see questions tagged &#39;amd64&#39;">amd64</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '16, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/6116b62f0eaf715d6fe35edb91f9a20b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuralsea&#39;s gravatar image" /><p><span>neuralsea</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuralsea has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '16, 11:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-56074" class="comments-container"><span id="56075"></span><div id="comment-56075" class="comment"><div id="post-56075-score" class="comment-score"></div><div class="comment-text"><p>You left out the last part of the error message. Please provide that as well.</p></div><div id="comment-56075-info" class="comment-info"><span class="comment-age">(02 Oct '16, 11:54)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-56074" class="comment-tools"></div><div class="clear"></div><div id="comment-56074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56076"></span>

<div id="answer-container-56076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56076-score" class="post-score" title="current number of votes">1</div><span id="post-56076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per the Developers Guide Section <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">2.2.10</a> you must create an environment variable indicating your target platform:</p><pre><code>WIRESHARK_TARGET_PLATFORM=win32 or win64 as required</code></pre><p>That means choose win32 or win64 as appropriate, not the whole string.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '16, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56076" class="comments-container"><span id="56078"></span><div id="comment-56078" class="comment"><div id="post-56078-score" class="comment-score"></div><div class="comment-text"><p>[Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.]</p><p>Thank you grahamb. This did not resolve the issue. See console output below:</p><pre><code>set WIRESHARK_TARGET_PLATFORM=win64

C:\dev\wsbuild64&gt;&quot;C:\Program Files\CMake\bin\cmake&quot; -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 14 2015 Win64&quot; ..\wireshark
-- The C compiler identification is MSVC 19.0.24210.0
-- The CXX compiler identification is MSVC 19.0.24210.0
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC /bin/x86_amd64/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC /bin/x86_amd64/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Generating build using CMake 3.6.2
-- Found POWERSHELL: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe
CMake Error at CMakeLists.txt:107 (message):
  The PLATFORM environment variable ([undefined]) doesn&#39;t match the generator
  platform (win64)

-- Configuring incomplete, errors occurred!
See also &quot;C:/dev/wsbuild64/CMakeFiles/CMakeOutput.log&quot;.</code></pre></div><div id="comment-56078-info" class="comment-info"><span class="comment-age">(02 Oct '16, 13:06)</span> <span class="comment-user userinfo">neuralsea</span></div></div><span id="56082"></span><div id="comment-56082" class="comment"><div id="post-56082-score" class="comment-score"></div><div class="comment-text"><p>CMakeList.txt actually says it's the environment variable PLATFORM that has to be set in this case, not WIRESHARK_TARGET_PLATFORM.</p><p>Simply reading CMakeList.txt should make it obvious what's needed (although not the why)</p></div><div id="comment-56082-info" class="comment-info"><span class="comment-age">(02 Oct '16, 14:05)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="56084"></span><div id="comment-56084" class="comment"><div id="post-56084-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap. CMake variables refer to x86 CXX path.</p><p>Also: //Name of generator platform. CMAKE_GENERATOR_PLATFORM:INTERNAL= //Name of generator toolset. CMAKE_GENERATOR_TOOLSET:INTERNAL=</p><p>Thank you again.</p></div><div id="comment-56084-info" class="comment-info"><span class="comment-age">(02 Oct '16, 16:05)</span> <span class="comment-user userinfo">neuralsea</span></div></div><span id="56085"></span><div id="comment-56085" class="comment"><div id="post-56085-score" class="comment-score"></div><div class="comment-text"><p><code>PLATFORM</code> is an environment variable defined by the Visual Studio "system", either when opening a Visual Studio Command Prompt or running any of the Visual Studio batch files (vcvars, vsvars, etc.) or using <a href="https://pscx.codeplex.com/">PSCX</a> <code>Import-VisualStudioVars</code>, so SHOULD NOT need to be defined by the user.</p><p>Please read and follow the section of the Developers Guide I noted above, <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">2.2.10</a> to correctly set up your build environment.</p><p>You might also note that support for VS2015 is currently experimental, the "official" compiler to use, as per the Developers Guide, is VS2013, although there have been reports of success with VS2015.</p></div><div id="comment-56085-info" class="comment-info"><span class="comment-age">(03 Oct '16, 02:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56088"></span><div id="comment-56088" class="comment"><div id="post-56088-score" class="comment-score"></div><div class="comment-text"><p>Good point Graham. <span>@neuralsea</span>: Are you using VS2015 ?</p></div><div id="comment-56088-info" class="comment-info"><span class="comment-age">(03 Oct '16, 05:28)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="56092"></span><div id="comment-56092" class="comment not_top_scorer"><div id="post-56092-score" class="comment-score"></div><div class="comment-text"><p>VS2015 should not be a problem as such, I'm using it every day to build Wireshark(64bits)...</p></div><div id="comment-56092-info" class="comment-info"><span class="comment-age">(03 Oct '16, 06:33)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="56140"></span><div id="comment-56140" class="comment not_top_scorer"><div id="post-56140-score" class="comment-score"></div><div class="comment-text"><p>Yes I am using VS 2015</p></div><div id="comment-56140-info" class="comment-info"><span class="comment-age">(04 Oct '16, 11:34)</span> <span class="comment-user userinfo">neuralsea</span></div></div><span id="56151"></span><div id="comment-56151" class="comment not_top_scorer"><div id="post-56151-score" class="comment-score"></div><div class="comment-text"><p>I pointed out the use of VS2015 more as an example of a deviation from the instructions in the Developers Guide, not as the particular issue in play here, which I believe is a deviation from the instructions in that the OP hasn't opened a Visual Studio command prompt as per section <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">2.2.10</a> which will set the PLATFORM env. var.</p></div><div id="comment-56151-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56076" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-56076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

