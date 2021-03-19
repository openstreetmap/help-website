+++
type = "question"
title = "Unable to load custom module"
description = '''Im refactoring my current dissector by splitting it up in different lua modules. The implemented protocol has multiple subprotocols. Which protocol is decided by a field in the top protocol. I created a lua module for each subprotocol, but I am unable to load the module into the wireshark. the file ...'''
date = "2015-01-09T06:21:00Z"
lastmod = "2015-01-09T10:26:00Z"
weight = 38996
keywords = [ "lua", "dissector", "linux" ]
aliases = [ "/questions/38996" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to load custom module](/questions/38996/unable-to-load-custom-module)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38996-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im refactoring my current dissector by splitting it up in different lua modules.</p><p>The implemented protocol has multiple subprotocols. Which protocol is decided by a field in the top protocol. I created a lua module for each subprotocol, but I am unable to load the module into the wireshark.</p><p>the file structure<br />
</p><pre><code>+$/.wireshark/plugins
    -proto.lua
    -tm_frame.lua</code></pre><p>A module</p><pre><code>local tm_frame = {}
function tm_frame.handle(tree, buffer)
    local tm_frame_tree = tree:add(buffer, &quot;TM Transfer Frame&quot;)
    ...
end
return tm_frame</code></pre><p>The line of code to call the module in the main plugin</p><pre><code>local tm_frame = require &#39;tm_frame&#39;</code></pre><p>Other information</p><pre><code>Mint 17
Lua 5.2.3
Wireshark 1.10.6</code></pre><p>How can i load the module?</p></div><div id="question-tags" class="tags-container tags">lua dissector linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/27fcbc2c78dd2c12e7b0de7b08efc891?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maarten&#39;s gravatar image" /><p>Maarten<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maarten has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '15, 06:22</p></div></div><div id="comments-container-38996" class="comments-container"></div><div id="comment-tools-38996" class="comment-tools"></div><div class="clear"></div><div id="comment-38996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39006"></span>

<div id="answer-container-39006" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39006-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're using Wireshark 1.12.0 or newer, then you can create a sub-directory for your module files in the personal plugins directory - let's call that new sub-directory "<code>tm_modules</code>" - and you can put the <code>tm_frame.lua</code> file in that "<code>tm_modules</code>" directory; keep your main <code>proto.lua</code> Lua file in the main personal plugins directory but put this line before your "<code>require</code>" line in it:</p><pre><code>package.prepend_path(&quot;tm_modules&quot;)
-- then do the require
local tm_frame = require &#39;tm_frame&#39;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '15, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39006" class="comments-container"><span id="39073"></span><div id="comment-39073" class="comment"><div id="post-39073-score" class="comment-score"></div><div class="comment-text"><p>Confirmed, compiled the source (1.12.3) with the --with-lua options. Prepend path isnt neccesary. Wireshark is able to find the file.</p></div><div id="comment-39073-info" class="comment-info"><span class="comment-age">(12 Jan '15, 02:59)</span> Maarten</div></div></div><div id="comment-tools-39006" class="comment-tools"></div><div class="clear"></div><div id="comment-39006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38997"></span>

<div id="answer-container-38997" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38997-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A bit of a guess but if you are placing two files in plugins directory they both will be executed by lua.</p><p>I'd maybe try to 1) place second file one directory above in separate directory ie: my_custom_lib 2) then try something like</p><pre><code>dofile(&quot;../my_custom_lib/tm_frame.lua&quot;)</code></pre><p>command in your code in proto.lua</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '15, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-38997" class="comments-container"><span id="39000"></span><div id="comment-39000" class="comment"><div id="post-39000-score" class="comment-score"></div><div class="comment-text"><p>dofile is not neccesary when it the files are in the wireshark plugin directory.</p></div><div id="comment-39000-info" class="comment-info"><span class="comment-age">(09 Jan '15, 07:10)</span> Maarten</div></div><span id="39004"></span><div id="comment-39004" class="comment"><div id="post-39004-score" class="comment-score"></div><div class="comment-text"><p>Yes, that's what I was guessing that will happen. Btw if you are looking at packaging there's pretty good example here</p><p><a href="https://github.com/martin-cowie/wireshark-dissector">https://github.com/martin-cowie/wireshark-dissector</a></p></div><div id="comment-39004-info" class="comment-info"><span class="comment-age">(09 Jan '15, 08:53)</span> izopizo</div></div><span id="39070"></span><div id="comment-39070" class="comment"><div id="post-39070-score" class="comment-score"></div><div class="comment-text"><p>never thought of doing dofile() somewhere else than in the init.lua file. Great example!</p></div><div id="comment-39070-info" class="comment-info"><span class="comment-age">(12 Jan '15, 01:30)</span> Maarten</div></div></div><div id="comment-tools-38997" class="comment-tools"></div><div class="clear"></div><div id="comment-38997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

