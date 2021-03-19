+++
type = "question"
title = "Chained dissector not working"
description = '''I&#x27;m trying to write a chained dissector for the CFLOW protocol, and was attempting to follow the example here: https://wiki.wireshark.org/Lua/Dissectors#chained_dissectors However, when I try to use it in Wireshark I get the Lua Error: attempt to index upvalue &#x27;original_cflow_dissector&#x27; (a nil value...'''
date = "2016-05-27T16:13:00Z"
lastmod = "2016-05-27T16:13:00Z"
weight = 53016
keywords = [ "chained-dissector", "lua", "dissector", "dissectortable" ]
aliases = [ "/questions/53016" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Chained dissector not working](/questions/53016/chained-dissector-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to write a chained dissector for the CFLOW protocol, and was attempting to follow the example here: <a href="https://wiki.wireshark.org/Lua/Dissectors#chained_dissectors">https://wiki.wireshark.org/Lua/Dissectors#chained_dissectors</a><br />
However, when I try to use it in Wireshark I get the Lua Error: attempt to index upvalue 'original_cflow_dissector' (a nil value).</p><p>Does anyone have insight as to what I've done wrong?<br />
</p><p>I think it has to do with my get_dissector call calling the udp dissector instead of the cflow dissector, but I'm not sure how to fix that. Replacing udp.port with tcp.port obviously didn't work, but it does compile and run so that makes me think its not an issue with the depth of my variable declaration.</p><p>Here's the code - I replaced some parts with comments, but they should be working fine.</p><pre><code>do
        --create the protocol

        --create the fields for our protocol

        --add the fields to the protocol

        --declare the fields to read

        local original_cflow_dissector
        function cflow_wrapper_proto.dissector(buffer, pinfo, tree)
            original_cflow_dissector:call(buffer, pinfo, tree)
            --do things
        end
        udp_dissector_table = DissectorTable.get(&quot;udp.port&quot;)
        original_cflow_dissector = udp_dissector_table:get_dissector(2055)
        udp_dissector_table:add(2055, cflow_wrapper_proto)
    end</code></pre></div><div id="question-tags" class="tags-container tags">chained-dissector lua dissector dissectortable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '16, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/69337c614f643f05439087eb2c42ac6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osarkar&#39;s gravatar image" /><p>osarkar<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osarkar has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-53016" class="comments-container"></div><div id="comment-tools-53016" class="comment-tools"></div><div class="clear"></div><div id="comment-53016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

