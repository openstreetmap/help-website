+++
type = "question"
title = "SSL Dissector working"
description = '''Hi, I wanted to know if every time i select a new SSL packet is the packet decrypted and dissected again. To be clearer If I give Wireshark the necessary info such as the session key and the client random the ssl stream is decrypted. Does this happen every time the packet is selected or it just happ...'''
date = "2016-10-17T02:57:00Z"
lastmod = "2016-10-17T03:22:00Z"
weight = 56439
keywords = [ "ssl", "ssl_decrypt" ]
aliases = [ "/questions/56439" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SSL Dissector working](/questions/56439/ssl-dissector-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I wanted to know if every time i select a new SSL packet is the packet decrypted and dissected again. To be clearer If I give Wireshark the necessary info such as the session key and the client random the ssl stream is decrypted. Does this happen every time the packet is selected or it just happens once and we keep the whole decrypted frame?</p><p>My intuition says it must be the Decrypted every time as keeping a decrypted record for every packet sounds impractical. Can someone please comment on this? Thanks</p><p>-Koundi</p></div><div id="question-tags" class="tags-container tags">ssl ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div></div><div id="comments-container-56439" class="comments-container"></div><div id="comment-tools-56439" class="comment-tools"></div><div class="clear"></div><div id="comment-56439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56443"></span>

<div id="answer-container-56443" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56443-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Once the TLS record is decrypted, it will be cached for future use.</p><p>Basically it works like this:</p><ol><li><p>The first time a packet is seen, decryption is tried. If the packet is visited again later (because you select the packet for example), it will be skipped. From the <code>dissect_ssl</code> function:</p><pre><code>/* try decryption only the first time we see this packet
 * (to keep cipher synchronized) */
if (pinfo-&gt;fd-&gt;flags.visited)
     ssl_session = NULL;</code></pre></li><li><p>Function <code>dissect_ssl3_record</code> will try to decrypt the record if the <code>SslDecryptSession</code> pointer is still valid (here, <code>ssl</code> is the same as <code>ssl_session</code> above).</p><pre><code>    if (ssl){
        decrypt_ssl3_record(tvb, pinfo, offset,
            record_length, content_type, ssl, TRUE);
    }
    ...
    dissect_ssl_payload(tvb, pinfo, offset, tree, session, app_handle);</code></pre></li><li><p>Function <code>decrypt_ssl3_record</code> will try to decrypt the data and then calls <code>ssl_add_data_info</code> to cache the result (on success). Note that this is only invoked the first time.</p></li><li>Function <code>dissect_ssl_payload</code> will try to load the decrypted data via <code>ssl_get_data_info</code>. This may be invoked multiple times for the same packet.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56443" class="comments-container"><span id="56444"></span><div id="comment-56444" class="comment"><div id="post-56444-score" class="comment-score"></div><div class="comment-text"><p>so you what you are basically saying is it does store the decrypted record for every packet ?</p></div><div id="comment-56444-info" class="comment-info"><span class="comment-age">(17 Oct '16, 03:26)</span> koundi</div></div><span id="56445"></span><div id="comment-56445" class="comment"><div id="post-56445-score" class="comment-score"></div><div class="comment-text"><p>Yes it does store the decrypted record for every packet. Note that only the data (bytes) are stored, not the tree itself.</p></div><div id="comment-56445-info" class="comment-info"><span class="comment-age">(17 Oct '16, 03:31)</span> Lekensteyn</div></div><span id="56459"></span><div id="comment-56459" class="comment"><div id="post-56459-score" class="comment-score"></div><div class="comment-text"><p>yup! thanks. Also can you please tell me why not just store the tvb instead of the bytes. When the packet is decrypted first time when the visited flag is not set then we create a tvb and add it as a data source and pass it onto the next dissectors.</p><p>So when I come back to the same point and get the existing decrypted record and create another tvb is not a redundancy? or is tvb not file scoped ??</p><p>Thanks a lot for answering these questions! I knew you would be the one answering this question :)</p></div><div id="comment-56459-info" class="comment-info"><span class="comment-age">(17 Oct '16, 05:53)</span> koundi</div></div><span id="56460"></span><div id="comment-56460" class="comment"><div id="post-56460-score" class="comment-score"></div><div class="comment-text"><p>Ok, actually when I said "bytes", I meant the tvb which was created from the decrypted data. This seems a good trade-off between memory use and CPU usage :)</p></div><div id="comment-56460-info" class="comment-info"><span class="comment-age">(17 Oct '16, 06:01)</span> Lekensteyn</div></div><span id="56462"></span><div id="comment-56462" class="comment"><div id="post-56462-score" class="comment-score"></div><div class="comment-text"><p>I am sorry but when I look into the code it looks like the ssl_add_data_info is actually copying the character array(guchar*) using wmem_alloc and doing a memcpy with a file scope.</p><p>But by doing this isnt the first tvb left dangling?(yes later when tvb_free is called it is freed) but we are creating two tvbs with the same data are we not?? Can you please tell me when the tvb goes out of "scope"? Thanks again!</p></div><div id="comment-56462-info" class="comment-info"><span class="comment-age">(17 Oct '16, 06:18)</span> koundi</div></div><span id="56465"></span><div id="comment-56465" class="comment not_top_scorer"><div id="post-56465-score" class="comment-score"></div><div class="comment-text"><p>Ok sorry for the misinformation, I just looked again and indeed the decrypted data is first stored in the <code>SslDataInfo</code> structure. A new Tvb is created every time in <code>dissect_ssl_payload</code> based on this data, but it seems that the real data is not copied, only a pointer seems stored (see <code>tvb_new_child_real_data</code> -&gt; <code>tvb_new_real_data</code>, the data pointer is stored in the <code>real_data</code> member).</p><p>Based on the comments in <code>epan/tvbuff.h</code>, a Tvb is freed when returning to the top-level dissector. All chained (child) Tvbs are also released at the same time (but note that the "real data" is not freed because the <code>free_cb</code> is not set in <code>tvb_new_real_data</code>).</p><p>As for the SSL memory, note it is using wmem-allocated memory from the <code>wmem_file_scope</code> pool which means that the memory is released when the packet file closed.</p></div><div id="comment-56465-info" class="comment-info"><span class="comment-age">(17 Oct '16, 06:40)</span> Lekensteyn</div></div><span id="56466"></span><div id="comment-56466" class="comment not_top_scorer"><div id="post-56466-score" class="comment-score"></div><div class="comment-text"><p>yes thanks a lot!</p></div><div id="comment-56466-info" class="comment-info"><span class="comment-age">(17 Oct '16, 06:52)</span> koundi</div></div></div><div id="comment-tools-56443" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-56443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

