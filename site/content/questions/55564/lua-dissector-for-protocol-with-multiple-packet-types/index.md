+++
type = "question"
title = "Lua dissector for protocol with multiple packet types"
description = '''Dear experts, I have the following problem: I am trying to build a LUA dissector for a custom protocol which has multiple packet formats. The protocol is built on top of UDP and has the following format: | UDP | Header - 8 bytes (0 to 7) | Fixed length PDUs 37 bytes - different types | The type of t...'''
date = "2016-09-15T06:51:00Z"
lastmod = "2016-09-15T07:15:00Z"
weight = 55564
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/55564" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua dissector for protocol with multiple packet types](/questions/55564/lua-dissector-for-protocol-with-multiple-packet-types)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55564-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear experts,</p><p>I have the following problem: I am trying to build a LUA dissector for a custom protocol which has multiple packet formats. The protocol is built on top of UDP and has the following format:</p><p>| UDP | Header - 8 bytes (0 to 7) | Fixed length PDUs 37 bytes - different types |</p><p>The type of the PDU is given by the 8th byte.</p><p>The question is: How can I identify the PDU type using the value of the 8th byte?</p><p>I have tried comparing the int value with no result! If I use the following code inside the dissector function,I get the error message "C stack overflow"</p><pre><code>-- let&#39;s say byte 8 is in HEX 0x35
local TYPE = buffer(8,1):uint()
   if TYPE:uint() == 53 then
    subtree:add (.....)
   end</code></pre><p>Any ideas/hints about how to solve this would be appreciated!</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '16, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/736170f27313125d7a9c6d3f7f9e9cda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="panai&#39;s gravatar image" /><p>panai<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="panai has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '16, 22:37</p></div></div><div id="comments-container-55564" class="comments-container"></div><div id="comment-tools-55564" class="comment-tools"></div><div class="clear"></div><div id="comment-55564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55565"></span>

<div id="answer-container-55565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55565-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try using:</p><pre><code>...
if TYPE == 0x35 then
...</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '16, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55565" class="comments-container"><span id="55582"></span><div id="comment-55582" class="comment"><div id="post-55582-score" class="comment-score"></div><div class="comment-text"><p>Hello grahamb</p><p>I used:</p><p>local TYPE = buffer(8,1):uint()</p><p>if TYPE == 0x53 then ...</p><p>I get the same error " C Stack Overflow " - I don'd understand how the type conversion works, now regarding the above code I did not expect it to work because I defined the TYPE variable as a decimal value, so basically I am trying to compare a decimal value with a hex one ..I don't know ...</p><p>Thank You</p></div><div id="comment-55582-info" class="comment-info"><span class="comment-age">(15 Sep '16, 23:08)</span> panai</div></div><span id="55585"></span><div id="comment-55585" class="comment"><div id="post-55585-score" class="comment-score"></div><div class="comment-text"><p>Lua variables are not typed, the :uint() suffix says how to treat the byte(s) read from the buffer. A hex integer literal of 0x35 is simply another representation of the decimal value 53.</p><p>You must have some other error in your Lua code causing the issue, either post the full contents so others can look at it and help, or try commenting out sections until you find which bit breaks.</p></div><div id="comment-55585-info" class="comment-info"><span class="comment-age">(16 Sep '16, 02:19)</span> grahamb ♦</div></div><span id="55592"></span><div id="comment-55592" class="comment"><div id="post-55592-score" class="comment-score"></div><div class="comment-text"><p>Very strange, I have somehow fixed the issue! I have changed the parameters of the buffer function in the subtree initialization.</p><p>Originally I had:</p><p>local subtree = tree:add (PROTO, buffer())</p><p>I changed it to:</p><p>function PROTO.dissector (buffer, pinfo, tree)</p><p>local subtree = tree:add (PROTO, buffer(0, 1))</p><p>pinfo.cols.info:append (" (" .. PROTO.description .. ")")</p><p>subtree:add (f.type, buffer(0,1)) subtree:add (f.seq, buffer(1,1)) subtree:add (f.length, buffer(2,2)) subtree:add (f.time, buffer(4,4))</p><p>PDU_TYPE = buffer(8,1):uint()</p><p>if PDU_TYPE == 0x35 then ....</p><p>and everything works</p><p>Thank you for the explanations!</p></div><div id="comment-55592-info" class="comment-info"><span class="comment-age">(16 Sep '16, 04:45)</span> panai</div></div><span id="55594"></span><div id="comment-55594" class="comment"><div id="post-55594-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-55594-info" class="comment-info"><span class="comment-age">(16 Sep '16, 05:10)</span> grahamb ♦</div></div></div><div id="comment-tools-55565" class="comment-tools"></div><div class="clear"></div><div id="comment-55565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

