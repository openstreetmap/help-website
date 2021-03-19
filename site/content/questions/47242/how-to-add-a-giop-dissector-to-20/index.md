+++
type = "question"
title = "How to add a GIOP dissector to 2.0"
description = '''I am trying to add a dissector to the new 2.0 build for Windows and need a bit of help as this is my first time using the new cmake structure. The dissector is a CORBA dissector generated from our IDL using the wireshark_be.py script for omniorb. I have put the .c file in epan/dissectors and added i...'''
date = "2015-11-04T08:05:00Z"
lastmod = "2015-11-04T09:53:00Z"
weight = 47242
keywords = [ "dissector", "custom" ]
aliases = [ "/questions/47242" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add a GIOP dissector to 2.0](/questions/47242/how-to-add-a-giop-dissector-to-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47242-score" class="post-score" title="current number of votes">0</div><span id="post-47242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to add a dissector to the new 2.0 build for Windows and need a bit of help as this is my first time using the new cmake structure.</p><p>The dissector is a CORBA dissector generated from our IDL using the wireshark_be.py script for omniorb.</p><p>I have put the .c file in epan/dissectors and added it to epan/CMakeListsCustom.txt</p><p>I've run cmake and can see it including the custom list.</p><p>I then run msbuild /m /p:Configuration=RelWithDebInfo wireshark.sln. This appears to compile my dissector with no errors and the.obj file exists with all the other packet-*.obj files.</p><p>But when I run Wireshark my dissector isn't in the list. So what is the step I'm missing to get the dissector linked in.</p><p>Thanks for any help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '15, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/3d25bda262a989924649329d5e0b6b0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Ling&#39;s gravatar image" /><p><span>Andy Ling</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Ling has no accepted answers">0%</span></p></div></div><div id="comments-container-47242" class="comments-container"></div><div id="comment-tools-47242" class="comment-tools"></div><div class="clear"></div><div id="comment-47242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47245"></span>

<div id="answer-container-47245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47245-score" class="post-score" title="current number of votes">0</div><span id="post-47245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The documentation on this is somewhat lacking, all contributions accepted.</p><p>If this is really a plugin, then epan\CMakeListsCustom.txt is not the place for this as that's for built in dissectors.</p><p>For a plugin, you need to add the plugin directory to the list of plugin directories, I'm not entirely sure how you do this. In the main CMakeLists.txt there is a variable <code>PLUGIN_SRC_DIRS</code>, that is set to all the "standard" plugins and is also has the value <code>CUSTOM_PLUGIN_SRC_DIR</code> appended to it, so I think you need to arrange that that variable contains the source directory of your plugin, probably via a <code>-D CUSTOM_PLUGIN_SRC_DIR=plugins/xxx</code> on the CMake command line. For multiple directories you'll need to experiment.</p><p>You'll also need an appropriate CMakeLists.txt in your plugin source directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '15, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47245" class="comments-container"><span id="47246"></span><div id="comment-47246" class="comment"><div id="post-47246-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the input.</p><p>I have got it working. It looks like the problem was actually a warning I'd ignored on some other plugins I've added that I thought were working. Fixing that warning has made the GIOP disector work.</p><p>As to your comments about what is &amp; isn't a plugin, I'm not sure, but what I am doing roughly maps what I was told for version 1 Wireshark.</p><p>I have some "real" plugins which dissect their own protocol and these are in plugins/xxx directories. This required creating a CMakeListsCustom.txt in the root directory of Wireshark. There is an example file to show you what to do.</p><p>The GIOP plugin/dissector is an "add on" to GIOP. These all seem to live in epan/dissectors and there is a CMakeListsCustom.txt file in epan to let you add new ones. Which is what I have done.</p><p>If this isn't the right way, then can someone tell me what is.</p><p>Thanks</p></div><div id="comment-47246-info" class="comment-info"><span class="comment-age">(04 Nov '15, 09:11)</span> <span class="comment-user userinfo">Andy Ling</span></div></div><span id="47251"></span><div id="comment-47251" class="comment"><div id="post-47251-score" class="comment-score"></div><div class="comment-text"><p>Simple rule is if it's in epan\dissectors, then its classed as a built-in dissector, even if it does "plug-in" to giop. After all tcp "plugs-in" to ip.</p><p>In the Wireshark world, a plugin lives outside of epan\dissectors, is a separate loadable module (a dll on Windows) and shows up in the plugins tab of the About dialog.</p><p>I'd missed the CMakeListCustom.txt.example in the root of the sources, I looked for it in the plugins directory where the additional plugins were listed for nmake builds and a grep for .txt files including <code>CUSTOM_PLUGIN_SRC_DIR</code> obviously missed the example file.</p><p>Anyway, your issue is solved, and I'm now a bit wiser.</p></div><div id="comment-47251-info" class="comment-info"><span class="comment-age">(04 Nov '15, 09:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47245" class="comment-tools"></div><div class="clear"></div><div id="comment-47245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

