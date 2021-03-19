+++
type = "question"
title = "Decrypt SSL"
description = '''I am attempting to decrypt SSL and have the pem file included but I am not able to see the decrypted application data. dissect_ssl enter frame #15 (first time)  conversation = 0000000007C268B8, ssl_session = 0000000007C26EC8  record: offset = 0, reported_length_remaining = 458 dissect_ssl3_record: c...'''
date = "2013-09-09T09:31:00Z"
lastmod = "2013-09-09T22:00:00Z"
weight = 24488
keywords = [ "ssl" ]
aliases = [ "/questions/24488" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypt SSL](/questions/24488/decrypt-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24488-score" class="post-score" title="current number of votes">0</div><span id="post-24488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to decrypt SSL and have the pem file included but I am not able to see the decrypted application data.</p><pre><code>dissect_ssl enter frame #15 (first time)
  conversation = 0000000007C268B8, ssl_session = 0000000007C26EC8
  record: offset = 0, reported_length_remaining = 458
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 453, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 34543 found 0000000000000000
association_find: TCP port 443 found 0000000006CF10C0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '13, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/25dd8fab6fe2fc138cae973bbec62ffe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davidmoody&#39;s gravatar image" /><p><span>davidmoody</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davidmoody has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Sep '13, 09:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-24488" class="comments-container"></div><div id="comment-tools-24488" class="comment-tools"></div><div class="clear"></div><div id="comment-24488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24497"></span>

<div id="answer-container-24497" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24497-score" class="post-score" title="current number of votes">0</div><span id="post-24497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are three things you need to make sure of to make decryption work in Wireshark:</p><ul><li>Provide the proper private key (check the ssl-debug log to see if it actually loaded OK)</li><li>Make sure the whole SSL handshake for this SSL session is in the tracefile (make sure you see the "Certificate" message from the server)</li><li>Check whether you're <strong>not</strong> using a DiffieHellman cipher (the cipher in the ServerHello message should not contain DHE or DH)</li></ul><p>If that does not get you started, have a look at my <a href="http://sharkfest.wireshark.org/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">Sharkfest presentation on troubleshooting SSL</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24497" class="comments-container"></div><div id="comment-tools-24497" class="comment-tools"></div><div class="clear"></div><div id="comment-24497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

