+++
type = "question"
title = "Which protocols use facebook???"
description = '''Hey, do you know wich protocols facebook use when you chat, like somethink, whatch a video...? Wireshark shows me only https with tcp everywhere.  Is it possible to encrypt this to see what protocols are using? Thx guys!'''
date = "2014-08-01T08:51:00Z"
lastmod = "2014-08-03T10:14:00Z"
weight = 35069
keywords = [ "facebook" ]
aliases = [ "/questions/35069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Which protocols use facebook???](/questions/35069/which-protocols-use-facebook)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, do you know wich protocols facebook use when you chat, like somethink, whatch a video...? Wireshark shows me only https with tcp everywhere.</p><p>Is it possible to encrypt this to see what protocols are using?</p><p>Thx guys!</p></div><div id="question-tags" class="tags-container tags">facebook</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '14, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/4c1111343a1153fc6c112ec797ad55df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jan%20Muster&#39;s gravatar image" /><p>Jan Muster<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jan Muster has no accepted answers">0%</span></p></div></div><div id="comments-container-35069" class="comments-container"></div><div id="comment-tools-35069" class="comment-tools"></div><div class="clear"></div><div id="comment-35069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35104"></span>

<div id="answer-container-35104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35104-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Wireshark <strong>shows me only https</strong> with tcp everywhere.</p></blockquote><p>because that's what Facebook is using.</p><blockquote><p>Is it possible to <strong>encrypt</strong> this to see what protocols are using?</p></blockquote><p>You need to <strong>decrpyt</strong> the traffic, however, that's near to impossible, as you certainly don't have access to the private key(s) of the facebook servers, do you?</p><p>If you are trying to decrypt the traffic of your own browser, you could tell the browser to expose the SSL/TLS session keys and then use that to decrypt the https traffic. Alternatively you can use a proxy that is able to do SSL/TLS decrpytion (like Fiddler). See my answer to a similar question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/29936/decrypting-ssl-traffic-in-wireshark-processed-by-sslsniff">http://ask.wireshark.org/questions/29936/decrypting-ssl-traffic-in-wireshark-processed-by-sslsniff</a><br />
</p></blockquote><p>and some other resources.</p><blockquote><p><a href="http://www.cloudshield.com/blog/advanced-malware/how-to-decrypt-openssl-sessions-using-wireshark-and-ssl-session-identifiers/">http://www.cloudshield.com/blog/advanced-malware/how-to-decrypt-openssl-sessions-using-wireshark-and-ssl-session-identifiers/</a><br />
<a href="http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html">http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '14, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-35104" class="comments-container"></div><div id="comment-tools-35104" class="comment-tools"></div><div class="clear"></div><div id="comment-35104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

