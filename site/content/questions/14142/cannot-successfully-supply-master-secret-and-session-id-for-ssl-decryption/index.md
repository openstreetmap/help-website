+++
type = "question"
title = "Cannot successfully supply Master Secret and Session ID for SSL Decryption?"
description = '''After capturing some SSL traffic (using tcpdump on an embedded linux system), I&#x27;m attempting to decrypt the traffic from the dumpfile using Wireshark (I&#x27;ve tried both v1.8.1 on linux and v1.8.2 on Win32). The Session-ID was taken from the packet capture and the master secret was obtained from the me...'''
date = "2012-09-08T14:33:00Z"
lastmod = "2012-09-11T11:11:00Z"
weight = 14142
keywords = [ "session-id", "ssl", "decrypt", "keyfile", "master" ]
aliases = [ "/questions/14142" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot successfully supply Master Secret and Session ID for SSL Decryption?](/questions/14142/cannot-successfully-supply-master-secret-and-session-id-for-ssl-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14142-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After capturing some SSL traffic (using tcpdump on an embedded linux system), I'm attempting to decrypt the traffic from the dumpfile using Wireshark (I've tried both v1.8.1 on linux and v1.8.2 on Win32).</p><p>The Session-ID was taken from the packet capture and the master secret was obtained from the memory of an application executing on the embedded system.</p><p>My file key file looks like</p><pre><code>RSA Session-ID:D5407D99D48D4D094871F9938EF28F284C80ADA4F86EA96E75AB8E4E9374C7D6 Master-Key:26D5441D31A01A98C8C12140DE5312E3905E0619351D25A906152FAB9834ABC2CFBA14C11841447ECB175646185F3FB8</code></pre><p>With the obligatory newline afterwards.</p><p>I've selected "data" as the protocol (as I'm not sure what protocol lies inside the session--though most likely XML), but when applied, I get an error of "Can't load private key from /root/<a href="http://dump.test.ms">dump.test.ms</a>" on the console and "ssl_load_key: can't import pem data" in the ssl.debug file.</p><p>It almost seems as if wireshark is treating the keyfile as an RSA/X.509 key and not the session &amp; master secret?</p><p>Furthermore, if the master secret were incorrect, I would still expect wireshark to "decrypt" the data and present that in the view as decrypted.</p><p>Any pointers or thoughts would be appreciated.</p></div><div id="question-tags" class="tags-container tags">session-id ssl decrypt keyfile master</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '12, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/55544c00e6057fb682dc445f34558af0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="puffdaddy&#39;s gravatar image" /><p>puffdaddy<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="puffdaddy has one accepted answer">100%</span></p></div></div><div id="comments-container-14142" class="comments-container"><span id="35163"></span><div id="comment-35163" class="comment"><div id="post-35163-score" class="comment-score"></div><div class="comment-text"><p>puffdaddy ... I need to Get Session-ID and Master-Secret for a win32 c++ application For Decrypting SSL/TLS trafic. How you get the Session-ID and Master-Secret. Witch Software did you used. Could you please point me to a right direction ?</p></div><div id="comment-35163-info" class="comment-info"><span class="comment-age">(04 Aug '14, 09:30)</span> izeid</div></div></div><div id="comment-tools-14142" class="comment-tools"></div><div class="clear"></div><div id="comment-14142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14188"></span>

<div id="answer-container-14188" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14188-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To answer my own question, this was simple user error, as I didn't understand that the SSL Protocol dialog provided an input for RSA sever keys, and a separate method to input Session-IDs and Master-Secrets (i.e. Edit-&gt;Preferences-&gt;Protocols-&gt;SSL-&gt; "(Pre)-Master-Secret log filename:", and the file that you specify there should contain separate lines with the <code>RSA Session-ID:D5407D99D48D4D094871F9938EF28F284C80ADA4F86EA96E75AB8E4E9374C7D6 Master-Key:26D5441D31A01A98C8C12140DE5312E3905E0619351D25A906152FAB9834ABC2CFBA14C11841447ECB175646185F3FB8</code> syntax.</p><p>After adding my file in that fashion, I needed to restart wireshark, and then (after the restart--which seemed to perhaps allow wireshark to load and posses the secrets contained in that file) I was able to then select "Follow SSL stream" and view the decrypted stream.</p><p>Cheers!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '12, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/55544c00e6057fb682dc445f34558af0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="puffdaddy&#39;s gravatar image" /><p>puffdaddy<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="puffdaddy has one accepted answer">100%</span></p></div></div><div id="comments-container-14188" class="comments-container"></div><div id="comment-tools-14188" class="comment-tools"></div><div class="clear"></div><div id="comment-14188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

