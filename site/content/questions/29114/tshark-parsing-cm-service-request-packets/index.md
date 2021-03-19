+++
type = "question"
title = "tshark: parsing CM Service Request packets"
description = '''I am using tshark to parse capture files of GSM sessions. For particular CM Service Request packets, I wish to determine and output the CM Service Type. I can currently parse Mobility Management messages by filtering with &quot;gsm_a.dtap_msg_mm_type == 0x24&quot; and get all the CM Service Request packets. H...'''
date = "2014-01-22T15:56:00Z"
lastmod = "2014-01-24T07:40:00Z"
weight = 29114
keywords = [ "tshark", "parsing" ]
aliases = [ "/questions/29114" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: parsing CM Service Request packets](/questions/29114/tshark-parsing-cm-service-request-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29114-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using tshark to parse capture files of GSM sessions. For particular CM Service Request packets, I wish to determine and output the CM Service Type. I can currently parse Mobility Management messages by filtering with "gsm_a.dtap_msg_mm_type == 0x24" and get all the CM Service Request packets. However, I have not been able to figure out how to output the specific CM Service type for such packets.</p><p>I have searched through the online Display Filter Reference, but I have found nothing that can extract the CM Service type (I am using "-T fields -e gsm_a.dtap_msg_mm_type -e etc" to output specific data for the packet).</p><p>Is is possible to extract that info with tshark? Any suggestions are appreciated.</p><p>Thanks,</p><p>John</p></div><div id="question-tags" class="tags-container tags">tshark parsing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/8339fd0996779002cffd77d4b084a745?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jotten&#39;s gravatar image" /><p>jotten<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jotten has no accepted answers">0%</span></p></div></div><div id="comments-container-29114" class="comments-container"></div><div id="comment-tools-29114" class="comment-tools"></div><div class="clear"></div><div id="comment-29114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29140"></span>

<div id="answer-container-29140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29140-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I can see in the code, the 'service type' is only added as text to the tree, so there is no separate field for it.</p><p>File: <a href="http://anonsvn.wireshark.org/wireshark/trunk-1.10/epan/dissectors/packet-gsm_a_dtap.c">packet-gsm_a_dtap.c</a></p><pre><code>    subtree = proto_item_add_subtree(item, ett_gsm_dtap_elem[DE_CM_SRVC_TYPE]);

    switch (oct &amp; 0x0f)
    {
    case 0x01: str = &quot;Mobile originating call establishment or packet mode connection establishment&quot;; break;
    case 0x02: str = &quot;Emergency call establishment&quot;; break;
    case 0x04: str = &quot;Short message service&quot;; break;
    case 0x08: str = &quot;Supplementary service activation&quot;; break;
    case 0x09: str = &quot;Voice group call establishment&quot;; break;
    case 0x0a: str = &quot;Voice broadcast call establishment&quot;; break;
    case 0x0b: str = &quot;Location Services&quot;; break;
    default:
        str = &quot;Reserved&quot;;
        break;
    }

    other_decode_bitfield_value(a_bigbuf, oct, 0x0f, 8);
    proto_tree_add_text(subtree,
        tvb, curr_offset, 1,
        &quot;%s = Service Type: (%u) %s&quot;,
        a_bigbuf,
        oct &amp; 0x0f,
        str);</code></pre><p>So, if you need to get the service type from tshark output you can</p><ul><li>file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and hope one of the developers find some time to add that feature (if possible)</li><li>let tshark print PDML and parse the output yourself (with a script) to get those values:<br />
1.) <code>tshark -nr input.pcap -Y "gsm_a.dtap_msg_mm_type == 0x24" -T pdml | your-script.pl</code><br />
Not easy, but currently the only option I see.</li></ul><p><strong>++ UPDATE ++</strong><br />
</p><p>as mentioned by @Anders in the comment, that change has already been implemented in the latest 1.11.x build.</p><p>@jotten: if you download the lastest 1.11.x build, you should be able to use <code>-e gsm_a.dtap.service_type</code> in tshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '14, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '14, 08:21</p></div></div><div id="comments-container-29140" class="comments-container"><span id="29143"></span><div id="comment-29143" class="comment"><div id="post-29143-score" class="comment-score"></div><div class="comment-text"><p>Looks like that's implemented in trunk allready, so if on windows downloading a buildboot build is an option.</p></div><div id="comment-29143-info" class="comment-info"><span class="comment-age">(24 Jan '14, 08:09)</span> Anders ♦</div></div><span id="29144"></span><div id="comment-29144" class="comment"><div id="post-29144-score" class="comment-score"></div><div class="comment-text"><p>:-)) You are right. I should have checked <code>trunk</code>. Thanks for the hint!</p><blockquote><p><a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-gsm_a_dtap.c">http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-gsm_a_dtap.c</a></p></blockquote><pre><code>      { &amp;hf_gsm_a_dtap_service_type, { &quot;Service Type&quot;, &quot;gsm_a.dtap.service_type&quot;, FT_UINT8, BASE_DEC, VALS(gsm_a_dtap_service_type_vals), 0x0F, NULL, HFILL }},</code></pre><p>@jotten: if you download the lastest 1.11.x build, you should be able to use <code>-e gsm_a.dtap.service_type</code> in tshark.</p></div><div id="comment-29144-info" class="comment-info"><span class="comment-age">(24 Jan '14, 08:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29140" class="comment-tools"></div><div class="clear"></div><div id="comment-29140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

