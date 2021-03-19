+++
type = "question"
title = "Is it possible to decrypt an SSL Session post capture"
description = '''I know its possibly to decrypt an SSL session, but is it possible to decrypt an SSL session post capture?  I have a capture that was done with another product that they have no idea if or how to configure it to decrypt the SSL session. And putting wireshark on the network so far isn&#x27;t happening, but...'''
date = "2013-04-30T11:43:00Z"
lastmod = "2013-04-30T13:08:00Z"
weight = 20855
keywords = [ "ssl" ]
aliases = [ "/questions/20855" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to decrypt an SSL Session post capture](/questions/20855/is-it-possible-to-decrypt-an-ssl-session-post-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20855-score" class="post-score" title="current number of votes">0</div><span id="post-20855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know its possibly to decrypt an SSL session, but is it possible to decrypt an SSL session post capture?</p><p>I have a capture that was done with another product that they have no idea if or how to configure it to decrypt the SSL session. And putting wireshark on the network so far isn't happening, but I do have the SSL keys so the obvious question that I came up with, can I do it on that saved capture file?</p><p>THanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '13, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/1c6a54b83aa6ac638da2a21377a68452?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="modeerf&#39;s gravatar image" /><p><span>modeerf</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="modeerf has no accepted answers">0%</span></p></div></div><div id="comments-container-20855" class="comments-container"></div><div id="comment-tools-20855" class="comment-tools"></div><div class="clear"></div><div id="comment-20855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20856"></span>

<div id="answer-container-20856" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20856-score" class="post-score" title="current number of votes">1</div><span id="post-20856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes that is possible. In fact, I mostly capture on other devices and do the decryption in Wireshark on my laptop later on.</p><p>Keep in mind that there are 3 basic conditions that must be met to succesfully decrypt SSL traffic:</p><ul><li>You have to have the server private key that corresponds to the certificate in the captures SSL session. You seem to have those.</li><li>For each SSL session in the capture file that you would like to decrypt, you need to have the full SSL handshake (including the ClientKeyExchange handshake message). Especially if you have no control over the client nor server during capturing, they often reuse sessions that had their handshake before you started capturing.</li><li>The chosen cipher must not use a DiffieHellman key exchange (DH in the cipher name), as wireshark is unable to extract the MasterSecret (with the session key used for the encryption) from the capture when DH is used.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '13, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20856" class="comments-container"></div><div id="comment-tools-20856" class="comment-tools"></div><div class="clear"></div><div id="comment-20856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

