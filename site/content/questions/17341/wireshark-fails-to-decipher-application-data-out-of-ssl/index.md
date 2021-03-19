+++
type = "question"
title = "Wireshark fails to decipher application data out of SSL"
description = '''I&#x27;ve looked around for similar logs, but found no actual solution. Dump was taken using tcpdump -s 0 -i eth0 -v -w dump.pcap  Log: pastebin Dump: cloudshark I&#x27;m out of ideas what may be wrong, some time earlier it worked as usual, but now it does not.'''
date = "2012-12-31T04:56:00Z"
lastmod = "2012-12-31T05:35:00Z"
weight = 17341
keywords = [ "ssl", "tlsv1" ]
aliases = [ "/questions/17341" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark fails to decipher application data out of SSL](/questions/17341/wireshark-fails-to-decipher-application-data-out-of-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17341-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've looked around for similar logs, but found no actual solution. Dump was taken using</p><pre><code>tcpdump -s 0 -i eth0 -v -w dump.pcap</code></pre><p>Log: <a href="http://pastebin.com/JVZvTbd0">pastebin</a> Dump: <a href="http://cloudshark.org/captures/2fc8e1821979">cloudshark</a></p><p>I'm out of ideas what may be wrong, some time earlier it worked as usual, but now it does not.</p></div><div id="question-tags" class="tags-container tags">ssl tlsv1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '12, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/64873147ffef8b124c107247100a9a5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexey%20Pelykh&#39;s gravatar image" /><p>Alexey Pelykh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexey Pelykh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Dec '12, 05:26</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-17341" class="comments-container"><span id="17342"></span><div id="comment-17342" class="comment"><div id="post-17342-score" class="comment-score"></div><div class="comment-text"><p>Probably it's due to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303</a></p></div><div id="comment-17342-info" class="comment-info"><span class="comment-age">(31 Dec '12, 05:09)</span> Alexey Pelykh</div></div></div><div id="comment-tools-17341" class="comment-tools"></div><div class="clear"></div><div id="comment-17341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17343"></span>

<div id="answer-container-17343" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17343-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The only SSL/TLS connections in that capture file are to servers of <a href="http://whatsapp.net">whatsapp.net</a>. Do <strong>you</strong> have access to <strong>their</strong> private key?</p><p>If <strong>no</strong>, then you <strong>cannot</strong> decrypt those SSL connections. See the SSL wiki:</p><blockquote><p><code>http://wiki.wireshark.org/SSL</code><br />
</p></blockquote><p>If <strong>yes</strong> (because you are the WhatsApp CEO or the web server admin), then you have entered the key in the wrong format, hence the following message in the debug file:</p><blockquote><p><code>ssl_find_private_key can't find private key for this server!</code><br />
</p></blockquote><p>What are you trying to do?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '12, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Dec '12, 05:40</p></div></div><div id="comments-container-17343" class="comments-container"><span id="17344"></span><div id="comment-17344" class="comment"><div id="post-17344-score" class="comment-score"></div><div class="comment-text"><p>Yes, I don't have private key, but the odd thing is: dissect_ssl3_hnd_srv_hello trying to generate keys ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57) dissect_ssl3_hnd_srv_hello can't generate keyring material record: offset = 86, reported_length_remaining = 1374 need_desegmentation: offset = 86, reported_length_remaining = 1374</p></div><div id="comment-17344-info" class="comment-info"><span class="comment-age">(31 Dec '12, 05:41)</span> Alexey Pelykh</div></div><span id="17346"></span><div id="comment-17346" class="comment"><div id="post-17346-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Yes, I don't have private key,</p></blockquote><p>Then you <strong>cannot</strong> decrypt SSL, unless you have found a secret bug in the SSL encryption scheme ;-)</p><p>An alternative would be to use the '(Pre)-Master-Secret' output by the SSL client (see SSL wiki).</p></div><div id="comment-17346-info" class="comment-info"><span class="comment-age">(31 Dec '12, 05:44)</span> Kurt Knochner ♦</div></div><span id="17383"></span><div id="comment-17383" class="comment"><div id="post-17383-score" class="comment-score"></div><div class="comment-text"><p>Kurt is right, @Alexey. SSL is purposely designed to be unencryptable by a man-in-the-middle, which is what Wireshark is. In absence of the remote site's private key, you would need to have state information generated on the fly within the local program setting up the SSL session. Read more about SSL and you will see why this is the case.</p></div><div id="comment-17383-info" class="comment-info"><span class="comment-age">(02 Jan '13, 06:20)</span> Warren Young</div></div><span id="17387"></span><div id="comment-17387" class="comment"><div id="post-17387-score" class="comment-score"></div><div class="comment-text"><p>Totally agree :) Just over-debugged myself, shame on me :)</p></div><div id="comment-17387-info" class="comment-info"><span class="comment-age">(02 Jan '13, 06:39)</span> Alexey Pelykh</div></div></div><div id="comment-tools-17343" class="comment-tools"></div><div class="clear"></div><div id="comment-17343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

