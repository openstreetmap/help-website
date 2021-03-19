+++
type = "question"
title = "TLSV1 &quot;Ignored Unknown Record&quot;"
description = '''A wireshark trace of a TLS mailflow has packets with &quot;Ignored Unknown Record&quot; and I can&#x27;t seem to find a solution to display them.  Allow Subdissector to Reassemble TCP Streams as suggested by Laura&#x27;s is already checked.  http://ask.wireshark.org/questions/703/ssl-and-tls-ignored-unknown-record  Wha...'''
date = "2013-12-04T11:54:00Z"
lastmod = "2013-12-04T21:20:00Z"
weight = 27773
keywords = [ "tls", "ignored", "record", "smtp", "unknown" ]
aliases = [ "/questions/27773" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TLSV1 "Ignored Unknown Record"](/questions/27773/tlsv1-ignored-unknown-record)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27773-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A wireshark trace of a TLS mailflow has packets with "Ignored Unknown Record" and I can't seem to find a solution to display them.</p><p>Allow Subdissector to Reassemble TCP Streams as suggested by Laura's is already checked.</p><blockquote><p><a href="http://ask.wireshark.org/questions/703/ssl-and-tls-ignored-unknown-record">http://ask.wireshark.org/questions/703/ssl-and-tls-ignored-unknown-record</a></p></blockquote><p>What else may cause Ignored Unknown Record ?</p></div><div id="question-tags" class="tags-container tags">tls ignored record smtp unknown</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '13, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-27773" class="comments-container"></div><div id="comment-tools-27773" class="comment-tools"></div><div class="clear"></div><div id="comment-27773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27796"></span>

<div id="answer-container-27796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27796-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You probably have a SMTP handshake happening before the TLS negotiation. See <a href="http://en.wikipedia.org/wiki/SMTP_Authentication">http://en.wikipedia.org/wiki/SMTP_Authentication</a> . So, if you do the "Decode as SSL" on all packets wireshark will treat those as unknown TLS.<br />
</p><pre><code>&gt; S: 220 smtp.example.com ESMTP Server  
&gt; C: EHLO client.example.com   S:
&gt; 250-smtp.example.com Hello
&gt; client.example.com   S: 250-AUTH
&gt; GSSAPI DIGEST-MD5   S:
&gt; 250-ENHANCEDSTATUSCODES   S: 250
&gt; STARTTLS   C: STARTTLS   S: 220 Ready
&gt; to start TLS
&gt;     ... TLS negotiation proceeds. 
&gt;      Further commands protected by TLS layer ...   C: EHLO client.example.com
&gt; S: 250-smtp.example.com Hello
&gt; client.example.com   S: 250 AUTH
&gt; GSSAPI DIGEST-MD5 PLAIN   C: AUTH
&gt; PLAIN dGVzdAB0ZXN0ADEyMzQ=   S: 235
&gt; 2.7.0 Authentication successful</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '13, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-27796" class="comments-container"><span id="27800"></span><div id="comment-27800" class="comment"><div id="post-27800-score" class="comment-score"></div><div class="comment-text"><p>Good idea!</p></div><div id="comment-27800-info" class="comment-info"><span class="comment-age">(05 Dec '13, 02:17)</span> Kurt Knochner ♦</div></div><span id="27803"></span><div id="comment-27803" class="comment"><div id="post-27803-score" class="comment-score"></div><div class="comment-text"><p>while you are right regarding the "Decode as" part (Wireshark indeed shows the SMTP traffic as "Ignored Unknown Record", it is <strong>not necessary</strong> to run "Decode as", because Wireshark detects the STARTTLS command and shows the following frames as TLS.</p><p>So I wonder why the OP should have done "Decode as" !?! Let's see if @net_tech ever responds to this....</p></div><div id="comment-27803-info" class="comment-info"><span class="comment-age">(05 Dec '13, 04:26)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27796" class="comment-tools"></div><div class="clear"></div><div id="comment-27796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27785"></span>

<div id="answer-container-27785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27785-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What else may cause Ignored Unknown Record ?</p></blockquote><p>Maybe your mail server (deducted from the phrase 'mailflow') uses a TLS record type that is unknown to Wireshark (in general, or the version you are using).</p><p>From the code: packet-ssl.c</p><pre><code>       / TLS 1.0/1.1 just ignores unknown records - RFC 2246 chapter 6. The TLS Record Protocol /
        if ((conv_version==SSL_VER_TLS || conv_version==SSL_VER_TLSv1DOT1 || *conv_version==SSL_VER_TLSv1DOT2) &amp;&amp;
            (available_bytes &gt;=1 ) &amp;&amp; !ssl_is_valid_content_type(tvb_get_guint8(tvb, offset))) {
            proto_tree_add_text(tree, tvb, offset, available_bytes, &quot;Ignored Unknown Record&quot;);</code></pre><p>Then from RFC2246 chapter 6</p><pre><code>   Any new record types should
   allocate type values immediately beyond the ContentType values for
   the four record types described here (see Appendix A.2). If a TLS
   implementation receives a record type it does not understand, it
   should just ignore it.</code></pre><p>Then from packet-ssl-utils.c</p><pre><code>int
ssl_is_valid_content_type(guint8 type)
{
    if ((type &gt;= 0x14) &amp;&amp; (type &lt;= 0x18))
    {
        return 1;
    }

    return 0;</code></pre><p>So, Wireshark will only be able to 'understand' types between 0x14 and 0x18. What do you see in your capture file?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '13, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '13, 15:04</p></div></div><div id="comments-container-27785" class="comments-container"><span id="27809"></span><div id="comment-27809" class="comment"><div id="post-27809-score" class="comment-score"></div><div class="comment-text"><p>Got a little problem here. As I was working with the trace, instead of saving the file I exported it as text from Wireshark 1.4 and could not import it back. I can open the exported file in 1.10, but I think some of the metadata was lost during the export. To make the problem worse, the issue was corrected at the receiver’s end and I can’t recapture questionable traffic.</p><p>I did however find several references to TLS &amp; encryption issues caused by watchguard firebox firewall, which is exactly what is used at the other side of the wire</p><p><a href="https://support.google.com/postini/answer/138468?hl=en">https://support.google.com/postini/answer/138468?hl=en</a></p></div><div id="comment-27809-info" class="comment-info"><span class="comment-age">(05 Dec '13, 06:05)</span> net_tech</div></div><span id="27812"></span><div id="comment-27812" class="comment"><div id="post-27812-score" class="comment-score"></div><div class="comment-text"><p>Upgraded to Wireshark 1.10.3 but I still see "Ignored Unknown Records" in other SMTP connections.</p><p>If I do "Decode as SSL" or simply "Follow SSL Stream" as mrEEde suggested I get decrypted SMTP communication. (private key is added to SSL protocol)</p></div><div id="comment-27812-info" class="comment-info"><span class="comment-age">(05 Dec '13, 06:32)</span> net_tech</div></div><span id="27813"></span><div id="comment-27813" class="comment"><div id="post-27813-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>is content type stored in tcp.flags field ?</p></div><div id="comment-27813-info" class="comment-info"><span class="comment-age">(05 Dec '13, 06:39)</span> net_tech</div></div><span id="27814"></span><div id="comment-27814" class="comment not_top_scorer"><div id="post-27814-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Upgraded to Wireshark 1.10.3 but I still see "Ignored Unknown Records" in other SMTP connections.</p></blockquote><p>can you post a sample capture (without key) on google drive, dropbox, cloudshark.org or mega.co.nz?</p><blockquote><p>is content type stored in tcp.flags field ?</p></blockquote><p>no, in ssl.record.content_type</p></div><div id="comment-27814-info" class="comment-info"><span class="comment-age">(05 Dec '13, 06:55)</span> Kurt Knochner ♦</div></div><span id="27815"></span><div id="comment-27815" class="comment not_top_scorer"><div id="post-27815-score" class="comment-score"></div><div class="comment-text"><p>can't post a capture, but can share a screenshot</p><p><img src="https://osqa-ask.wireshark.org/upfiles/jpg2.JPG" alt="alt text" /></p></div><div id="comment-27815-info" class="comment-info"><span class="comment-age">(05 Dec '13, 07:05)</span> net_tech</div></div><span id="27816"></span><div id="comment-27816" class="comment not_top_scorer"><div id="post-27816-score" class="comment-score"></div><div class="comment-text"><p>I think I figured it out. the packet shown below becomes "Ignored Unknown Records" when private key is added to the SSL protocol</p><p><img src="https://osqa-ask.wireshark.org/upfiles/pack.JPG" alt="alt text" /></p></div><div id="comment-27816-info" class="comment-info"><span class="comment-age">(05 Dec '13, 07:20)</span> net_tech</div></div><span id="27817"></span><div id="comment-27817" class="comment not_top_scorer"><div id="post-27817-score" class="comment-score"></div><div class="comment-text"><p>well, is that with or without "Decode as ..." ? Please check</p><blockquote><p>Analyze -&gt; Decode as -&gt; Show current</p></blockquote><p>If there is any entry for port 25, delete it and test again.</p></div><div id="comment-27817-info" class="comment-info"><span class="comment-age">(05 Dec '13, 07:37)</span> Kurt Knochner ♦</div></div><span id="27819"></span><div id="comment-27819" class="comment not_top_scorer"><div id="post-27819-score" class="comment-score"></div><div class="comment-text"><p>Not sure if I explained what happens clear enough. If I go to Edit -&gt; Preferences -&gt; Protocols -&gt; SSL and remove my private key from the RSA key list, frame 5578 is displayed as shown below.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/smtp.JPG" alt="alt text" /></p><p>If I go back and add the private key and specify IP, TCP port and protocol, the same frame changes it’s display to the Ignored Unknown Record.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ign.JPG" alt="alt text" /></p></div><div id="comment-27819-info" class="comment-info"><span class="comment-age">(05 Dec '13, 08:08)</span> net_tech</div></div><span id="27821"></span><div id="comment-27821" class="comment not_top_scorer"><div id="post-27821-score" class="comment-score"></div><div class="comment-text"><p>ah, so you <strong>only</strong> see that message when you are decrypting the TLS data in the SMTP connection? There is no "Decode as" configured, right?</p></div><div id="comment-27821-info" class="comment-info"><span class="comment-age">(05 Dec '13, 08:14)</span> Kurt Knochner ♦</div></div><span id="27822"></span><div id="comment-27822" class="comment not_top_scorer"><div id="post-27822-score" class="comment-score"></div><div class="comment-text"><p>correct, no "Decode as" configured</p></div><div id="comment-27822-info" class="comment-info"><span class="comment-age">(05 Dec '13, 08:20)</span> net_tech</div></div><span id="27824"></span><div id="comment-27824" class="comment"><div id="post-27824-score" class="comment-score">1</div><div class="comment-text"><p>O.K. could be a 'bug' with the TLS (SMTP) decryption routine, as Frame #5578 is dissected as SMTP traffic 'before' you decrypt it.</p></div><div id="comment-27824-info" class="comment-info"><span class="comment-age">(05 Dec '13, 08:29)</span> Kurt Knochner ♦</div></div><span id="27832"></span><div id="comment-27832" class="comment"><div id="post-27832-score" class="comment-score">1</div><div class="comment-text"><p>I can confirm the behavior @net_tech found. As soon as a key is used to decrypt 'STARTTLS traffic' the former SMTP frames will be shown as "Ignored Unknown Record". Looks like a bug. Not sure if that is easy to fix....</p><p>@net_tech: please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-27832-info" class="comment-info"><span class="comment-age">(05 Dec '13, 09:38)</span> Kurt Knochner ♦</div></div><span id="27837"></span><div id="comment-27837" class="comment not_top_scorer"><div id="post-27837-score" class="comment-score"></div><div class="comment-text"><p>submitted as bug # 9515</p></div><div id="comment-27837-info" class="comment-info"><span class="comment-age">(05 Dec '13, 10:37)</span> net_tech</div></div></div><div id="comment-tools-27785" class="comment-tools"><span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a></div><div class="clear"></div><div id="comment-27785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

