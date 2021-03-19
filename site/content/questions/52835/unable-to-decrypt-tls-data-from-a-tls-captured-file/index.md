+++
type = "question"
title = "Unable to decrypt TLS data from a TLS captured file"
description = '''HI , AM trying to open a file which have got tls handshake messages and data further. My Intention was to decrypt the TLS data. Our data is directly below TCP like (TCP--TLS--data). Steps followed:  Opened the file Edit-preference-protocol-ssl-127.0.0.1,4444,ssl,/home/dh/openssl/device.key Followed ...'''
date = "2016-05-23T06:22:00Z"
lastmod = "2016-05-24T03:30:00Z"
weight = 52835
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/52835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt TLS data from a TLS captured file](/questions/52835/unable-to-decrypt-tls-data-from-a-tls-captured-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52835-score" class="post-score" title="current number of votes">0</div><span id="post-52835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI ,</p><p>AM trying to open a file which have got tls handshake messages and data further. My Intention was to decrypt the TLS data. Our data is directly below TCP like (TCP--TLS--data).</p><p>Steps followed:</p><ol><li>Opened the file</li><li>Edit-preference-protocol-ssl-127.0.0.1,4444,ssl,/home/dh/openssl/device.key</li><li>Followed the TCP stream - still the data is not decrypted.</li></ol><p>AM using version 1.0.15 with GnuTLS 1.4.1, with Gcrypt 1.4.4.</p><p>This is the command i used ,</p><p>[<span class="__cf_email__" data-cfemail="8bf9e4e4ffcbe5eeffe8e4e5ed">[email protected]</span> ~]# tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list:127.0.0.1,4444,http,/home/amanimar/openssl/device.key" -o "ssl.debug_file:/root/ssl.log" tcp port 4444 -w /root/packet.pcap.</p><p>Please Help Help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '16, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/df4dab12d9437bfe0ef8981b3526b069?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhanish&#39;s gravatar image" /><p><span>dhanish</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhanish has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '16, 23:32</strong> </span></p></div></div><div id="comments-container-52835" class="comments-container"><span id="52847"></span><div id="comment-52847" class="comment"><div id="post-52847-score" class="comment-score"></div><div class="comment-text"><p>Below is the ssl.log :</p><p><code> cat ssl.log  ssl_init keys string: 127.0.0.1,4444,http,/home/amanimar/openssl/device.key ssl_init found host entry 127.0.0.1,4444,http,/home/amanimar/openssl/device.key ssl_init addr '127.0.0.1' port '4444' filename '/home/amanimar/openssl/device.key' password(only for p12 file) '(null)' Private key imported: KeyID 83:33:D6:6E:68:A3:76:09:1E:C4:D9:DE:41:3A:AA:95:... ssl_init private key file /home/amanimar/openssl/device.key successfully loaded association_add TCP port 4444 protocol http handle 0x2b48f5246c40 association_find: TCP port 993 found 0x2b48f5a205b0 ssl_association_remove removing TCP 993 - imap handle 0x2b48f5265350 association_add TCP port 993 protocol imap handle 0x2b48f5265350 association_find: TCP port 995 found 0x2b48f5a20620 ssl_association_remove removing TCP 995 - pop handle 0x2b48f53e3160 association_add TCP port 995 protocol pop handle 0x2b48f53e3160 [[email protected] ~]#</code></p></div><div id="comment-52847-info" class="comment-info"><span class="comment-age">(23 May '16, 23:31)</span> <span class="comment-user userinfo">dhanish</span></div></div><span id="52860"></span><div id="comment-52860" class="comment"><div id="post-52860-score" class="comment-score"></div><div class="comment-text"><p>Your comment has been edited to use the correct format for code or text output to make it easier to read.</p></div><div id="comment-52860-info" class="comment-info"><span class="comment-age">(24 May '16, 03:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-52835" class="comment-tools"></div><div class="clear"></div><div id="comment-52835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

