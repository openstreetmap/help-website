+++
type = "question"
title = "TLS&#92;_RSA&#92;_CAMELLIA&#92;_256&#92;_CBC&#92;_SHA decryption"
description = '''Hi everyone! Does Wireshark support ssl RSA-CAMELLIA cipher decryption? I&#x27;m trying to decrypt a pcap log (with the well known RSA private key) of a https session between Firefox and my local server and I got the following error: dissect_ssl3_hnd_srv_hello can&#x27;t find cipher suite 0x84 Now, cipher sui...'''
date = "2013-01-30T02:45:00Z"
lastmod = "2013-09-12T17:03:00Z"
weight = 18087
keywords = [ "decryption", "camellia", "rsa" ]
aliases = [ "/questions/18087" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TLS\\\_RSA\\\_CAMELLIA\\\_256\\\_CBC\\\_SHA decryption](/questions/18087/tls_rsa_camellia_256_cbc_sha-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18087-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone!</p><p>Does Wireshark support ssl RSA-CAMELLIA cipher decryption? I'm trying to decrypt a pcap log (with the well known RSA private key) of a https session between Firefox and my local server and I got the following error:</p><p>dissect_ssl3_hnd_srv_hello can't find cipher suite 0x84</p><p>Now, cipher suite number 0x84 is: TLS_RSA_CAMELLIA_256_CBC_SHA1</p><p>So do I have to specify any flag during the building of the programm to enable camellia?</p><p>Thanks in advance, fex.</p></div><div id="question-tags" class="tags-container tags">decryption camellia rsa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '13, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/ae1e92711c8ce42e6e18ba8065456240?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fex&#39;s gravatar image" /><p>fex<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fex has no accepted answers">0%</span></p></div></div><div id="comments-container-18087" class="comments-container"><span id="18089"></span><div id="comment-18089" class="comment"><div id="post-18089-score" class="comment-score"></div><div class="comment-text"><p>My wireshark version: 1.8.3 with GnuTLS 2.12.20 (-&gt; GnuTLS 2.8.1). My GnuTLS is compiled with camellia support.</p></div><div id="comment-18089-info" class="comment-info"><span class="comment-age">(30 Jan '13, 03:36)</span> fex</div></div></div><div id="comment-tools-18087" class="comment-tools"></div><div class="clear"></div><div id="comment-18087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24618"></span>

<div id="answer-container-24618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24618-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark currently (1.10.2) does not support Camellia ciphers. After hitting this issue too, I decided to fix it. The resulting patch can be found on the Wireshark bugtracker: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144">Bug 9144 - [PATCH] Support for Camellia ciphers</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '13, 17:03</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '13, 23:50</p></div></div><div id="comments-container-24618" class="comments-container"></div><div id="comment-tools-24618" class="comment-tools"></div><div class="clear"></div><div id="comment-24618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18122"></span>

<div id="answer-container-18122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18122-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the definition in <strong>epan/dissectors/packet-ssl-utils.c:cipher_suites[]</strong> the mentioned cipher suite (0x84) is <strong>not defined</strong>. Maybe it is sufficient to add it to the list of <strong>cipher_suites</strong> and recompile Wireshark, but I have <strong>not</strong> checked if that would work. I believe there is more to do than just that ....</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '13, 12:27</p></div></div><div id="comments-container-18122" class="comments-container"></div><div id="comment-tools-18122" class="comment-tools"></div><div class="clear"></div><div id="comment-18122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

