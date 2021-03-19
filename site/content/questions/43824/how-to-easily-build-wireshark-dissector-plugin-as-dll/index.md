+++
type = "question"
title = "How to easily build wireshark dissector plugin as dll?"
description = '''Hi, I modified an unclompete Wireshark dissector plugin, i.e. I did some modifications to the already existing c-files. I neither added a new file in the plugin directory nor did I add some new includes in the c-files. I just added some missing functionality in the c-files. Now I want to build a dll...'''
date = "2015-07-02T09:25:00Z"
lastmod = "2015-07-02T09:40:00Z"
weight = 43824
keywords = [ "mingw", "make", "plugin", "dissector", "dll" ]
aliases = [ "/questions/43824" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to easily build wireshark dissector plugin as dll?](/questions/43824/how-to-easily-build-wireshark-dissector-plugin-as-dll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43824-score" class="post-score" title="current number of votes">0</div><span id="post-43824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I modified an unclompete Wireshark dissector plugin, i.e. I did some modifications to the already existing c-files. I neither added a new file in the plugin directory nor did I add some new includes in the c-files. I just added some missing functionality in the c-files. Now I want to build a dll file out of the source files. Is there a way to do this without installing the whole toolchain (Visual Studion, Qt, Cygwin, Python, ...) and building the whole Wireshark as described here <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</a>? I just want to compile the few c-files with gcc (MinGW), put them into a dll and replace the old dll with the new one.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mingw" rel="tag" title="see questions tagged &#39;mingw&#39;">mingw</span> <span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '15, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/79b7102a413f15d1d82da92963633346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Obs&#39;s gravatar image" /><p><span>Obs</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Obs has no accepted answers">0%</span></p></div></div><div id="comments-container-43824" class="comments-container"></div><div id="comment-tools-43824" class="comment-tools"></div><div class="clear"></div><div id="comment-43824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43826"></span>

<div id="answer-container-43826" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43826-score" class="post-score" title="current number of votes">0</div><span id="post-43826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nope. You'll need to have a working build environment on Windows to build the plugin DLL. Also note you really should (must ??) use the same version of Visual Studio to build the plugin as was used to build the version of Wireshark that you wish to add the plugin to, i.e. for Wireshark 1.12.x that means Visual Studio 2010.</p><p>Building with MinGW on windows isn't supported.</p><p>Also make sure you're complying with the GPL regarding distribution and access to the sources of the plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '15, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43826" class="comments-container"></div><div id="comment-tools-43826" class="comment-tools"></div><div class="clear"></div><div id="comment-43826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

