+++
type = "question"
title = "How to find the ethernet dissector."
description = '''In previous Lua code we would do the following  --  -- This is not a COMEX message. Get the default dissector and invoke it.  -- local default_dissector = Dissector.get( &quot;eth&quot; ) default_dissector:call( tvb , pinfo , tree )  We would call the ethernet dissector if we chose to not analyze this. This w...'''
date = "2016-10-16T21:30:00Z"
lastmod = "2016-10-17T01:33:00Z"
weight = 56432
keywords = [ "ethernet" ]
aliases = [ "/questions/56432" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find the ethernet dissector.](/questions/56432/how-to-find-the-ethernet-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56432-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In previous Lua code we would do the following</p><pre><code>    --
    -- This is not a COMEX message. Get the default dissector and invoke it.
    --
local default_dissector = Dissector.get( &quot;eth&quot; )
default_dissector:call( tvb , pinfo , tree )</code></pre>We would call the ethernet dissector if we chose to not analyze this.<p>This work with 2.0.x versions of Wireshark</p><p>Now we are getting an error with 2.2.0</p><p>What are we doing wrong ?</p></div><div id="question-tags" class="tags-container tags">ethernet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '16, 21:30</strong></p><img src="https://secure.gravatar.com/avatar/6e8b1db33a7ee4961eee9aed5627ff32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Randy%20Rohrbach&#39;s gravatar image" /><p>Randy Rohrbach<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Randy Rohrbach has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '16, 22:20</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-56432" class="comments-container"></div><div id="comment-tools-56432" class="comment-tools"></div><div class="clear"></div><div id="comment-56432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56436"></span>

<div id="answer-container-56436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56436-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The name has been changed:</p><pre><code>  register_dissector(&quot;eth_withoutfcs&quot;, dissect_eth_withoutfcs, proto_eth);

  register_dissector(&quot;eth_withfcs&quot;, dissect_eth_withfcs, proto_eth);

  register_dissector(&quot;eth_maybefcs&quot;, dissect_eth_maybefcs, proto_eth);</code></pre><p>You probably want "eth_withoutfcs"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-56436" class="comments-container"></div><div id="comment-tools-56436" class="comment-tools"></div><div class="clear"></div><div id="comment-56436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

