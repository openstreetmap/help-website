+++
type = "question"
title = "sctp.ppi m3ua dissector causes C Stack Overflow error when called from LUA"
description = '''I&#x27;m using wireshark 2.2.3 in ubuntu.  When I try to call the dissector I always get an error. This is my code: local sctp_payload_dissector_table = DissectorTable.get(&quot;sctp.ppi&quot;) original_m3ua_dissector = sctp_payload_dissector_table:get_dissector(3)  sctp_payload_dissector_table:add(3, tcap_time_pr...'''
date = "2017-01-20T03:20:00Z"
lastmod = "2017-01-20T03:20:00Z"
weight = 58901
keywords = [ "lua", "dissector", "m3ua" ]
aliases = [ "/questions/58901" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [sctp.ppi m3ua dissector causes C Stack Overflow error when called from LUA](/questions/58901/sctpppi-m3ua-dissector-causes-c-stack-overflow-error-when-called-from-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58901-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using wireshark 2.2.3 in ubuntu.</p><p>When I try to call the dissector I always get an error. This is my code:</p><pre><code>local sctp_payload_dissector_table = DissectorTable.get(&quot;sctp.ppi&quot;)
original_m3ua_dissector = sctp_payload_dissector_table:get_dissector(3) 
sctp_payload_dissector_table:add(3, tcap_time_proto)</code></pre><p>When I then call it from the dissector function:</p><pre><code>function tcap_time_proto.dissector(buffer,pinfo,tree)
  original_m3ua_dissector:call(buffer, pinfo, tree)</code></pre><p>It fails.</p><p>Is there anything worng with my code?</p><p>Carlos.</p></div><div id="question-tags" class="tags-container tags">lua dissector m3ua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '17, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/aa9c89ae16fe7b7ad1502afa28d16f68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csigueros&#39;s gravatar image" /><p>csigueros<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csigueros has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jan '17, 05:36</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-58901" class="comments-container"><span id="58902"></span><div id="comment-58902" class="comment"><div id="post-58902-score" class="comment-score"></div><div class="comment-text"><p>Can you provide the lua source file and the capture you're using for testing so others can attempt to replicate the issue, hopefully under a debugger?</p></div><div id="comment-58902-info" class="comment-info"><span class="comment-age">(20 Jan '17, 03:29)</span> grahamb ♦</div></div><span id="58903"></span><div id="comment-58903" class="comment"><div id="post-58903-score" class="comment-score"></div><div class="comment-text"><p>Sure, here they are.</p><p><a href="https://app.box.com/s/qjh67cjnfqjw8s57uvfb25vaqc92s8ds">https://app.box.com/s/qjh67cjnfqjw8s57uvfb25vaqc92s8ds</a> <a href="https://app.box.com/s/2tiqdh5z2elgpo40skccrv4y2fdmqqeg">https://app.box.com/s/2tiqdh5z2elgpo40skccrv4y2fdmqqeg</a></p></div><div id="comment-58903-info" class="comment-info"><span class="comment-age">(20 Jan '17, 04:31)</span> csigueros</div></div><span id="59098"></span><div id="comment-59098" class="comment"><div id="post-59098-score" class="comment-score"></div><div class="comment-text"><p>I have tested this with the new 2.2.4 version. Same error.</p><p>This is the output in wireshark for any sctp message:</p><pre><code>Frame 1: 246 bytes on wire (1968 bits), 246 bytes captured (1968 bits)
Ethernet II, Src: JuniperN_e6:e8:7f (00:05:85:e6:e8:7f), Dst: HewlettP_b3:fd:d0 (ec:b1:d7:b3:fd:d0)
Internet Protocol Version 4, Src: 10.80.11.55, Dst: 10.91.33.118
Stream Control Transmission Protocol, Src Port: 2905 (2905), Dst Port: 2905 (2905)
&lt;Wireshark Lua fake item&gt;
Lua Error: [string &quot;/usr/lib/x86_64-linux-gnu/wireshark/plugins/2...&quot;]:18: C stack overflow     
    [Expert Info (Error/Undecoded): Lua Error: [string &quot;/usr/lib/x86_64-linux-gnu/wireshark/plugins/2...&quot;]:18: C stack overflow]
        [Lua Error: [string &quot;/usr/lib/x86_64-linux-gnu/wireshark/plugins/2...&quot;]:18: C stack overflow]
        &lt;Message: Lua Error: [string &quot;/usr/lib/x86_64-linux-gnu/wireshark/plugins/2...&quot;]:18: C stack overflow&gt;
        [Severity level: Error]
        [Group: Undecoded]</code></pre><p>Line 18 in the LUA script is:</p><pre><code> original_m3ua_dissector:call(buffer, pinfo, tree)</code></pre></div><div id="comment-59098-info" class="comment-info"><span class="comment-age">(27 Jan '17, 00:00)</span> csigueros</div></div></div><div id="comment-tools-58901" class="comment-tools"></div><div class="clear"></div><div id="comment-58901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

