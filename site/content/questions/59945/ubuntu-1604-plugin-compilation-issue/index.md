+++
type = "question"
title = "Ubuntu 16.04 plugin compilation issue"
description = '''I have successfully upgraded my wireshark plugin on windows 7(from 1.6 to 2.2). It works perfectly. But now I have been trying to compile the code on Ubuntu 16.04 and it is showing a lot of errors. I have removed a lot of it but got stuck in the following issue. This appears everytime I open Wiresha...'''
date = "2017-03-09T00:35:00Z"
lastmod = "2017-03-09T06:50:00Z"
weight = 59945
keywords = [ "custom", "dissector", "updateplugin", "ubuntu" ]
aliases = [ "/questions/59945" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ubuntu 16.04 plugin compilation issue](/questions/59945/ubuntu-1604-plugin-compilation-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59945-score" class="post-score" title="current number of votes">0</div><span id="post-59945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have successfully upgraded my wireshark plugin on windows 7(from 1.6 to 2.2). It works perfectly. But now I have been trying to compile the code on Ubuntu 16.04 and it is showing a lot of errors. I have removed a lot of it but got stuck in the following issue. This appears everytime I open Wireshark.</p><pre><code>&quot;The plugin &#39;myPlugin.so&#39; has no registration routines&quot;</code></pre><p>I have both -</p><pre><code> void proto_register_myPlugin(void);
 void proto_reg_handoff_myPlugin(void);</code></pre><p>functions. What should I do now? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-updateplugin" rel="tag" title="see questions tagged &#39;updateplugin&#39;">updateplugin</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '17, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p><span>xaheen</span><br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-59945" class="comments-container"><span id="59946"></span><div id="comment-59946" class="comment"><div id="post-59946-score" class="comment-score"></div><div class="comment-text"><p>plus, is there any official guideline for compiling custom plugin on Linux? Thanks</p></div><div id="comment-59946-info" class="comment-info"><span class="comment-age">(09 Mar '17, 00:38)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="59953"></span><div id="comment-59953" class="comment"><div id="post-59953-score" class="comment-score"></div><div class="comment-text"><p>How are you building, CMake or autotools? If you use CMake, then Windows and linux should be the same.</p></div><div id="comment-59953-info" class="comment-info"><span class="comment-age">(09 Mar '17, 02:36)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="59954"></span><div id="comment-59954" class="comment"><div id="post-59954-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> I am using "make -f Makefile.linux" - This command</p></div><div id="comment-59954-info" class="comment-info"><span class="comment-age">(09 Mar '17, 02:40)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-59945" class="comment-tools"></div><div class="clear"></div><div id="comment-59945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59955"></span>

<div id="answer-container-59955" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59955-score" class="post-score" title="current number of votes">1</div><span id="post-59955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xaheen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably that Makefile is autotools derived somehow. I suspect you'll have to regenerate the makefile using autotools and there my knowledge ends. The Developers Guide info on building on Unix is <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html#_building_on_unix">here</a> and that suggests:</p><pre><code>Run the autogen.sh script at the top-level wireshark directory to configure your build directory.

$ ./autogen.sh
$ ./configure
$ make

If you need to build with a non-standard configuration, you can run

$ ./configure --help</code></pre><p>On the few times I've built on Linux I've used CMake, in exactly the same way as it's done on Windows except for the actual build command where I use <code>cmake --build</code> rather than <code>msbuild ...</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '17, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59955" class="comments-container"><span id="59956"></span><div id="comment-59956" class="comment"><div id="post-59956-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. So after building wireshark, what cmake command do I use to compile the plugin? and do I put the plugin source code in the wireshark/plugin folder, just like on windows?</p></div><div id="comment-59956-info" class="comment-info"><span class="comment-age">(09 Mar '17, 05:14)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="59958"></span><div id="comment-59958" class="comment"><div id="post-59958-score" class="comment-score">1</div><div class="comment-text"><p>CMake builds should be very similar on both platforms as that's the point of CMake, so simply do the same as on Windows, e.e. as per section 3.1 of doc\README.plugins:</p><pre><code>For CMake builds, either pass the custom plugin dir on the CMake generation
step command line:

CMake ... -DCUSTOM_PLUGIN_SRC_DIR=&quot;plugins/foo&quot;

or copy the top-level file CMakeListsCustom.txt.example to CMakeListsCustom.txt
(also in the top-level source dir) and edit so that CUSTOM_PLUGIN_SRC_DIR is
set() to the relative path of your plugin, e.g.

set(CUSTOM_PLUGIN_SRC_DIR plugins/foo)

and re-run the CMake generation step.

To build the plugin, run your normal Wireshark build step.</code></pre></div><div id="comment-59958-info" class="comment-info"><span class="comment-age">(09 Mar '17, 05:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="59963"></span><div id="comment-59963" class="comment"><div id="post-59963-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot</p></div><div id="comment-59963-info" class="comment-info"><span class="comment-age">(09 Mar '17, 06:50)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-59955" class="comment-tools"></div><div class="clear"></div><div id="comment-59955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

