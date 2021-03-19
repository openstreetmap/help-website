+++
type = "question"
title = "SSL &quot;key exchange 0 different from KEX_RSA&quot; but using RSA"
description = '''I&#x27;m trying to decrypt a small TLSv1.2 stream, using Wireshark 1.8.6 Win64 (stock build from wireshark.org). I&#x27;ve configured the server&#x27;s private key in the preferences. I have prior experience with SSL/TLS and OpenSSL, so I&#x27;m reasonably sure all of this is correct. The SSL debug log shows the &quot;key e...'''
date = "2013-04-20T20:20:00Z"
lastmod = "2013-04-20T20:20:00Z"
weight = 20667
keywords = [ "kex_rsa", "ssl" ]
aliases = [ "/questions/20667" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL "key exchange 0 different from KEX\_RSA" but using RSA](/questions/20667/ssl-key-exchange-0-different-from-kex_rsa-but-using-rsa)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20667-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt a small TLSv1.2 stream, using Wireshark 1.8.6 Win64 (stock build from wireshark.org). I've configured the server's private key in the preferences. I have prior experience with SSL/TLS and OpenSSL, so I'm reasonably sure all of this is correct.</p><p>The SSL debug log shows the "key exchange 0 different from KEX_RSA" message immediately before complaining it can't decrypt the pre-master secret. The only other posting I've seen about this message identified the cause as a non-RSA cypher suite, which makes sense; but this conversation <em>is</em> using RSA. The Server Hello dissection shows "Cipher Suite: TLS_RSA_WITH_AES_256_GCM_SHA384 (0x009d)". And indeed the Client Key Exchange dissection says "RSA Encrypted PreMaster Secret".</p><p>My next move was going to be to pull the current sources and build for debug (I've done that before), but I figured it was worth asking if anyone had any quick suggestions before I go through the trouble.</p><p>Client Key Exchange begins with 10 00 00 82 00 80, followed by the actual encrypted pre-master, if that helps.</p></div><div id="question-tags" class="tags-container tags">kex_rsa ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '13, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/513295189ee24340b8de5822e630c627?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwojcik&#39;s gravatar image" /><p>mwojcik<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwojcik has no accepted answers">0%</span></p></div></div><div id="comments-container-20667" class="comments-container"></div><div id="comment-tools-20667" class="comment-tools"></div><div class="clear"></div><div id="comment-20667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

