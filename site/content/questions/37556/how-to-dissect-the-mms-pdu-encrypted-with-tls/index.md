+++
type = "question"
title = "How to dissect the MMS pdu encrypted with TLS?"
description = '''Hi everyone, in my client/server application I&#x27;m sending some MMS packets ecnrypted in the TLS session. I&#x27;m able to decrypt the TLS data, and take a look at the plain text in the segments with the &quot;Follow SSL stream&quot; function (according to the instructions in https://ask.wireshark.org/questions/4229...'''
date = "2014-11-03T07:34:00Z"
lastmod = "2014-11-06T03:08:00Z"
weight = 37556
keywords = [ "tls", "ssl", "mms", "encryption" ]
aliases = [ "/questions/37556" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect the MMS pdu encrypted with TLS?](/questions/37556/how-to-dissect-the-mms-pdu-encrypted-with-tls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37556-score" class="post-score" title="current number of votes">0</div><span id="post-37556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>in my client/server application I'm sending some MMS packets ecnrypted in the TLS session. I'm able to decrypt the TLS data, and take a look at the plain text in the segments with the "Follow SSL stream" function (according to the instructions in <a href="https://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id">https://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id</a>).</p><p>I'm looking for a way to present the MMS data properly, with the common protocol structure visualization, not only a textual presentation.</p><p><img src="http://i60.tinypic.com/35ho4up.png" alt="alt text" /></p><p>I would like to see the MMS protocol menu instead of "Encrypted Application Data"</p><p>I've already tried with no success what has been write here: <a href="https://ask.wireshark.org/questions/6298/wireshark-cannot-dissect-mms-packets-that-dont-begin-with-initiate">https://ask.wireshark.org/questions/6298/wireshark-cannot-dissect-mms-packets-that-dont-begin-with-initiate</a></p><p>I'm using Wireshark 1.12.</p><p>Marc</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-mms" rel="tag" title="see questions tagged &#39;mms&#39;">mms</span> <span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '14, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/c7306c011d7f22a048e2cd12e503ae8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc184&#39;s gravatar image" /><p><span>Marc184</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc184 has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Nov '14, 06:20</strong> </span></p></div></div><div id="comments-container-37556" class="comments-container"><span id="37567"></span><div id="comment-37567" class="comment"><div id="post-37567-score" class="comment-score"></div><div class="comment-text"><p><em>Update</em></p><p>I've tried the <a href="http://blogs.technet.com/b/nettracer/archive/2013/10/12/decrypting-ssl-tls-sessions-with-wireshark-reloaded.aspx">rsa private key approach</a> to decrypt the TLS session, by giving to wireshark the rsa private keys in .pem files, plus ip address and tcp port of the sniffed machines, and the indication of the application protocol used, MMS.</p><p>I've also mantained the previous SSL settings (tls session id and rsa pre master secret in .log files)</p><p>In the picture you can see what I've obtained:</p><p><img src="http://i60.tinypic.com/2z7rkvb.png" alt="alt text" /></p><p>In the SSL stream I can see the decrypted session correctly, but wireshark can't reconstruct the MMS pdu.</p><p>Any ideas?</p></div><div id="comment-37567-info" class="comment-info"><span class="comment-age">(04 Nov '14, 05:02)</span> <span class="comment-user userinfo">Marc184</span></div></div><span id="37593"></span><div id="comment-37593" class="comment"><div id="post-37593-score" class="comment-score"></div><div class="comment-text"><p>I converted your Answer to a Comment since it doesn't appear to be an answer to your question. (Remember that this is a Q&amp;A site, not a forum.)</p></div><div id="comment-37593-info" class="comment-info"><span class="comment-age">(05 Nov '14, 07:50)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="37603"></span><div id="comment-37603" class="comment"><div id="post-37603-score" class="comment-score"></div><div class="comment-text"><p>Tahnks, you're right, I'm sorry for the mistake.</p></div><div id="comment-37603-info" class="comment-info"><span class="comment-age">(06 Nov '14, 00:16)</span> <span class="comment-user userinfo">Marc184</span></div></div></div><div id="comment-tools-37556" class="comment-tools"></div><div class="clear"></div><div id="comment-37556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37612"></span>

<div id="answer-container-37612" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37612-score" class="post-score" title="current number of votes">0</div><span id="post-37612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marc184 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found the solution!</p><p>In the <em>SSL protocol preferences -&gt; RSA keys list -&gt; Edit</em> the protocol I choosed was wrong. The correct one is <strong>tpkt</strong>, not mms. Now I can see all the decrypted MMS structured payload.</p><p><img src="http://i62.tinypic.com/28b5kt1.png" alt="alt text" /></p><h2 id="solution-recap">SOLUTION RECAP</h2><ul><li><p>create a .log file with SSL session id and pre master secret key. Use the format:</p><pre><code>RSA Session-ID:xxxx Master-Key:xxxx</code></pre></li></ul><p>don't forget the CRLF at the end of the line. You should obtain something like:</p><pre><code>    RSA Session-ID:B5AEB800F43F96A9BAD007A5D26423E43479B904166FA72A4789DEA15A830E26 Master-Key:454AD3030F0AE8234508DF959EF533675E225BBB388EE5F80A20A007BAB63E1ABB972F39401796FB02F27AF95AB083A4</code></pre><p>(one line only)</p><p>Go to SSL protocol preferences.</p><ul><li><p>Link the .log file you've created in the <em>(Pre)-master secret log filename</em> form</p></li><li><p>For this step we need the private keys of machines involved in the SSL session.</p></li></ul><p>The .pem file with the private key should look like this:</p><pre><code>    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAtIvaDmeOGleYuxT01GfAmgugHVlqCOFfGYqy3gxMWt/fxO/7
    s7BJzqnhAFOWBjmBAdj7hHmPyCoJM7/MdCDJt1y7d20BJAGxD0ZQ4kxzGZDCjc5z
    ....... some 20-100 lines of base64 encoded data ...............
    Jh2kZkKoVG3Qr+66IlBDuVllIbwQU0F1fYy2FTjZL4vbmdupwHUyTnPK57vP8RJ7
    cpc1qwLZxfurxZfhI9gxXOO5eUg1WBupw029SSoSafYBqO4a9wg1OA==
    -----END RSA PRIVATE KEY-----</code></pre><p>If the .pem file format is:</p><pre><code>    -----BEGIN RSA PRIVATE KEY-----
    Proc-Type: 4,ENCRYPTED
    DEK-Info: DES-EDE3-CBC,CB7BE7B5A318ACE6

    ScuaEtGA1xy7iVvvntc4hZ9Kl0VOKmA9sOcfP1CnrUVpAuLoHPEXTsc10smlXwsl
     [...]
    yy7ANfGCZTWaWP89uOIwlXK0n8hHZjTjw5axBuWXvgWHNbvein7tsg==
    -----END RSA PRIVATE KEY-----</code></pre><p>the key is protected with a passphrase, and wireshark can't decipher it. We have to create a plain text key file. We can use openssl:</p><pre><code>    openssl rsa -in &lt; old-keyfile &gt; -out &lt; new-keyfile &gt;</code></pre><p>when asked, insert the passphrase you used to create the original .pem file.</p><p>Now go to <em>RSA keys list-&gt;Edit</em> and create 2 rules, one for each "way" of the SSL communication. Insert the Ip address of the sender, the TCP port, the application protocol used (<strong>TKPT</strong> in this case) and the private key plain text .pem file</p><p>At this point you will be able to see corretly the decrypted MMS structured pdu, not only the deciphered data in the <em>Follow SSL stream</em> function .</p><p>References:</p><ul><li><a href="https://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id">Session id + master secret procedure</a></li><li><a href="http://blogs.technet.com/b/nettracer/archive/2013/10/12/decrypting-ssl-tls-sessions-with-wireshark-reloaded.aspx">Adding RSA keys</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '14, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/c7306c011d7f22a048e2cd12e503ae8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc184&#39;s gravatar image" /><p><span>Marc184</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc184 has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Nov '14, 03:16</strong> </span></p></div></div><div id="comments-container-37612" class="comments-container"></div><div id="comment-tools-37612" class="comment-tools"></div><div class="clear"></div><div id="comment-37612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

