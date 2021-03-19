+++
type = "question"
title = "Exactly how does Wireshark determine and label a Gratuitous ARP as Gratuitous?"
description = '''For definitions and background, this is a great post: My specific question: Exactly what factors does Wireshark look for to label a Gratuitous ARP as Gratuitous? This is a PCAP which includes 3 gratuitous ARPs pulled from various capture sessions. All three are definitely Gratuitous, but Wireshark i...'''
date = "2017-01-13T20:40:00Z"
lastmod = "2017-01-16T08:53:00Z"
weight = 58755
keywords = [ "arp", "gratuitous" ]
aliases = [ "/questions/58755" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Exactly how does Wireshark determine and label a Gratuitous ARP as Gratuitous?](/questions/58755/exactly-how-does-wireshark-determine-and-label-a-gratuitous-arp-as-gratuitous)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58755-score" class="post-score" title="current number of votes">0</div><span id="post-58755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>For definitions and background, <a href="https://ask.wireshark.org/questions/45400/ethernet-packet-arp#fmanswer">this is a great pos</a>t:</p><p>My specific question: <strong>Exactly what factors does Wireshark look for to label a Gratuitous ARP as Gratuitous?</strong></p><p><a href="https://www.dropbox.com/s/s3v8g6l7q4jlx74/garps.pcapng?dl=0">This is a PCAP</a> which includes 3 gratuitous ARPs pulled from various capture sessions.</p><p>All three are definitely Gratuitous, but Wireshark is only marking the first two as Gratuitous.</p><p>The third packet conforms to the RFC 5227 Probe, used to preemptively detect duplicate addresses before putting an IP address to use. The probe is, by definition, gratuitous, as it wasn't prompted by an ARP Request. But Wireshark does not label it as such. Why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-gratuitous" rel="tag" title="see questions tagged &#39;gratuitous&#39;">gratuitous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '17, 20:40</strong></p><img src="https://secure.gravatar.com/avatar/bd5b2672e3e176f57a24e5f6a0af8c3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erh&#39;s gravatar image" /><p><span>erh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erh has no accepted answers">0%</span></p></div></div><div id="comments-container-58755" class="comments-container"></div><div id="comment-tools-58755" class="comment-tools"></div><div class="clear"></div><div id="comment-58755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58756"></span>

<div id="answer-container-58756" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58756-score" class="post-score" title="current number of votes">3</div><span id="post-58756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="erh has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To quote the comment in the Wireshark ARP dissector:</p><pre><code> ARP requests/replies with the same sender and target protocol
 address are flagged as &quot;gratuitous ARPs&quot;, i.e. ARPs sent out as,
 in effect, an announcement that the machine has MAC address
 XX:XX:XX:XX:XX:XX and IPv4 address YY.YY.YY.YY. Requests are to
 provoke complaints if some other machine has the same IPv4 address,
 replies are used to announce relocation of network address, like
 in failover solutions.</code></pre><p>See also <a href="https://wiki.wireshark.org/Gratuitous_ARP">the Wireshark Wiki page on gratuitous ARPs</a>.</p><p>RFC 5227 says, in <a href="https://tools.ietf.org/html/rfc5227#section-1.1">section 1.1 "Conventions and Terminology Used in This Document"</a>:</p><pre><code>In this document, the term &#39;ARP Announcement&#39; is used to refer to an
ARP Request packet, broadcast on the local link, identical to the ARP
Probe described above, except that both the sender and target IP
address fields contain the IP address being announced.  It conveys a
stronger statement than an ARP Probe, namely, &quot;This is the address I
am now using.&quot;</code></pre><p>and says in <a href="https://tools.ietf.org/html/rfc5227#section-4">section 4 "Historical Note"</a> that:</p><pre><code>... What Stevens describes as
Gratuitous ARP is the exact same packet that this document refers to
by the more descriptive term &#39;ARP Announcement&#39;. ...</code></pre><p>The first two packets are capital-G Gratuitous ARPs/ARP Announcements, as the source and target protocol (IP) addresses are the same. The third packet isn't a capital-G Gratuitous ARP.</p><p>Perhaps Wireshark should drop the term "Gratuitous ARP" and, instead, detect and report "ARP Announcement" and "ARP Probe" packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '17, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-58756" class="comments-container"><span id="58764"></span><div id="comment-58764" class="comment"><div id="post-58764-score" class="comment-score"></div><div class="comment-text"><p>I think the 3. packet is an ARP Probe in accordance to the RFC 5227, too.</p><p>In Section 2.1.1 we can read, that an ARP Probe may fillthe IP_Sender filed with all zeros:</p><pre><code>2.1.1.  Probe Details
A host probes to see if an address is already in use by broadcasting
   an ARP Request for the desired address.  The client MUST fill in the
   &#39;sender hardware address&#39; field of the ARP Request with the hardware
   address of the interface through which it is sending the packet.  The
   &#39;sender IP address&#39; field MUST be set to all zeroes; this is to avoid
   polluting ARP caches in other hosts on the same link in the case
   where the address turns out to be already in use by another host.
   The &#39;target hardware address&#39; field is ignored and SHOULD be set to
   all zeroes.  The &#39;target IP address&#39; field MUST be set to the address
   being probed.  An ARP Request constructed this way, with an all-zero
   &#39;sender IP address&#39;, is referred to as an &#39;ARP Probe&#39;.
...</code></pre><p>Even if ARP Probe/Anouncement may be more correct, the terms Gratiuos ARP Request/Response are more known I think.</p></div><div id="comment-58764-info" class="comment-info"><span class="comment-age">(14 Jan '17, 06:30)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="58765"></span><div id="comment-58765" class="comment"><div id="post-58765-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I think the 3. packet is an ARP Probe in accordance to the RFC 5227, too.</p></blockquote><p>Yes, that's why I mentioned ARP Probes in my comment.</p><blockquote><p>Even if ARP Probe/Anouncement may be more correct, the terms Gratiuos ARP Request/Response are more known I think.</p></blockquote><p>Is there any place that defines an ARP Probe, rather than an ARP Announcement, as a "Gratuitous ARP"? Richard Stevens' book defines it as "a host [sending] an ARP request looking for its own address.”, which is what RFC 5227 called an "ARP Announcement":</p><blockquote><p>What Stevens describes as Gratuitous ARP is the exact same packet that this document refers to by the more descriptive term 'ARP Announcement'.</p></blockquote><p><a href="https://tools.ietf.org/html/rfc2002#section-4.6">RFC 2002 section 4.6 "ARP, Proxy ARP, and Gratuitous ARP"</a> and <a href="https://tools.ietf.org/html/rfc5944#section-4.6">RFC 5944 section 4.6 "ARP, Proxy ARP, and Gratuitous ARP"</a> say:</p><blockquote><p>A Gratuitous ARP [23] is an ARP packet sent by a node in order to spontaneously cause other nodes to update an entry in their ARP cache. A gratuitous ARP MAY use either an ARP Request or an ARP Reply packet. In either case, the ARP Sender Protocol Address and ARP Target Protocol Address are both set to the IP address of the cache entry to be updated, and the ARP Sender Hardware Address is set to the link-layer address to which this cache entry should be updated. When using an ARP Reply packet, the Target Hardware Address is also set to the link-layer address to which this cache entry should be updated (this field is not used in an ARP Request packet).</p></blockquote></div><div id="comment-58765-info" class="comment-info"><span class="comment-age">(14 Jan '17, 14:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="58768"></span><div id="comment-58768" class="comment"><div id="post-58768-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Guy Harris</span> It seems that I have missunderstood you answer a liitel bit.</p><p>So I would not change the term GRAP into ARP Anouncement. But it might be helpful to name the ARP Probe as an ARP Probe.</p></div><div id="comment-58768-info" class="comment-info"><span class="comment-age">(15 Jan '17, 01:21)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="58815"></span><div id="comment-58815" class="comment"><div id="post-58815-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the run down, Guy. Maybe getting Wireshark to label the 3rd packet as an ARP Probe or Announcement would be beneficial. Because (as you pointed out) it isn't exactly a Gratuitous ARP, but it is <em>closer</em> to a Gratuitous ARP than a regular ARP Request/Response conversation. It would be more accurate to call it Gratuitous, but <em>most</em> accurate to call it an ARP Probe.</p></div><div id="comment-58815-info" class="comment-info"><span class="comment-age">(16 Jan '17, 08:46)</span> <span class="comment-user userinfo">erh</span></div></div><span id="58816"></span><div id="comment-58816" class="comment"><div id="post-58816-score" class="comment-score"></div><div class="comment-text"><p>To go a step further. There is a distinction between a ARP Probe and an ARP Announcement. I went ahead and captured the ARP packets after setting a new IP address on Win10 (but I believe this is the same process on Win8 and beyond, per <a href="https://blogs.technet.microsoft.com/networking/2013/04/16/gratuitous-arp-and-dad-in-windows-xp-windows-7vista-windows-8-and-failover-cluster/">this</a>). I updated <a href="https://www.dropbox.com/s/s3v8g6l7q4jlx74/garps.pcapng?dl=0">the original packet capture</a> to include four additional ARP packets.</p><p>Of the last 4 packets, the first 3 (packet#4/5/6) are <strong>ARP Probes</strong>, they include a Sender MAC and Target IP address for the IP address/mapping they are trying to validate (192.168.0.254). <em>They include a Sender IP and Target MAC of all zeros</em>, in order to not accidentally update an ARP cache on the network with information that is not yet determined to be conflict free. These are ARP Probes.</p><p>The last packet (packet#7) is an ARP Announcement -- the host, having successfully determined that the IP address is not in use, "claims" it by sending out this final ARP Announcement. Wireshark currently labels this as Gratuitous ARP, which I believe is accurate enough. The only difference between this ARP Announcement and a true gratuitous arp is <em>maybe</em> that the ARP Announcement is still an ARP Request packet, where as the true Gratuitous ARP packets I've seen have all been ARP Replies.</p><p>That said, the RFC's do not specify that a Gratuitous ARP must be a Reply, it in fact leaves it up to the vendor to implement as a Reply or Response. So given that, I'm not sure there is enough of a way to distinguish a true Gratuitous ARP from an ARP Announcement. But it very well may be sufficient to continue to label the ARP Announcement as a Gratuitous ARP.</p><p>(But the ARP Probe should definitely be labeled as such, as it is neither an Gratuitous ARP or a regular ARP Request/Reply).</p></div><div id="comment-58816-info" class="comment-info"><span class="comment-age">(16 Jan '17, 08:53)</span> <span class="comment-user userinfo">erh</span></div></div></div><div id="comment-tools-58756" class="comment-tools"></div><div class="clear"></div><div id="comment-58756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

