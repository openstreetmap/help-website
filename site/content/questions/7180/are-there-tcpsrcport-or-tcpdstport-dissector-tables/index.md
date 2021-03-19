+++
type = "question"
title = "Are there &quot;tcp.srcport&quot; or &quot;tcp.dstport&quot; dissector tables?"
description = '''Is it possible to get DissectorTable according to &quot;tcp.srcport&quot; or &quot;tcp.dstport&quot; in Lua? Now,I have two package, one&#x27;s tcp source port is 7709, another&#x27;s tcp destination port is 7709. That is ,a request and a response. The fields of request package and response package are different. So I need to re...'''
date = "2011-11-01T07:14:00Z"
lastmod = "2014-07-24T19:16:00Z"
weight = 7180
keywords = [ "dissectortable", "lua" ]
aliases = [ "/questions/7180" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Are there "tcp.srcport" or "tcp.dstport" dissector tables?](/questions/7180/are-there-tcpsrcport-or-tcpdstport-dissector-tables)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7180-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to get DissectorTable according to "tcp.srcport" or "tcp.dstport" in Lua? Now,I have two package, one's tcp source port is 7709, another's tcp destination port is 7709. That is ,a request and a response. The fields of request package and response package are different. So I need to register two different dissector to process the two different packaget. At the time, I do it like this: local tcp_req_table = DissectorTable.get("tcp.port") tcp_req_table:add(7709,p_req)</p><p>local tcp_res_table = DissectorTable.get("tcp.port") tcp_res_table:add(7709,p_res)</p><p>But,finally, only the p_res works. So, How should I register the two different dissector? When I try "DissectorTable.get("tcp.srcport")", wireshark said that didn't exist. Thank you!</p></div><div id="question-tags" class="tags-container tags">dissectortable lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '11, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/efc2b9ab9b08370fea301906167c1761?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="happyboy8909&#39;s gravatar image" /><p>happyboy8909<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="happyboy8909 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Nov '11, 12:56</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7180" class="comments-container"></div><div id="comment-tools-7180" class="comment-tools"></div><div class="clear"></div><div id="comment-7180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="7184"></span>

<div id="answer-container-7184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7184-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There do not exist "tcp.srcport" or "tcp.dstport" dissector tables, so you can't get them in any programming language, whether it's C or Lua or....</p><p>You do not need to register two different dissectors for this case. You merely need to have the one-and-only dissector for port 7709 determine whether the packet is a request or a response and dissect it appropriately?</p><p>Does this protocol truly have no field in the packet to indicate whether it's a request or a response? If it truly has no such field, then the best you can do is something such as checking whether the matching port value is the same as the source port or the destination port. In a C-language dissector, this would be done by comparing <code>pinfo-&gt;match_uint</code> with <code>pinfo-&gt;srcport</code> or <code>pinfo-&gt;dstport</code>; I think there is a Lua API to access <code>match_uint</code>, but it doesn't look as if there's one to access <code>srcport</code> or <code>dstport</code>, so you might have to compare <code>match_uint</code> against 7709.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '11, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7184" class="comments-container"><span id="7303"></span><div id="comment-7303" class="comment"><div id="post-7303-score" class="comment-score"></div><div class="comment-text"><p>Lua has <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html#lua_class_Pinfo"><code>pinfo</code></a><code>.src_port</code> and <code>pinfo.dst_port</code></p></div><div id="comment-7303-info" class="comment-info"><span class="comment-age">(08 Nov '11, 17:52)</span> helloworld</div></div></div><div id="comment-tools-7184" class="comment-tools"></div><div class="clear"></div><div id="comment-7184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7301"></span>

<div id="answer-container-7301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7301-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To add a few notes for the Guy's answer, if you want to register multiple dissectors per port you have an option of saving previous dissector registered for that port and calling it in your dissector, thus creating dissector chain. The sample code can be found within wiki and looks smth like this:</p><pre><code>do
        local wrapper_proto    = Proto(&quot;my_proto&quot;, &quot;My Protocol&quot;)
        local MY_PORT          = 7709

        local f_tcp_srcport    = Field.new(&quot;tcp.srcport&quot;)
        local f_tcp_dstport    = Field.new(&quot;tcp.srcport&quot;)

        local original_dissector

        function wrapper_proto.dissector(tvbuffer, pinfo, treeitem)

            -- invoke original dissector
            pcall(
                    function()
                        original_dissector:call(tvbuffer, pinfo, treeitem)
                    end
                )

            -- now do your job
            if f_tcp_srcport() &amp;&amp; f_tcp_srcport().value == MY_PORT then
                -- handle response
            end
            if f_tcp_dstport() &amp;&amp; f_tcp_dstport().value == MY_PORT then
                -- handle request
            end

        end

        local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
        -- save the original dissector so we can still get to it
        original_dissector = tcp_dissector_table:get_dissector( MY_PORT ) 
        -- and take its place in the dissector table
        tcp_dissector_table:add( MY_PORT, wrapper_proto)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p>ShomeaX<br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '11, 16:38</p></div></div><div id="comments-container-7301" class="comments-container"></div><div id="comment-tools-7301" class="comment-tools"></div><div class="clear"></div><div id="comment-7301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34903"></span>

<div id="answer-container-34903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34903-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, ShowmeaX is right. I test it as following:</p><p>1) data.dissector</p><p>2) report.dissector</p><p>3)</p><pre><code>local data_dissector = data.dissector
local report_dissector = report.dissector
function wrapper.dissector(buffer, pinfo, tree)
if *** then
    data_dissector:call(buffer, pinfo, tree)
elseif *** then
    report_dissector:call(buffer, pinfo, tree)
end</code></pre><p>4) add wrapper to dissectorTable</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '14, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/7b6f62723a894576f644d5e2f51933e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark_xg&#39;s gravatar image" /><p>wireshark_xg<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark_xg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '14, 19:18</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34903" class="comments-container"></div><div id="comment-tools-34903" class="comment-tools"></div><div class="clear"></div><div id="comment-34903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

