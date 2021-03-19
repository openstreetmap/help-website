+++
type = "question"
title = "Decrypting TLS messages which is using Diffie hellman algorithm"
description = '''From the Client I am logging all the master secret key for all the sessions.Using that key how to generate the .key file and is that be possible to decrypt the DHE messages in wireshark using Master secret key? Wireshark will be able to understand the way of decrypting DHE?'''
date = "2013-05-07T21:28:00Z"
lastmod = "2013-05-15T03:02:00Z"
weight = 21011
keywords = [ "decryption", "openssl", "diffie-hellman" ]
aliases = [ "/questions/21011" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting TLS messages which is using Diffie hellman algorithm](/questions/21011/decrypting-tls-messages-which-is-using-diffie-hellman-algorithm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21011-score" class="post-score" title="current number of votes">0</div><span id="post-21011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From the Client I am logging all the master secret key for all the sessions.Using that key how to generate the .key file and is that be possible to decrypt the DHE messages in wireshark using Master secret key? Wireshark will be able to understand the way of decrypting DHE?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-openssl" rel="tag" title="see questions tagged &#39;openssl&#39;">openssl</span> <span class="post-tag tag-link-diffie-hellman" rel="tag" title="see questions tagged &#39;diffie-hellman&#39;">diffie-hellman</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '13, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/3606fb2f161676306a345c0e2809e550?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalai&#39;s gravatar image" /><p><span>Kalai</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalai has no accepted answers">0%</span></p></div></div><div id="comments-container-21011" class="comments-container"></div><div id="comment-tools-21011" class="comment-tools"></div><div class="clear"></div><div id="comment-21011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21012"></span>

<div id="answer-container-21012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21012-score" class="post-score" title="current number of votes">1</div><span id="post-21012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While it is not possible to create the private key of the server from the master keys, you will be able to decrypt the sessions in the tracefile that correspond to the logged master keys.</p><p>You will need to put the master keys in a file as follows (from the source code):</p><pre><code>         &quot;RSA &lt;EPMS&gt; &lt;PMS&gt;\n&quot;
         &quot;RSA Session-ID:&lt;SSLID&gt; Master-Key:&lt;MS&gt;\n&quot;
         &quot;\n&quot;
         &quot;Where:\n&quot;
         &quot;&lt;EPMS&gt; = First 8 bytes of the Encrypted PMS\n&quot;
         &quot;&lt;PMS&gt; = The Pre-Master-Secret (PMS)\n&quot;
         &quot;&lt;SSLID&gt; = The SSL Session ID\n&quot;
         &quot;&lt;MS&gt; = The Master-Secret (MS)\n&quot;
         &quot;\n&quot;
         &quot;(All fields are in hex notation)&quot;,</code></pre><p>So for example:</p><pre><code>RSA Session-ID:fbcf322128ed0a00b272d6ac85843f50deccdd94ac33261523189639f5ba189a Master-Key:bda6ea472f6c39a9fcfd5dc79eb161d1a4cae5d924fdde800f276263fd6df1ee8ed246b5a6412e328eb85744c9bf7cf2
RSA Session-ID:db00c2aad79cfda109ce4f65a9801aa8d5f1bbeb9e1f848f6a2f7551f9de7577 Master-Key:92cdc769c670ba6f48cfe756992ad435401a26d0235900c0f67c846b5f360c108df167ca6b6f443f4d2b118de0ccadb8</code></pre><p>You then point to the file in the SSL protocol preferences by using the "(Pre-)Master-secret log filename" setting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '13, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '13, 22:37</strong> </span></p></div></div><div id="comments-container-21012" class="comments-container"><span id="21014"></span><div id="comment-21014" class="comment"><div id="post-21014-score" class="comment-score"></div><div class="comment-text"><p>Hi.Thanks for the reply.Do I need Encrypted PMS and PMS keys? If so What are those keys? As Master secret is used to encrypt and decrypt the messages in DHE, only master secret and session Id's are not enough like in your example?</p></div><div id="comment-21014-info" class="comment-info"><span class="comment-age">(08 May '13, 00:11)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21015"></span><div id="comment-21015" class="comment"><div id="post-21015-score" class="comment-score"></div><div class="comment-text"><p>And also I used %02x format to print Master secret. Should I have to use the same format for session Id's also?</p></div><div id="comment-21015-info" class="comment-info"><span class="comment-age">(08 May '13, 00:57)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21016"></span><div id="comment-21016" class="comment"><div id="post-21016-score" class="comment-score"></div><div class="comment-text"><p>You will only need the SessionID/Master Secret combinations. The other format is for the export that Chrome/Firefox can make when compiled with a debug option.</p><p>Yes, the sessionID should also be in hexformat.</p></div><div id="comment-21016-info" class="comment-info"><span class="comment-age">(08 May '13, 01:02)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21020"></span><div id="comment-21020" class="comment"><div id="post-21020-score" class="comment-score"></div><div class="comment-text"><p>I provided the log file in Edit&gt;preference&gt;pre-master key log file tab (RSA Session-ID:9835348 Master-Key:EC6B8B3131B3842CCFB47308B73B31BB9F870E43B1FA26098064B2C724FA14E910D8F509676BA37D74F15AA6351EDBC0) But nothing is happening ... The ssl debug file is showing the following:</p><p><code> dissect_ssl enter frame #1 (first time) ssl_session_init: initializing ptr 056610A4 size 588   conversation = 05660E64, ssl_session = 056610A4   record: offset = 0, reported_length_remaining = 437 dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10 dissect_ssl3_record: content_type 23 Application Data decrypt_ssl3_record: app_data len 432, ssl state 0x10 association_find: TCP port 9970 found 00000000 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available association_find: TCP port 9970 found 00000000 association_find: TCP port 3456 found 00000000 association_find: TCP port 0 found 00000000</code></p><p>What could be the issue?</p></div><div id="comment-21020-info" class="comment-info"><span class="comment-age">(08 May '13, 03:47)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21028"></span><div id="comment-21028" class="comment"><div id="post-21028-score" class="comment-score"></div><div class="comment-text"><p>The SSL SessionID is usually a 32 octet value. It's best to take it from the ServerHello:</p><pre><code>Session ID Length: 32
Session ID: db00c2aad79cfda109ce4f65a9801aa8d5f1bbeb9e1f848f...</code></pre><p>The value listed by wireshark is truncated, but can be capied by rightclick -&gt; copy -&gt; bytes -&gt; hex stream. This will result in:</p><pre><code>db00c2aad79cfda109ce4f65a9801aa8d5f1bbeb9e1f848f6a2f7551f9de7577</code></pre></div><div id="comment-21028-info" class="comment-info"><span class="comment-age">(08 May '13, 07:17)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21036"></span><div id="comment-21036" class="comment not_top_scorer"><div id="post-21036-score" class="comment-score"></div><div class="comment-text"><p>Hi in the server hello the session ID length is 0, and also am getting the following lines in the debug file checking keylog line: RSA Session-ID:9E7D348s3 line does not match encrypted pre-master secret line does not match checking keylog line: Master-Key:530BAAC26D6D57CE75B1DF8284EA57291882F46BD337DC72171BFBC3201F8B263B0E98607C1F4F673E39052AC70FC23F line does not match</p><p>Is that the problem with the session-ID?</p></div><div id="comment-21036-info" class="comment-info"><span class="comment-age">(08 May '13, 08:56)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21040"></span><div id="comment-21040" class="comment not_top_scorer"><div id="post-21040-score" class="comment-score"></div><div class="comment-text"><p>OK, if there is no session id, you will need to revert to the first method of logging the first 8 octets of the encrypted Pre-Mastersecret together with the Pre-Mastersecret. Both in hex notation.</p><p>This will need to look like this:</p><pre><code>RSA 46BD337DC72171BF \
  B1DF8284EA57291882F46BD337DC72171BFBC3201F8B263B0E98607C1FB1DF8284EA57291882F46BD337DC72171BFBC3</code></pre></div><div id="comment-21040-info" class="comment-info"><span class="comment-age">(08 May '13, 14:28)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21055"></span><div id="comment-21055" class="comment not_top_scorer"><div id="post-21055-score" class="comment-score"></div><div class="comment-text"><p>Hi my keylog file is looking like this:</p><pre><code>RSA D0135C1A76C9857E C80D3BC9FD3654BC95A3E68124B747C6B581FD06EC427AEFAD871104F5C42DCFBBF237067FAABF11266A0D76B049CBC3CB68DFC3659736DABEE5CA092B5D05831498F6354EDE3A0CD65DFDA7701C1F4600834FFDE9AA9B5848437255F4391A78E779084ADD5D5F5FEA8E05E8E97F02BC5613C1B73082AF6EB3A0B52BDACBEBC8
RSA Session-ID:8C8C348
Master-Key:3FB3843CDD2DC0FB7AD4C81B75A19C4434AEA0A5B977EB562BB2B099A180B0884CBFC380A03FA767AF01032601703C6B</code></pre><p>Still I am getting,</p><pre><code>trying to use SSL keylog in C:\keylog.txt
  checking keylog line: RSA D0135C1A76C9857E C80D3BC9FD3654BC95A3E68124B747C6B581FD06EC427AEFAD871104F5C42DCFBBF237067FAABF11266A0D76B049CBC3CB68DFC3659736DABEE5CA092B5D05831498F6354EDE3A0CD65DFDA7701C1F4600834FFDE9AA9B5848437255F4391A78E779084ADD5D5F5FEA8E05E8E97F02BC5613C1B73082AF6EB3A0B52BDACBEBC8
    line does not match encrypted pre-master secret    line does not match
  checking keylog line: RSA Session-ID:8C8C348
    line does not match encrypted pre-master secret    line does not match
  checking keylog line: Master-Key:3FB3843CDD2DC0FB7AD4C81B75A19C4434AEA0A5B977EB562BB2B099A180B0884CBFC380A03FA767AF01032601703C6
    line does not match
  record: offset = 139, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 85 offset 150 length 7676257 bytes, remaining 198</code></pre></div><div id="comment-21055-info" class="comment-info"><span class="comment-age">(09 May '13, 07:18)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21061"></span><div id="comment-21061" class="comment not_top_scorer"><div id="post-21061-score" class="comment-score"></div><div class="comment-text"><p>Are you able to post the tracefile on www.cloudshark.org? If you are worried about the application data, only the SSL handshake is needed.</p></div><div id="comment-21061-info" class="comment-info"><span class="comment-age">(09 May '13, 09:44)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21077"></span><div id="comment-21077" class="comment not_top_scorer"><div id="post-21077-score" class="comment-score"></div><div class="comment-text"><p>I have added the file in the link: <a href="http://cloudshark.org/captures/4161807df249">http://cloudshark.org/captures/4161807df249</a> RSA Session-ID:8C8C348 Master-Key:3FB3843CDD2DC0FB7AD4C81B75A19C4434AEA0A5B977EB562BB2B099A180B0884CBFC380A03FA767AF01032601703C6B PreMaster key-C80D3BC9FD3654BC95A3E68124B747C6B581FD06EC427AEFAD871104F5C42DCFBBF237067FAABF11266A0D76B049CBC3CB68DFC3659736DABEE5CA092B5D05831498F6354EDE3A0CD65DFDA7701C1F4600834FFDE9AA9B5848437255F4391A78E779084ADD5D5F5FEA8E05E8E97F02BC5613C1B73082AF6EB3A0B52BDACBEBC8</p></div><div id="comment-21077-info" class="comment-info"><span class="comment-age">(09 May '13, 22:21)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21110"></span><div id="comment-21110" class="comment not_top_scorer"><div id="post-21110-score" class="comment-score"></div><div class="comment-text"><p>I am having access to the client completely.Any other workaround which will decrypt the application data in wireshark?</p></div><div id="comment-21110-info" class="comment-info"><span class="comment-age">(13 May '13, 03:11)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21111"></span><div id="comment-21111" class="comment not_top_scorer"><div id="post-21111-score" class="comment-score"></div><div class="comment-text"><p>I was looking at your trace and made a trace myself, but I need to look into the source code to see if it is a simple fix to be able to decrypt SSL sessions for which the key has been exchanged by DH. It does not seem to do that now, even though I believe that logging the (pre-)master secret would be enough to go on (as long as it can be indexed in some way to identify the session).</p><p>Unfortunately, I do not have the time at the moment to dive some deeper. So for now I'm afraid there is no decryption possible for DH sessions, not even with the session keys logged.</p></div><div id="comment-21111-info" class="comment-info"><span class="comment-age">(13 May '13, 04:47)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21145"></span><div id="comment-21145" class="comment not_top_scorer"><div id="post-21145-score" class="comment-score"></div><div class="comment-text"><p>Hi The decryption of DHE session is working when I used CLIENT_RANDOM &lt;hex clientrandom=""&gt; &lt;hex masterkey=""&gt;. When I used capital letters for hex it was not working and its working fine when I use small letters.Thanks for your help...</p></div><div id="comment-21145-info" class="comment-info"><span class="comment-age">(15 May '13, 03:02)</span> <span class="comment-user userinfo">Kalai</span></div></div></div><div id="comment-tools-21012" class="comment-tools"><span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a></div><div class="clear"></div><div id="comment-21012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

