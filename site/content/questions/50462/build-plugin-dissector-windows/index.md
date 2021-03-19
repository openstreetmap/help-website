+++
type = "question"
title = "build plugin dissector windows"
description = '''Hello, I try to build a custom plugin dissector on windows. I work on sources from tag 2.0.1. Build with VS2013 express. The build environnement is working (https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html) even if I&#x27;m not able to make the installer and there are some errors on doc...'''
date = "2016-02-24T02:15:00Z"
lastmod = "2016-02-25T04:27:00Z"
weight = 50462
keywords = [ "windows7", "dissector", "vs2013", "plugin" ]
aliases = [ "/questions/50462" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [build plugin dissector windows](/questions/50462/build-plugin-dissector-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50462-score" class="post-score" title="current number of votes">0</div><span id="post-50462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I try to build a custom plugin dissector on windows. I work on sources from tag 2.0.1. Build with VS2013 express.</p><p>The build environnement is working (<a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html)">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html)</a> even if I'm not able to make the installer and there are some errors on doc generation but that's not the point.</p><p>When I try to build a plugin (for example gryphon "nmake -f Makefile.nmake all" ) I get following error : NMAKE : fatal error U1073: incapable d'obtenir '....\epan\libwireshark.lib' .</p><p>Can anyone help me to build the missing file : libwireshark.lib or explein what is wrong in how I build the plugin ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-vs2013" rel="tag" title="see questions tagged &#39;vs2013&#39;">vs2013</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '16, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/195c8bfd4768041efdfdd094508cc2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atsju2&#39;s gravatar image" /><p><span>atsju2</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atsju2 has no accepted answers">0%</span></p></div></div><div id="comments-container-50462" class="comments-container"></div><div id="comment-tools-50462" class="comment-tools"></div><div class="clear"></div><div id="comment-50462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50464"></span>

<div id="answer-container-50464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50464-score" class="post-score" title="current number of votes">0</div><span id="post-50464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You likely haven't followed the Developers Guide instructions exactly as written as CMake is now the primary build system for 2.x and CMake will generate a Visual Studio solution that you build using Visual Studio or msbuild, rather than nmake.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '16, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50464" class="comments-container"><span id="50466"></span><div id="comment-50466" class="comment"><div id="post-50466-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer about Cmake and VS. Even if a bit short it helps me search in the right direction.</p><p>Be sure I (re-re-re-)read the Developers Guide and README.plugins. I even had a look to README.dissector but I haven't seen precise information on how to build the plugins.</p><ul><li>I cleaned my git checkout.</li><li>I folowed README.plugins until step 3.1 included (I have a plugin\foo directory and I do not need a permanent addition, I just want to build my plugin to get the dll to add in existing wireshark installations.)</li><li>Cmake at top level generates the visual studio solution .</li><li>I build wireshark with msbuild. (gryphon seems to build...)</li></ul><p>So far so good, now how to build the foo plugin ?</p><p>Meanwhile I will try to do the permanent addition procedure but I still want to undestand how to do the custom extension! =&gt; permanent addition seems to work. Custom extension should be better explained or removed from documentation if not compatible with Cmake.</p></div><div id="comment-50466-info" class="comment-info"><span class="comment-age">(24 Feb '16, 05:41)</span> <span class="comment-user userinfo">atsju2</span></div></div><span id="50470"></span><div id="comment-50470" class="comment"><div id="post-50470-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@atsju2</span></p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>A quick look at README.plugins shows there's some improvement to be made.</p><p>To add a temporary custom plugin, re-run the CMake generation step adding the following definition to the CMake command, modified as appropriate for your plugin:</p><pre><code>-D CUSTOM_PLUGIN_SRC_DIR=&quot;plugins/foo&quot;</code></pre><p>Then build as before (VS or msbuild).</p><p>To make a permanent addition, modify the top-level CMakeLists.txt to add the plugin directory to the PLUGIN_DIRS list.</p></div><div id="comment-50470-info" class="comment-info"><span class="comment-age">(24 Feb '16, 07:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="50474"></span><div id="comment-50474" class="comment"><div id="post-50474-score" class="comment-score"></div><div class="comment-text"><p>In the plugin dir create a file CMakeListsCustom.txt</p><p>In the file add:</p><p>set(CUSTOM_PLUGIN_SRC_DIR foo/bar )</p></div><div id="comment-50474-info" class="comment-info"><span class="comment-age">(24 Feb '16, 08:43)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="50475"></span><div id="comment-50475" class="comment"><div id="post-50475-score" class="comment-score">1</div><div class="comment-text"><p>I think <span>@Anders</span> meant: copy the source top-level <code>CMakeListsCustom.txt.example</code> to <code>CMakeListsCustom.txt</code> (also in the source top-level directory), and edit to set CUSTOM_PLUGIN_SRC_DIR as required. Note the relative path from the top-level source dir is required.</p><p>Making the change this way will affect all subsequent CMake generation steps. The way I noted will only affect the CMake generation step it's used on (and thereafter as it's cached in CMakeCache.txt).</p></div><div id="comment-50475-info" class="comment-info"><span class="comment-age">(24 Feb '16, 09:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="50495"></span><div id="comment-50495" class="comment not_top_scorer"><div id="post-50495-score" class="comment-score"></div><div class="comment-text"><p>Thank you, the last solution works and is easyer then the permanent addition. README.plugin should be updated to be more complete</p></div><div id="comment-50495-info" class="comment-info"><span class="comment-age">(25 Feb '16, 01:11)</span> <span class="comment-user userinfo">atsju2</span></div></div><span id="50504"></span><div id="comment-50504" class="comment"><div id="post-50504-score" class="comment-score">1</div><div class="comment-text"><p>This was done in commit <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=4fec250ed953192b3de697f6fb6b773d03e1a0c5">4fec250ed</a>.</p></div><div id="comment-50504-info" class="comment-info"><span class="comment-age">(25 Feb '16, 04:27)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-50464" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-50464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

