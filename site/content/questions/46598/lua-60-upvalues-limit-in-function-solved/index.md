+++
type = "question"
title = "LUA 60 upvalues limit in function [Solved]"
description = '''Hi all, We use some LUA files to decode our specifics frames. Some of or LUA have a lot of values (more than 60) in the function (dissector). Wireshark displays me an alert message before launching &quot;Function at line 141 has more than 60 upvalues&quot; here an example ok LUA function : --Dissector functio...'''
date = "2015-10-16T00:52:00Z"
lastmod = "2015-10-16T06:28:00Z"
weight = 46598
keywords = [ "function", "lua", "limit", "upvalues" ]
aliases = [ "/questions/46598" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA 60 upvalues limit in function \[Solved\]](/questions/46598/lua-60-upvalues-limit-in-function-solved)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46598-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>We use some LUA files to decode our specifics frames. Some of or LUA have a lot of values (more than 60) in the function (dissector). Wireshark displays me an alert message before launching "Function at line 141 has more than 60 upvalues"</p><p>here an example ok LUA function :</p><pre><code>--Dissector
function p_omap_Global_Counters.dissector(buf, pkt, root)

    --Set info
    pkt.cols.info:append(&quot; : &quot; .. p_omap_Global_Counters.name)

    --Root
    local Global_Counters_tree = root:add(p_omap_Global_Counters, buf(0))
    Global_Counters_tree:add(f_counter_arrayasync_data_sync_unshared_data_dropped_, buf(0, 4))
    Global_Counters_tree:add(f_counter_arrayccp_com_safe_rx_message_dropped_, buf(4, 4))
    Global_Counters_tree:add(f_counter_arrayccp_com_safe_rx_unkown_message_dropped_, buf(8, 4))
etc...</code></pre><p>Is it possible to change this limitation ? (We use version 1.10.3) thx for your help Mickaël</p></div><div id="question-tags" class="tags-container tags">function lua limit upvalues</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/7f760b4c43ce1fedf31523c7797b882d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micka%C3%ABl&#39;s gravatar image" /><p>Mickaël<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mickaël has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '15, 06:29</p></div></div><div id="comments-container-46598" class="comments-container"></div><div id="comment-tools-46598" class="comment-tools"></div><div class="clear"></div><div id="comment-46598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46619"></span>

<div id="answer-container-46619" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46619-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The pb came from the number of local variable declared (&gt;60) I solved it by declaring all my local variable into one array :</p><pre><code>--Protocol
local omapVars =
{
   myVar1example = ...,
   myVar2example = ...,
       ....
    }</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/7f760b4c43ce1fedf31523c7797b882d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micka%C3%ABl&#39;s gravatar image" /><p>Mickaël<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mickaël has no accepted answers">0%</span></p></div></div><div id="comments-container-46619" class="comments-container"></div><div id="comment-tools-46619" class="comment-tools"></div><div class="clear"></div><div id="comment-46619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

