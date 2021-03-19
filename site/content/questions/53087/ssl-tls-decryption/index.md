+++
type = "question"
title = "SSL &#92; TLS Decryption"
description = '''Hi, I have a question, do I need to export the personal key in the server, I mean mmc -&amp;gt; certificates -&amp;gt; personal?'''
date = "2016-05-31T16:35:00Z"
lastmod = "2016-06-01T02:11:00Z"
weight = 53087
keywords = [ "tls", "ssl", "decryption" ]
aliases = [ "/questions/53087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL \\ TLS Decryption](/questions/53087/ssl-tls-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53087-score" class="post-score" title="current number of votes">0</div><span id="post-53087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a question, do I need to export the personal key in the server, I mean mmc -&gt; certificates -&gt; personal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '16, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/c350038a7dd33938cf13107a22cfb311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ogoname&#39;s gravatar image" /><p><span>ogoname</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ogoname has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted <strong>01 Jun '16, 01:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53087" class="comments-container"><span id="53091"></span><div id="comment-53091" class="comment"><div id="post-53091-score" class="comment-score"></div><div class="comment-text"><p>Your comment has been converted to a new question as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-53091-info" class="comment-info"><span class="comment-age">(01 Jun '16, 02:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-53087" class="comment-tools"></div><div class="clear"></div><div id="comment-53087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53092"></span>

<div id="answer-container-53092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53092-score" class="post-score" title="current number of votes">0</div><span id="post-53092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do the instructions on the Wiki <a href="https://wiki.wireshark.org/SSL#SSL_dissection_in_Wireshark">SSL</a> page help?</p><p>Basically, yes, you must extract the key from wherever it resides into a format that Wireshark can handle, usually a PEM file. For Windows, you'll need to install openssl to do this, export the certificate with the private key to a .pfx file (PKCS #12), and then use the <code>openssl pkcs12</code> command given on the SSL page to extract the key. Windows will force you to protect the key in the .pfx file with a password, that should be given to openssl when it asks for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53092" class="comments-container"></div><div id="comment-tools-53092" class="comment-tools"></div><div class="clear"></div><div id="comment-53092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

