+++
type = "question"
title = "how to use Lua to write multi protocol dissector plugin"
description = '''I am writing an XLES protocol dissector, but this protocol is in the payload of LAPV5, so I have to write the LAPV5 dissector first. How do I connect the two protocols? I wrote something like this: udp_encap_table = DissectorTable.get(&quot;udp.port&quot;) udp_encap_table:add(49152,lapV5Proto)  lapV5Dessector...'''
date = "2012-05-03T19:40:00Z"
lastmod = "2012-05-11T23:39:00Z"
weight = 10658
keywords = [ "lua" ]
aliases = [ "/questions/10658" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to use Lua to write multi protocol dissector plugin](/questions/10658/how-to-use-lua-to-write-multi-protocol-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10658-score" class="post-score" title="current number of votes">0</div><span id="post-10658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing an XLES protocol dissector, but this protocol is in the payload of LAPV5, so I have to write the LAPV5 dissector first. How do I connect the two protocols?</p><p>I wrote something like this:</p><pre><code>udp_encap_table = DissectorTable.get(&quot;udp.port&quot;)
udp_encap_table:add(49152,lapV5Proto)

lapV5DessectorTable = DissectorTable.new(&quot;lapv5.data&quot;, &quot;lapv5 dissector table&quot;,ftypes.STRING,base.none)
lapv5_encap_table = DissectorTable.get(&quot;lapv5.data&quot;)
lapv5_encap_table:add(&quot;.&quot;,xlesProto)</code></pre><p>But it doesn't work. XLES only exists when LAPV5 has a payload. Does the <code>pattern</code> argument in <code>DissectorTable.add(pattern,dissector)</code> only support a full match?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '12, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/afc6e4f52606362f04f8f06ee31ea0b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ww2521&#39;s gravatar image" /><p><span>ww2521</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ww2521 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 May '12, 03:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10658" class="comments-container"></div><div id="comment-tools-10658" class="comment-tools"></div><div class="clear"></div><div id="comment-10658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10895"></span>

<div id="answer-container-10895" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10895-score" class="post-score" title="current number of votes">3</div><span id="post-10895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ww2521 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In your case, you would daisy-chain the dissectors. That is, <a href="http://wiki.wireshark.org/LuaAPI/Dissector#dissector:call.28tvb.2C_pinfo.2C_tree.29">call</a> your XLES dissector directly from your LAPV5 dissector. Try this Lua:</p><pre><code>-- ############# 
-- # XLES
-- #############
local proto_xles = Proto(&quot;xles&quot;, &quot;XLES Protocol&quot;)

function proto_xles.dissector(buf, pinfo, tree)
    print(&#39;XLES&#39;, tostring(buf))
end

-- ############# 
-- # LAPV5
-- #############
local proto_lap5 = Proto(&quot;lapv5&quot;, &quot;LAPV5 Protocol&quot;)

-- assume data (i.e., the body) is present only if the packet is
-- longer than the header
local HEADER_LEN = 5

function proto_lap5.dissector(buf, pinfo, tree)

    if buf:len() &gt; HEADER_LEN then
        -- create a new buffer containing only the XLES data,
        -- and pass it to the XLES dissector
        Dissector.get(&quot;xles&quot;):call(buf(HEADER_LEN):tvb(),  pinfo, tree)
    end

end

-- install LAPV5 dissector at UDP port 49152
DissectorTable.get(&quot;udp.port&quot;):add(49152, proto_lap5)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-10895" class="comments-container"><span id="10953"></span><div id="comment-10953" class="comment"><div id="post-10953-score" class="comment-score"></div><div class="comment-text"><p>hi, that works. Thanks for your help.</p></div><div id="comment-10953-info" class="comment-info"><span class="comment-age">(11 May '12, 23:39)</span> <span class="comment-user userinfo">ww2521</span></div></div></div><div id="comment-tools-10895" class="comment-tools"></div><div class="clear"></div><div id="comment-10895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

