+++
type = "question"
title = "How to solve error C2099 and LNK2019 when building dissector plugin on Windows 7 64bit?"
description = '''Hi all, I am using the up-to-date Wireshark source and I was able to build WS on Windows 7 64bit ok. Now I wanted to start with a dissector plugin. For the first try I started with a built-in dissector called packet-mqtt.c and copied that as packet-mqttmod.c to the plugin location. Following the ste...'''
date = "2016-04-13T02:15:00Z"
lastmod = "2016-04-22T10:03:00Z"
weight = 51625
keywords = [ "windows7", "dissector", "linker", "64-bit", "plugin" ]
aliases = [ "/questions/51625" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to solve error C2099 and LNK2019 when building dissector plugin on Windows 7 64bit?](/questions/51625/how-to-solve-error-c2099-and-lnk2019-when-building-dissector-plugin-on-windows-7-64bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51625-score" class="post-score" title="current number of votes">0</div><span id="post-51625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am using the up-to-date Wireshark source and I was able to build WS on Windows 7 64bit ok. Now I wanted to start with a dissector plugin. For the first try I started with a built-in dissector called packet-mqtt.c and copied that as packet-mqttmod.c to the plugin location. Following the steps in README.plugins.</p><p>I didn't change anything in the code except the names from mqtt and MQTT to mqttmod to MQTTMOD so I know it is "my" dissector. When I try to build, I get the following error:</p><p><code>C:\Development\wireshark\plugins\mqttmod\packet-mqttmod.c(569): error C2099: initializer is not a constant [c:\Development\wsbuild64\plugins\mqttmod\mqttmod.vcxproj]</code></p><p>If I comment out the error causing code to see if the rest runs through, I get another error:</p><p><code>(Link target) -&gt; packet-mqttmod.obj : error LNK2019: unresolved external symbol dissect_uleb128 referenced in function dissect_mqttmod [c:\Development\wsbuild64\plugins\mqttmod\mqttmod.vcxproj]  C:\Development\wsbuild64\run\RelWithDebInfo\plugins\mqttmod.dll : fatal error LNK1120: 1 unresolved externals [c:\Development\wsbuild64\plugins\mqttmod\mqttmod.vcxproj]</code></p><p>At least for the second error I found that this is related to dwarf.h/dwarf.c, but I could not find out in which library this is compiled and spot the correct *.lib file. And then still I would not know how to satisfy this dependency for the build.</p><p>I'd appreciate any suggestions. Best regards, Mike</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-linker" rel="tag" title="see questions tagged &#39;linker&#39;">linker</span> <span class="post-tag tag-link-64-bit" rel="tag" title="see questions tagged &#39;64-bit&#39;">64-bit</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '16, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/c288ec16e3d47bc1e1602e5b4e283949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikethebo&#39;s gravatar image" /><p><span>mikethebo</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikethebo has no accepted answers">0%</span></p></div></div><div id="comments-container-51625" class="comments-container"></div><div id="comment-tools-51625" class="comment-tools"></div><div class="clear"></div><div id="comment-51625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51626"></span>

<div id="answer-container-51626" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51626-score" class="post-score" title="current number of votes">0</div><span id="post-51626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mikethebo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure about the first error, what version of Visual Studio are you using?</p><p>For the second, the function <code>dissect_uleb128()</code> is in libwireshark, but it isn't exported so can't be linked to by a plugin in a separate DLL. To export the function, add <code>WS_DLL_PUBLIC</code> to the declaration in dwarf.h.</p><p><strong>Edit</strong> dwarf.h will also need to <code>#include "ws_symbol_export.h"</code> to get the correct declaration of <code>WS_DLL_PUBLIC</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Apr '16, 07:46</strong> </span></p></div></div><div id="comments-container-51626" class="comments-container"><span id="51633"></span><div id="comment-51633" class="comment"><div id="post-51633-score" class="comment-score"></div><div class="comment-text"><p>Yes sorry I forgot. I am using VS2013 and I am setting all environment variables accordingly.</p></div><div id="comment-51633-info" class="comment-info"><span class="comment-age">(13 Apr '16, 07:24)</span> <span class="comment-user userinfo">mikethebo</span></div></div><span id="51634"></span><div id="comment-51634" class="comment"><div id="post-51634-score" class="comment-score"></div><div class="comment-text"><p>As the files compiles quite happily in its normal place I suspect it's something else that isn't ex\imported. Maybe <code>tfs_set_notset</code>, although that is marked as WS_DLL_PUBLIC</p><p>Also note my edit about dwarf.h above.</p></div><div id="comment-51634-info" class="comment-info"><span class="comment-age">(13 Apr '16, 07:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51659"></span><div id="comment-51659" class="comment"><div id="post-51659-score" class="comment-score"></div><div class="comment-text"><p>This solved the linker error. Thank you. Funny things is, that the first error is related to <code>TFS(&amp;tfs_set_notset)</code>. From what I found with google the const char in the typedef of tfs.h might be the cause. If I pass <code>NULL</code> instead of <code>TFS(&amp;tfs_set_notset)</code> it is fine.</p></div><div id="comment-51659-info" class="comment-info"><span class="comment-age">(14 Apr '16, 00:55)</span> <span class="comment-user userinfo">mikethebo</span></div></div><span id="51661"></span><div id="comment-51661" class="comment"><div id="post-51661-score" class="comment-score"></div><div class="comment-text"><p>If I remember correctly there is a problem with using global tfs strings on Windows in plugins, somting with DATA and inter dll. You'll be better of defining them locally.</p></div><div id="comment-51661-info" class="comment-info"><span class="comment-age">(14 Apr '16, 01:42)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="51880"></span><div id="comment-51880" class="comment"><div id="post-51880-score" class="comment-score"></div><div class="comment-text"><p>Also check comment in <a href="https://ask.wireshark.org/questions/51660/what-does-define-__tfs_h__-do-in-tfsh">this</a> question for the C2099 error when compiling for Windows.</p></div><div id="comment-51880-info" class="comment-info"><span class="comment-age">(22 Apr '16, 10:03)</span> <span class="comment-user userinfo">mikethebo</span></div></div></div><div id="comment-tools-51626" class="comment-tools"></div><div class="clear"></div><div id="comment-51626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

