+++
type = "question"
title = "New in-built dissector not visible"
description = '''With 2.3.0 version, I am creating a new in-built dissector as listed below. I have updated the epan/dissectors/CMakeLists and added my file that contains the dissector, packet-probe.c Done cmake and msbuild and build my wireshark version. However I don&#x27;t see my dissector when I run my wireshark vers...'''
date = "2017-03-16T09:22:00Z"
lastmod = "2017-03-16T09:22:00Z"
weight = 60112
keywords = [ "new", "dissector" ]
aliases = [ "/questions/60112" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [New in-built dissector not visible](/questions/60112/new-in-built-dissector-not-visible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60112-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With 2.3.0 version, I am creating a new in-built dissector as listed below. I have updated the epan/dissectors/CMakeLists and added my file that contains the dissector, packet-probe.c</p><p>Done cmake and msbuild and build my wireshark version. However I don't see my dissector when I run my wireshark version.</p><p>Could you please let me know if there are any othe makefile or registry files that I need to update?</p><pre><code>proto_register_pb(void)
{
...
  proto_probe = proto_register_protocol(&quot;Probe&quot;, &quot;PROBE&quot;, &quot;probe&quot;);
  proto_register_field_array(proto_probe, hf, array_length(hf));
  proto_register_subtree_array(ett, array_length(ett));
}

proto_reg_handoff_probe(void)
{
  dissector_handle_t probe_handle;
  ip_handle = find_dissector(&quot;ip&quot;);
  rsvp_handle = find_dissector(&quot;rsvp&quot;);
  probe_handle = create_dissector_handle(dissect_probe, proto_probe); 
  dissector_add_uint(&quot;udp.port&quot;, UDP_PORT_PROBE, probe_handle);
}

static void
dissect_probe(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;PROBE&quot;);
    if (tree) {
    ...
    }
...
}</code></pre><p>Regards</p><p>Sanj</p></div><div id="question-tags" class="tags-container tags">new dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '17, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/f9240775213c2976f22cafb258a453dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanj123&#39;s gravatar image" /><p>Sanj123<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanj123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Mar '17, 09:38</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60112" class="comments-container"><span id="60113"></span><div id="comment-60113" class="comment"><div id="post-60113-score" class="comment-score"></div><div class="comment-text"><p>Does your protocol show up under the menu item Analyze -&gt; Enabled Protocols?</p></div><div id="comment-60113-info" class="comment-info"><span class="comment-age">(16 Mar '17, 09:39)</span> grahamb ♦</div></div><span id="60115"></span><div id="comment-60115" class="comment"><div id="post-60115-score" class="comment-score"></div><div class="comment-text"><p>No, I am not seeing my "probe" protocol under the Analyze-&gt;Enable Protocols menu.</p></div><div id="comment-60115-info" class="comment-info"><span class="comment-age">(16 Mar '17, 09:53)</span> Sanj123</div></div><span id="60116"></span><div id="comment-60116" class="comment"><div id="post-60116-score" class="comment-score"></div><div class="comment-text"><p>If your code is in the order shown in your excerpt, i.e. <code>dissect_probe()</code> defined after it's used in <code>proto_reg_handoff_probe()</code> then I suspect it isn't being compiled which would point to a CMake problem.</p><p>Presumably you added your dissector to the <code>DISSECTOR_SRC</code> item in epan/dissectors/CMakeLists.txt?</p><p>Try opening the solution in Visual Studio and checking if your source file is shown in the Solution Explorer under <code>Libs\epan\dissectors\dissectors\dissectors</code>.</p></div><div id="comment-60116-info" class="comment-info"><span class="comment-age">(16 Mar '17, 10:05)</span> grahamb ♦</div></div><span id="60117"></span><div id="comment-60117" class="comment"><div id="post-60117-score" class="comment-score"></div><div class="comment-text"><p>dissect_probe() is the 1st and proto_reg_handoff_probe() is the last call in the file. Sorry about the order listed in the example.</p><p>I had added the packet-probe.c file.c to set(DISSECTOR_SRC...) I am trying to figure out how to look up the file in Solution Explorer.</p></div><div id="comment-60117-info" class="comment-info"><span class="comment-age">(16 Mar '17, 10:28)</span> Sanj123</div></div><span id="60118"></span><div id="comment-60118" class="comment"><div id="post-60118-score" class="comment-score"></div><div class="comment-text"><p>If the order is the correct way around it may well be compiled.</p><p>In your build directory do you see <code>packet-probe.obj</code> under <code>epan\dissectors\dissectors.dir\RelWithDebInfo</code>?</p></div><div id="comment-60118-info" class="comment-info"><span class="comment-age">(16 Mar '17, 10:48)</span> grahamb ♦</div></div><span id="60119"></span><div id="comment-60119" class="comment not_top_scorer"><div id="post-60119-score" class="comment-score"></div><div class="comment-text"><p>Yes, I do see the packet-prob.obj under Development/wsbuild64\epan\dissectors\dissectors.dir\RelWithDebInfo</p></div><div id="comment-60119-info" class="comment-info"><span class="comment-age">(16 Mar '17, 10:55)</span> Sanj123</div></div><span id="60120"></span><div id="comment-60120" class="comment not_top_scorer"><div id="post-60120-score" class="comment-score"></div><div class="comment-text"><p>It's compiled then.</p><p>Are you certain you're running the Wireshark you've just built, i.e. from your build directory <code>run\RelWithDebInfo\Wireshark.exe</code>?</p></div><div id="comment-60120-info" class="comment-info"><span class="comment-age">(16 Mar '17, 11:31)</span> grahamb ♦</div></div><span id="60121"></span><div id="comment-60121" class="comment not_top_scorer"><div id="post-60121-score" class="comment-score"></div><div class="comment-text"><p>Yes, I have checked the timestamp, I am running the one I built with the probe.</p></div><div id="comment-60121-info" class="comment-info"><span class="comment-age">(16 Mar '17, 11:53)</span> Sanj123</div></div><span id="60126"></span><div id="comment-60126" class="comment not_top_scorer"><div id="post-60126-score" class="comment-score"></div><div class="comment-text"><p>The .obj was being created but the executable did not show the new protocol. I deleted the RelWithDebInfo directory and rebuild. Now I can correctly see my protocol. Thanks for your help!!</p></div><div id="comment-60126-info" class="comment-info"><span class="comment-age">(16 Mar '17, 13:25)</span> Sanj123</div></div><span id="60127"></span><div id="comment-60127" class="comment not_top_scorer"><div id="post-60127-score" class="comment-score"></div><div class="comment-text"><p>If you open the generated file register.c is your dissectors register function included,if not delete the file to have it regenerated.</p></div><div id="comment-60127-info" class="comment-info"><span class="comment-age">(16 Mar '17, 13:26)</span> Anders ♦</div></div><span id="60152"></span><div id="comment-60152" class="comment not_top_scorer"><div id="post-60152-score" class="comment-score"></div><div class="comment-text"><p>Thanks both!!</p></div><div id="comment-60152-info" class="comment-info"><span class="comment-age">(17 Mar '17, 07:37)</span> Sanj123</div></div></div><div id="comment-tools-60112" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-60112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

