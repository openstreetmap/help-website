+++
type = "question"
title = "How can I decrypt IKEv1 and/or ESP packets ?"
description = '''I am using the latest development release. When I try to create a new SA for ISAKMP, it asks for Initiator Cookie and Encryption Cookie. I know the initiator cookie but I am not sure where I can I get this encryption. I know all the configuration of my VPN (encryption algorithm, authentication algor...'''
date = "2012-06-18T06:27:00Z"
lastmod = "2018-06-26T10:17:00Z"
weight = 12019
keywords = [ "isakmp", "esp", "decryption", "ike", "ikev1" ]
aliases = [ "/questions/12019" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [How can I decrypt IKEv1 and/or ESP packets ?](/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12019-score" class="post-score" title="current number of votes">1</div><span id="post-12019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the latest development release. When I try to create a new SA for ISAKMP, it asks for Initiator Cookie and Encryption Cookie. I know the initiator cookie but I am not sure where I can I get this encryption. I know all the configuration of my VPN (encryption algorithm, authentication algorithm, pre-shared key) let me know if it is required here.</p><p>I have to tried to input the pre-shared-key there but it does not take it.</p><p>Please help. There is no documentation available for this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-isakmp" rel="tag" title="see questions tagged &#39;isakmp&#39;">isakmp</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ike" rel="tag" title="see questions tagged &#39;ike&#39;">ike</span> <span class="post-tag tag-link-ikev1" rel="tag" title="see questions tagged &#39;ikev1&#39;">ikev1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '12, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/f3c734c6d4986e0c52057d181b06c488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chetan1989&#39;s gravatar image" /><p><span>chetan1989</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chetan1989 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jul '13, 16:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-12019" class="comments-container"></div><div id="comment-tools-12019" class="comment-tools"></div><div class="clear"></div><div id="comment-12019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="12924"></span>

<div id="answer-container-12924" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12924-score" class="post-score" title="current number of votes">4</div><span id="post-12924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chetan1989 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>IKEv1 Decryption</strong></p><p>First of all: Wireshark 1.8.0 implements only 3DES and DES for IKEv1 decryption (same for version 1.6.8).</p><blockquote><p><code>See: epan\dissectors\packet-isakmp.c: decrypt_payload()</code><br />
</p></blockquote><p>If you want do decrypt any other algorithm, the dissector needs to be extended (Volunteers are welcome!). You can file an enhancement request for this at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>, possibly with a link to this question.</p><p>To get the required IKEv1 parameters for the dissector (<strong>Initiator's COOKIE</strong> and <strong>Encryption Key</strong>) you need debug output from your IPSEC implementation.<br />
</p><p>I tested with <a href="http://www.strongswan.org/">strongSwan 4.4</a> on Linux and with this <a href="http://cloudshark.org/captures/6ad6e687ed9d">capture file</a> (with the capture file and the data provided in this answer, you can try it yourself). To get the value of "enc key" in the log, you need at least this debug option: <strong><code>--debug-crypt</code></strong>.</p><p>Look for <strong>ICOOKIE</strong> and <strong>enc key</strong> in the Pluto debug log.</p><pre><code>gw205:/# ps auxww | grep pluto
root     24522  0.0  0.3  12572  3488 ?        Ss   15:46   0:00 /usr/libexec/ipsec/pluto --nofork --debug-raw --debug-crypt --debug-parsing --debug-emitting --debug-control --nocrsend --nat_traversal --keep_alive 60

strongSwan ipsec debug log:

2012:07:23-16:40:04 gw205 pluto[24522]: | 
2012:07:23-16:40:04 gw205 pluto[24522]: | *received whack message
2012:07:23-16:40:04 gw205 pluto[24522]: | creating state object #12 at 0x9fd77a8
2012:07:23-16:40:04 gw205 pluto[24522]: | ICOOKIE:  c6 d1 45 92  85 15 0c 7e
2012:07:23-16:40:04 gw205 pluto[24522]: | RCOOKIE:  00 00 00 00  00 00 00 00
2012:07:23-16:40:04 gw205 pluto[24522]: | peer:  c0 a8 8c c8
2012:07:23-16:40:04 gw205 pluto[24522]: | state hash entry 22

2012:07:23-16:40:14 gw205 pluto[24522]: | Skeyid_e:  b0 16 81 21  5f 16 20 23  03 18 6d 28  14 dc 56 86
2012:07:23-16:40:14 gw205 pluto[24522]: |   ca 5a 47 33
2012:07:23-16:40:14 gw205 pluto[24522]: | enc key:  44 9e 82 9e  a9 66 d4 21  fb cb 86 bd  7a d9 2e 86
2012:07:23-16:40:14 gw205 pluto[24522]: |   5a ba b1 5b  aa 5c 67 2a
2012:07:23-16:40:14 gw205 pluto[24522]: | IV:  dc f8 5e 03  f2 76 ab b9  89 e6 ae ff  46 a9 58 16
2012:07:23-16:40:14 gw205 pluto[24522]: |   f4 96 86 25</code></pre><p><strong>HINT:</strong> If you use any other IPSEC implementation please read the manual how to get that information.</p><p>Extract the values of <strong>ICOOKIE</strong> and <strong>'enc key'</strong> WITHOUT spaces. <strong>HINT:</strong> The "enc key" spans two lines!!</p><p><strong>ICOOKIE:</strong> c6d1459285150c7e<br />
<strong>Enc Key:</strong> 449e829ea966d421fbcb86bd7ad92e865abab15baa5c672a</p><p>Use those values for</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Protocols -&gt; ISAKMP -&gt; IKEv1 Decryption Table:</code><br />
</p></blockquote><p>Test File: <a href="https://www.cloudshark.org/captures/6ad6e687ed9d">ipsec.pcap</a></p><p><strong>Result without decryption</strong>:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IKEv1_no_decrypt_phase_1.png" alt="IKEv1 main mode - no decryption" /><br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IKEv1_no_decrypt_phase_2.png" alt="IKEv1 quick mode - no decryption" /></p><p><strong>Result with decryption</strong>:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IKEv1_decrypted_phase_1.png" alt="IKEv1 main mode - WITH decryption" /><br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IKEv1_decrypted_phase_2.png" alt="IKEv1 quick mode - WITH decryption" /></p><p><strong>ESP Decryption</strong></p><p>To decrypt ESP packets with Wireshark 1.8.0, you need again debug output from your IPSEC implementation. For Linux and strongSwan, you'll get that information with this command:</p><blockquote><p><code>ip xfrm state</code><br />
</p></blockquote><p>Output:</p><pre><code>gw205:/ # ip xfrm state
src 192.168.140.200 dst 192.168.140.205
        proto esp spi 0x0879355b reqid 16421 mode tunnel
        replay-window 32 flag noecn nopmtudisc af-unspec
        auth hmac(sha1) 0xb8dd42a1c505bed19c2bf23cef00e5d8223c2a5b
        enc cbc(des3_ede) 0xae76ea430b10c72c882c4aeab2283444c54f913d87f5e109
src 192.168.140.205 dst 192.168.140.200
        proto esp spi 0x1c0d7b38 reqid 16421 mode tunnel
        replay-window 32 flag noecn nopmtudisc af-unspec
        auth hmac(sha1) 0xc364660133b04a4f20e52000dbe4a6ba154c09c1
        enc cbc(des3_ede) 0x39e87c9ca500616b36f2f0d3c7fb688621d7bbf31414abbd</code></pre><p>Use those values for the ESP dissector parameters, as shown in the following screenshots. <strong>HINT:</strong> Take care not to add a space at the end of any parameter (SPI, key, etc.) as decryption will not work in that case.</p><p>First enable ESP decryption.</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Protocols -&gt; ESP -&gt; Attempt to detect/decode encrypted ESP payloads</code></p></blockquote><p><img src="https://osqa-ask.wireshark.org/upfiles/ESP_parameter.png" alt="ESP Parameter" /></p><p>Then add the two ESP SAs (one for each direction!)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESP_parameter_spi_a.png" alt="SPI_A" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESP_parameter_spi_b.png" alt="SPI_B" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESP_parameter_SA_all.png" alt="ALL SAs" /></p><p>If the parameters match the capture file data, Wireshark will be able to dissect the ESP packets.</p><p><strong>Result without decryption</strong>:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESP_no_decrypt.png" alt="ESP no decryption" /></p><p><strong>Result WITH decryption</strong>:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESP_decrypted.png" alt="ESP decrypted" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '15, 06:37</strong> </span></p></div></div><div id="comments-container-12924" class="comments-container"><span id="56853"></span><div id="comment-56853" class="comment"><div id="post-56853-score" class="comment-score"></div><div class="comment-text"><p>can you give command: ip xfrm state --- for windows?</p></div><div id="comment-56853-info" class="comment-info"><span class="comment-age">(31 Oct '16, 02:05)</span> <span class="comment-user userinfo">friis</span></div></div><span id="64339"></span><div id="comment-64339" class="comment"><div id="post-64339-score" class="comment-score"></div><div class="comment-text"><p>Could you fix/update the images referenced above? They all show as broken links now.</p></div><div id="comment-64339-info" class="comment-info"><span class="comment-age">(26 Jun '18, 10:17)</span> <span class="comment-user userinfo">slm</span></div></div></div><div id="comment-tools-12924" class="comment-tools"></div><div class="clear"></div><div id="comment-12924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12024"></span>

<div id="answer-container-12024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12024-score" class="post-score" title="current number of votes">0</div><span id="post-12024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>did you add the PSK under the ESP options?</p><blockquote><p><code>Edit -&gt; Preferences -&gt; ESP -&gt; ESP SAs -&gt; New -&gt; Encryption Key</code><br />
</p></blockquote><p>BTW: Did you check this?</p><blockquote><p><code>http://wiki.wireshark.org/ESP_Preferences</code><br />
</p></blockquote><p>Especially, if your version of Wireshark is built with libcrypt!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '12, 07:36</strong> </span></p></div></div><div id="comments-container-12024" class="comments-container"><span id="12025"></span><div id="comment-12025" class="comment"><div id="post-12025-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply.</p><p>I don't see option to create New Encryption Key, there is an option to create a new SA (Security Association) wherein I provide the Encryption Key. But when I try to put the same key in ISAKMP Encryption Key field it gives me an error "error in field 'Encryption Key': Error parsing hex string"</p><p>I don't know how to get the hex value.</p><p>P.S. My wireshark is built with Gcrypt. I don't think that could be a problem because I can decrypt ESP packets easily</p></div><div id="comment-12025-info" class="comment-info"><span class="comment-age">(18 Jun '12, 07:46)</span> <span class="comment-user userinfo">chetan1989</span></div></div><span id="12027"></span><div id="comment-12027" class="comment"><div id="post-12027-score" class="comment-score"></div><div class="comment-text"><blockquote><p>because I can decrypt ESP packets easily</p></blockquote><p>O.K. I think I misunderstood your request. Do you want to decrypt IKE Phase I packets 5+6 (the encrypted ones) and possibly the whole IKE Phase II traffic?</p></div><div id="comment-12027-info" class="comment-info"><span class="comment-age">(18 Jun '12, 08:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12029"></span><div id="comment-12029" class="comment"><div id="post-12029-score" class="comment-score"></div><div class="comment-text"><p>Yes you are correct</p></div><div id="comment-12029-info" class="comment-info"><span class="comment-age">(18 Jun '12, 12:08)</span> <span class="comment-user userinfo">chetan1989</span></div></div></div><div id="comment-tools-12024" class="comment-tools"></div><div class="clear"></div><div id="comment-12024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12592"></span>

<div id="answer-container-12592" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12592-score" class="post-score" title="current number of votes">0</div><span id="post-12592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>If you are using racoon (from ipsec-tools), you can see the encryption key from the debug logs of racoon. e.g:</p><p>2012-07-11 11:35:55: DEBUG: final encryption key computed: 2012-07-11 11:35:55: DEBUG: 79d5eabc 78ae740b 47258300 f8de371e a4a9da87 4facf41</p><p>Also, I had found issues in decryption when i use aes algorithm. With 3des, decryption works fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '12, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/e24ac4559501b4fc421cb481aa6455d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="divya&#39;s gravatar image" /><p><span>divya</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="divya has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-12592" class="comments-container"></div><div id="comment-tools-12592" class="comment-tools"></div><div class="clear"></div><div id="comment-12592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59349"></span>

<div id="answer-container-59349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59349-score" class="post-score" title="current number of votes">0</div><span id="post-59349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are looking for the cookie and encryption key in <code>vpnc</code>'s output, run as <code>vpnc --debug 99</code> and look for lines matching the following:</p><pre><code>WARNING! active debug level is &gt;= 99, output includes username and password (hex encoded)
...
S4.1 create_nonce
 [2017-02-11 20:15:04]
   i_cookie: da849309 7bd61433
...
S4.4 AM_packet2
...
   enc-key:
   a635f195 bd412619 17821107 c7d32726 9f5e4781 2ffd7992</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '17, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/a913ff1821be75c981d066f685816ed9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dlenski&#39;s gravatar image" /><p><span>dlenski</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dlenski has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '17, 20:42</strong> </span></p></div></div><div id="comments-container-59349" class="comments-container"></div><div id="comment-tools-59349" class="comment-tools"></div><div class="clear"></div><div id="comment-59349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

