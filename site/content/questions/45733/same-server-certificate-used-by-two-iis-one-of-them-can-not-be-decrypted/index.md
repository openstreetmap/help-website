+++
type = "question"
title = "Same server certificate used by two IIS, one of them can not be decrypted."
description = '''Dear Team, I have 2 IIS which IIS8 running on Windows 2012 and IIS7.5 running on Windows 2008R2, today I need to do some troubleshooting for the encrypted http. The strange thing is I can decrypt the HTTP data in IIS7.5 but CAN&#x27;T decrypt in IIS8, could you please assist on this? I just put both capt...'''
date = "2015-09-09T02:19:00Z"
lastmod = "2015-09-15T14:27:00Z"
weight = 45733
keywords = [ "iis7.5", "iis8", "ssl", "decryption" ]
aliases = [ "/questions/45733" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Same server certificate used by two IIS, one of them can not be decrypted.](/questions/45733/same-server-certificate-used-by-two-iis-one-of-them-can-not-be-decrypted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45733-score" class="post-score" title="current number of votes">0</div><span id="post-45733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Team,</p><p>I have 2 IIS which IIS8 running on Windows 2012 and IIS7.5 running on Windows 2008R2, today I need to do some troubleshooting for the encrypted http. The strange thing is I can decrypt the HTTP data in IIS7.5 but CAN'T decrypt in IIS8, could you please assist on this?</p><p>I just put both captures/debug files and decryption key into Skydrive, the link is <a href="http://1drv.ms/1icxA3G.">http://1drv.ms/1icxA3G.</a> For IIS7.5 the related files are: IIS7.5.pcapng and IIS7.5_with_Windows2008R2_debug.txt.zip. For IIS8 the related files are: IIS8_with_Windows2012.pcapng and IIS8_with_Windows2012_debug.txt. The decrypting key filename is: comp01.key</p><p>Thanks, Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iis7.5" rel="tag" title="see questions tagged &#39;iis7.5&#39;">iis7.5</span> <span class="post-tag tag-link-iis8" rel="tag" title="see questions tagged &#39;iis8&#39;">iis8</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '15, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/dae8cbd064b9748232e957cd6b172012?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metasploit&#39;s gravatar image" /><p><span>Metasploit</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metasploit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Sep '15, 02:36</strong> </span></p></div></div><div id="comments-container-45733" class="comments-container"></div><div id="comment-tools-45733" class="comment-tools"></div><div class="clear"></div><div id="comment-45733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45799"></span>

<div id="answer-container-45799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45799-score" class="post-score" title="current number of votes">1</div><span id="post-45799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I can decrypt the HTTP data in IIS7.5 but CAN'T decrypt in IIS8, could you please assist on this?</p></blockquote><p>Without having seen the SSL debug logs or the pcap file, I simply <strong>guess</strong> that IIS8 uses different ciphers, which are based on Diffie Hellman (DHE, DHCE). If so, bad luck! You can't decrypt TLS sessions with a server RSA key that use DHE/DHCE ciphers, as that's exactly why they have been developed (well not exatly because of that, but ... ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '15, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45799" class="comments-container"><span id="45802"></span><div id="comment-45802" class="comment"><div id="post-45802-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Would you mind to check my captures and debugs? it's here <a href="http://1drv.ms/1icxA3G">http://1drv.ms/1icxA3G</a> .</p><p>Thanks, Sam</p></div><div id="comment-45802-info" class="comment-info"><span class="comment-age">(11 Sep '15, 20:26)</span> <span class="comment-user userinfo">Metasploit</span></div></div><span id="45815"></span><div id="comment-45815" class="comment"><div id="post-45815-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, I checked the captures again, seems IIS8 using EC Diffie-Hellman. Is there a plan to add this capability? I mean decryption of ECDHE cipher. Thanks, Sam</p></div><div id="comment-45815-info" class="comment-info"><span class="comment-age">(12 Sep '15, 09:11)</span> <span class="comment-user userinfo">Metasploit</span></div></div><span id="45816"></span><div id="comment-45816" class="comment"><div id="post-45816-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Is there a plan to add this capability? I mean decryption of ECDHE cipher.</p></blockquote><p>There is no plan, because it's technically impossible.</p><p>You can only decrypt the traffic, if the client (browser) reveals the negotiated session key (master secret).</p><p>see here:</p><blockquote><p><a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/</a><br />
<a href="https://www.google.com/#q=site:ask.wireshark.org+SSLKEYLOGFILE">https://www.google.com/#q=site:ask.wireshark.org+SSLKEYLOGFILE</a></p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-45816-info" class="comment-info"><span class="comment-age">(12 Sep '15, 12:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45825"></span><div id="comment-45825" class="comment"><div id="post-45825-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Million thanks, I got it and works like a charm!</p><p>Best Regards, Sam</p></div><div id="comment-45825-info" class="comment-info"><span class="comment-age">(14 Sep '15, 02:51)</span> <span class="comment-user userinfo">Metasploit</span></div></div><span id="45864"></span><div id="comment-45864" class="comment"><div id="post-45864-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-45864-info" class="comment-info"><span class="comment-age">(15 Sep '15, 14:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45799" class="comment-tools"></div><div class="clear"></div><div id="comment-45799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

