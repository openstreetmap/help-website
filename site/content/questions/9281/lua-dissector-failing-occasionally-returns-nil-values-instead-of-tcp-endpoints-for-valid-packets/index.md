+++
type = "question"
title = "Lua dissector failing: occasionally returns nil values instead of TCP endpoints for valid packets"
description = '''Hi all. I have a small dissector, which keeps returning nil values for a normal TCP packets from time to time.  For some reason, even if pinfo.net_src is set, ip_src_f() may return nil. Also, I can&#x27;t get how to decode ip_len_f() return, which is userdata, to number.  do  local testdissector = Proto(...'''
date = "2012-02-29T08:04:00Z"
lastmod = "2012-02-29T08:04:00Z"
weight = 9281
keywords = [ "frames", "lua", "tcp" ]
aliases = [ "/questions/9281" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua dissector failing: occasionally returns nil values instead of TCP endpoints for valid packets](/questions/9281/lua-dissector-failing-occasionally-returns-nil-values-instead-of-tcp-endpoints-for-valid-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9281-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. I have a small dissector, which keeps returning nil values for a normal TCP packets from time to time.</p><p>For some reason, even if pinfo.net_src is set, ip_src_f() may return nil. Also, I can't get how to decode ip_len_f() return, which is userdata, to number.</p><pre><code>    do
        local testdissector = Proto(&quot;Test&quot;, &quot;Test&quot;);

        ip_src_f = Field.new(&quot;ip.src&quot;)
        ip_dst_f = Field.new(&quot;ip.dst&quot;)
        tcp_src_f = Field.new(&quot;tcp.srcport&quot;)
        tcp_dst_f = Field.new(&quot;tcp.dstport&quot;)
        time_f =  Field.new(&quot;frame.time_epoch&quot;)
        ip_len_f = Field.new(&quot;ip.len&quot;)
        frame_len_f = Field.new(&quot;frame.len&quot;)
        tcp_hlen_f = Field.new(&quot;tcp.hdr_len&quot;)
        tcp_ack = Field.new(&quot;tcp.flags.ack&quot;)
        tcp_syn = Field.new(&quot;tcp.flags.syn&quot;)
        tcp_psh = Field.new(&quot;tcp.flags.push&quot;)
        tcp_rst = Field.new(&quot;tcp.flags.reset&quot;)
        tcp_fin = Field.new(&quot;tcp.flags.fin&quot;)

        function testdissector.dissector(tvbuffer, pinfo, treeitem)
            if 1 == 1 then ---sport then

               local sport = tcp_src_f() -- alright
               local dport = tcp_dst_f() -- alright
               local saddr = pinfo.net_src -- 50% nil
               local daddr = pinfo.net_dst -- 50% nil
           --- do something
               end
         return -- nil, to comply with no-reassembly requirements
         end
    register_postdissector(testdissector)
end</code></pre><p>TCP reassembly is turned off, HTTP dissector is disabled</p></div><div id="question-tags" class="tags-container tags">frames lua tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '12, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/9ea8d24625eb393ad806db229932b468?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cagali-san&#39;s gravatar image" /><p>cagali-san<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cagali-san has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Feb '12, 08:07</p></div></div><div id="comments-container-9281" class="comments-container"></div><div id="comment-tools-9281" class="comment-tools"></div><div class="clear"></div><div id="comment-9281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

