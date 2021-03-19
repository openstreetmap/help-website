+++
type = "question"
title = "Dissector Plugin version info Error at 2.0.0 build"
description = '''I&#x27;m getting the build error below from the command prompt at building a dissector plugin using Wireshark 2.0 source and guide:  (ResourceCompile target) -&amp;gt;  C:&#92;Development&#92;wsbuild32&#92;plugins&#92;foo&#92;plugin.rc(5): error RC2127: version WORDs separated by commas expected [C:&#92;Development&#92;wsbuild32-1&#92;plug...'''
date = "2015-12-18T07:38:00Z"
lastmod = "2015-12-18T08:36:00Z"
weight = 48629
keywords = [ "build_error", "dissector", "plugin" ]
aliases = [ "/questions/48629" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector Plugin version info Error at 2.0.0 build](/questions/48629/dissector-plugin-version-info-error-at-200-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48629-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting the build error below from the command prompt at building a dissector plugin using Wireshark 2.0 source and guide:</p><pre><code>       (ResourceCompile target) -&gt;
     C:\Development\wsbuild32\plugins\foo\plugin.rc(5): error RC2127: version WORDs separated by commas expected [C:\Development\wsbuild32-1\plugins\foo\foo.vcxproj]
     C:\Development\wsbuild32\plugins\foo\plugin.rc(5): error RC2167: unrecognized VERSIONINFO field;  BEGIN or comma expected [C:\Development\wsbuild32\plugins\foo\foo.vcxproj]</code></pre><p>I had made version number modifications, thought I might have left a bad character on the text file so I got new files and left them untouched, ran the build with /t:Clean, re-ran the build and I am still getting this error. From Visual Studio 2013, getting the same build errors, I notice that the plugin.rc file gets auto-generated without most plugin-related information as if the data is not getting parsed correctly at build. Editing the file manually allows the build to complete successfully.</p><p>I'd like to know what is preventing the version number along with other fields from getting to this file? I copied the moduleinfo.h and moduleinfo.nmake files from the gryphon plugin's folder and simply changed package name and version number. The README.plugins file states that the plugin.rc.in needs no editing.</p><p>Thanks in advanced!</p></div><div id="question-tags" class="tags-container tags">build_error dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p>coloncm<br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '16, 07:23</p></div></div><div id="comments-container-48629" class="comments-container"></div><div id="comment-tools-48629" class="comment-tools"></div><div class="clear"></div><div id="comment-48629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48630"></span>

<div id="answer-container-48630" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48630-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you appear to be using the CMake build, the nmake files are irrelevant.</p><p>CMake processes the template file plugin.rc.in in the plugin directory using the call <code>set_module_info()</code> in the plugins CMakeLists.txt.</p><p>Have you got the template and the CMakeLists.txt file for your plugin, and is the call to <code>set_module_info()</code> in CMakeLists.txt correct?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '15, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48630" class="comments-container"><span id="48631"></span><div id="comment-48631" class="comment"><div id="post-48631-score" class="comment-score"></div><div class="comment-text"><p>Oh, good to know! Yes, I also included the CMakeList.txt from the gryphon plugin's folder and changed the lines as below:</p><p>...</p><p>set_module_info(foo 2 0 0 0)</p><p>set(DISSECTOR_SRC packet-foo.c )</p><p>...</p><p>add_plugin_library(foo)</p><p>...</p><p>Am I missing something?</p></div><div id="comment-48631-info" class="comment-info"><span class="comment-age">(18 Dec '15, 10:00)</span> coloncm</div></div><span id="48632"></span><div id="comment-48632" class="comment"><div id="post-48632-score" class="comment-score"></div><div class="comment-text"><p>So, after the CMake generation step the plug.rc file should be generated at the <code>path\to\your\build\plugins\foo\plugin.rc</code>.</p><p>Is that the .rc file that you think is not being generated correctly?</p></div><div id="comment-48632-info" class="comment-info"><span class="comment-age">(18 Dec '15, 10:36)</span> grahamb ♦</div></div><span id="48633"></span><div id="comment-48633" class="comment"><div id="post-48633-score" class="comment-score"></div><div class="comment-text"><p>Yes. When I open the solution in Visual Studio after the error and I rebuild it to view the error, I open the file for edit to manually enter the FILEVERSION (@[email protected]) entry, which comes up empty, with the version number, then run the build both in Visual Studio or the command prompt, it succeeds. But there are other entries that comes up empty such as the FileDescription (@[email protected]), FileVersion (@[email protected]), InternalName (@[email protected] @[email protected]), OriginalFilename (@[email protected]), ProductVersion (@[email protected]), and event Comments (Built with @[email protected]). This leads me to believe that parsing is not being done.</p></div><div id="comment-48633-info" class="comment-info"><span class="comment-age">(18 Dec '15, 13:50)</span> coloncm</div></div><span id="48636"></span><div id="comment-48636" class="comment"><div id="post-48636-score" class="comment-score"></div><div class="comment-text"><p>I can't see why your plugin CMakeLists.txt isn't transforming the plugin.rc.in file. Maybe you can add some debugging output to your CMakeLists.txt using the message function, e.g.</p><pre><code>message(STATUS &quot;Some text, a variable: ${RC_MODULE_VERSION}&quot;)</code></pre><p>Do this before and after the <code>set_module_info()</code> call, delete plugin.rc from the build directory and run the CMake generation step again. Redirect the CMake generation output to a file to examine it, e.g. <code>2&gt;&amp;1 &gt; c:\temp\log.txt</code>.</p></div><div id="comment-48636-info" class="comment-info"><span class="comment-age">(18 Dec '15, 16:24)</span> grahamb ♦</div></div><span id="48646"></span><div id="comment-48646" class="comment"><div id="post-48646-score" class="comment-score">1</div><div class="comment-text"><p>I think this may have been fixed in trunk.</p></div><div id="comment-48646-info" class="comment-info"><span class="comment-age">(20 Dec '15, 00:38)</span> Anders ♦</div></div><span id="48659"></span><div id="comment-48659" class="comment not_top_scorer"><div id="post-48659-score" class="comment-score"></div><div class="comment-text"><p>Good to know! It's not a showstopper for me since the solution builds now. Thanks.</p></div><div id="comment-48659-info" class="comment-info"><span class="comment-age">(21 Dec '15, 07:05)</span> coloncm</div></div></div><div id="comment-tools-48630" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-48630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

