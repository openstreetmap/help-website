+++
type = "question"
title = "Client sends FIN immediately after SSL Handshake"
description = '''One of the user is not able to open a ssl website,after capture there is a below pattern,immediately after SSL handshake client is sending FIN packet.what could be reason for this.Client machine is xp and domain which he is trying has a multi domain certificate. 1) Client sends [SYN] to server. 2) S...'''
date = "2014-05-25T05:25:00Z"
lastmod = "2014-07-01T05:36:00Z"
weight = 33054
keywords = [ "ssl" ]
aliases = [ "/questions/33054" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Client sends FIN immediately after SSL Handshake](/questions/33054/client-sends-fin-immediately-after-ssl-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33054-score" class="post-score" title="current number of votes">0</div><span id="post-33054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>One of the user is not able to open a ssl website,after capture there is a below pattern,immediately after SSL handshake client is sending FIN packet.what could be reason for this.Client machine is xp and domain which he is trying has a multi domain certificate.</p><pre><code>1) Client sends [SYN] to server.
2) Server sends [SYN,ACK] to client.
3) Client sends [ACK] to server.
4) Client sends the message “Client Hello” to the server.
5) Server sends its public key with the message “Server Hello, Certificate, Server Hello Done”
6) Client sends its public key with the message “Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message”
7) Server sends encrypted handshake message with the message “Change Cipher Spec, Encrypted Handshake Message”
8) Client sends [FIN,ACK]
9) Server sends RST</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '14, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '14, 05:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-33054" class="comments-container"></div><div id="comment-tools-33054" class="comment-tools"></div><div class="clear"></div><div id="comment-33054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="34295"></span>

<div id="answer-container-34295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34295-score" class="post-score" title="current number of votes">1</div><span id="post-34295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You mentioned Windows XP. In the capture, I can see that the certificates are signed with a SHA256 ("SHA-2") algorithm. The older Windows XP versions do not support this algorithm, you need to have at least Windows XP SP3 for supporting these certificates.</p><p>See also this MS KB article: <a href="http://support.microsoft.com/kb/968730">Windows Server 2003 and Windows XP clients cannot obtain certificates from a Windows Server 2008-based certification authority (CA) if the CA is configured to use SHA2 256 or higher encryption</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '14, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-34295" class="comments-container"><span id="34318"></span><div id="comment-34318" class="comment"><div id="post-34318-score" class="comment-score"></div><div class="comment-text"><p>Great information,thanks for giving your thoughts.</p></div><div id="comment-34318-info" class="comment-info"><span class="comment-age">(01 Jul '14, 04:54)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="34319"></span><div id="comment-34319" class="comment"><div id="post-34319-score" class="comment-score"></div><div class="comment-text"><p>I see you have asked many questions here, please consider marking some as answered and/ or voting on them if you consider them helpful.</p></div><div id="comment-34319-info" class="comment-info"><span class="comment-age">(01 Jul '14, 05:36)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-34295" class="comment-tools"></div><div class="clear"></div><div id="comment-34295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33055"></span>

<div id="answer-container-33055" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33055-score" class="post-score" title="current number of votes">0</div><span id="post-33055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like the client either only wanted to check if the server is still alive, or it was not happy with the something the server sent. You should do a capture of one of the users that <strong>is able</strong> to access the website and determine the differences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '14, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33055" class="comments-container"><span id="33056"></span><div id="comment-33056" class="comment"><div id="post-33056-score" class="comment-score"></div><div class="comment-text"><p>Uploading a capture - <a href="https://www.cloudshark.org/captures/34eb13edbb31">https://www.cloudshark.org/captures/34eb13edbb31</a></p></div><div id="comment-33056-info" class="comment-info"><span class="comment-age">(25 May '14, 05:50)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="33069"></span><div id="comment-33069" class="comment"><div id="post-33069-score" class="comment-score"></div><div class="comment-text"><p>what is the name of the server you are accessing?</p></div><div id="comment-33069-info" class="comment-info"><span class="comment-age">(25 May '14, 12:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33072"></span><div id="comment-33072" class="comment"><div id="post-33072-score" class="comment-score"></div><div class="comment-text"><p><a href="https://current-uk.nadlcorp.com">https://current-uk.nadlcorp.com</a></p></div><div id="comment-33072-info" class="comment-info"><span class="comment-age">(25 May '14, 22:52)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-33055" class="comment-tools"></div><div class="clear"></div><div id="comment-33055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33065"></span>

<div id="answer-container-33065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33065-score" class="post-score" title="current number of votes">0</div><span id="post-33065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like packet loss between the client and the server. There are Dup ACK's and Retransmissions. Seems that some of the ACK's are not making it from the client to the server, then after a while, they give up and tear down the connection.</p><p>It's also worth noting that the server does not support SACK, and has a MSS of 956 bytes. Possibly some security device modifying the TCP options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '14, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-33065" class="comments-container"><span id="33074"></span><div id="comment-33074" class="comment"><div id="post-33074-score" class="comment-score"></div><div class="comment-text"><p>Loadbalancer is sitting on top of server and may be modifying it,if you see the IP.TTL field you will see that TTL during tcp handshake and ssl handshake is different because Loadbalancer is taking care of tcp handshake and ssl is by server.</p></div><div id="comment-33074-info" class="comment-info"><span class="comment-age">(25 May '14, 22:59)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-33065" class="comment-tools"></div><div class="clear"></div><div id="comment-33065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33071"></span>

<div id="answer-container-33071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33071-score" class="post-score" title="current number of votes">0</div><span id="post-33071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The client does <strong><em>not</em></strong> send the FIN <strong><em>immediately</em></strong> after the SSL handshake. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_200.png" alt="alt text" /></p><hr /><p>GET request from Microsoft CryptoAPI <img src="https://osqa-ask.wireshark.org/upfiles/Selection_201.png" alt="alt text" /></p><hr /><p>GoDaddy CA Certificate <img src="https://osqa-ask.wireshark.org/upfiles/GoDaddy.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '14, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '14, 23:05</strong> </span></p></div></div><div id="comments-container-33071" class="comments-container"><span id="33073"></span><div id="comment-33073" class="comment"><div id="post-33073-score" class="comment-score"></div><div class="comment-text"><p>Thanks,even i noticed it but not sure that this could be causing it,if i extract the Intermediate CA certificate received from above http request,it matches the one with received in server hello.</p></div><div id="comment-33073-info" class="comment-info"><span class="comment-age">(25 May '14, 22:55)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="33075"></span><div id="comment-33075" class="comment"><div id="post-33075-score" class="comment-score"></div><div class="comment-text"><p>Do you have the Go Daddy Root Certificate installed as trusted?</p></div><div id="comment-33075-info" class="comment-info"><span class="comment-age">(25 May '14, 23:06)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="33238"></span><div id="comment-33238" class="comment"><div id="post-33238-score" class="comment-score"></div><div class="comment-text"><p>Hi,yes it has root certificate installed.</p></div><div id="comment-33238-info" class="comment-info"><span class="comment-age">(01 Jun '14, 03:30)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-33071" class="comment-tools"></div><div class="clear"></div><div id="comment-33071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

