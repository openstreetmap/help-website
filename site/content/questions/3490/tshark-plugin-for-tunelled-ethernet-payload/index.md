+++
type = "question"
title = "tshark plugin for tunelled ethernet payload"
description = '''Hello! I am writing a tshark plug-in for a proprietary protocol with ethernet type 0x8787. The plug-in is supposed to dissect frames coming onto an ethernet interface with the below format:  Dst Mac | Src Mac | type | Custom Hdr &amp;lt;12 bytes&amp;gt; | Dst Mac | Src Mac | type | &amp;lt; ethernet body &amp;gt; |...'''
date = "2011-04-13T16:32:00Z"
lastmod = "2011-04-16T08:49:00Z"
weight = 3490
keywords = [ "ethernet", "dissector", "tshark", "plugin" ]
aliases = [ "/questions/3490" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark plugin for tunelled ethernet payload](/questions/3490/tshark-plugin-for-tunelled-ethernet-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I am writing a tshark plug-in for a proprietary protocol with ethernet type 0x8787. The plug-in is supposed to dissect frames coming onto an ethernet interface with the below format:</p><hr /><h2 id="dst-mac-src-mac-type-custom-hdr-12-bytes-dst-mac-src-mac-type-ethernet-body">Dst Mac | Src Mac | type | Custom Hdr &lt;12 bytes&gt; | Dst Mac | Src Mac | type | &lt; ethernet body &gt; |</h2><p>I am able to dissect frames until the end of the custom header. However, to decode the ethernet frame &amp; its payload that follows the custom header (like an ARP packet / IP packet etc), I tried calling the ethernet dissector (call_dissector), but for some reason I see only raw hex data. can someone please help me find where I am going wrong &amp; how to get the real ethernet frame dissected? BTW - The wireshark library that I use is 1.4.3</p><p>Here is my code: / <em>packet-test.c</em> /</p><h1 id="include-stdio.h">include &lt;stdio.h&gt;</h1><h1 id="include-stdlib.h">include &lt;stdlib.h&gt;</h1><h1 id="include-ctype.h">include &lt;ctype.h&gt;</h1><h1 id="include-time.h">include &lt;time.h&gt;</h1><h1 id="include-string.h">include &lt;string.h&gt;</h1><h1 id="include-glib.h">include &lt;glib.h&gt;</h1><h1 id="include-epan-packet.h">include &lt;epan packet.h=""&gt;</h1><h1 id="include-epan-prefs.h">include &lt;epan prefs.h=""&gt;</h1><h1 id="include-epan-emem.h">include &lt;epan emem.h=""&gt;</h1><p>void proto_reg_handoff_test_131_data(void);</p><p>/ <em>Handles for the test protocols</em> /</p><p>static int proto_131_data = -1;</p><p>static int hf_131_data_ftag = -1; static int hf_131_data_flags = -1; static int hf_131_data_client = -1; static int hf_131_data_type = -1;</p><p>static int hf_131_comm_len = -1; static int ett_131_data = -1; static int ett_131_comm = -1;</p><p>static dissector_handle_t ip_handle; static dissector_handle_t data_handle; static dissector_handle_t eth_handle; static dissector_handle_t test_comm_handle; static dissector_handle_t wlan_handle;</p><p>static void dissect_test_131_data(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree <em>tree) { proto_tree</em> ti,<em>test_tree; char clientmac[8]; tvbuff_t</em> next_tvb = 0;</p><pre><code>tvb_memcpy(tvb, clientmac, 4, 6);

if (check_col(pinfo-&gt;cinfo, COL_PROTOCOL))
{
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;T EP-CP Data&quot;);
}

/* Set the info column */
if (check_col(pinfo-&gt;cinfo, COL_INFO))
{
    col_add_str(pinfo-&gt;cinfo, COL_INFO, &quot;Test EP-CP L2 Tunneled Data&quot;);
}

if (tree)
{
    ti = proto_tree_add_item(tree, proto_131_data, tvb, 0, 12, FALSE);
    test_tree = proto_item_add_subtree(ti, ett_131_data);
    proto_tree_add_item(test_tree, hf_131_data_ftag, tvb, 0, 2, FALSE);
    proto_tree_add_item(test_tree, hf_131_data_flags, tvb, 2, 2, FALSE);
    proto_tree_add_ether(test_tree, hf_131_data_client, tvb, 4, 6, clientmac);
    proto_tree_add_item(test_tree, hf_131_data_type, tvb, 10, 2, FALSE);
}

call_dissector(eth_handle, tvb, pinfo, tree);</code></pre><p>}</p><p>void proto_register_test_131_data(void) { / <em>Register header fields</em> / static hf_register_info hf[] = { { &amp;hf_131_data_ftag, { "Ftag", "test.131.ftag", FT_UINT16, BASE_DEC, NULL, 0x0, "The protocol version being used", HFILL }}, { &amp;hf_131_data_flags, { "Flags", "test.131.flags", FT_UINT16, BASE_HEX, NULL, 0x0, "Miscellaneous flags", HFILL }}, { &amp;hf_131_data_client, { "C#", "test.131.clientmac", FT_ETHER, BASE_NONE, NULL, 0x0, "C# Address", HFILL }}, { &amp;hf_131_data_type, { "Type", "test.131.type", FT_UINT16, BASE_HEX, NULL, 0x0, "Tunneled Ethernet Type", HFILL }},</p><pre><code>};

static gint *ett[] =
{
    &amp;ett_131_data,
};

proto_131_data = proto_register_protocol(&quot;Test EP-CP L2 Tunnel&quot;,&quot;T EP-CP Data&quot;,&quot;test_131_data&quot;);

proto_register_field_array(proto_131_data, hf, array_length(hf));
proto_register_subtree_array(ett, array_length(ett));

register_dissector(&quot;test_131_data&quot;, dissect_test_131_data, proto_131_data);
ip_handle   = find_dissector(&quot;ip&quot;);
data_handle = find_dissector(&quot;data&quot;);
eth_handle  = find_dissector(&quot;eth&quot;);
wlan_handle = find_dissector(&quot;wlan&quot;);</code></pre><p>}</p><p>void proto_reg_handoff_test_131_data(void) { static int test_initialized = FALSE; static dissector_handle_t test_handle;</p><pre><code>if (!test_initialized)
{
    test_handle = create_dissector_handle(dissect_test_131_data, proto_131_data);  
    dissector_add(&quot;ethertype&quot;, 0x8787, test_handle);
    test_handle = find_dissector(&quot;test_131_data&quot;);
    test_initialized = TRUE;
}</code></pre><p>}</p><p>-- Thanks /R</p></div><div id="question-tags" class="tags-container tags">ethernet dissector tshark plugin</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '11, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/c2f093aae48ae803c3409e8eb2b2eb39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramesh&#39;s gravatar image" /><p>Ramesh<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramesh has no accepted answers">0%</span></p></div></div><div id="comments-container-3490" class="comments-container"></div><div id="comment-tools-3490" class="comment-tools"></div><div class="clear"></div><div id="comment-3490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3533"></span>

<div id="answer-container-3533" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3533-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For one thing, before calling, "<code>call_dissector(eth_handle, tvb, pinfo, tree);</code>", you need to pass it a new <code>tvb</code> that strips off the fields before it that are not applicable to Ethernet. This is typically done using something like,</p><pre><code>next_tvb = tvb_new_subset_remaining(tvb, 12);
call_dissector(eth_handle, next_tvb, pinfo, tree);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '11, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3533" class="comments-container"></div><div id="comment-tools-3533" class="comment-tools"></div><div class="clear"></div><div id="comment-3533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

