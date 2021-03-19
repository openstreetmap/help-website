+++
type = "question"
title = "disply info on column of customise protocol"
description = '''I have created the customise protocol in Lua and I want to display the subtree info on the same line of main tree ( which display the name of my customise protocol). please find the code below and let me know what should I do . function cus_proto.dissector(tvbuf, pktinfo, root)  dprint2(&quot;cus_proto.d...'''
date = "2015-12-04T03:41:00Z"
lastmod = "2015-12-04T03:41:00Z"
weight = 48258
keywords = [ "column", "of", "customise", "protocol", "lua" ]
aliases = [ "/questions/48258" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [disply info on column of customise protocol](/questions/48258/disply-info-on-column-of-customise-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48258-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created the customise protocol in Lua and I want to display the subtree info on the same line of main tree ( which display the name of my customise protocol).</p><p>please find the code below and let me know what should I do .</p><pre><code>function cus_proto.dissector(tvbuf, pktinfo, root)
    dprint2(&quot;cus_proto.dissector called&quot;)
    -- reset the save Tvbs
    tvbs = {}

    -- get the length of the packet buffer (Tvb).
    local pktlen = tvbuf:len()

    --local bytes_consumed = 0
    if pklen==0 then return end

    pktinfo.cols.protocol=cus_proto.name

    --create subtree for cus proto
    subtree=root:add(cus_proto,tvbuf(0))

    -- add protocol fields to subtree
    subtree:add(hdr_fields.msg_data_length, tvbuf(0,4))
    subtree:add(hdr_fields.msg_id, tvbuf(4,1))
    subtree:add(hdr_fields.msg_type, tvbuf(5,1))
    subtree:add(hdr_fields.msg_method_id, tvbuf(6,1))
end</code></pre></div><div id="question-tags" class="tags-container tags">column of customise protocol lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '15, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/5f95711321f840922720016670d7d3b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tony_2013&#39;s gravatar image" /><p>Tony_2013<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tony_2013 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '15, 03:50</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48258" class="comments-container"></div><div id="comment-tools-48258" class="comment-tools"></div><div class="clear"></div><div id="comment-48258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

