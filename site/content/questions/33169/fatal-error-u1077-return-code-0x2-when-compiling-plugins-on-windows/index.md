+++
type = "question"
title = "Fatal Error U1077 return code 0x2 when compiling plugins on Windows"
description = '''When I try to nmake my plugins on the latest x64 Windows build, I encounter this error:  Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 16.00.40219.01 for 80x86 Copyright (C) Microsoft Corporation. All rights reserved. packet-ptcm.c plugin.c packet-ptcm.c(199) : error C2220: warning treated ...'''
date = "2014-05-29T08:02:00Z"
lastmod = "2014-05-30T11:55:00Z"
weight = 33169
keywords = [ "windows", "compile", "error", "build", "plugin" ]
aliases = [ "/questions/33169" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Fatal Error U1077 return code 0x2 when compiling plugins on Windows](/questions/33169/fatal-error-u1077-return-code-0x2-when-compiling-plugins-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33169-score" class="post-score" title="current number of votes">0</div><span id="post-33169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I try to nmake my plugins on the latest x64 Windows build, I encounter this error:</p><pre><code>    Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 16.00.40219.01 for 80x86
Copyright (C) Microsoft Corporation.  All rights reserved.
packet-ptcm.c
plugin.c
packet-ptcm.c(199) : error C2220: warning treated as error - no &#39;object&#39; file generated
packet-ptcm.c(199) : warning C4047: &#39;function&#39; : &#39;expert_field *&#39; differs in levels of indirection from &#39;int&#39;
packet-ptcm.c(199) : warning C4024: &#39;expert_add_info_format&#39; : different types for formal and actual parameter 3
packet-ptcm.c(199) : warning C4047: &#39;function&#39; : &#39;const char *&#39; differs in levels of indirection from &#39;int&#39;
packet-ptcm.c(199) : warning C4024: &#39;expert_add_info_format&#39; : different types for formal and actual parameter 4
packet-ptcm.c(212) : warning C4047: &#39;function&#39; : &#39;expert_field *&#39; differs in levels of indirection from &#39;int&#39;
packet-ptcm.c(212) : warning C4024: &#39;expert_add_info_format&#39; : different types for formal and actual parameter 3
packet-ptcm.c(212) : warning C4047: &#39;function&#39; : &#39;const char *&#39; differs in levels of indirection from &#39;int&#39;
packet-ptcm.c(212) : warning C4024: &#39;expert_add_info_format&#39; : different types for formal and actual parameter 4
packet-ptcm.c(219) : warning C4047: &#39;function&#39; : &#39;expert_field *&#39; differs in levels of indirection from &#39;int&#39;
packet-ptcm.c(219) : warning C4024: &#39;expert_add_info_format&#39; : different types for formal and actual parameter 3
packet-ptcm.c(219) : warning C4047: &#39;function&#39; : &#39;const char *&#39; differs in levels of indirection from &#39;int&#39;
packet-ptcm.c(219) : warning C4024: &#39;expert_add_info_format&#39; : different types for formal and actual parameter 4
packet-ptcm.c(230) : error C2198: &#39;dissector_try_heuristic&#39; : too few arguments for call
packet-ptcm.c(381) : warning C4113: &#39;int (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;new_dissector_t&#39;
packet-ptcm.c(382) : warning C4113: &#39;int (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;new_dissector_t&#39;
packet-ptcm.c(395) : warning C4113: &#39;int (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;heur_dissector_t&#39;
packet-ptcm.c(398) : warning C4113: &#39;int (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;heur_dissector_t&#39;
packet-ptcm.c(414) : warning C4113: &#39;int (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;heur_dissector_t&#39;
packet-ptcm.c(417) : warning C4113: &#39;int (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;heur_dissector_t&#39;
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>I was able to compile successfully on the latest Linux build, but I can't figure out Windows. What should I do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '14, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/8f51fdd676352de28608f014b75acbcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20G&#39;s gravatar image" /><p><span>Thomas G</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas G has one accepted answer">100%</span></p></div></div><div id="comments-container-33169" class="comments-container"></div><div id="comment-tools-33169" class="comment-tools"></div><div class="clear"></div><div id="comment-33169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33221"></span>

<div id="answer-container-33221" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33221-score" class="post-score" title="current number of votes">0</div><span id="post-33221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Thomas G has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to solve the problem. The error that was preventing the build from continuing was</p><blockquote><p>packet-ptcm.c(230) : error C2198: 'dissector_try_heuristic' : too few arguments for call</p></blockquote><p>and I solved it by finding the line</p><blockquote><p>if (! dissector_try_heuristic(heur_dissector_list, payload, pinfo, ptcm_tree)) {</p></blockquote><p>and adding a NULL parameter to dissector_try_heuristic</p><blockquote><p>if (! dissector_try_heuristic(heur_dissector_list, payload, pinfo, ptcm_tree, NULL)) {</p></blockquote><p>This was necessary because of an API change which added an extra parameter to that function.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '14, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/8f51fdd676352de28608f014b75acbcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20G&#39;s gravatar image" /><p><span>Thomas G</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas G has one accepted answer">100%</span></p></div></div><div id="comments-container-33221" class="comments-container"></div><div id="comment-tools-33221" class="comment-tools"></div><div class="clear"></div><div id="comment-33221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33175"></span>

<div id="answer-container-33175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33175-score" class="post-score" title="current number of votes">0</div><span id="post-33175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you switched from an x86 to x64 build? If so, did you run a "clean" and check there were no old <em>.obj and</em> lib files lying around?</p><p>Can you build a vanilla version without your plugin?</p><p>What version are you building, is the source from git, or via a tarball\zip?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '14, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33175" class="comments-container"><span id="33176"></span><div id="comment-33176" class="comment"><div id="post-33176-score" class="comment-score"></div><div class="comment-text"><p>I have only ever used an x64 build<br />
I can build a vanilla version without my plugins<br />
I am using version 1.10.7 from git<br />
</p><p>These plugins were made by a previous employee for version 1.9 and later patched for 1.10 compatibility, and they have no problems running on linux.</p></div><div id="comment-33176-info" class="comment-info"><span class="comment-age">(29 May '14, 09:43)</span> <span class="comment-user userinfo">Thomas G</span></div></div><span id="33178"></span><div id="comment-33178" class="comment"><div id="post-33178-score" class="comment-score"></div><div class="comment-text"><p>It's going to be difficult to comment further without actually seeing the code. Can you post it in a public space anywhere?, or at least an excerpt from around line 199 including context before and after. It looks like a variable type declaration is incorrect somewhere, maybe an include issue.</p></div><div id="comment-33178-info" class="comment-info"><span class="comment-age">(29 May '14, 10:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33175" class="comment-tools"></div><div class="clear"></div><div id="comment-33175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

