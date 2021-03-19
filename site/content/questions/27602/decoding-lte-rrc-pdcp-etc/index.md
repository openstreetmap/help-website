+++
type = "question"
title = "Decoding LTE (RRC, PDCP, etc)"
description = '''I&#x27;m new to Wireshark and I hope that someone can tell me what I shall do to be able to decode LTE control signaling (headers: RRC, PDCP, etc). I like to use Wireshark to decode the LTE signaling between eNodeB and UE for which I develope the software myself (i.e. I&#x27;m not sending data via the air int...'''
date = "2013-12-01T04:29:00Z"
lastmod = "2013-12-01T04:29:00Z"
weight = 27602
keywords = [ "pdcp", "rrc", "lte" ]
aliases = [ "/questions/27602" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding LTE (RRC, PDCP, etc)](/questions/27602/decoding-lte-rrc-pdcp-etc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27602-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark and I hope that someone can tell me what I shall do to be able to decode LTE control signaling (headers: RRC, PDCP, etc).</p><p>I like to use Wireshark to decode the LTE signaling between eNodeB and UE for which I develope the software myself (i.e. I'm not sending data via the air interface. The signaling from eNodeB to UE is going from one network card to another using two Linux machines). I have added an own header of four bytes before the ASN.1 message (RRC) which is the reason why I can not use the default dissector for RRC in Wireshark. My own header includes information about if the packet is a RACH req/resp or if it is ASN.1 message. I hoped that it was possible to specify in Wireshark in a easy way that there shall be a offset of four bytes before the actual header starts, but that doesn't seem to be the case.</p><p>Here below are my questions. If you haven't got answer to all my questions then I would appreciate if you can answer a few of them.</p><ol><li><p>Do I need to write a filter or dissector to be able to decode the RRC-messages ? I assume that I need a dissector to inform Wireshark to skip the 4 bytes header before the ASN.1 message (RRC).</p></li><li><p>If I write a dissector, can I write a dissector for just my own 4 byte header? Or do I need to rewrite the RRC dissector ? i.e. will the RRC dissector that is included in Wireshark be triggered after the dissector that I write myself ?</p></li><li><p>If I write a dissector, can I just make a shared object file (.so) that I can put in the plugin folder, or do I need to rebuild the whole Wireshark ? I have read somewhere that there exist a Python script that can be used to build dissectors for RRC from the 3GPP spec, which will rebuild Wireshark. I assume that there exist some easier way to include the updated dissector.</p></li><li><p>I've tried the foo dissector example but I don't understand how to use it. After I moved the shared object file (.so) to the plugin folder and restarted Wireshark I don't understand how to use the foo dissector. The foo dissector does not pop up in the "Decode As ..." selector. I can see that "foo" is included in the list of enabled protocols in Wireshark.</p></li><li><p>Will it be possible to decode both RRC and PDCP headers at the same time or will I need separate dissectors for these headers ?</p></li></ol><p>I like to get a detailed instruction for making and installing the dissector, step by step, and I wonder if there exist such an instruction that you can recommend ?</p><p>I run Wireshark 1.6.7 on Ubuntu Linux and I installed Wireshark via aptitude.</p></div><div id="question-tags" class="tags-container tags">pdcp rrc lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '13, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/23d580d121dff4437a951a761ad1150a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="staffan&#39;s gravatar image" /><p>staffan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="staffan has no accepted answers">0%</span></p></div></div><div id="comments-container-27602" class="comments-container"><span id="27650"></span><div id="comment-27650" class="comment"><div id="post-27650-score" class="comment-score"></div><div class="comment-text"><p>It should be possible to write a simple dissector for your custom header then call the appropriate RRC dissector with the actual RRC payload. For an example of doing this, see the function dissect_rrc_lte() in <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-catapult-dct2000.c?revision=53520&amp;view=markup.">http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-catapult-dct2000.c?revision=53520&amp;view=markup.</a> There is no need to re-generate the RRC dissector, just work out which channel/direction and look up the appropriate entry point (assuming you have the necessary information in your header).</p><p>If your frames do include PDCP, then you will need to do something similar to the function dissect_pdcp_lte() in the same file, i.e. allocate &amp; fill in a struct pdcp_lte_info and attach it to the frame then call the PDCP dissector with the remainder.</p><p>In order for your dissector to get called in the first place, you will need to register for whatever can be used to identify your frames (e.g. a UDP or TCP port, ethertype).</p><p>Lastly, 1.6.7 is quite an old version. There is support for the LTE protocols, but there have been lots of improvements since then. There is documentation elsewhere about either building Wireshark yourself for a built-in dissector, or compiling your dissector as a plugin.</p><p>Hope this helps, Martin</p></div><div id="comment-27650-info" class="comment-info"><span class="comment-age">(02 Dec '13, 01:27)</span> MartinM</div></div><span id="28836"></span><div id="comment-28836" class="comment"><div id="post-28836-score" class="comment-score"></div><div class="comment-text"><p>I have written a PDCP dissector according to your description. But I did not succeed to create the struct <code>pdcp_lte_info</code>. The <code>p_get_proto_data()</code> functions needs the <code>proto_pdcp_lte</code> id which is declared in packet-pdcp-lte.c so I have done an external declaration of this variable in my file. I can compile my code but when I start wireshark I get a failure with the "undefined symbol:proto_pdcp_lte" cause. Do I need to activate/load/compile the PDCP-LTE module in wireshark? When I look at Internals-&gt;Supported protocols in wireshark i can find the PDCP-LTE name in the list so it should be included in my wireshark version (1.10.3). Does someone know how to handle the <code>pdcp_lte_info</code> id correctly or how the <code>pdcp_lte_info</code> structure should be created?</p><p>BR</p><p>/Emmanuel</p><p>Here is my dissector code:</p><pre><code>extern int proto_pdcp_lte;

static int
dissect_pdcp (tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    gint offset = 0;
    dissector_handle_t pdcp_lte_handle  = 0;
    pdcp_lte_info *p_pdcp_lte_info;
    unsigned int bearer = 0;

    /* TODO: read the 4 bytes long internal header (the bearer value will be extracted here) */
    offset += 4;

    pdcp_lte_handle = find_dissector(&quot;pdcp-lte&quot;);
    pdcp_tvb = tvb_new_subset_remaining(tvb, offset);

    /* Reuse or allocate struct */
    p_pdcp_lte_info = (pdcp_lte_info *)p_get_proto_data(pinfo-&gt;fd, proto_pdcp_lte);
    if (p_pdcp_lte_info == NULL) {
        p_pdcp_lte_info = se_alloc0(sizeof(struct pdcp_lte_info));
        /* Store info in packet */
        p_add_proto_data(pinfo-&gt;fd, proto_pdcp_lte, p_pdcp_lte_info);
    }

    p_pdcp_lte_info-&gt;ueid = 0;
    p_pdcp_lte_info-&gt;channelType = Channel_DCCH;
    p_pdcp_lte_info-&gt;channelId = bearer;
    p_pdcp_lte_info-&gt;direction = DIRECTION_UPLINK;

    /* Set plane and sequence number length */
    p_pdcp_lte_info-&gt;no_header_pdu = FALSE;
    p_pdcp_lte_info-&gt;plane = SIGNALING_PLANE;
    p_pdcp_lte_info-&gt;seqnum_length = 5;

    call_dissector(pdcp_lte_handle, pdcp_tvb, pinfo, tree);
}</code></pre></div><div id="comment-28836-info" class="comment-info"><span class="comment-age">(13 Jan '14, 03:07)</span> emmanuel</div></div><span id="28837"></span><div id="comment-28837" class="comment"><div id="post-28837-score" class="comment-score"></div><div class="comment-text"><p>Emmanuel,</p><p>If you dissector is built-in, rather than a plugin, this should work, as this is exactly what e.g. packet-rlc-lte.c does. If you are writing a plugin, then I don't think it will work, as you've seen.</p><p>For LTE MAC, we added helper functions that mean you don't need to extern the symbol. This is from packet-mac-lte.h:</p><p>/ <em>Functions to be called from outside this module (e.g. in a plugin, where mac_lte_info isn't available) to get/set per-packet data</em> / WS_DLL_PUBLIC mac_lte_info <em>get_mac_lte_proto_data(packet_info</em> pinfo); WS_DLL_PUBLIC void set_mac_lte_proto_data(packet_info <em>pinfo, mac_lte_info</em> p_mac_lte_info);</p></div><div id="comment-28837-info" class="comment-info"><span class="comment-age">(13 Jan '14, 03:43)</span> MartinM</div></div><span id="28862"></span><div id="comment-28862" class="comment"><div id="post-28862-score" class="comment-score"></div><div class="comment-text"><p>I meant to say in my reply yesterday - if you are writing a plugin and would like similar exported functions added (as was done for MAC), please raise a bug/request on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p></div><div id="comment-28862-info" class="comment-info"><span class="comment-age">(14 Jan '14, 07:19)</span> MartinM</div></div></div><div id="comment-tools-27602" class="comment-tools"></div><div class="clear"></div><div id="comment-27602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

