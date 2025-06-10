+++
type = "question"
title = "Compile osmium tool for Windows"
description = '''Hi I&#x27;ve been trying to compile Osmium Tool for Windows using Visual Studio and I can&#x27;t get past this error and am not sure how to resolve it. Any help would be appreciated (unfortunately I don&#x27;t know much about C++) but am trying my best! I see it was successful here but the artifacts are gone now. ...'''
date = "2022-02-05T19:20:00Z"
lastmod = "2023-03-04T14:00:00Z"
weight = 83374
keywords = [ "osmium" ]
aliases = [ "/questions/83374" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Compile osmium tool for Windows](/questions/83374/compile-osmium-tool-for-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83374-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've been trying to compile Osmium Tool for Windows using Visual Studio and I can't get past this error and am not sure how to resolve it. Any help would be appreciated (unfortunately I don't know much about C++) but am trying my best! I see it was successful here but the artifacts are gone now. <a href="https://ci.appveyor.com/project/Mapbox/osmium-tool/build/1.0.281/job/va8388o8synhjii8">https://ci.appveyor.com/project/Mapbox/osmium-tool/build/1.0.281/job/va8388o8synhjii8</a></p>
<pre><code>https://github.com/osmcode/osmium-tool
&#10;Used repo tag 1.13.2
&#10;Reviewed appveyor.yml
&#10;VS2019
&#10;    Installed Visual Studio 2019 (16.11.9)
    - installed desktop development with c++
    - installed MSVC v140 - VS 2015 C++ build tools (v14.00)
&#10;    Reviewed build-appveyor.bat
    - Updated vcvarsall.bat location for VS2019 install location (VC\Auxiliary\Build\vcvarsall.bat)
    - Changed cmake_cmd &quot;Visual Studio 14 Win64&quot; to &quot;Visual Studio 16&quot;
    - Changed toolsversion from 14.0 to Current
&#10;VS2015 community edition
&#10;    Reviewed build-appveyor.bat
    - Updated vcvarsall.bat location for VS2019 install location (VC\vcvarsall.bat)
&#10;    Downloaded lastest cmake, added to path C:\Program Files\CMake\bin
&#10;In C:\projects
    git clone --depth 1 https://github.com/osmcode/libosmium
    git clone --depth 1 https://github.com/mapbox/protozero
&#10;Download latest nuget.exe and placed in path
&#10;Downloaded boost 1.63 to C:/Libraries/boost_1_63_0
- ran bootstrap.bat
- ran b2.exe
&#10;Ran build-local.bat
&#10;ERRORS:
&#10;libboost_program_options-vc140-mt-1_63.lib(options_description.obj) : fatal error LNK1112: module machine type &#39;X86&#39; conflicts with target machine type &#39;x64&#39; [C:\projects\osmium-tool\build\test\unit_tests.vcxproj]
Done Building Project &quot;C:\projects\osmium-tool\build\test\unit_tests.vcxproj&quot; (default targets) -- FAILED.
Done Building Project &quot;C:\projects\osmium-tool\build\test\unit_tests.vcxproj.metaproj&quot; (default targets) -- FAILED.
Done Building Project &quot;C:\projects\osmium-tool\build\ALL_BUILD.vcxproj.metaproj&quot; (default targets) -- FAILED.
Done Building Project &quot;C:\projects\osmium-tool\build\osmium.sln&quot; (default targets) -- FAILED.
&#10;Build FAILED.
&#10;&quot;C:\projects\osmium-tool\build\osmium.sln&quot; (default target) (1) -&gt;
&quot;C:\projects\osmium-tool\build\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
&quot;C:\projects\osmium-tool\build\test\unit_tests.vcxproj.metaproj&quot; (default target) (6) -&gt;
&quot;C:\projects\osmium-tool\build\test\unit_tests.vcxproj&quot; (default target) (7) -&gt;
(ClCompile target) -&gt; 
  c:\projects\osmium-tool\test\include\catch.hpp(1648): warning C4800: &#39;osmium::io::overwrite&#39;: forcing value to bool &#39;true&#39; or &#39;false&#39; (performance warning) [C:\projects\osmium-tool\build\test\unit_tests.vcxproj]
&#10;
&quot;C:\projects\osmium-tool\build\osmium.sln&quot; (default target) (1) -&gt;
&quot;C:\projects\osmium-tool\build\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
&quot;C:\projects\osmium-tool\build\src\osmium.vcxproj.metaproj&quot; (default target) (4) -&gt;
&quot;C:\projects\osmium-tool\build\src\osmium.vcxproj&quot; (default target) (5) -&gt;
(Link target) -&gt; 
  libboost_program_options-vc140-mt-1_63.lib(options_description.obj) : fatal error LNK1112: module machine type &#39;X86&#39; conflicts with target machine type &#39;x64&#39; [C:\projects\osmium-tool\build\src\osmium.vcxproj]
&#10;
&quot;C:\projects\osmium-tool\build\osmium.sln&quot; (default target) (1) -&gt;
&quot;C:\projects\osmium-tool\build\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
&quot;C:\projects\osmium-tool\build\test\unit_tests.vcxproj.metaproj&quot; (default target) (6) -&gt;
&quot;C:\projects\osmium-tool\build\test\unit_tests.vcxproj&quot; (default target) (7) -&gt;
  libboost_program_options-vc140-mt-1_63.lib(options_description.obj) : fatal error LNK1112: module machine type &#39;X86&#39; conflicts with target machine type &#39;x64&#39; [C:\projects\osmium-tool\build\test\unit_tests.vcxproj]
&#10;    1 Warning(s)
    2 Error(s)
&#10;Time Elapsed 00:08:06.76
~~~~~~ ERROR C:\projects\osmium-tool\build-appveyor.bat ~~~~~~</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '22, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/dd57ba63729e44a014376d152f9dcf67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aarismendi&#39;s gravatar image" />
<p><span>aarismendi</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aarismendi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '22, 19:23</strong> </span></p>
</div>
</div>
<div id="comments-container-83374" class="comments-container">
&#10;</div>
<div id="comment-tools-83374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83374-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="83375"></span>

<div id="answer-container-83375" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83375-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Got it working, instead of building boost I used a pre-built binary -</p>
<p><a href="https://sourceforge.net/projects/boost/">https://sourceforge.net/projects/boost/</a></p>
<p><a href="https://iweb.dl.sourceforge.net/project/boost/boost-binaries/1.63.0/boost_1_63_0-msvc-14.0-64.exe">https://iweb.dl.sourceforge.net/project/boost/boost-binaries/1.63.0/boost_1_63_0-msvc-14.0-64.exe</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '22, 01:52</strong></p>
<img src="https://secure.gravatar.com/avatar/dd57ba63729e44a014376d152f9dcf67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aarismendi&#39;s gravatar image" />
<p><span>aarismendi</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aarismendi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83375" class="comments-container">
&#10;</div>
<div id="comment-tools-83375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83375-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86873"></span>

<div id="answer-container-86873" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86873-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have no problem opening, building and debugging in Visual Studio on Windows.<br />
You need to make sure that all required c++ components are installed, incl cmake and vcpkg.</p>
<ul>
<li><a href="https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170">Install C++ in VS</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170#installation">CMake Installation</a></li>
<li><a href="https://vcpkg.io/en/getting-started.html">Install vcpkg</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170#vcpkg-integration">Vcpkg integration</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170#ide-integration">Open CMake project in VS</a></li>
</ul>
<p>Tested on latest Visual Studio 2022 Community version, Windows 11.<br />
My build artefacts: <a href="https://drive.google.com/drive/folders/15ImH-DCtIPyoFrzQnFyhUBm3YsmUZtRa">google drive</a>.</p>
<p>Easy local build script using <a href="https://github.com/microsoft/vcpkg">vcpkg</a>, like github actions <a href="https://github.com/osmcode/osmium-tool/blob/583db02ac9193dfb5217f93c823a4975405338ac/.github/actions/cmake-windows/action.yml">cmake</a> and <a href="https://github.com/osmcode/osmium-tool/blob/583db02ac9193dfb5217f93c823a4975405338ac/.github/actions/build-windows/action.yml">build</a>:</p>
<ol>
<li>Install <code>vcpkg</code> <a href="https://github.com/microsoft/vcpkg#quick-start-windows">https://github.com/microsoft/vcpkg#quick-start-windows</a></li>
<li>Install <code>cmake</code> (set PATH environment) <a href="https://cmake.org/download/">https://cmake.org/download/</a></li>
<li>Cd work dir, clone <code>osmium-tool</code>, <code>libosmium</code>, <code>protozero</code></li>
<li>Copy <code>build-local-vcpkg.bat</code> (see google drive) to <code>osmium-tool</code> dir and launch</li>
<li>The binaries dir: <code>work-dir\osmium-tool\build\src\Release\</code></li>
</ol>
<p>Should work without Visual Studio.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '23, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a4d0974f0b47ec75fe84cf6740b562d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ildar&#39;s gravatar image" />
<p><span>Ildar</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ildar has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Oct '23, 18:26</strong> </span></p>
</div>
</div>
<div id="comments-container-86873" class="comments-container">
<span id="86874"></span>
<div id="comment-86874" class="comment">
<div id="post-86874-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For completeness, which Visual Studio version you were using?</p>
</div>
<div id="comment-86874-info" class="comment-info">
<span class="comment-age">(04 Mar '23, 10:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="86876"></span>
<div id="comment-86876" class="comment">
<div id="post-86876-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> VS 2022, answer updated.</p>
</div>
<div id="comment-86876-info" class="comment-info">
<span class="comment-age">(04 Mar '23, 14:00)</span> <span class="comment-user userinfo">Ildar</span>
</div>
</div>
</div>
<div id="comment-tools-86873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86873-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84392"></span>

<div id="answer-container-84392" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi aarismendi, I also look for osmium.exe for windows. But I am not able to compile it by myself. Can you share the osmium.exe for windows ? If yes, please contact me thomas(at)img2ms.de</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '22, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9fbaa9a481c1ff01706ba5ab66868a0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morgen1&#39;s gravatar image" />
<p><span>morgen1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morgen1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84392" class="comments-container">
<span id="84393"></span>
<div id="comment-84393" class="comment">
<div id="post-84393-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just a thought - would Windows Subsystem for Linux be an option for you? That way you wouldn't have to be a small Windows dog on the floor waiting for he crumbs to fall off the Linux table :)</p>
</div>
<div id="comment-84393-info" class="comment-info">
<span class="comment-age">(06 May '22, 21:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84398"></span>
<div id="comment-84398" class="comment">
<div id="post-84398-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will try to install the linux subsystem... maybee it is the solution..</p>
</div>
<div id="comment-84398-info" class="comment-info">
<span class="comment-age">(07 May '22, 07:11)</span> <span class="comment-user userinfo">morgen1</span>
</div>
</div>
</div>
<div id="comment-tools-84392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84392-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86875"></span>

<div id="answer-container-86875" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no need to compile it for windows by yourself. There are ready to use compiled builds available at internet: My way : install anacaonda, it includes all binaries and the osmium.exe. After installing Anacanda, I get a directory \Anaconda3\Library\bin. Then i copied boost_program_options.dll; libbz2.dll;libexpat.dll;liblz4.dll;zlib.dll and osmium.exe to a other PC and can work with osmium.exe.</p>
<p>morgen1</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '23, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/9fbaa9a481c1ff01706ba5ab66868a0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morgen1&#39;s gravatar image" />
<p><span>morgen1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morgen1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86875" class="comments-container">
&#10;</div>
<div id="comment-tools-86875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86875-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

