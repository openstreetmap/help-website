+++
type = "question"
title = "Can I register a tap by lua?"
description = '''I want to register a tap for statisticing private protocols. I can do it by calling the register_tap c api, by how can I do it by lua script?'''
date = "2015-03-13T02:51:00Z"
lastmod = "2015-03-15T19:37:00Z"
weight = 40535
keywords = [ "lua", "statistics", "tap" ]
aliases = [ "/questions/40535" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I register a tap by lua?](/questions/40535/can-i-register-a-tap-by-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40535-score" class="post-score" title="current number of votes">0</div><span id="post-40535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to register a tap for statisticing private protocols. I can do it by calling the register_tap c api, by how can I do it by lua script?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '15, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/250f0ea2aef45cd0d2fbfc46f4038733?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Francis%20Wong&#39;s gravatar image" /><p><span>Francis Wong</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Francis Wong has no accepted answers">0%</span></p></div></div><div id="comments-container-40535" class="comments-container"></div><div id="comment-tools-40535" class="comment-tools"></div><div class="clear"></div><div id="comment-40535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40536"></span>

<div id="answer-container-40536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40536-score" class="post-score" title="current number of votes">0</div><span id="post-40536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Listener.html">Listener</a> function.</p><p>Have you looked at the example in the Developers Guide: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/wslua_tap_example.html">10.3. Example of Listener written in Lua</a>?</p><p>There are also some listener examples on the Wireshark Lua <a href="https://wiki.wireshark.org/Lua/Examples">examples</a> page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '15, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40536" class="comments-container"><span id="40600"></span><div id="comment-40600" class="comment"><div id="post-40600-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer; I want to build a stats tree like the http packet counter(Statistics/HTTP/Packet Counter); I can't call tap_queue_packet manually by lua, so I use the C plugin instead of lua now. Thank U again.^-^</p></div><div id="comment-40600-info" class="comment-info"><span class="comment-age">(15 Mar '15, 19:37)</span> <span class="comment-user userinfo">Francis Wong</span></div></div></div><div id="comment-tools-40536" class="comment-tools"></div><div class="clear"></div><div id="comment-40536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

