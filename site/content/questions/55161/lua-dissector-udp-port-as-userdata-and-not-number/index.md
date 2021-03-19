+++
type = "question"
title = "lua dissector: udp port as userdata and not number"
description = '''hallo, I have modified the simple example found in wiki: -- trivial protocol example -- declare our protocol trivial_proto = Proto(&quot;trivial&quot;,&quot;Trivial Protocol&quot;)  udp_src_f = Field.new(&quot;udp.srcport&quot;) udp_dst_f = Field.new(&quot;udp.dstport&quot;)  -- create a function to dissect it function trivial_proto.disse...'''
date = "2016-08-29T03:08:00Z"
lastmod = "2016-08-29T05:33:00Z"
weight = 55161
keywords = [ "lua", "dissector", "number", "userdata" ]
aliases = [ "/questions/55161" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [lua dissector: udp port as userdata and not number](/questions/55161/lua-dissector-udp-port-as-userdata-and-not-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55161-score" class="post-score" title="current number of votes">0</div><span id="post-55161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hallo, I have modified the simple example found in wiki:</p><pre><code>-- trivial protocol example
-- declare our protocol
trivial_proto = Proto(&quot;trivial&quot;,&quot;Trivial Protocol&quot;)

udp_src_f = Field.new(&quot;udp.srcport&quot;)
udp_dst_f = Field.new(&quot;udp.dstport&quot;)

-- create a function to dissect it
function trivial_proto.dissector(buffer,pinfo,tree)
    local udp_src = udp_src_f()
    local udp_dst = udp_dst_f()

    if udp_src==8002 then
        pinfo.cols.protocol = &quot;PBUS_RESP&quot;
    end

    if udp_dst==8002 then
        pinfo.cols.protocol = &quot;PBUS_REQ&quot;
    end

    local subtree = tree:add(trivial_proto,buffer(),&quot;Trivial Protocol Data&quot;)
    subtree:add(buffer(0,2),&quot;port: &quot; .. tostring(udp_src) .. &quot;-&gt;&quot; .. tostring(udp_dst) .. &quot; ::: type &quot; .. type(udp_dst))
    subtree:add(buffer(0,2),&quot;The first two bytes: &quot; .. buffer(0,2):uint())
    subtree = subtree:add(buffer(2,2),&quot;The next two bytes&quot;)
    subtree:add(buffer(2,1),&quot;The 3rd byte: &quot; .. buffer(2,1):uint())
    subtree:add(buffer(3,1),&quot;The 4th byte: &quot; .. buffer(3,1):uint())
end
-- load the udp.port table
udp_table = DissectorTable.get(&quot;udp.port&quot;)
-- register our protocol to handle udp port 7777
udp_table:add(8002,trivial_proto)</code></pre><p>udp_src and udp_dst are userdata and the "if" are avways false. Why udp_src and udp_dst are userdata, and how to "cast" them to number?</p><p>best regards</p><p>Max</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span> <span class="post-tag tag-link-userdata" rel="tag" title="see questions tagged &#39;userdata&#39;">userdata</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '16, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/d7ed6d77e609ba6ea79fbd77078a7fe9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mastupristi&#39;s gravatar image" /><p><span>mastupristi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mastupristi has no accepted answers">0%</span></p></div></div><div id="comments-container-55161" class="comments-container"></div><div id="comment-tools-55161" class="comment-tools"></div><div class="clear"></div><div id="comment-55161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55162"></span>

<div id="answer-container-55162" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55162-score" class="post-score" title="current number of votes">1</div><span id="post-55162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mastupristi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use</p><pre><code>local udp_src = udp_src_f().value
local udp_dst = udp_dst_f().value</code></pre><p>The functions defined using <code>Field.new</code> provide access to the whole structure of the field, which contains several information values. You need to choose the <code>value</code> one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '16, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Aug '16, 06:09</strong> </span></p></div></div><div id="comments-container-55162" class="comments-container"></div><div id="comment-tools-55162" class="comment-tools"></div><div class="clear"></div><div id="comment-55162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

