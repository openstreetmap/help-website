+++
type = "question"
title = "SSL decryption works only on the first client request. Remaining packets are not decrypted"
description = '''Hi all, I am trying to decrypt an SSL session which is running on my test environment and I am partially successful in that. The problem is that every time to successfully decrypt an SSL capture, I need to restart my browser and the first transaction gets decrypted properly. The subsequent requests ...'''
date = "2012-10-22T07:40:00Z"
lastmod = "2012-10-22T08:29:00Z"
weight = 15160
keywords = [ "ssl", "rsa" ]
aliases = [ "/questions/15160" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL decryption works only on the first client request. Remaining packets are not decrypted](/questions/15160/ssl-decryption-works-only-on-the-first-client-request-remaining-packets-are-not-decrypted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15160-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am trying to decrypt an SSL session which is running on my test environment and I am partially successful in that. The problem is that every time to successfully decrypt an SSL capture, I need to restart my browser and the first transaction gets decrypted properly. The subsequent requests from client system were not decrypted as expected.</p><p>I dont know the issue is with my current SSL server setup or with the wireshark setup. I have uploaded my capture file at <a href="http://www.cloudshark.org/captures/a9718e5fdb28">link</a>.</p><p>The RSA private key is given below:</p><pre><code>-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC7FQvv8ZbSAokS8PNXLsFcls9F6rlhlJ5YeQuh81LdMyx/9ui5
zb1mSNaenUed4UE2lo83v4P3EzMi93B9faVSoWNP1GtRUuH7QwZiKr3Cxihnuvcg
ZGcdJm5shwiGAqzXLxQ9TLcNg45dgPYlCjVBeI+gSsA1+w84fAJF4gwqTwIDAQAB
AoGATBHKwM3jHZGaWvFOgOyqAxPvQ+alamAb4q2VZUyjLP5Z4c5r4uEdWjHT0rrx
G+kzsxaVNX3SEuzjphwmyWAFkFiRYAREhaRDICnAAlSt3IKwRNIJPkx2iDTZeA6H
/Pr8hsAdafvU8f6EWEs9ji27BZBCLxcC0+Y3ezPN2mPTfcECQQD13DyCizH8SMv4
Fl5i/OxXmEtC/X9wYGY64xDxenCegHifs+QcL1Sh5JPSSwLURRruxuQBcj1fxyNg
eJppZ8tVAkEAwsw8/0p4QCZSmT/6+VJ20grtpH33vkJO54go3FZBBAPGHUkKog2z
AeGEq+wjaKZqhbaasJPhT1FKkPXSCSXHEwJBAKwK5TzkcqH7vt9np7zVB/1z0Jac
FSVqD599bUnNSClh9QasNx+R70MqVFZ/rwcjJGmaO8rXSiNPkm3bdxHzU9ECQDrj
Sz1R4fBipW22rcRZbZopu5WSjyZxHTFZNCEH4je4fFe2EQTUZ10WM+lVRY8JYAJ0
JWdkDSTRSl1wMsKZLQkCQFSsy2/AWZfyj53lcd7tRrEq1BSUUbSzGParBJ2x1ZOR
O5oUfZiCfug69oiQ1+qKvp8ldPZCPgnV1QeRFx/acLQ=
-----END RSA PRIVATE KEY-----</code></pre><p>In the attached capture file, the packet at 15 gets decrypted properly with the given key. All other packets will not get decrypted. This happens when I reuse the same browser session to request the server. Any suggestion to dig into this issue is appreciated.</p><p>Regards, Ashbi</p></div><div id="question-tags" class="tags-container tags">ssl rsa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '12, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/0584b6c981d900eb4897be3243f08745?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashbi&#39;s gravatar image" /><p>ashbi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashbi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '12, 07:46</p></div></div><div id="comments-container-15160" class="comments-container"></div><div id="comment-tools-15160" class="comment-tools"></div><div class="clear"></div><div id="comment-15160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15166"></span>

<div id="answer-container-15166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15166-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A quick look at your trace shows that your client and server both support "TLS session tickets" and are indeed using them to reuse SSL sessions. Wireshark (AFAIK) does not yet support the use of "TLS session tickets" in regard to SSL decryption (the SSL keying material is not internally kept between sessions).</p><p>Could you file an enhancement report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and add the tracefile as well as the private key to the report?</p><p>In the mean time, you can disable the use of "TLS session tickets" to make sure you can decrypt the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '12, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-15166" class="comments-container"><span id="15170"></span><div id="comment-15170" class="comment"><div id="post-15170-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for the reply. I will configure the server to reuse the session and check whether the issue can be solved.</p></div><div id="comment-15170-info" class="comment-info"><span class="comment-age">(22 Oct '12, 09:37)</span> ashbi</div></div><span id="15179"></span><div id="comment-15179" class="comment"><div id="post-15179-score" class="comment-score"></div><div class="comment-text"><p>What you need to do, I believe, is to configure the server to NOT reuse sessions, so that Wireshark can capture the full key exchange process before the start of each session.</p></div><div id="comment-15179-info" class="comment-info"><span class="comment-age">(23 Oct '12, 01:33)</span> inetdog</div></div><span id="15181"></span><div id="comment-15181" class="comment"><div id="post-15181-score" class="comment-score"></div><div class="comment-text"><p>It's no problem for the server to re-use sessions, as long as it does not use "session tickets". But indeed, if you want to be able to decrypt each and every session independently without hassle, you might indeed disable session reuse altogether.</p></div><div id="comment-15181-info" class="comment-info"><span class="comment-age">(23 Oct '12, 01:47)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-15166" class="comment-tools"></div><div class="clear"></div><div id="comment-15166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

