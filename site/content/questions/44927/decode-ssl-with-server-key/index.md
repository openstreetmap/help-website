+++
type = "question"
title = "Decode SSL with server key"
description = '''I am trying to decode a simple HTTPS session on wireshark 1.8.2 (sorry, it&#x27;s a bit old). I have the server key file (no password). Went to wireshark preference for SSL and added an entry for RSA list: IP:port:protocol:KeyFile as 127.0.0.1:443:http:/home/user/server.key. I thought I did everything ri...'''
date = "2015-08-07T16:33:00Z"
lastmod = "2015-08-11T16:26:00Z"
weight = 44927
keywords = [ "wireshark" ]
aliases = [ "/questions/44927" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decode SSL with server key](/questions/44927/decode-ssl-with-server-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44927-score" class="post-score" title="current number of votes">0</div><span id="post-44927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decode a simple HTTPS session on wireshark 1.8.2 (sorry, it's a bit old). I have the server key file (no password). Went to wireshark preference for SSL and added an entry for RSA list: IP:port:protocol:KeyFile as 127.0.0.1:443:http:/home/user/server.key.</p><p>I thought I did everything right, but it just won't decrypt. Wonder what could have gone wrong. Thanks.</p><p>Here are the <a href="http://pastebin.com/tPJwh84Z">debug log</a> and <a href="https://www.cloudshark.org/captures/39e43d6beb36">pcap file</a>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '15, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-44927" class="comments-container"></div><div id="comment-tools-44927" class="comment-tools"></div><div class="clear"></div><div id="comment-44927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44975"></span>

<div id="answer-container-44975" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44975-score" class="post-score" title="current number of votes">1</div><span id="post-44975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is shown here:</p><blockquote><p>dissect_ssl3_hnd_srv_hello <strong>can't find cipher suite 0x9E</strong></p></blockquote><p>cipher suite 0x94 is a <strong>Diffie Hellman</strong> based cipher (DHE-RSA-AES128-GCM-SHA256). Due to the nature of Diffie Hellman, you can't decrypt the SSL traffic with only the private key of the server. Diffie Hellmann is made and used to prevent exactly that. This is not a limitation of Wireshark, it's how it is supposed to work.</p><p>If you want to decrypt the traffic, you would need the so called <strong>session keys</strong>, generated by the client (browser). Some browsers will export those keys if told to do so.</p><blockquote><p><a href="http://security.stackexchange.com/questions/35639/decrypting-tls-in-wireshark-when-using-dhe-rsa-ciphersuites">http://security.stackexchange.com/questions/35639/decrypting-tls-in-wireshark-when-using-dhe-rsa-ciphersuites</a><br />
<a href="https://ask.wireshark.org/questions/37223/wireshark-decryption">https://ask.wireshark.org/questions/37223/wireshark-decryption</a><br />
<a href="https://ask.wireshark.org/questions/21011/decrypting-tls-messages-which-is-using-diffie-hellman-algorithm">https://ask.wireshark.org/questions/21011/decrypting-tls-messages-which-is-using-diffie-hellman-algorithm</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-44975" class="comments-container"></div><div id="comment-tools-44975" class="comment-tools"></div><div class="clear"></div><div id="comment-44975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

