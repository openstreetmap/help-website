+++
type = "question"
title = "How to obtain a private TLS key"
description = '''I&#x27;m trying to decrypt some TLSv1 packages, but I don&#x27;t have the server private key. How can I obtain the private key? Here are some images: Client Hello: http://www.imagebam.com/image/8d0f17478413719 Server Hello: http://www.imagebam.com/image/6c0b60478413729 Client Handshake: http://www.imagebam.co...'''
date = "2016-04-17T02:34:00Z"
lastmod = "2016-04-17T08:16:00Z"
weight = 51724
keywords = [ "tls", "key", "private" ]
aliases = [ "/questions/51724" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to obtain a private TLS key](/questions/51724/how-to-obtain-a-private-tls-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51724-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt some TLSv1 packages, but I don't have the server private key. How can I obtain the private key?</p><p>Here are some images:</p><p>Client Hello: <a href="http://www.imagebam.com/image/8d0f17478413719">http://www.imagebam.com/image/8d0f17478413719</a></p><p>Server Hello: <a href="http://www.imagebam.com/image/6c0b60478413729">http://www.imagebam.com/image/6c0b60478413729</a></p><p>Client Handshake: <a href="http://www.imagebam.com/image/482dff478413715">http://www.imagebam.com/image/482dff478413715</a></p><p>Server Handshake: <a href="http://www.imagebam.com/image/fa6eb5478413724">http://www.imagebam.com/image/fa6eb5478413724</a></p></div><div id="question-tags" class="tags-container tags">tls key private</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '16, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/39f2186530ec6e8babb86ad81f147fc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xenocyde&#39;s gravatar image" /><p>Xenocyde<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xenocyde has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '16, 06:45</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-51724" class="comments-container"></div><div id="comment-tools-51724" class="comment-tools"></div><div class="clear"></div><div id="comment-51724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51730"></span>

<div id="answer-container-51730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51730-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You get the server private key by asking the server administrator to give it to you. You can't get it from the packets. If you could, this would not be a secure method of communication.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '16, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51730" class="comments-container"><span id="51731"></span><div id="comment-51731" class="comment"><div id="post-51731-score" class="comment-score"></div><div class="comment-text"><p>Are we absolutely sure there's isn't any other way to obtain the private key?</p></div><div id="comment-51731-info" class="comment-info"><span class="comment-age">(17 Apr '16, 09:25)</span> Xenocyde</div></div><span id="51734"></span><div id="comment-51734" class="comment"><div id="post-51734-score" class="comment-score">2</div><div class="comment-text"><p>Yes, and if you're not able to get the private key from the server administrator, then it means they don't want you to have the key and you are not authorized to decrypt the traffic.</p></div><div id="comment-51734-info" class="comment-info"><span class="comment-age">(17 Apr '16, 10:38)</span> Jim Aragon</div></div><span id="51749"></span><div id="comment-51749" class="comment"><div id="post-51749-score" class="comment-score">1</div><div class="comment-text"><p>Another option is that you may be able to persuade the client application, e.g. by configuration or recompiling, to give up the session key or pre-master secret.</p><p>See <a href="https://wiki.wireshark.org/SSL#Using_the_.28Pre.29-Master-Secret">this</a> section of the Wireshark Wiki page on SSL.</p></div><div id="comment-51749-info" class="comment-info"><span class="comment-age">(18 Apr '16, 03:05)</span> grahamb ♦</div></div><span id="51792"></span><div id="comment-51792" class="comment"><div id="post-51792-score" class="comment-score">1</div><div class="comment-text"><p>@Xenocyde: The server key would not help you at all, as the server suggests to use a Diffie Hellman cipher, so the only thing that helps is what @grahamb sugested.</p><p>BTW: What is your problem? Maybe there are other way to achieve analyze a problem, like a SSL MITM Proxy.</p></div><div id="comment-51792-info" class="comment-info"><span class="comment-age">(19 Apr '16, 09:21)</span> Kurt Knochner ♦</div></div><span id="51794"></span><div id="comment-51794" class="comment"><div id="post-51794-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner: I need to see the code sent by the client and by the server to analyze a few instructions. So the SSL MITM Proxy might help me here. Thanks for the info.</p></div><div id="comment-51794-info" class="comment-info"><span class="comment-age">(19 Apr '16, 09:28)</span> Xenocyde</div></div></div><div id="comment-tools-51730" class="comment-tools"></div><div class="clear"></div><div id="comment-51730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

