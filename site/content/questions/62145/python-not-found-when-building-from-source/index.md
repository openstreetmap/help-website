+++
type = "question"
title = "Python not found when building from source"
description = '''Hi all -  I&#x27;ve been trying to freshen our build and update some prepared filters but since about 2.2.4 (the last build that I&#x27;ve done) I&#x27;ve found that the build is picking up the wrong python interpreter - or rather, not picking up anything at all I&#x27;ve explicitly added it to the path &quot;cmake.exe&quot; -DG...'''
date = "2017-06-19T18:22:00Z"
lastmod = "2017-06-21T07:05:00Z"
weight = 62145
keywords = [ "python", "build_error", "development", "build" ]
aliases = [ "/questions/62145" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Python not found when building from source](/questions/62145/python-not-found-when-building-from-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62145-score" class="post-score" title="current number of votes">0</div><span id="post-62145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all - I've been trying to freshen our build and update some prepared filters but since about 2.2.4 (the last build that I've done) I've found that the build is picking up the wrong python interpreter - or rather, not picking up anything at all</p><p>I've explicitly added it to the path</p><pre><code>&quot;cmake.exe&quot; -DGIT_EXECUTABLE=&quot;C:\Program Files\Git\bin\git&quot; -DPYTHON_EXECUTABLE=&quot;C:\python36\python.exe&quot; -DENABLE_CHM_GUIDES=off ..\wireshark-2.2.7 2&gt;&amp;1 &gt; cmake_msbuild.txt</code></pre><p>CMakeCache reports the correct Python version</p><pre><code>2017-06-20 10:41:55:0103    747 PYTHON_EXECUTABLE:FILEPATH=C:/Python36/python.exe
2017-06-20 10:41:55:0104    1194    FIND_PACKAGE_MESSAGE_DETAILS_PythonInterp:INTERNAL=[C:/Python36/python.exe][v3.6.1(2)]</code></pre><p>The Cmake output appears correct:</p><pre><code>2017-06-20 10:53:27:0396    24  -- Found PythonInterp: C:/Python36/python.exe (found version &quot;3.6.1&quot;)
2017-06-20 10:53:27:0396    25  -- Found python module asn2wrs: C:\Wireshark\wireshark-2.2.7\tools\asn2wrs.py
2017-06-20 10:53:27:0397    196 -- Found PythonInterp: C:/Python36/python.exe (found suitable version &quot;3.6.1&quot;, minimum required is &quot;2&quot;)
2017-06-20 10:53:27:0397    368 -- Found python module make-dissector-reg: C:\Wireshark\wireshark-2.2.7\tools\make-dissector-reg.py</code></pre><p>But the solution build fails with the error below:</p><pre><code>92&gt;CustomBuild:
     running a2x with args --verbose --attribute=build_dir=/cygdrive/c/Wireshark/build32/docbook --attribute=docinfo --destination-dir=/cygdrive/c/Wireshark/build32/docbook --asciidoc-opts=--conf-file=/cygdrive/c/Wireshark/wireshark-2.2.7/docbook/asciidoc.conf --conf-file=/cygdrive/c/Wireshark/wireshark-2.2.7/docbook/asciidoctor-asciidoc.conf --no-xmllint --format=docbook --fop --stylesheet=ws.css /cygdrive/c/Wireshark/wireshark-2.2.7/docbook/user-guide.asciidoc
     /usr/bin/env: &#39;python&#39;: No such file or directory
92&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: &quot;cmd.exe&quot; exited with code 127. [C:\Wireshark\build32\docbook\generate_usea2xr-guide.xml.vcxproj]
92&gt;Done Building Project &quot;C:\Wireshark\build32\docbook\generate_user-guide.xml.vcxproj&quot; (default targets) -- FAILED.</code></pre><p>I've seen some advice to remove cygwin from my path, but I can't see what's actually picking it up Do you think it might be an issue with asciidoc/a2x?</p><p>Has anyone seen this before, so would I be best to scrub my environment.</p><p>Best regards, Baffled of Sydney.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '17, 18:22</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p><span>Scott Harman</span><br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-62145" class="comments-container"><span id="62152"></span><div id="comment-62152" class="comment"><div id="post-62152-score" class="comment-score"></div><div class="comment-text"><p>Same issue with release notes:</p><p>101&gt;CustomBuild: Generating release-notes.html</p><p>101&gt;CustomBuild:</p><p>running a2x with args --format=xhtml --destination-dir=/cygdrive/c/Wireshark/build32/docbook --asciidoc-opts= --fop --stylesheet=ws.css release-notes.asciidoc</p><p>101&gt;CustomBuild: /usr/bin/env: 'python': No such file or directory</p><p>101&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: "cmd.exe" exited with code 127. [C:\Wireshark\build32\docbook\release_notes_html.vcxproj]</p></div><div id="comment-62152-info" class="comment-info"><span class="comment-age">(19 Jun '17, 20:48)</span> <span class="comment-user userinfo">Scott Harman</span></div></div></div><div id="comment-tools-62145" class="comment-tools"></div><div class="clear"></div><div id="comment-62145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62150"></span>

<div id="answer-container-62150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62150-score" class="post-score" title="current number of votes">1</div><span id="post-62150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>a2x (AsciiDoc) is part of your Cygwin installation and does not use the Python interpreter from your Windows installation. Does your Cygwin installation have a Python binary ("python", not just "python2" or "python3").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 20:12</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-62150" class="comments-container"><span id="62192"></span><div id="comment-62192" class="comment"><div id="post-62192-score" class="comment-score"></div><div class="comment-text"><p>Well that's just annoying - I've got python2 installed, and running which python returns the path to local Windows python under /cygdrive/c/Python27/python</p><p>I'll attempt to scrub it all and go again, but something seems screwy.</p></div><div id="comment-62192-info" class="comment-info"><span class="comment-age">(20 Jun '17, 17:37)</span> <span class="comment-user userinfo">Scott Harman</span></div></div><span id="62196"></span><div id="comment-62196" class="comment"><div id="post-62196-score" class="comment-score"></div><div class="comment-text"><p>Had to completely remove and reinstall cygwin and both version 2 and version 3 of python - it looks like having Python on Windows PATH actually breaks a2x as adding it to PATH and refreshing variables gives me the /cygdrive/c/Python27/python path - which still shouldn't fail, but hey ho.</p><p>Not the end of the world ;) Cheers</p></div><div id="comment-62196-info" class="comment-info"><span class="comment-age">(20 Jun '17, 19:49)</span> <span class="comment-user userinfo">Scott Harman</span></div></div></div><div id="comment-tools-62150" class="comment-tools"></div><div class="clear"></div><div id="comment-62150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62208"></span>

<div id="answer-container-62208" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62208-score" class="post-score" title="current number of votes">0</div><span id="post-62208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not entirely sure why your build is going wrong, but I see a couple of things that look odd to me:</p><ol><li>I've never had to explicitly pass the Git path to CMake. Git for Windows will, by default add itself to the system path.</li><li>I've never had to explicitly pass the Windows Python path to CMake. Python usually adds itself to the path and CMake is reasonably adept at deducing the location of python via registry entries if not on the path.</li><li>I make sure Cygwin is NOT on the path. CMake finds it reasonably well, but if you do have it in an odd place, then pass the path to CMake.</li><li>As you've noted CMake caches paths etc. in CMakeCache.txt, so if you fix up paths etc. and want CMake to pick up the new paths, then you must either delete the items from CMakeCache.txt or delete the entire file.</li><li>You MUST have Cygwin Python installed, the Cygwin docbook tools (asciidoc) depend on it. Having Windows Python installed is a good idea some parts of the build use Python to generate files and a native Python is much quicker than the Cygwin one for this.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '17, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62208" class="comments-container"></div><div id="comment-tools-62208" class="comment-tools"></div><div class="clear"></div><div id="comment-62208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

