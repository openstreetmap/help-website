+++
type = "question"
title = "extract certificate info with TSHARK"
description = '''Is there a way to extract certificate infomation that is viewable from wireshark in tshark? For example, fields like common name, organization, serial number.'''
date = "2015-03-30T12:27:00Z"
lastmod = "2015-04-08T11:45:00Z"
weight = 41034
keywords = [ "certificates", "tshark" ]
aliases = [ "/questions/41034" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [extract certificate info with TSHARK](/questions/41034/extract-certificate-info-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41034-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to extract certificate infomation that is viewable from wireshark in tshark? For example, fields like common name, organization, serial number.</p></div><div id="question-tags" class="tags-container tags">certificates tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '15, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/663d096785363633d7a610b72b2f2874?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crevitch&#39;s gravatar image" /><p>crevitch<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crevitch has no accepted answers">0%</span></p></div></div><div id="comments-container-41034" class="comments-container"></div><div id="comment-tools-41034" class="comment-tools"></div><div class="clear"></div><div id="comment-41034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41035"></span>

<div id="answer-container-41035" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41035-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>sure, you can run tshark in verbose mode and then parse the output with a script:</p><blockquote><p>tshark -nr ssl.pcapng -2 -R "ssl.handshake.certificate" -V &gt; out.txt</p></blockquote><p>Example output:</p><pre><code>               Certificate (id-at-commonName=ssl4338.cloudflare.com,id-at-organizationName=CloudFlare, Inc.,id-at-localtyName=San Francisco,id-at-stateOrProvinceName=CA,id-at-countryName=US)
                       version: v3 (2)
                       serialNumber : 0x1121c2cb499715e11699032fa4a393e81d90
                       validity
                           notBefore: utcTime (0)
                               utcTime: 14-10-15 03:29:31 (UTC)
                           notAfter: utcTime (0)
                               utcTime: 15-10-11 15:31:39 (UTC)</code></pre><p>As an alternative, you can print whatever field sounds interesting for you: <a href="https://www.wireshark.org/docs/dfref/s/ssl.html">https://www.wireshark.org/docs/dfref/s/ssl.html</a></p><blockquote><p>tshark -nr ssl.pcapng -2 -R "ssl.handshake.certificate" -T fields -e xxxx -e yyyy</p></blockquote><p>Please replace xxxx and yyyy with fields listed in the reference.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41035" class="comments-container"></div><div id="comment-tools-41035" class="comment-tools"></div><div class="clear"></div><div id="comment-41035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41299"></span>

<div id="answer-container-41299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41299-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For printing the certificate, I couldn't find any fields that list the url of the certificate (that work, anyway. ssl.handshake.cert_url.url_hash (URL and Hash) looked promising, but didn't give me anything on tshark 1.12.4. I finally wound up doing this: tshark -nr ssl.pcap -R "ssl.handshake.certificate" -V | grep "Certificate (id-at-commonName=" | sort | uniq &gt; certs.txt</p><p>It would be nice if ssl.handshake.cert_url just gave you something like "amazon.com"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '15, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/793e766d0269cb4fcc1fb2933a8604d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John52&#39;s gravatar image" /><p>John52<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John52 has no accepted answers">0%</span></p></div></div><div id="comments-container-41299" class="comments-container"></div><div id="comment-tools-41299" class="comment-tools"></div><div class="clear"></div><div id="comment-41299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

