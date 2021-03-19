+++
type = "question"
title = "Can&#x27;t decrypt ssl in capture from windump"
description = '''having trouble decrypting ssl; I am trying to analyze a capture file created by windump. Someone else had a similar question, and the response was to check three things: a) private key b) ssl handshake c) encryption type I have exported the server cert, converted to pem and separated out the private...'''
date = "2013-12-16T04:19:00Z"
lastmod = "2013-12-18T23:47:00Z"
weight = 28145
keywords = [ "ssl", "wireshark", "decryption" ]
aliases = [ "/questions/28145" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decrypt ssl in capture from windump](/questions/28145/cant-decrypt-ssl-in-capture-from-windump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28145-score" class="post-score" title="current number of votes">0</div><span id="post-28145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>having trouble decrypting ssl; I am trying to analyze a capture file created by windump.</p><p>Someone else had a similar question, and the response was to check three things: a) private key b) ssl handshake c) encryption type</p><p>I have exported the server cert, converted to pem and separated out the private key. In the file, it says 'rsa', and there is no reference to 'ephemeral'</p><p>I think i'm getting the full session... the ssl handshake looks like: ..."ClientHello" ..."Server Hello, Certificat, Server Hello Done ..."Client Key Exchange ..."Change Cipher Spec ..."Encrypted Handshake message ..."Change Cipher Spec, Encrypted Handshake message ..."Client Key Exchange ..."Change Cipher Spec ..."Encrypted Handshake Message ..."Change Cipher Spec, Encrypted Handshake Message ..."Application Data</p><p>the application data packet at the end is still encrypted</p><p>The only thing left is to try to figure out if wireshark likes the key i provided it...</p><p>some questions: - i see some references to an 'ssl debug file'. How do you configure this? In preferences/protocols/ssl you can browse for a file, but i notice that you can only specify files that already exist.</p><p>I created a file, and specified it, but the file is always zero length.</p><ul><li><p>a lot of the packets are showing red ("Bad Checksum"). Is this a problem?</p></li><li><p>the trace destination ip is not the same as what is returned by "nslookup SITENAME". When configuring at preferences/protocols/ssl/RSA keys list, should I use the ip returned by nslookup, or the ip that that shows up as the destination in the trace? I've tried both IPs, as well as 0.0.0.0.</p></li></ul><p>any insight would be appreciated...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '13, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/8a1c296b364850c080cc8fea3bb3f534?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmc_lat47&#39;s gravatar image" /><p><span>dmc_lat47</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmc_lat47 has no accepted answers">0%</span></p></div></div><div id="comments-container-28145" class="comments-container"><span id="28172"></span><div id="comment-28172" class="comment"><div id="post-28172-score" class="comment-score"></div><div class="comment-text"><p>so.. if anyone could tell me how to get the ssl debug log going, that would at least give me one more thing to look at...</p><p>thanks in advance...</p></div><div id="comment-28172-info" class="comment-info"><span class="comment-age">(16 Dec '13, 11:01)</span> <span class="comment-user userinfo">dmc_lat47</span></div></div></div><div id="comment-tools-28145" class="comment-tools"></div><div class="clear"></div><div id="comment-28145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28247"></span>

<div id="answer-container-28247" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28247-score" class="post-score" title="current number of votes">1</div><span id="post-28247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do you configure this? In preferences/protocols/ssl you can browse for a file, but i notice that you can only specify files that already exist. I created a file, and specified it, but the file is always zero length.</p></blockquote><p>The file selection dialog behaves kind of strange sometimes. It's probably better to just paste the full path of the file to the field <code>SSL debug file</code></p><blockquote><p>if anyone could tell me how to get the ssl debug log going</p></blockquote><p>The only thing you need to do is to specify the debug log. Then close Wireshark, empty or delete the file and restart Wireshark. The file will then be filled with debug messages, <strong>if the user that runs Wireshark</strong> has enough rights to create the file and to write to it, as Wireshark will run in the user context. If that does not happen on your system, please add the following information</p><ul><li>OS and OS version</li><li>Wireshark version</li><li>full path to the debug file</li></ul><blockquote><p>a lot of the packets are showing red ("Bad Checksum"). Is this a problem?</p></blockquote><p>No. That's most certainly due to checksum offloading, as you were capturing on the server itself.</p><blockquote><p>should I use the ip returned by nslookup, or the ip that that shows up as the destination in the trace?</p></blockquote><p>Of course the IP in the trace file. That's the only one Wireshark can see.</p><blockquote><p>How is the ssl debug log configured? <strong>Will the log be written to when wire shark is analyzing a trace file,</strong></p></blockquote><p>Yes. see above.</p><blockquote><p>Then i converted the pem, and placed the rsa private key portion into a separate file.</p></blockquote><p>The key file should look like this:</p><pre><code>-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC8/gQ2y24WaJuuoF4cAibeqLOU7JnkeX21ozjVe7tpeT1ZqSMc
gRLUGAGquCmIT7XipvWLfll7itGGiCMTXdAqNPgiWvxdNVhMh8W/vlv7xTdnbquY
... some lines ....
BMb1winyNNcTHu1vLScCQQCrYa+AfS879mK+L3kFXrliXnJ5+4uBsY55dUQc8j97
CKuarIR9Pb4OAE1mAg6SIWoXOaIp0XmFtXtohBmav3ex
-----END RSA PRIVATE KEY-----</code></pre><p>If you see the following (or similar) lines in the key file</p><pre><code>-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,530703DFD90796F4

kEa20CNx8Pn5zw2sq/UtI5BFk0IlXImzDzdh9Mlv8LdIHwz67rtwQTDstJf9Wucj</code></pre><p>then your exported key is encrypted and you must give Wireshark the passphrase for the key.</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; SSL -&gt; RSA Key List --&gt; Password: within the key entry.</p></blockquote><p>If the key is not encrypted and it still does not work, the following 'problem' occurs sometimes:</p><p>Your SSL/TLS connection is using a cipher that cannot be decrypted with only the RSA key of the server. That's all ciphers with <strong>DH</strong> in the name (Diffie Hellman). The ssl debug log will show the cipher used, as well as Wireshark itself, by looking at the SSL handshake.</p><p>Add a <a href="http://www.lovemytool.com/blog/2011/05/wireshark-151-add-and-customize-columns-by-joke-snelders.html">custom column in the GUI</a> with the following field, to view the negotiated cipher suite.</p><blockquote><p>ssl.handshake.ciphersuite</p></blockquote><p>If the connection is using a DH cipher, you need to SSL session keys, exported by your client. See here:</p><blockquote><p><a href="https://developer.mozilla.org/en-US/docs/NSS_Key_Log_Format">https://developer.mozilla.org/en-US/docs/NSS_Key_Log_Format</a> <a href="https://www.google.com/?q=site%3Aask.wireshark.org+SSLKEYLOGFILE+">https://www.google.com/?q=site%3Aask.wireshark.org+SSLKEYLOGFILE+</a> <a href="http://wiki.wireshark.org/SSL">http://wiki.wireshark.org/SSL</a></p></blockquote><p>Read the questions and answers about using the RSA key log file generated by a browser (by using the environment variable SSLKEYLOGFILE).</p><p>Finally, try to decrypt a SSL session that is known to work.</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys">http://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '13, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28247" class="comments-container"><span id="28280"></span><div id="comment-28280" class="comment"><div id="post-28280-score" class="comment-score"></div><div class="comment-text"><p>thanks so much for the help!!!</p><p>The ssl debug log revealed that i wasn't using the right key.</p><p>Now i've another problem, but that's the subject of another post.</p></div><div id="comment-28280-info" class="comment-info"><span class="comment-age">(18 Dec '13, 23:27)</span> <span class="comment-user userinfo">dmc_lat47</span></div></div><span id="28281"></span><div id="comment-28281" class="comment"><div id="post-28281-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-28281-info" class="comment-info"><span class="comment-age">(18 Dec '13, 23:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28247" class="comment-tools"></div><div class="clear"></div><div id="comment-28247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28231"></span>

<div id="answer-container-28231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28231-score" class="post-score" title="current number of votes">0</div><span id="post-28231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"I have exported the server cert, converted to pem and separated out the <strong>private key</strong>."</p><p>Hm, if that was possible all it would take to decrypt a SSL/TLS session would be to trace the negotiation .<br />
The private key is not sent during negotiation, that is kept at the server. So unless you are given the private key by the server's administrator, there is no way to decrypt the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '13, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-28231" class="comments-container"><span id="28235"></span><div id="comment-28235" class="comment"><div id="post-28235-score" class="comment-score"></div><div class="comment-text"><p>thanks for your response.</p><p>hmm... well, though not it's not something i do well, i <em>am</em> what passes for the server admin on this machine. I used mmc to export the certificate, and made sure to include the private key. Then i converted the pem, and placed the rsa private key portion into a separate file.<br />
</p><p>How is the ssl debug log configured? Will the log be written to when wire shark is analyzing a trace file, or does wire shark need to be run live on the server? (in order to minimize the amount of software installed there, i installed only windump, and copy over the capture files to analyze on a separate machine running wireshark).</p></div><div id="comment-28235-info" class="comment-info"><span class="comment-age">(18 Dec '13, 00:10)</span> <span class="comment-user userinfo">dmc_lat47</span></div></div></div><div id="comment-tools-28231" class="comment-tools"></div><div class="clear"></div><div id="comment-28231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

