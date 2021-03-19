+++
type = "question"
title = "LDAP SSL malformed packet causing error in decoding"
description = '''Hi everybody, I&#x27;m trying to debug LDAP SSL communication and experience a problem with SSL decryption. After a malformed packet is seen from the client, all the client data are no longer decoded by wireshark. Kindly note that the server data is still decoded by wireshark and the SSL debug file shows...'''
date = "2014-01-09T03:33:00Z"
lastmod = "2014-01-13T07:10:00Z"
weight = 28720
keywords = [ "ssl", "decryption", "ldap" ]
aliases = [ "/questions/28720" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LDAP SSL malformed packet causing error in decoding](/questions/28720/ldap-ssl-malformed-packet-causing-error-in-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28720-score" class="post-score" title="current number of votes">0</div><span id="post-28720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>I'm trying to debug LDAP SSL communication and experience a problem with SSL decryption. After a malformed packet is seen from the client, all the client data are no longer decoded by wireshark. Kindly note that the server data is still decoded by wireshark and the SSL debug file shows some information of the data that was no decrypted in wireshark.</p><p>Below is the link to the ssl debug log and a snapshot of the packets as seen in wireshark</p><p>SSL debug: <a href="https://dl.dropboxusercontent.com/u/68667178/ssl.log">link text</a></p><p>image: <a href="https://osqa-ask.wireshark.org/upfiles/Capture_13.PNG">link text</a></p><p>Could you advise me on a way to resolve that issue so that I could decode all the packets? Could it be a bug?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ldap" rel="tag" title="see questions tagged &#39;ldap&#39;">ldap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '14, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/6e15c129ad20741c691b4b1ee8316a89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MSK&#39;s gravatar image" /><p><span>MSK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MSK has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jan '14, 03:34</strong> </span></p></div></div><div id="comments-container-28720" class="comments-container"></div><div id="comment-tools-28720" class="comment-tools"></div><div class="clear"></div><div id="comment-28720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28829"></span>

<div id="answer-container-28829" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28829-score" class="post-score" title="current number of votes">0</div><span id="post-28829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Let's have a look at the 'malformed' frame #21 in the debug log.</p><pre><code>dissect_ssl enter frame #21 (first time)
  conversation = 0000000007AFC998, ssl_session = 0000000007AFCFA8
  record: offset = 0, reported_length_remaining = 202
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
| 2d 62 f5 53 ae 48 a8 54 91 eb 4e 92 3b ff 5f 2b |-bõS®H¨T‘ëN’;ÿ_+|
| f5 e6 4c 49 ad 52 38 88 9a af e7 8e da 68 4c e1 |õæLI­R8.š¯çŽÚhLá|
Plaintext[32]:
| 30 b5 c5 d7 ce 5b d2 41 c9 e3 a8 88 1b 45 b5 e0 |0µÅ×Î[ÒAÉã¨..Eµà|
| 2d f8 2e 22 80 0a 0a 0a 0a 0a 0a 0a 0a 0a 0a 0a |-ø.&quot;............|
ssl_decrypt_record found padding 10 final len 21
checking mac (len 1, version 301, ct 23 seq 2)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| b5 c5 d7 ce 5b d2 41 c9 e3 a8 88 1b 45 b5 e0 2d |µÅ×Î[ÒAÉã¨..Eµà-|
| f8 2e 22 80                                     |ø.&quot;.            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 1, seq = 64, nxtseq = 65
association_find: TCP port 46329 found 0000000000000000
association_find: TCP port 8400 found 0000000006DEFED0
dissect_ssl3_record decrypted len 1
decrypted app data fragment[1]:
| 30                                              |0               |

dissect_ssl3_record found association 0000000006DEFED0</code></pre><p>As you can see, the decrypted data part (only one byte: 0x30) is not a valid LDAP frame (obvious). The question is, why the dissector believes there is only 32 bytes of 'app_data len', whereas the frame len itself is 268 bytes. That does not match. Interesting: The frame and the MAC get decrypted correctly!??!</p><p>This could be a dissector bug. Is the frame in question somehow fragmented (at IP level)?</p><p>Please open a bug request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p><strong>HOWEVER</strong> to be able to debug this particular problem, you would have to provide some 'private' data, as</p><ul><li>the capture file itself</li><li>the server key</li></ul><p>I'm not sure if that's possible, as the ssl debug log suggests you have taken the capture file at a production site !?!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '14, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28829" class="comments-container"><span id="28834"></span><div id="comment-28834" class="comment"><div id="post-28834-score" class="comment-score"></div><div class="comment-text"><p>I was afraid that the both the capture and the key would be needed. Unfortunately this is not possible, i had a hard time posting the SSL debug log in itself. Is there another alternative that we can use? can i open a bug and provide the same information i provided here or it wouldn't be enough?</p><p>The "Reassemble fragmented IPv4" option is checked and i have also noticed that this link <a href="http://ask.wireshark.org/questions/25156/ldap-ssl-decrypt-issue">http://ask.wireshark.org/questions/25156/ldap-ssl-decrypt-issue</a></p><p>describe the same issue (more or less)</p><p>Regards, MSK</p></div><div id="comment-28834-info" class="comment-info"><span class="comment-age">(12 Jan '14, 23:09)</span> <span class="comment-user userinfo">MSK</span></div></div><span id="28841"></span><div id="comment-28841" class="comment"><div id="post-28841-score" class="comment-score"></div><div class="comment-text"><blockquote><p>can i open a bug and provide the same information i provided here or it wouldn't be enough?</p></blockquote><p>I believe without the key, there is no way to debug this, but of course you can try. Maybe one of the developers has seen that before, but had no time to fix it ;-)</p><blockquote><p>The "Reassemble fragmented IPv4" option is checked</p></blockquote><p>O.K. but is the frame itself part of a fragment (see the IP header options for fragmentation)</p><blockquote><p>describe the same issue (more or less)</p></blockquote><p>no, that's a different problem as far as I could see.</p></div><div id="comment-28841-info" class="comment-info"><span class="comment-age">(13 Jan '14, 07:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28842"></span><div id="comment-28842" class="comment"><div id="post-28842-score" class="comment-score"></div><div class="comment-text"><p><strong>HINT:</strong> you could try to <strong>decrypt</strong> the stream <strong>with ssldump</strong> (<a href="http://www.rtfm.com/ssldump/">http://www.rtfm.com/ssldump/</a> - should be available in the repository of several Linux distributions). If that works, it's a bug in the dissector. If ssldump fails to decrypt the traffic, your LDAP client messed up the encryption and/or the LDAP request.</p></div><div id="comment-28842-info" class="comment-info"><span class="comment-age">(13 Jan '14, 07:10)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28829" class="comment-tools"></div><div class="clear"></div><div id="comment-28829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

