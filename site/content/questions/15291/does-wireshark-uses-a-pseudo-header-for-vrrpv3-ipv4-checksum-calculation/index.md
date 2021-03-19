+++
type = "question"
title = "Does Wireshark uses a pseudo-header for VRRPv3 IPv4 checksum calculation?"
description = '''According to draft-ietf-vrrp-ipv6-spec-08 (VRRPv3) IPv4 is defined in RFC3768 (VRRPv2).  &quot;This protocol is intended for use with IPv6 routers only. VRRP for IPv4 is defined in VRRP-V4.&quot; , sentence from draft-ietf-vrrp-ipv6-spec-08, section 1.1 - Scope It appears that Wireshark uses the pseudo-header...'''
date = "2012-10-26T03:44:00Z"
lastmod = "2012-11-06T02:54:00Z"
weight = 15291
keywords = [ "checksum", "vrrp", "pseudo-header" ]
aliases = [ "/questions/15291" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Does Wireshark uses a pseudo-header for VRRPv3 IPv4 checksum calculation?](/questions/15291/does-wireshark-uses-a-pseudo-header-for-vrrpv3-ipv4-checksum-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15291-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to <strong>draft-ietf-vrrp-ipv6-spec-08</strong> (VRRPv3) IPv4 is defined in <strong>RFC3768</strong> (VRRPv2).</p><p><em>"This protocol is intended for use with IPv6 routers only. VRRP for IPv4 is defined in <a href="http://tools.ietf.org/html/draft-ietf-vrrp-ipv6-spec-08#ref-VRRP-V4">VRRP-V4</a>."</em> , sentence from <strong>draft-ietf-vrrp-ipv6-spec-08</strong>, section 1.1 - Scope</p><p>It appears that Wireshark uses the pseudo-header in the checksum calculation for IPv4 and for IPv6. For me the pseudo-header should be used for IPv6 as defined in the <strong>draft</strong> but should not be used in IPv4 since it doesn't appear in the checksum calculation defined in the section 5.3.8. of <strong>RFC3768</strong>.</p><p>Could you confirm that the Wireshark's checksum calculation for VRRPv3 uses a pseudo-header even for IPv4? It is intentional or a bug?</p></div><div id="question-tags" class="tags-container tags">checksum vrrp pseudo-header</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '12, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/248b88ae837ada13a907a17f7565c087?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToinoBiclas&#39;s gravatar image" /><p>ToinoBiclas<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToinoBiclas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '12, 03:45</p></div></div><div id="comments-container-15291" class="comments-container"></div><div id="comment-tools-15291" class="comment-tools"></div><div class="clear"></div><div id="comment-15291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15573"></span>

<div id="answer-container-15573" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15573-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://tools.ietf.org/html/rfc5798">RFC5798</a> defines VRRPv3 for IPv4 <strong>and</strong> IPv6. There are header field related to the IP protocol version and those that are independent of the IP protocol version.</p><p>The checksum is independent of the IP protocol version. See</p><pre><code>5.2.8. Checksum
   The checksum field is used to detect data corruption in the VRRP
   message.

   The checksum is the 16-bit one&#39;s complement of the one&#39;s complement
   sum of the entire VRRP message starting with the version field and a
   &quot;pseudo-header&quot; as defined in Section 8.1 of [RFC2460].  The next
   header field in the &quot;pseudo-header&quot; should be set to 112 (decimal)
   for VRRP.  For computing the checksum, the checksum field is set to
   zero.  See RFC1071 for more detail [RFC1071].</code></pre><p>So the checksum calculation of Wireshark is correct, as it only adds the pseudo header for VRRPv3, regardless of the IP protocol (however, see below!).</p><p><strong>packet-vrrp.c</strong>:</p><p><code>         cksum = tvb_get_ntohs(tvb, offset);         vrrp_len = (gint)tvb_reported_length(tvb);         if (!pinfo-&gt;fragmented &amp;&amp; (gint)tvb_length(tvb) &gt;= vrrp_len) {             / The packet isn't part of a fragmented datagram                and isn't truncated, so we can checksum it. /             switch(hi_nibble(ver_type)) {             case 3:                 / Set up the fields of the pseudo-header. /                 cksum_vec[0].ptr = pinfo-&gt;src.data;                 cksum_vec[0].len = pinfo-&gt;src.len;                 cksum_vec1.ptr = pinfo-&gt;dst.data;                 cksum_vec1.len = pinfo-&gt;dst.len;                 cksum_vec2.ptr = (const guint8 *)&amp;phdr;                 phdr[0] = g_htonl(vrrp_len);                 phdr1 = g_htonl(IP_PROTO_VRRP);                 cksum_vec2.len = 8;                 cksum_vec3.ptr = tvb_get_ptr(tvb, 0, vrrp_len);                 cksum_vec3.len = vrrp_len;                 computed_cksum = in_cksum(cksum_vec, 4);                 break;             case 2:             default:                 cksum_vec[0].ptr = tvb_get_ptr(tvb, 0, vrrp_len);                 cksum_vec[0].len = vrrp_len;                 computed_cksum = in_cksum(&amp;cksum_vec[0], 1);                 break;             }</code></p><p><strong>However</strong>, <a href="http://tools.ietf.org/html/rfc5798">RFC5798</a> is a bit unclear, as it refers to the IPv6 pseudo header in <a href="http://tools.ietf.org/html/rfc2460#section-8.1">RFC2460</a> without explanation how to apply that to IPv4 for the checksum calculation.</p><p>There have been discussions about this, apparently without a clear result !?!</p><blockquote><p><code>http://www.ietf.org/mail-archive/web/vrrp/current/msg01466.html</code><br />
<code>http://www.ietf.org/mail-archive/web/vrrp/current/msg01469.html</code><br />
</p></blockquote><p>So, this is again one of those RFC interpretation versus interoperability issues and I guess different implementations calculate the checksum differently.</p><p>There is also a bug report for this:</p><blockquote><p><code>https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5008</code><br />
</p></blockquote><p>BTW: If you want clarification, you can contact the author of the RFC. You'll find his e-mail address at the end of the RFC. However, he did not comment on the discussion about the checksum.</p><blockquote><p><code>http://www.ietf.org/mail-archive/web/vrrp/current/threads.html</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '12, 03:12</p></div></div><div id="comments-container-15573" class="comments-container"><span id="31671"></span><div id="comment-31671" class="comment"><div id="post-31671-score" class="comment-score"></div><div class="comment-text"><p>Added a preference to the VRRP dissector in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=a653014e69a4f0e0b59393ddc03871006057b36a">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=a653014e69a4f0e0b59393ddc03871006057b36a</a> whether to use V2 or V3 metod for V3 packets.</p></div><div id="comment-31671-info" class="comment-info"><span class="comment-age">(09 Apr '14, 07:06)</span> Anders ♦</div></div></div><div id="comment-tools-15573" class="comment-tools"></div><div class="clear"></div><div id="comment-15573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

