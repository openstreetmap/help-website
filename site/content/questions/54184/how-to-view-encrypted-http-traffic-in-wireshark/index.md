+++
type = "question"
title = "How to view encrypted HTTP traffic in wireshark?"
description = '''Hello, I am trying to view HTTP traffic. I have pcap with me but it&#x27;s encrypted with TLS exchange messages. I have added Server Private key into Wireshark under Preferences Option; however, it does not work. Private key is in .pem format and I have given below details: IP : for which I want to see h...'''
date = "2016-07-20T06:04:00Z"
lastmod = "2016-07-20T06:04:00Z"
weight = 54184
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/54184" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to view encrypted HTTP traffic in wireshark?](/questions/54184/how-to-view-encrypted-http-traffic-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54184-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to view HTTP traffic. I have pcap with me but it's encrypted with TLS exchange messages. I have added Server Private key into Wireshark under Preferences Option; however, it does not work. Private key is in .pem format and I have given below details:</p><p>IP : for which I want to see http traffic Port : 443 Protocol : http Key : private in .pem format</p><p>Kindly suggest</p></div><div id="question-tags" class="tags-container tags">ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '16, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/962349492f305ec7bae240fb8c9996ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tech%20round&#39;s gravatar image" /><p>tech round<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tech round has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 08:00</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-54184" class="comments-container"><span id="54207"></span><div id="comment-54207" class="comment"><div id="post-54207-score" class="comment-score">1</div><div class="comment-text"><p>In <code>Edit -&gt; Preferences -&gt; Protocols -&gt; SSL</code>, define a SSL debug file and reload your capture. Try to find the explanation why the deciphering does not work in the SSL debug file; if it does not help you, post the contents of the SSL debug file here so that others could have a look.</p></div><div id="comment-54207-info" class="comment-info"><span class="comment-age">(20 Jul '16, 13:38)</span> sindy</div></div></div><div id="comment-tools-54184" class="comment-tools"></div><div class="clear"></div><div id="comment-54184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

