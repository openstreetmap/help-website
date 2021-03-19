+++
type = "question"
title = "TLS public key decryption?"
description = '''I have a trace including handshake for TLS between two servers using SIPS. I cannot decode because wireshark wants private keys? Why would wireshark want private keys? Why wouldn&#x27;t the public keys work. I have both public keys from each server and cannot get it to work because wireshark will not acc...'''
date = "2012-01-30T10:24:00Z"
lastmod = "2012-01-30T10:34:00Z"
weight = 8708
keywords = [ "tlsv1" ]
aliases = [ "/questions/8708" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TLS public key decryption?](/questions/8708/tls-public-key-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8708-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace including handshake for TLS between two servers using SIPS. I cannot decode because wireshark wants private keys? Why would wireshark want private keys? Why wouldn't the public keys work. I have both public keys from each server and cannot get it to work because wireshark will not accept the public key.</p><p>Listen most organizations are not going to give you their private key, in fact everything I have read says never give out your private key. So why would wireshark request your private key.</p><p>This is an integration between two pcs telecom gear and the TLS does work; Each side shares their public key and it works. So if these two devices can decode each others TLS with their respective public keys why can't Wireshark?</p><p>Am I missing something fundamental here?</p></div><div id="question-tags" class="tags-container tags">tlsv1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '12, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/5b3c0665afc2aef6adadf968e6550243?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Messel&#39;s gravatar image" /><p>David Messel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Messel has no accepted answers">0%</span></p></div></div><div id="comments-container-8708" class="comments-container"></div><div id="comment-tools-8708" class="comment-tools"></div><div class="clear"></div><div id="comment-8708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8709"></span>

<div id="answer-container-8709" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8709-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer:</p><p>The way that Public Key Encryption works is as follows:</p><p>A sender encrypts a message using the receiver's public key.</p><p>The receiver then uses the receiver's <em>private</em> key to decrypt the message.</p><p>So: to be able to decrypt a message the private key is needed.</p><p>See any description of Public Key encryption for further details....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '12, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-8709" class="comments-container"><span id="8710"></span><div id="comment-8710" class="comment"><div id="post-8710-score" class="comment-score"></div><div class="comment-text"><p>thanks I new I had to have something fundamental; screwed up in my thinking.</p></div><div id="comment-8710-info" class="comment-info"><span class="comment-age">(30 Jan '12, 10:52)</span> David Messel</div></div></div><div id="comment-tools-8709" class="comment-tools"></div><div class="clear"></div><div id="comment-8709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

