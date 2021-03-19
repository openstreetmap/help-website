+++
type = "question"
title = "Decryption of HTTPS Traffic"
description = '''I have been trying to decrypt HTTPS Traffic between my server and client for couple of days. Version of Wireshark I have been using is Version 1.12.2 (v1.12.2-0-g898fa22 from master-1.12). I have the private key from my server and did upload the same in Wireshark(Edit &amp;gt; Preferences and RSA Keys L...'''
date = "2014-12-18T16:54:00Z"
lastmod = "2014-12-18T16:54:00Z"
weight = 38635
keywords = [ "decryption", "https" ]
aliases = [ "/questions/38635" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decryption of HTTPS Traffic](/questions/38635/decryption-of-https-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been trying to decrypt HTTPS Traffic between my server and client for couple of days. Version of Wireshark I have been using is <strong>Version 1.12.2</strong> (v1.12.2-0-g898fa22 from master-1.12).</p><p>I have the private key from my server and did upload the same in Wireshark(Edit &gt; Preferences and RSA Keys List.)</p><p>Even after sharing the private key of my server in wireshark, I'm unable to see decrypted data. Upon seeing my SSL debug logs, I could see these lines - <em>ssl_decrypt_pre_master_secret wrong pre_master_secret length (256, expected 48) ssl_generate_pre_master_secret: can't decrypt pre master secret</em></p><p>Wondering same works fine between client and server, but when I try decrypt them using same private key of my server in Wireshark, it couldn't be decrypted.</p><p>Any pointer will be highly appreciated.</p></div><div id="question-tags" class="tags-container tags">decryption https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '14, 16:54</strong></p><img src="https://secure.gravatar.com/avatar/40d46dc7a7144a5863899be317e9c6b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chocka&#39;s gravatar image" /><p>Chocka<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chocka has no accepted answers">0%</span></p></div></div><div id="comments-container-38635" class="comments-container"><span id="38636"></span><div id="comment-38636" class="comment"><div id="post-38636-score" class="comment-score"></div><div class="comment-text"><p>Please have a look at <a href="https://ask.wireshark.org/questions/38441/problem-with-decrypting-the-ssl-using-the-private-key.">https://ask.wireshark.org/questions/38441/problem-with-decrypting-the-ssl-using-the-private-key.</a> There are some requirements for decrypting traffic in Wireshark.</p></div><div id="comment-38636-info" class="comment-info"><span class="comment-age">(19 Dec '14, 03:46)</span> Uli</div></div><span id="38752"></span><div id="comment-38752" class="comment"><div id="post-38752-score" class="comment-score"></div><div class="comment-text"><p>are you able to decrypt the sample capture files in the wiki (keys included)?</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys">http://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys</a></p></blockquote></div><div id="comment-38752-info" class="comment-info"><span class="comment-age">(27 Dec '14, 12:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38635" class="comment-tools"></div><div class="clear"></div><div id="comment-38635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

