+++
type = "question"
title = "Adding external lib to my own plugin"
description = '''Hello, I am trying to write my own wireshark v2.0.2 plugin and I need to use a custom library and xerces library (.lib files) in my dissector. I try to add this libraries in Makefile.am like this :  LIBS = -L -lcustom_lib -lxerces-c_3 I also try to add libraries in Makefile.nmake like this :  CFLAGS...'''
date = "2017-01-23T00:55:00Z"
lastmod = "2017-01-23T05:10:00Z"
weight = 58963
keywords = [ "libraries", "include", "library", "lib", "dll" ]
aliases = [ "/questions/58963" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Adding external lib to my own plugin](/questions/58963/adding-external-lib-to-my-own-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58963-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to write my own wireshark v2.0.2 plugin and I need to use a custom library and xerces library (.lib files) in my dissector.</p><p>I try to add this libraries in Makefile.am like this :</p><pre><code>LIBS = -L -lcustom_lib -lxerces-c_3</code></pre><p>I also try to add libraries in Makefile.nmake like this :</p><pre><code>CFLAGS=$(WARNINGS_ARE_ERRORS) $(STANDARD_CFLAGS) \
    /I../.. $(GLIB_CFLAGS) \
    /I$(PCAP_DIR)\include \
    /Icustom_lib\include
    ...
LINK_PLUGIN_WITH=....\epan\libwireshark.lib
CFLAGS=$(CFLAGS)
LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) xerces-c_3.lib
LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) custom_lib.lib</code></pre><p>But none of these solutions works for me, I have this error message when I run "msbuild" command :</p><p><strong>error LNK2019: unresolved external symbol __imp__custom_init fatal error<br />
LNK1120: 1 unresolved externals</strong></p><p>Can anyone help me please ?</p><p>Thanks you.</p></div><div id="question-tags" class="tags-container tags">libraries include library lib dll</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '17, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/c8994d2c88e422266e0cf1ee75e81d3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sguaiana&#39;s gravatar image" /><p>sguaiana<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sguaiana has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jan '17, 01:02</p></div></div><div id="comments-container-58963" class="comments-container"><span id="58969"></span><div id="comment-58969" class="comment"><div id="post-58969-score" class="comment-score"></div><div class="comment-text"><p>Your problem description is a little confusing, mixing up Makefile.am (used by autotools builds on platforms other than Windows), Makefile.nmake (deprecated and used by non-CMake builds on Windows) and msbuild, used by CMake builds on Windows.</p><p>So, how are you building, using CMake and msbuild on Windows?</p></div><div id="comment-58969-info" class="comment-info"><span class="comment-age">(23 Jan '17, 03:06)</span> grahamb ♦</div></div><span id="58973"></span><div id="comment-58973" class="comment"><div id="post-58973-score" class="comment-score"></div><div class="comment-text"><p>Hello, yes I use CMake and msbuild on Windows</p></div><div id="comment-58973-info" class="comment-info"><span class="comment-age">(23 Jan '17, 04:04)</span> sguaiana</div></div></div><div id="comment-tools-58963" class="comment-tools"></div><div class="clear"></div><div id="comment-58963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58975"></span>

<div id="answer-container-58975" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58975-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you should be able to modify CMakeLists.txt in your plugin directory to add the required library to your plugin target after the target is created with the <code>add_plugin_target()</code> call, using <a href="https://cmake.org/cmake/help/v3.4/command/target_link_libraries.html#command:target_link_libraries"><code>target_link_libraries</code></a> something like:</p><pre><code>add_plugin_library(your_plugin_name)
target_link_libraries(your_plugin_name path\to\your\library)</code></pre><p>Extra work will then be required to copy the library dll to the build directory and then add it into the packaging.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '17, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58975" class="comments-container"><span id="58978"></span><div id="comment-58978" class="comment"><div id="post-58978-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your help.</p><p>I had this line in CMakeLists.txt (in my plugin folder) just after 'add_plugin_library' line so I have :</p><pre><code>add_plugin_library(myplugin)
target_link_libraries(myplugin custom_lib.lib xerces-c_3.lib)</code></pre><p>When I run 'msbuild' command I have this error :</p><p><strong>LINK : fatal error LNK1181: cannot open input file 'custom_lib.lib'</strong></p></div><div id="comment-58978-info" class="comment-info"><span class="comment-age">(23 Jan '17, 06:48)</span> sguaiana</div></div><span id="58979"></span><div id="comment-58979" class="comment"><div id="post-58979-score" class="comment-score">1</div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>And where are the libraries custom_lib.lib and xerces-c_3.lib?</p><p>Note that my example included the path\to\ the library.</p><p>Finding libraries in CMake is somewhat complicated, e.g. see <a href="https://cmake.org/Wiki/CMake:How_To_Find_Libraries">here</a>. You can shortcut that by providing the path in the call to <code>target_link_libraries</code>, or by adding the link paths with a call to <a href="https://cmake.org/cmake/help/v3.0/command/link_directories.html"><code>link_directories</code></a>, or possibly by importing the library as shown in <a href="http://stackoverflow.com/questions/28597351/how-do-i-add-a-library-path-in-cmake">this</a> S.O answer</p></div><div id="comment-58979-info" class="comment-info"><span class="comment-age">(23 Jan '17, 07:00)</span> grahamb ♦</div></div><span id="58980"></span><div id="comment-58980" class="comment"><div id="post-58980-score" class="comment-score"></div><div class="comment-text"><p>My libraries are in plugin folder "..src/plugins/myplugin/".</p><p>If I build with absolute path to my libraries, msbuild works. But I want to use relative path (I think it's better). So as you advised me, I put this line before 'add_plugin_library' :</p><pre><code>link_directories(${CMAKE_CURRENT_SOURCE_DIR})</code></pre><p>CMake and msbuild command seem to work, no error occured.</p><p>When I run Wireshark, an error messages appears indicating that it could not load custom_lib and xerces-c_3. So, I put custom_lib.dll and xerces-c_3.dll in 'build\run\RelWithDebInfo' folder and error messages disappears.</p><p>Thank you very much for your help ! Best regards.</p></div><div id="comment-58980-info" class="comment-info"><span class="comment-age">(23 Jan '17, 07:39)</span> sguaiana</div></div><span id="58981"></span><div id="comment-58981" class="comment"><div id="post-58981-score" class="comment-score"></div><div class="comment-text"><blockquote>When I run Wireshark, an error messages appears indicating that it could not load custom_lib and xerces-c_3. So, I put custom_lib.dll and xerces-c_3.dll in 'build\run\RelWithDebInfo' folder and error messages disappears.</blockquote><p>This was what I meant in part of my answer:</p><blockquote>Extra work will then be required to copy the library dll to the build directory and then add it into the packaging.</blockquote><p>You could add copy commands similar to what's done in the top-level CMakeLists.txt to copy over the 3rd party DLL's to the build directory, and to build an installer you would need to modify packaging\nsis\custom_plugins.txt</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-58981-info" class="comment-info"><span class="comment-age">(23 Jan '17, 07:57)</span> grahamb ♦</div></div></div><div id="comment-tools-58975" class="comment-tools"></div><div class="clear"></div><div id="comment-58975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

