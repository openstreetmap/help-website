+++
type = "question"
title = "SSL decryption mystery"
description = '''I&#x27;m trying to decrypt SSL packets that are coming from the internet to an application in Windows, and I can&#x27;t get the decryption to work. Below are the things that I&#x27;ve checked out (thanks again to Sake Blok&#x27;s presentation for giving me these ideas): --I may be wrong about this, but I believe that t...'''
date = "2013-03-17T09:02:00Z"
lastmod = "2013-03-19T21:39:00Z"
weight = 19588
keywords = [ "ssl" ]
aliases = [ "/questions/19588" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decryption mystery](/questions/19588/ssl-decryption-mystery)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19588-score" class="post-score" title="current number of votes">0</div><span id="post-19588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt SSL packets that are coming from the internet to an application in Windows, and I can't get the decryption to work. Below are the things that I've checked out (thanks again to Sake Blok's <a href="http://sharkfest.wireshark.org/sharkfest.12/presentations/MB-1_SSL_Troubleshooting_with%20_Wireshark_Software.pdf">presentation</a> for giving me these ideas):</p><p>--I may be wrong about this, but I believe that the cipher selected by the server is not Diffie-Hellman based. From the <code>server hello</code>, the cipher is <code>TLS_RSA_WITH_AES_128_CBC_SHA</code>.</p><p>--The capture session I'm trying to decrypt does include both the client and the server hello.</p><p>--This may be the cause of the problem: When the server sends me the 'Certificate' part of the handshake, it sends me THREE certificates, but I only have ONE private key. I've compared the modulus output of my private key to that of the three certificates, and my private key matches the first certificate listed, but not the other two.</p><p>In my debug file, the private key is loaded successfully, but I noticed the following two items which I think may indicate a problem:</p><pre><code>dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material</code></pre><p>and</p><pre><code>ssl_decrypt_pre_master_secret wrong pre_master_secret length (67, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret</code></pre><p>Thanks for any ideas you might have.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '13, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/f1e3f650da5cc31a11f1d32ab15e69f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sandwiches9&#39;s gravatar image" /><p><span>sandwiches9</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sandwiches9 has no accepted answers">0%</span></p></div></div><div id="comments-container-19588" class="comments-container"></div><div id="comment-tools-19588" class="comment-tools"></div><div class="clear"></div><div id="comment-19588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19589"></span>

<div id="answer-container-19589" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19589-score" class="post-score" title="current number of votes">1</div><span id="post-19589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sandwiches9 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>This may be the cause of the problem: When the server sends me the 'Certificate' part of the handshake, it sends me THREE certificates, but I only have ONE private key. I've compared the modulus output of my private key to that of the three certificates, and my private key matches the first certificate listed, but not the other two.</p></blockquote><p>That is normal, when the server sends it's certificate, it will send all the Intermediate CA certificates too, so that the client can validate the whole chain up to the root certificate (which it must have in it's trust store).</p><blockquote><p>ssl_decrypt_pre_master_secret wrong pre_master_secret length (67, expected 48) dissect_ssl3_handshake can't decrypt pre master secret</p></blockquote><p>That usually indicates a mismatch between the private key configured in Wireshark and the certificate/private key on the server. However...</p><blockquote><p>I've compared the modulus output of my private key to that of the three certificates, and my private key matches the first certificate listed</p></blockquote><p>Which means you <strong>do</strong> have the right key.</p><p>There have been some issues in the SSL libraries used by Wireshark on Linux systems lately, so that might be the cause of your troubles, cause AFAICT you're right on track in getting decryption to work...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '13, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19589" class="comments-container"><span id="19590"></span><div id="comment-19590" class="comment"><div id="post-19590-score" class="comment-score">1</div><div class="comment-text"><p>Have you tried decrypting the <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=snakeoil2_070531.tgz">snakeoil file</a> described at <a href="http://wiki.wireshark.org/SSL">http://wiki.wireshark.org/SSL</a>?</p><p>If that does not work, then there is something wrong with your decryption libraries. It if does work, then we need to dig deeper in why you can't get it to work with your own capture file...</p></div><div id="comment-19590-info" class="comment-info"><span class="comment-age">(17 Mar '13, 09:34)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="19591"></span><div id="comment-19591" class="comment"><div id="post-19591-score" class="comment-score"></div><div class="comment-text"><p>Thanks for bringing that up, I meant to mention that in my question -- I did try to decrypt the snakeoil file, and to my surprise, it did decrypt just fine. Also, one more piece of information, I'm using Wireshark 1.8.6 on Windows 7.</p></div><div id="comment-19591-info" class="comment-info"><span class="comment-age">(17 Mar '13, 09:39)</span> <span class="comment-user userinfo">sandwiches9</span></div></div><span id="19592"></span><div id="comment-19592" class="comment"><div id="post-19592-score" class="comment-score">1</div><div class="comment-text"><p>OK, now that we know that (in principle) your decryption works fine. Let's look at the tracefile and ssl debug logging. Are you able to share your trace file (on www.cloudshark.org for instance)? And can you share the private key? Or is it a production server? If so, can you post the contents of the whole ssl-debug here?</p><p>If you can't share the files with the public, can you share them with me? (My email address is in the notes on my profile)</p></div><div id="comment-19592-info" class="comment-info"><span class="comment-age">(17 Mar '13, 09:46)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="19593"></span><div id="comment-19593" class="comment"><div id="post-19593-score" class="comment-score"></div><div class="comment-text"><p>Thanks a ton for helping me with this, e-mail sent.</p></div><div id="comment-19593-info" class="comment-info"><span class="comment-age">(17 Mar '13, 12:59)</span> <span class="comment-user userinfo">sandwiches9</span></div></div><span id="19619"></span><div id="comment-19619" class="comment"><div id="post-19619-score" class="comment-score">1</div><div class="comment-text"><p>The ssl session is being set up with client certificates. In an RSA key exchange, the public key inside the <em>server</em> certificate is used to encrypt the pre-master secret (from which the session key for encryption is derived). So, you only need the corresponding private key to decrypt the pre-master secret and subsequently decrypt the application data.</p><p>As discussed on the mail, you are using the private key of the Client certificate instead of the private key of the server certificate.</p></div><div id="comment-19619-info" class="comment-info"><span class="comment-age">(18 Mar '13, 07:36)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="19666"></span><div id="comment-19666" class="comment not_top_scorer"><div id="post-19666-score" class="comment-score"></div><div class="comment-text"><p>^^^Right, after some further reading yesterday and today, I have a better understanding of how all that works. Thanks again for going out of your way and pointing me in the right direction.</p></div><div id="comment-19666-info" class="comment-info"><span class="comment-age">(19 Mar '13, 21:39)</span> <span class="comment-user userinfo">sandwiches9</span></div></div></div><div id="comment-tools-19589" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-19589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

