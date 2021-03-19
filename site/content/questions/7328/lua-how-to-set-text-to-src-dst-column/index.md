+++
type = "question"
title = "lua how to set text to src dst column"
description = '''Hi, All, Does anyone know how to set text to src or dst column using LUA? I can set text to protocol and info column. I can only set IP addresses to src/dst column, but cannot find a way for string. thanks! Bruce'''
date = "2011-11-09T08:20:00Z"
lastmod = "2011-11-09T17:09:00Z"
weight = 7328
keywords = [ "lua" ]
aliases = [ "/questions/7328" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua how to set text to src dst column](/questions/7328/lua-how-to-set-text-to-src-dst-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7328-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, All,</p><p>Does anyone know how to set text to src or dst column using LUA? I can set text to protocol and info column. I can only set IP addresses to src/dst column, but cannot find a way for string.</p><p>thanks! Bruce</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '11, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/c12465f5c6653c94557bec9593d25c2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruce%20Z&#39;s gravatar image" /><p>Bruce Z<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruce Z has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '11, 08:21</p></div></div><div id="comments-container-7328" class="comments-container"></div><div id="comment-tools-7328" class="comment-tools"></div><div class="clear"></div><div id="comment-7328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7349"></span>

<div id="answer-container-7349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7349-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>that's because of the column field type is "Source address" I guess. I'm not sure if this can be changed from Lua. But you can add your own fields with arbitrary addresses (even ZIP code if you want) and configure Preferences/Columns to not display original source address field and display your field instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p>ShomeaX<br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span></p></div></div><div id="comments-container-7349" class="comments-container"><span id="7379"></span><div id="comment-7379" class="comment"><div id="post-7379-score" class="comment-score"></div><div class="comment-text"><p>Thx. I want to modify the source and destination since these fields are automatically picked up by Statistics-&gt;Flow Graph tool. I am pretty sure that these fields are modifiable thru C code, e.g. MTP3 layer changes them to point codes. Just want to know if it's possible in LUA.</p></div><div id="comment-7379-info" class="comment-info"><span class="comment-age">(10 Nov '11, 13:30)</span> Bruce Z</div></div></div><div id="comment-tools-7349" class="comment-tools"></div><div class="clear"></div><div id="comment-7349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

