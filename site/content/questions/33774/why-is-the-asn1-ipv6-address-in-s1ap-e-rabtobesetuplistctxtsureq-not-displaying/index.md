+++
type = "question"
title = "Why is the ASN.1 IPv6 address in s1ap E-RABToBeSetupListCtxtSUReq not displaying?"
description = '''I&#x27;m using wireshark to decode the s1ap InitialContextSetupRequest but it doesn&#x27;t seem to display the IPv6 address of the transportLayerAddress. When decoding IPv4 it displays it fine but not when IPv4 and IPv6 are included. Is this a decodeAs issue or encoding error? Item 3: id-E-RABToBeSetupListCtx...'''
date = "2014-06-13T08:26:00Z"
lastmod = "2014-06-13T08:26:00Z"
weight = 33774
keywords = [ "asn.1", "36.413", "s1ap" ]
aliases = [ "/questions/33774" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the ASN.1 IPv6 address in s1ap E-RABToBeSetupListCtxtSUReq not displaying?](/questions/33774/why-is-the-asn1-ipv6-address-in-s1ap-e-rabtobesetuplistctxtsureq-not-displaying)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33774-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using wireshark to decode the s1ap InitialContextSetupRequest but it doesn't seem to display the IPv6 address of the transportLayerAddress. When decoding IPv4 it displays it fine but not when IPv4 and IPv6 are included. Is this a decodeAs issue or encoding error?</p><pre><code>Item 3: id-E-RABToBeSetupListCtxtSUReq
                            ProtocolIE-Field
                                id: id-E-RABToBeSetupListCtxtSUReq (24)
                                criticality: reject (0)
                                value
                                    E-RABToBeSetupListCtxtSUReq: 1 item
                                        Item 0: id-E-RABToBeSetupItemCtxtSUReq
                                            ProtocolIE-SingleContainer
                                                id: id-E-RABToBeSetupItemCtxtSUReq (52)
                                                criticality: reject (0)
                                                value
                                                    E-RABToBeSetupItemCtxtSUReq
                                                        e-RAB-ID: 5
                                                        e-RABlevelQoSParameters
                                                        0... .... Extension Present Bit: False
                                                        transportLayerAddress: 9ba562c22606ae00204113000000000000000002 [bit length 160]
                                                        gTP-TEID: 83acc06b
                                                        nAS-PDU: 278541ea3402074202540620130181f20400755228c10108...
                                                        Non-Access-Stratum (NAS)PDU</code></pre><p>Wireshark version:</p><pre><code>Version 1.8.3 (SVN Rev Unknown from unknown)

Copyright 1998-2012 Gerald Combs &lt;[email protected]&gt; and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GTK+ 2.18.9, with Cairo 1.8.8, with Pango 1.28.1, with GLib 2.22.5, with libpcap, with libz 1.2.3, without POSIX capabilities, without SMI, without c-ares, without ADNS, without Lua, without Python, with GnuTLS
2.8.5, with Gcrypt 1.4.5, with MIT Kerberos, without GeoIP, without PortAudio, with AirPcap.

Running on Linux
2.6.32-279.el6.x86_64, with locale en_US.UTF-8, with libpcap version
1.0.0, with libz 1.2.3, GnuTLS 2.8.5, Gcrypt 1.4.5, without AirPcap.

Built using gcc 4.4.6 20110731 (Red Hat 4.4.6-3).</code></pre></div><div id="question-tags" class="tags-container tags">asn.1 36.413 s1ap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '14, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/99d800aebc5264c111925ece4ef612fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="run4life&#39;s gravatar image" /><p>run4life<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="run4life has no accepted answers">0%</span></p></div></div><div id="comments-container-33774" class="comments-container"><span id="33795"></span><div id="comment-33795" class="comment"><div id="post-33795-score" class="comment-score"></div><div class="comment-text"><p>Could you upload the file and post a link? That way I can at least check the newer versions, as 1.8.3 has been out for quite some time now. I suggest trying 1.10.8 if you haven't already.</p><p><a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a></p><p>Also for reference, this looks like the relevant code in 1.10.8, in packet-s1ap.c:</p><pre><code>    dissect_s1ap_TransportLayerAddress(tvbuff_t *tvb _U_, int offset _U_, asn1_ctx_t *actx _U_, proto_tree *tree _U_, int hf_index _U_) {
#line 250 &quot;../../asn1/s1ap/s1ap.cnf&quot;
  tvbuff_t *parameter_tvb=NULL;
  proto_tree *subtree;
  gint tvb_len;

  offset = dissect_per_bit_string(tvb, offset, actx, tree, hf_index,
                                     1, 160, TRUE, ¶meter_tvb);

  if (!parameter_tvb)
    return offset;

    /* Get the length */
    tvb_len = tvb_length(parameter_tvb);
    subtree = proto_item_add_subtree(actx-&gt;created_item, ett_s1ap_TransportLayerAddress);
    if (tvb_len==4){
        /* IPv4 */
         proto_tree_add_item(subtree, hf_s1ap_transportLayerAddressIPv4, parameter_tvb, 0, tvb_len, ENC_BIG_ENDIAN);
    }
    if (tvb_len==16){
        /* IPv6 */
         proto_tree_add_item(subtree, hf_s1ap_transportLayerAddressIPv6, parameter_tvb, 0, tvb_len, ENC_NA);
    }

  return offset;
}</code></pre></div><div id="comment-33795-info" class="comment-info"><span class="comment-age">(13 Jun '14, 17:22)</span> Quadratic</div></div><span id="33845"></span><div id="comment-33845" class="comment"><div id="post-33845-score" class="comment-score"></div><div class="comment-text"><p>The current code supports an IPv4 address, an IPv6 address, but not an Ipv4v6 one. Please fill a bug report on <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a> with your sample pcap attached.</p></div><div id="comment-33845-info" class="comment-info"><span class="comment-age">(15 Jun '14, 13:52)</span> Pascal Quantin</div></div></div><div id="comment-tools-33774" class="comment-tools"></div><div class="clear"></div><div id="comment-33774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

