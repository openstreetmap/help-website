+++
type = "question"
title = "Decrypting SSL in dissector"
description = '''I&#x27;m writing a new dissector for a protocol that can include SSL traffic. It is somewhat similar to LDAP in that it can start a session unencrypted and switch to SSL on the same port when a certain message is received, so I&#x27;ve based my code on packet-ldap. I&#x27;ve also referred to packet-pop, packet-htt...'''
date = "2014-01-07T09:38:00Z"
lastmod = "2015-02-10T07:21:00Z"
weight = 28642
keywords = [ "ssl", "dissector" ]
aliases = [ "/questions/28642" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting SSL in dissector](/questions/28642/decrypting-ssl-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28642-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a new dissector for a protocol that can include SSL traffic. It is somewhat similar to LDAP in that it can start a session unencrypted and switch to SSL on the same port when a certain message is received, so I've based my code on packet-ldap. I've also referred to packet-pop, packet-http, and packet-xmpp, which all have various forms of this code.</p><p>At the appropriate points, my code is successfully getting to:</p><pre><code>call_dissector(ssl_handle, tvb, pinfo, tree);</code></pre><p>But in the output of tshark, I don't see any decrypted data:</p><pre><code>tshark -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;ssl.desegment_ssl_application_data: TRUE&quot; -o &quot;ssl.keys_list: 172.16.244.160,52230,amp,cacert.key&quot; -r ../tests/AMP-connect-SSL-trimmed.pcap -x</code></pre><p>All this prints is the encrypted data.</p><p>If I switch the protocol to ldap, http or xmpp, then I get SSL decryption:</p><pre><code>tshark -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;ssl.desegment_ssl_application_data: TRUE&quot; -o &quot;ssl.keys_list: 172.16.244.160,52230,ldap,cacert.key&quot; -r ../tests/AMP-connect-SSL-trimmed.pcap -x

Frame (140 bytes):
0000  00 0c 29 22 80 34 00 50 56 c0 00 08 08 00 45 00   ..)&quot;.4.PV.....E.
0010  00 7e 31 1a 40 00 40 06 c8 9c ac 10 f4 01 ac 10   [email protected]@.........
0020  f4 a0 f0 e6 cc 06 5d df 0c 2f b2 cc ff fa 80 18   ......]../......
0030  20 00 39 1d 00 00 01 01 08 0a 34 15 f0 11 09 a1    .9.......4.....
0040  28 8f 17 03 00 00 20 ad d1 99 13 3a 22 ec 45 b9   (..... ....:&quot;.E.
0050  b1 ec 0e 1f 52 e7 84 d8 b9 27 9a 72 60 66 17 f2   ....R....&#39;.r`f..
0060  95 2a 82 8e 5a 3b 39 17 03 00 00 20 3c fc 1e d2   .*..Z;9.... &lt;...
0070  b2 de 70 01 9b a7 00 b1 e9 3f 06 87 1d 5a 51 67   ..p......?...ZQg
0080  51 9d 2e 59 0b b1 35 a0 a2 de 37 a6               Q..Y..5...7.
Decrypted SSL data (9 bytes):
0000  00 00 00 01 01 00 00 00 02                        .........</code></pre><p>My code is almost identical to the ldap code. I've tried basing my code on the http, pop, xmpp code (which are all a little different), to no effect. I also tried going back to the <code>dissector_t</code> interface rather than <code>new_dissector_t</code>, but that didn't change anything.</p><pre><code>    if (amp_info &amp;&amp;
            amp_info-&gt;start_tls_frame &amp;&amp;
            ( pinfo-&gt;fd-&gt;num &gt;= amp_info-&gt;start_tls_frame))
    {
        guint32 old_start_tls_frame;

        dissector_delete_uint(&quot;tcp.port&quot;, AMP_PORT, amp_handle);
        ssl_dissector_add(AMP_PORT, &quot;amp&quot;, TRUE);

        old_start_tls_frame = amp_info-&gt;start_tls_frame;
        amp_info-&gt;start_tls_frame = 0; /* make sure we don&#39;t call SSL again */
        pinfo-&gt;can_desegment++; /* ignore this layer so SSL can use the TCP resegment */

        int dissected_length = call_dissector(ssl_handle, tvb, pinfo, tree);

        amp_info-&gt;start_tls_frame = old_start_tls_frame;
        ssl_dissector_delete(AMP_PORT, &quot;amp&quot;, TRUE);

        /* restore AMP as the dissector for this port */
        dissector_add_uint(&quot;tcp.port&quot;, AMP_PORT, amp_handle);

        /* we are done */
        return dissected_length;
    }</code></pre><p>I'm not certain where next to troubleshoot. Is there something else dissectors need to do in order to use SSL? I'm not getting warnings or errors.</p></div><div id="question-tags" class="tags-container tags">ssl dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '14, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/ed9a0d8cd44b62539b141f6c10405db1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20Napier&#39;s gravatar image" /><p>Rob Napier<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob Napier has one accepted answer">100%</span></p></div></div><div id="comments-container-28642" class="comments-container"></div><div id="comment-tools-28642" class="comment-tools"></div><div class="clear"></div><div id="comment-28642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28648"></span>

<div id="answer-container-28648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28648-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The developers mailing list is probably a better place to ask questions like this one ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '14, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28648" class="comments-container"><span id="28649"></span><div id="comment-28649" class="comment"><div id="post-28649-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I wasn't certain what each forum's "level" was.</p></div><div id="comment-28649-info" class="comment-info"><span class="comment-age">(07 Jan '14, 12:07)</span> Rob Napier</div></div><span id="28650"></span><div id="comment-28650" class="comment"><div id="post-28650-score" class="comment-score"></div><div class="comment-text"><p>Some developers are here as well, but by far not all...</p></div><div id="comment-28650-info" class="comment-info"><span class="comment-age">(07 Jan '14, 12:09)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28648" class="comment-tools"></div><div class="clear"></div><div id="comment-28648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39770"></span>

<div id="answer-container-39770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39770-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=93ed72642b3bc0771c6099c4861a39c080040b0e">commit 93ed72642b3bc0771c6099c4861a39c080040b0e</a> (v1.99.3rc0-71-g93ed726), you can use the new <code>ssl_starttls_ack</code> function to mark a conversation for continuation as SSL/TLS. This function takes care of reassembly and other details that are needed before handling the decrypted traffic to the dissector.</p><p>The code from your question has the issue that it makes the protocol dissector (XMPP) fully aware of the SSL layer above the protocol. As dissectors should not need to know the details between the transport layer and SSL, the new <code>ssl_starttls_ack</code> function abstracts some details for you.</p><p>For examples on application of this function, see <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=e190253478cea8ab10903e83daafeb3574ad0f04">commit e190253478cea8ab10903e83daafeb3574ad0f04</a>. You basically have to call <code>ssl_starttls_ack()</code> whenever you found the last plaintext packet before SSL and then the SSL dissector will ensure that your dissector is called for future decrypted packets.</p><p>Here is the prototype from packet-ssl-utils.h:</p><pre><code>/** Marks this packet as the last one before switching to SSL that is supposed
 * to encapsulate this protocol.
 * @param ssl_handle The dissector handle for SSL or DTLS.
 * @param pinfo Packet Info.
 * @param app_handle Dissector handle for the protocol inside the decrypted
 * Application Data record.
 * @return 0 for the first STARTTLS acknowledgement (success) or if ssl_handle
 * is NULL. &gt;0 if STARTTLS was started before.
 */
extern guint32
ssl_starttls_ack(dissector_handle_t ssl_handle, packet_info *pinfo,
                 dissector_handle_t app_handle);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-39770" class="comments-container"></div><div id="comment-tools-39770" class="comment-tools"></div><div class="clear"></div><div id="comment-39770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

