+++
type = "question"
title = "Decrypting SSL Application Data."
description = '''I have a commercial client &amp;gt; server application that uses SSL to encrypt data between the two end-points and I want to decrypt it. FWIW it&#x27;s using a non-standard port(it doesn&#x27;t use port 443, 389, etc).  In the Edit &amp;gt; Preferences &amp;gt; Protocols &amp;gt; SSL &amp;gt; RSA keys list: field, there&#x27;s a par...'''
date = "2013-07-19T17:16:00Z"
lastmod = "2013-07-20T05:26:00Z"
weight = 23185
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/23185" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypting SSL Application Data.](/questions/23185/decrypting-ssl-application-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23185-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a commercial client &gt; server application that uses SSL to encrypt data between the two end-points and I want to decrypt it. FWIW it's using a non-standard port(it doesn't use port 443, 389, etc).</p><p>In the Edit &gt; Preferences &gt; Protocols &gt; SSL &gt; RSA keys list: field, there's a parameter to specify a protocol. In the examples I've seen the protocol listed is a clear text protocol(like HTTP or LDAP) but I don't know what the commercial application uses. Is there a way for me to tell without asking the vendor? Or what should go in the protocol field?</p><p>When I decode it I can see the handshake data but the Application Data is still encrypted.<br />
</p><p>I have the private key since it resides on the server so it seems I'm only missing the protocol.</p><p>Thanks, Gary</p></div><div id="question-tags" class="tags-container tags">ssl decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '13, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/da6136bb05cad38216624bf45bec0aaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GaryT&#39;s gravatar image" /><p>GaryT<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GaryT has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jul '13, 20:25</p></div></div><div id="comments-container-23185" class="comments-container"></div><div id="comment-tools-23185" class="comment-tools"></div><div class="clear"></div><div id="comment-23185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23194"></span>

<div id="answer-container-23194" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23194-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The handshake is always un-encrypted up to (and including) the "ChangeCipherSpec", then the last handshake message is "Finished". It will show as "Encrypted Handshake Message" when there is no decryption and it will show up as "Finished" if decryption is being done.</p><p>Do you see a "Finished" handshake message in both directions? If not, decryption is not working and could have several causes, the most common ones are:</p><ul><li>The key has not been loaded correctly (see the ssl debug file) or does not match the certificate</li><li>The SSL session was resumed and the full SSL handshake is not in the tracefile</li><li>The server chose a DH cipher for this session</li></ul><p>If you do see both "Finished" messages, the application data should not be visible.</p><p>If you are not sure which protocol is used inside SSL then you can use the protocol "data" in the RSA keys list, it will just show the decrypted data without any further dissection. You can then do a "follow SSL stream" to manually determine the protocol...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '13, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23194" class="comments-container"><span id="23236"></span><div id="comment-23236" class="comment"><div id="post-23236-score" class="comment-score"></div><div class="comment-text"><p>Thank-you. That was just what I needed.</p></div><div id="comment-23236-info" class="comment-info"><span class="comment-age">(22 Jul '13, 09:10)</span> GaryT</div></div><span id="23237"></span><div id="comment-23237" class="comment"><div id="post-23237-score" class="comment-score"></div><div class="comment-text"><p>For future reference to others, did you see the "Finished" SSL handshake messages? And if not, what part of my answer was helpful in solving your issue?</p></div><div id="comment-23237-info" class="comment-info"><span class="comment-age">(22 Jul '13, 09:39)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-23194" class="comment-tools"></div><div class="clear"></div><div id="comment-23194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

