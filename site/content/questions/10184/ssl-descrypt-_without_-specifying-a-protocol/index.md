+++
type = "question"
title = "SSL Descrypt _without_ specifying a protocol?"
description = '''Hi there, Is there any way of NOT specifying a protocol when configuring Wireshark to automatically SSL decrypt (i.e. when adding the key to the RSA key list). I have a custom app that uses SSL to protect its connections, and I&#x27;d just like to decrypt the textual data that is passed. Instead, for now...'''
date = "2012-04-16T04:18:00Z"
lastmod = "2012-04-16T04:34:00Z"
weight = 10184
keywords = [ "ssl", "decrypt", "rsa" ]
aliases = [ "/questions/10184" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Descrypt \_without\_ specifying a protocol?](/questions/10184/ssl-descrypt-_without_-specifying-a-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10184-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>Is there any way of NOT specifying a protocol when configuring Wireshark to automatically SSL decrypt (i.e. when adding the key to the RSA key list).</p><p>I have a custom app that uses SSL to protect its connections, and I'd just like to decrypt the textual data that is passed. Instead, for now, I just put http, wireshark lists it as "Non-HTTP traffic" and it seems things get truncated...</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ssl decrypt rsa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/8054641efef8cb34de294336656bbc1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nafe&#39;s gravatar image" /><p>nafe<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nafe has no accepted answers">0%</span></p></div></div><div id="comments-container-10184" class="comments-container"></div><div id="comment-tools-10184" class="comment-tools"></div><div class="clear"></div><div id="comment-10184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10185"></span>

<div id="answer-container-10185" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10185-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can use "data" as the protocol. Wireshark will then just show the decrypted data as hex data.</p><p>Hmmm... thinking of this, it might be nice to have an "ascii" dissector that one can use if the decrypted protocol is ascii. You might want to file an enhancement request for it on <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a> if the data dissector does not provide the output you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10185" class="comments-container"></div><div id="comment-tools-10185" class="comment-tools"></div><div class="clear"></div><div id="comment-10185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

