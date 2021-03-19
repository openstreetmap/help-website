+++
type = "question"
title = "Lua: How can I detect a change of capture file?"
description = '''Hi, I&#x27;ve written a Wireshark Lua postdissector to calculate some timing values for HTTP packets. The initial code (the code that runs on Wireshark start up) includes the definition of some tables that are used to retain data between calls to the dissector function. Everything works OK but if I load ...'''
date = "2014-07-09T13:07:00Z"
lastmod = "2014-07-11T13:54:00Z"
weight = 34524
keywords = [ "lua", "postdissector", "wireshark" ]
aliases = [ "/questions/34524" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Lua: How can I detect a change of capture file?](/questions/34524/lua-how-can-i-detect-a-change-of-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34524-score" class="post-score" title="current number of votes">0</div><span id="post-34524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've written a Wireshark Lua postdissector to calculate some timing values for HTTP packets. The initial code (the code that runs on Wireshark start up) includes the definition of some tables that are used to retain data between calls to the dissector function. Everything works OK but if I load a new trace file I'm picking up residual table entries associated with the previous file.</p><p>I can then reinitialize the global tables if I know that the trace file has changed.</p><p>How can my dissector detect that the trace file has changed?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '14, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jul '14, 12:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34524" class="comments-container"><span id="34542"></span><div id="comment-34542" class="comment"><div id="post-34542-score" class="comment-score"></div><div class="comment-text"><p>Hadriel, is the <code>init_routines</code> table documented anywhere?</p></div><div id="comment-34542-info" class="comment-info"><span class="comment-age">(10 Jul '14, 01:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34571"></span><div id="comment-34571" class="comment"><div id="post-34571-score" class="comment-score"></div><div class="comment-text"><p>It's added to using the Lua "<code>Proto.init()</code>", so documented <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_attrib_proto_init">here</a>.</p></div><div id="comment-34571-info" class="comment-info"><span class="comment-age">(10 Jul '14, 11:33)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="34607"></span><div id="comment-34607" class="comment"><div id="post-34607-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that. It works fine.</p><p>Best regards...Paul</p></div><div id="comment-34607-info" class="comment-info"><span class="comment-age">(11 Jul '14, 13:54)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-34524" class="comment-tools"></div><div class="clear"></div><div id="comment-34524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34582"></span>

<div id="answer-container-34582" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34582-score" class="post-score" title="current number of votes">1</div><span id="post-34582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PaulOfford has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so you'd add an init routine, using Lua <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_attrib_proto_init"><code>Proto.init()</code></a>, as per Hadriel's comment.</p><p>Your init routine would be called whenever you need to reinitialize whatever global state you maintain.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '14, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34582" class="comments-container"></div><div id="comment-tools-34582" class="comment-tools"></div><div class="clear"></div><div id="comment-34582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

