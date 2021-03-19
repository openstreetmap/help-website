+++
type = "question"
title = "decrypting SIP packets sometimes not shown packets from/to endpoint"
description = '''Hi All, I have a problem when time to time wireshark decrypted only partial sip flow. And sometimes decrypted full flow. Such change in decryption happens randomly and I need to know what is wrong when wireshark can&#x27;t decrypt full flow. For example on following capture sip session (call) started fro...'''
date = "2013-11-30T15:02:00Z"
lastmod = "2013-11-30T15:02:00Z"
weight = 27590
keywords = [ "tls", "sip" ]
aliases = [ "/questions/27590" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decrypting SIP packets sometimes not shown packets from/to endpoint](/questions/27590/decrypting-sip-packets-sometimes-not-shown-packets-fromto-endpoint)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27590-score" class="post-score" title="current number of votes">0</div><span id="post-27590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have a problem when time to time wireshark decrypted only partial sip flow. And sometimes decrypted full flow. Such change in decryption happens randomly and I need to know what is wrong when wireshark can't decrypt full flow. For example on following capture sip session (call) started from 4418 packet - on this packet Originator sent INVITE to SIP PROXY but INVITE from SIP PROXY to Terminator wasn't decrypted. Another marked packet on this capture 2411 on which you can that messages from Terminator was decrypted successfully 15 seconds ago. <img src="http://ssmaker.ru/97c84bba.png" alt="alt text" /> [link to picture]<a href="http://ssmaker.ru/97c84bba.png">2</a></p><p>On the same capture I'm changed display filter to SSL and see that actually packets was captured but not decrypted:</p><p><img src="http://ssmaker.ru/811122ff.png" alt="alt text" /> [link to picture]<a href="http://ssmaker.ru/97c84bba.png">4</a></p><p>Packets 4423 and 4424 weren't decrypted. From SSL debug log:</p><pre><code>  dissect_ssl enter frame #4423 (first time)
  conversation = 05EFD918, ssl_session = 05EFDE18
  record: offset = 0, reported_length_remaining = 1448
  need_desegmentation: offset = 0, reported_length_remaining = 1448</code></pre><p>Can anybody suggest how to deal with this the problem? I'm using wireshark Version 1.10.3. Capturing with following tshark command:</p><pre><code>C:\Program Files (x86)/Wireshark/tshark.exe -l -i 1 -w capture_eth1.pcap -a filesize:15000</code></pre><p>Of course private key from certificate was imported to wireshark via wireshark GUI.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '13, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/6d1e7ab70067fe885a2871de13705130?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m2a0x&#39;s gravatar image" /><p><span>m2a0x</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m2a0x has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Nov '13, 15:27</strong> </span></p></div></div><div id="comments-container-27590" class="comments-container"></div><div id="comment-tools-27590" class="comment-tools"></div><div class="clear"></div><div id="comment-27590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

