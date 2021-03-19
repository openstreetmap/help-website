+++
type = "question"
title = "RLC-LTE support for DCCH"
description = '''This question is probably directed at Mr MartinM, hopefully you&#x27;re reading :) I have occasion to need to decode UL and DL DCCH messages, that arrive in a binary format with a custom indication of whether it is DL-DCCH or UL-DCCH. For example, I receive a binary message containing &#x27;20100500064f6e0180...'''
date = "2017-01-22T20:08:00Z"
lastmod = "2017-01-22T23:07:00Z"
weight = 58959
keywords = [ "rlc-lte", "dcch", "lte" ]
aliases = [ "/questions/58959" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RLC-LTE support for DCCH](/questions/58959/rlc-lte-support-for-dcch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58959-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This question is probably directed at Mr MartinM, hopefully you're reading :)</p><p>I have occasion to need to decode UL and DL DCCH messages, that arrive in a binary format with a custom indication of whether it is DL-DCCH or UL-DCCH. For example, I receive a binary message containing '20100500064f6e018060' with an indication that this is a DL-DCCH-MSG (rrcConnectionReconfiguration measConfig in this case).</p><p>For the other message types (DL/UL-CCCH, PCCH) that I receive, the rlc-lte decoder is doing its thing nicely in TM mode without any drama after packing the UDP header on it etc.</p><p>After having a look at the code, there seems to be no explicit handling of DCCH as its own type which would allow <code>dissect_rlc_lte_tm</code> to setup <code>protocol_handle = find_dissector("lte_rrc.ul_dcch")</code> (or <code>dl_dcch</code>).</p><p>This is easy enough to patch with a new <code>CHANNEL_TYPE_DCCH</code> defined and it works fine and decodes my DCCH packets after doing so.</p><p>My question is whether there was a reason this isn't currently implemented (or could not be implemented) - and if not, I am happy to submit a fix and/or send you a diff (so that I don't need to patch my colleagues Wiresharks to decode just these DCCH packets).</p><p>thanks for your work to date on the decoder,</p><p>regards, -jeff</p></div><div id="question-tags" class="tags-container tags">rlc-lte dcch lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '17, 20:08</strong></p><img src="https://secure.gravatar.com/avatar/cf6e2ca7fb8d6b1e75eb0bc5601d0551?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffG&#39;s gravatar image" /><p>JeffG<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffG has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '17, 20:20</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-58959" class="comments-container"></div><div id="comment-tools-58959" class="comment-tools"></div><div class="clear"></div><div id="comment-58959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58961"></span>

<div id="answer-container-58961" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58961-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will not find a call to UL/DL LTE RRC dissector in RLC dissector because in between you have PDCP dissector (for the 1 byte header and 4 bytes footer).</p><p>What you are dumping is not a RLC message, but you are using the fact that CCCH messages are sent in transparent mode while DCCH messages are not. So a patch adding this would be rejected. If you absolutely want to use the RLC framing protocol, prepend a 1 byte header for the PDCP SN and 4 bytes header for the MAC and configure RLC dissector to call PDCP dissector. PDCP dissector can then be configured to call RRC dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '17, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58961" class="comments-container"><span id="58967"></span><div id="comment-58967" class="comment"><div id="post-58967-score" class="comment-score"></div><div class="comment-text"><p>hi Pascal,</p><p>Thanks for your comments, I am mostly vague on the finer details of the LTE MAC layer, so I do appreciate the clarifications. For the problem of DCCH, I think your comments have given me the missing link. Any attempt to shove this DCCH payload into the rlc-lte dissector needs to be handled via AM not TM, with a RLC channel type of SRB. I see afterlooking through the <code>dissect_rlc_lte_am</code> code path that this should find its way to the pdcp dissector in <code>show_PDU_in_tree</code>.</p><p>regards jeff</p></div><div id="comment-58967-info" class="comment-info"><span class="comment-age">(23 Jan '17, 02:20)</span> JeffG</div></div><span id="58968"></span><div id="comment-58968" class="comment"><div id="post-58968-score" class="comment-score"></div><div class="comment-text"><p>Yes DCCH channels are always using RLC AM mode. Which means that you must also add a fake RLC header (which I forgot to add in my first message) but hopefully this is not complex. With all this plumbing, you will be able to use the RLC UDP framing protocol. You could also use directly the PDCP UDP framing protocol, or even better call directly the RRC dissector using whatever is convenient for you (Lua simple UDP dissector, etc...)</p></div><div id="comment-58968-info" class="comment-info"><span class="comment-age">(23 Jan '17, 02:43)</span> Pascal Quantin</div></div><span id="58998"></span><div id="comment-58998" class="comment"><div id="post-58998-score" class="comment-score"></div><div class="comment-text"><p>hi Pascal, Thanks - got it working with a fake RLC and PDCP headers, together with some seq num per rnti to keep the <code>expert</code> happy.</p><p>A followup question for you if I may. The next issue I have hit is that the following code in the pdcp dissector is causing all DCCH packets post <code>securityModeCommand</code> to be presumed encrypted and thus not passed to the rrc dissector - but my payload is intercepted pre/post-encryption, hence I would like to get past the &amp;&amp; section of this if:</p><pre><code>        /* RRC data is all but last 4 bytes.
           Call lte-rrc dissector (according to direction and channel type) if we have valid data */
        if ((global_pdcp_dissect_signalling_plane_as_rrc) &amp;&amp;
            ((pdu_security == NULL) || (pdu_security-&gt;ciphering == eea0) || payload_deciphered || !pdu_security-&gt;seen_next_ul_pdu)) {
            /* Get appropriate dissector handle */
            dissector_handle_t rrc_handle = lookup_rrc_dissector_handle(p_pdcp_info);</code></pre><p>In my case, pdu_security is non NULL and is (correctly) showing EEA2/EIA2. This seems unable to be skipped via any preference, do you have any suggestion on how to skip this (other than a new preference or Lua decoder)? The only thing I can think of is to fake out the securityMode packet and overwrite it with EEA0/EIA0.</p><p>Whilst I appreciate my situation is unique (I don't have to deal with data packets, only signalling, and nothing is encrypted), I am trying to avoid resorting to anything custom so that the result is portable where ever wireshark/tshark is installed.</p><p>thanks -jeff</p></div><div id="comment-58998-info" class="comment-info"><span class="comment-age">(24 Jan '17, 00:03)</span> JeffG</div></div><span id="59006"></span><div id="comment-59006" class="comment"><div id="post-59006-score" class="comment-score"></div><div class="comment-text"><p>You are right it cannot be skipped. The best would be to avoid the RLC/PDCP encapsulation anyway.</p><p>Do you need to have a real time display of the RRC messages, or is it some offline post decoding? On my side, I'm using the Exported PDU format <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/exported_pdu.h;h=8a3beb57c8f62ce26b801a7c6b987914bfab4508;hb=HEAD">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/exported_pdu.h;h=8a3beb57c8f62ce26b801a7c6b987914bfab4508;hb=HEAD</a> with a data linktype set to 252 in the pcap/pcapng header. But it might not fit your needs.</p></div><div id="comment-59006-info" class="comment-info"><span class="comment-age">(24 Jan '17, 02:26)</span> Pascal Quantin</div></div><span id="59038"></span><div id="comment-59038" class="comment"><div id="post-59038-score" class="comment-score"></div><div class="comment-text"><p>thanks for the pointer, I was not aware of exported_pdu, let me see if I can make do what I need. This is all offline post decoding for now, but it could become realtime in the future.</p></div><div id="comment-59038-info" class="comment-info"><span class="comment-age">(24 Jan '17, 19:17)</span> JeffG</div></div></div><div id="comment-tools-58961" class="comment-tools"></div><div class="clear"></div><div id="comment-58961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

