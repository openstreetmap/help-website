+++
type = "question"
title = "Reassembly not working with a chained dissector in Lua"
description = '''I&#x27;m writing a Lua chained dissector on top of the standard HTTP dissector to extract information from the HTTP payload. However, when I chain my dissector with the original HTTP dissector, reassembly is failing. I stripped down the Lua dissector to the bare minimum but still have the issue. Here is ...'''
date = "2016-11-28T15:02:00Z"
lastmod = "2016-12-04T07:47:00Z"
weight = 57685
keywords = [ "lua", "dissector", "http", "reassembly" ]
aliases = [ "/questions/57685" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Reassembly not working with a chained dissector in Lua](/questions/57685/reassembly-not-working-with-a-chained-dissector-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57685-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a Lua chained dissector on top of the standard HTTP dissector to extract information from the HTTP payload. However, when I chain my dissector with the original HTTP dissector, reassembly is failing. I stripped down the Lua dissector to the bare minimum but still have the issue. Here is the stripped down dissector:</p><pre><code>do
        local http_wrapper_proto = Proto(&quot;http_extra&quot;, &quot;Extra analysis of the HTTP protocol&quot;);
        local original_http_dissector
        function http_wrapper_proto.dissector(tvbuffer, pinfo, treeitem)
            original_http_dissector:call(tvbuffer, pinfo, treeitem)
        end

        local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
        original_http_dissector = Dissector.get(&quot;http&quot;)
        tcp_dissector_table:add(80, http_wrapper_proto)
        tcp_dissector_table:add(8888, http_wrapper_proto)
end</code></pre><p>Without the dissector, reassembly works fine:</p><pre><code>$ tshark -r li.buienradar.nl.pcapng -Y http
  5 0.028009000 192.168.0.17 -&gt; 192.168.0.18 HTTP 294 POST http://li.buienradar.nl/api/Publication HTTP/1.1  (application/json)
 11 0.463406000 192.168.0.18 -&gt; 192.168.0.17 HTTP 217 HTTP/1.1 200 OK  (application/json)
 24 116.487852000 192.168.0.17 -&gt; 192.168.0.18 HTTP 294 POST http://li.buienradar.nl/api/Publication HTTP/1.1  (application/json)
 28 116.628794000 192.168.0.18 -&gt; 192.168.0.17 HTTP 217 HTTP/1.1 200 OK  (application/json)
$</code></pre><p>But when the Lua dissector is used, reaassembly fails:</p><pre><code>$ tshark -r li.buienradar.nl.pcapng -Y http -X lua_script:http3.lua
  4 0.028009000 192.168.0.17 -&gt; 192.168.0.18 HTTP 428 POST http://li.buienradar.nl/api/Publication HTTP/1.1 
  9 0.437610000 192.168.0.18 -&gt; 192.168.0.17 HTTP 523 HTTP/1.1 200 OK 
 22 116.484815000 192.168.0.17 -&gt; 192.168.0.18 HTTP 428 POST http://li.buienradar.nl/api/Publication HTTP/1.1 
 26 116.535529000 192.168.0.18 -&gt; 192.168.0.17 HTTP 523 HTTP/1.1 200 OK 
$</code></pre><p>Am I doing something wrong? Is this a bug? Or is reassembly functionality somehow not implemented yet for chained Lua dissectors?</p></div><div id="question-tags" class="tags-container tags">lua dissector http reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '16, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57685" class="comments-container"></div><div id="comment-tools-57685" class="comment-tools"></div><div class="clear"></div><div id="comment-57685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57838"></span>

<div id="answer-container-57838" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57838-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>So what you're doing is inserting another dissector between TCP and HTTP, right?</p><p>The problem, I think, (having not tried anything) comes down to what's explained in this comment in <code>epan/packet.c</code>:</p><pre><code>    /*
     * can_desegment is set to 2 by anyone which offers the
     * desegmentation api/service.
     * Then everytime a subdissector is called it is decremented
     * by one.
     * Thus only the subdissector immediately on top of whoever
     * offers this service can use it.
     * We save the current value of &quot;can_desegment&quot; for the
     * benefit of TCP proxying dissectors such as SOCKS, so they
     * can restore it and allow the dissectors they call to use
     * the desegmentation service.
     */</code></pre><p>The important part is the <strong>Thus only the subdissector immediately on top of whoever offers this service can use it</strong> bit.</p><p>(pinfo-&gt;can_desegment, which is set here, is checked by the <code>req_resp_hdrs.c</code> code which is used by the HTTP dissector.)</p><p>You should (if the LUA API allows you) be able to solve this by incrementing <code>can_desegment</code> in your dissector (before calling the HTTP dissector). It appears that's what the SSL dissector does.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '16, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-57838" class="comments-container"><span id="57850"></span><div id="comment-57850" class="comment"><div id="post-57850-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff, that did the trick, here is the alteration for future reference:</p><pre><code>do
        local http_wrapper_proto = Proto(&quot;http_extra&quot;, &quot;Extra analysis of the HTTP protocol&quot;);
        local original_http_dissector
        function http_wrapper_proto.dissector(tvbuffer, pinfo, treeitem)
            local can_desegment_saved = pinfo.can_desegment
            if pinfo.can_desegment &gt; 0 then
                pinfo.can_desegment = 2
            end

            original_http_dissector:call(tvbuffer, pinfo, treeitem)

            -- my extra diseector code is inserted here

            pinfo.can_desegment = can_desegment_saved
        end

        local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
        original_http_dissector = Dissector.get(&quot;http&quot;)
        tcp_dissector_table:add(80, http_wrapper_proto)
        tcp_dissector_table:add(8888, http_wrapper_proto)
end</code></pre></div><div id="comment-57850-info" class="comment-info"><span class="comment-age">(04 Dec '16, 14:33)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-57838" class="comment-tools"></div><div class="clear"></div><div id="comment-57838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

