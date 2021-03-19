+++
type = "question"
title = "How to use &quot;require&quot; function by lua in wireshark?"
description = '''I wrote a Dissector by lua and I wrote two modules:&quot;common.lua&quot; and &quot;main.lua&quot;. In init.lua file,I use dofile(DATA_DIR..&quot;main.lua&quot;). In main.lua,I use &quot;local common = require(&quot;common&quot;);&quot;. main.lua and common.lua are in the same folder. But when I open wireshark,it&#x27;s error.This error message:&quot;module ...'''
date = "2015-02-04T00:02:00Z"
lastmod = "2015-02-04T01:43:00Z"
weight = 39625
keywords = [ "lua", "require", "dissector" ]
aliases = [ "/questions/39625" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use "require" function by lua in wireshark?](/questions/39625/how-to-use-require-function-by-lua-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39625-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a Dissector by lua and I wrote two modules:"common.lua" and "main.lua". In init.lua file,I use dofile(DATA_DIR.."main.lua"). In main.lua,I use "local common = require("common");". main.lua and common.lua are in the same folder. But when I open wireshark,it's error.This error message:"module 'common' not found: no field package.preload['common'] no file '/usr/local/share/lua/5.2/common.lua' no file '/usr/local/share/lua/5.2/common/init.lua' no file '/usr/local/lib/lua/5.2/common.lua' no file '/usr/local/lib/lua/5.2/common/init.lua' no file './common.lua' no file '/usr/local/lib/lua/5.2/common.so' no file '/usr/local/lib/lua/5.2/loadall.so' no file './common.so'"</p><p>Is that "require" function can't use in wireshark?</p><p>What should I do?</p></div><div id="question-tags" class="tags-container tags">lua require dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '15, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/b2b6df2a3742ea77be3e5365a414df36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fayn&#39;s gravatar image" /><p>fayn<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fayn has no accepted answers">0%</span></p></div></div><div id="comments-container-39625" class="comments-container"></div><div id="comment-tools-39625" class="comment-tools"></div><div class="clear"></div><div id="comment-39625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39628"></span>

<div id="answer-container-39628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39628-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at this answer to similar problem</p><p><a href="https://ask.wireshark.org/questions/38996/unable-to-load-custom-module">https://ask.wireshark.org/questions/38996/unable-to-load-custom-module</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '15, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-39628" class="comments-container"></div><div id="comment-tools-39628" class="comment-tools"></div><div class="clear"></div><div id="comment-39628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

