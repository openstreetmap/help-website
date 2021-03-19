+++
type = "question"
title = "SSL decoding not working 1.6.5 on Windows 7 64-bit"
description = '''The routine seems straight forward:  remote server has address  75.147.41.121 with port 8443 I have created its private key and placed its pem encoded form on the client for wireshark- in the preferences/protocol/ssl I have added the required information such that the ssl_keys file contains the foll...'''
date = "2012-02-21T02:08:00Z"
lastmod = "2012-02-21T05:47:00Z"
weight = 9158
keywords = [ "ssl" ]
aliases = [ "/questions/9158" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decoding not working 1.6.5 on Windows 7 64-bit](/questions/9158/ssl-decoding-not-working-165-on-windows-7-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9158-score" class="post-score" title="current number of votes">0</div><span id="post-9158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The routine seems straight forward:</p><ul><li>remote server has address 75.147.41.121 with port 8443</li><li>I have created its private key and placed its pem encoded form on the client for wireshark-</li><li>in the preferences/protocol/ssl I have added the required information such that the ssl_keys file contains the following:-</li><li>"75.147.121.41","8443","http","C:\users\brian\projects\cJoxPlz\demo\BaseManagerWan_SecureRawHttpSend\res\tomcat75.pem",""</li></ul><p>Everything looks correct according to the documentation, this forum, googling etc. The ssl debug log indicates that the pem-encoded private key is properly loaded:</p><pre><code>ssl_association_remove removing TCP 8443 - http handle 000000000418A280
Private key imported: KeyID bc:43:14:85:bd:de:53:9a:67:10:1d:f3:26:9f:b1:42:...
ssl_init IPv4 addr &#39;75.147.121.41&#39; (75.147.121.41) port &#39;8443&#39; filename &#39;C:\users\brian\projects\JoxPlz\demo\BaseManagerWan_SecureRawHttpSend\res\tomcat75.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\users\brian\projects\JoxPlz\demo\BaseManagerWan_SecureRawHttpSend\res\tomcat75.pem successfully loaded.
association_add TCP port 8443 protocol http handle 000000000418A280</code></pre><p>But during an actual exchange the very next block of information in the debug log gives the following error:</p><pre><code>dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0000000005C51D30 size 680
  conversation = 0000000005C51880, ssl_session = 0000000005C51D30
  record: offset = 0, reported_length_remaining = 103
packet_from_server: is from server - FALSE
ssl_find_private_key server 75.147.41.121:8443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
client random len: 32 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01</code></pre><p>It can't find the private key for the server yet it is successfully loaded. Restart of wireshark, system reboot, etc (also suggested) does not solve the problem. Address and all other parameters look correct. I cannot see what I am doing wrong. So all I get to see is SSL encrypted junk and no possibility to debug. (Axis2/Rampart doesn't like my SAML token and I don't know why!)</p><p>Do I need the private key of the client? (The client key validation is not part of this exchange.)-</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '12, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/d85cfde395796ff8d2093974f53173b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gyannea&#39;s gravatar image" /><p><span>gyannea</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gyannea has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Feb '12, 04:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-9158" class="comments-container"></div><div id="comment-tools-9158" class="comment-tools"></div><div class="clear"></div><div id="comment-9158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9159"></span>

<div id="answer-container-9159" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9159-score" class="post-score" title="current number of votes">2</div><span id="post-9159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gyannea has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check your IP addresses. In your text you state the server has 75.147.<strong>41.121</strong>, yet the line showing your key definition has 75.147.<strong>121.41</strong>.</p><p>This is reflected in the debug log output:</p><p>ssl_init IPv4 addr '75.147.<strong>121.41</strong>' (75.147.<strong>121.41</strong>) port '8443' ...</p><p>ssl_find_private_key server 75.147.<strong>41.121</strong>:8443</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '12, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9159" class="comments-container"><span id="9161"></span><div id="comment-9161" class="comment"><div id="post-9161-score" class="comment-score"></div><div class="comment-text"><p>Man you are a god send! How could I do something so stupid!?! Do you know I spent a whole day on that? Reminds me of a stupid error on a stats test years ago where I wrote 2 + 2 = 2 and had to have the prof point it out after days of trying (n vain) to find the mistake. Worse is that someone else made a similar mistake on this site SO I ACTUALLY LOOKED for such an error. AAARRRG! But thanks. It works!</p></div><div id="comment-9161-info" class="comment-info"><span class="comment-age">(21 Feb '12, 04:44)</span> <span class="comment-user userinfo">gyannea</span></div></div><span id="9163"></span><div id="comment-9163" class="comment"><div id="post-9163-score" class="comment-score"></div><div class="comment-text"><p>No problem, we've all made similar mistakes. Could you accept the answer instead of voting it up, thanks.</p></div><div id="comment-9163-info" class="comment-info"><span class="comment-age">(21 Feb '12, 04:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="9165"></span><div id="comment-9165" class="comment"><div id="post-9165-score" class="comment-score">1</div><div class="comment-text"><p>Ahh, took a while but now I see how to mark something as answered.</p></div><div id="comment-9165-info" class="comment-info"><span class="comment-age">(21 Feb '12, 05:47)</span> <span class="comment-user userinfo">gyannea</span></div></div></div><div id="comment-tools-9159" class="comment-tools"></div><div class="clear"></div><div id="comment-9159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

