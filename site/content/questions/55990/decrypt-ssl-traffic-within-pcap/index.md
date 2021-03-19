+++
type = "question"
title = "Decrypt SSL traffic within PCAP."
description = '''I have a PCAP that includes SSL traffic that I would like to decrypt in order to retrieve a flag. I was able to find the server certificate which I exported into a .der file. I am able to convert from .der to .pem and am able to view the .pem which resembles a public key. If I attempt to use this to...'''
date = "2016-09-29T10:46:00Z"
lastmod = "2016-09-29T10:46:00Z"
weight = 55990
keywords = [ "decryption", "rsa", "ssl_decrypt" ]
aliases = [ "/questions/55990" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt SSL traffic within PCAP.](/questions/55990/decrypt-ssl-traffic-within-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55990-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a PCAP that includes SSL traffic that I would like to decrypt in order to retrieve a flag. I was able to find the server certificate which I exported into a .der file. I am able to convert from .der to .pem and am able to view the .pem which resembles a public key. If I attempt to use this to decrypt the traffic it does not. So I believe that I need to move to another step but am unable to find that step. I believe the next step involves using the random bytes value from the handshake within the SSL section of the server hello packet. I just do not know how to perform this task. I am hoping someone can shed some light.</p></div><div id="question-tags" class="tags-container tags">decryption rsa ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '16, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/f76e660895fd30cdecf30c8c53f1adae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdpadro&#39;s gravatar image" /><p>jdpadro<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdpadro has no accepted answers">0%</span></p></div></div><div id="comments-container-55990" class="comments-container"><span id="55993"></span><div id="comment-55993" class="comment"><div id="post-55993-score" class="comment-score"></div><div class="comment-text"><p>Check that: (1) RSA private keys can only decrypt sessions which use RSA for key exchange, (EC)DHE cipher suites do not qualify. (2) does the private key really match the server certificate? Furthermore, you cannot just pick random bytes from the handshake and calculate the (pre-)master secret, for that you would need more data (which is RSA-encrypted in the case of a RSA key exchange, or the private DH exponents which you are unlikely to have in possession).</p></div><div id="comment-55993-info" class="comment-info"><span class="comment-age">(29 Sep '16, 11:05)</span> Lekensteyn</div></div></div><div id="comment-tools-55990" class="comment-tools"></div><div class="clear"></div><div id="comment-55990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

