+++
type = "question"
title = "How do I dissect decrypted SSL data when I&#x27;m using a Master-Secret log?"
description = '''I&#x27;m trying to dissect data protected with SSL/TLS encryption. I can decrypt the SSL data, because I have access to the Master Secret, but I can&#x27;t figure out how to apply a dissector on the decrypted data. I can see in SSL preferences that if I were using an RSA key list, I could just input the name ...'''
date = "2016-12-18T11:25:00Z"
lastmod = "2017-01-10T12:49:00Z"
weight = 58217
keywords = [ "ssl", "master-secret", "ssl_decrypt" ]
aliases = [ "/questions/58217" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I dissect decrypted SSL data when I'm using a Master-Secret log?](/questions/58217/how-do-i-dissect-decrypted-ssl-data-when-im-using-a-master-secret-log)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58217-score" class="post-score" title="current number of votes">0</div><span id="post-58217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to dissect data protected with SSL/TLS encryption. I can decrypt the SSL data, because I have access to the Master Secret, but I can't figure out how to apply a dissector on the decrypted data. I can see in SSL preferences that if I were using an RSA key list, I could just input the name of the protocol to use for the decrypted data (and I've tested that it works). I'd like to get that same functionality when I'm using a Master-Secret log, is that possible?</p><p>Alternatively, is it possible to write a Lua dissector chained with the built-in SSL dissector to dissect the decrypted data? If so, how do I access the decrypted data? The SSL dissector puts them in as a new Data Source, but I don't know how to work with that, is there a way? Can I somehow get a Tvb filled with the decrypted data?</p><p>Thank you for any advice!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-master-secret" rel="tag" title="see questions tagged &#39;master-secret&#39;">master-secret</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '16, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/772b2f4eb7ad67d98edb0d0f64d77d04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MixMaxMo&#39;s gravatar image" /><p><span>MixMaxMo</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MixMaxMo has no accepted answers">0%</span></p></div></div><div id="comments-container-58217" class="comments-container"><span id="58489"></span><div id="comment-58489" class="comment"><div id="post-58489-score" class="comment-score"></div><div class="comment-text"><p>I don't use SSL much but, after doing decrypting, can you right-click on one of the packets and do Decode-As your dissector? Or will that do Decode-As at the TCP layer rather than the SSL layer?</p></div><div id="comment-58489-info" class="comment-info"><span class="comment-age">(03 Jan '17, 15:26)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-58217" class="comment-tools"></div><div class="clear"></div><div id="comment-58217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58562"></span>

<div id="answer-container-58562" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58562-score" class="post-score" title="current number of votes">1</div><span id="post-58562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MixMaxMo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK I tried it out in Wireshark 2.2.3 and it appears that once you've decrypted using a Master-Secret file that you're then able to right-click on a frame and Decode-As the SSL/TLS port as some protocol of your choosing (you just want to choose the Field name <code>SSL TCP Dissector</code>).</p><p>@luffy_loundi is correct: if you control the (upper layer) dissector it is easy enough to register the dissector on the <code>ssl.port</code> dissector table. Along the same lines (to answer your second question), yes, you could write a Lua dissector to register for the appropriate <code>ssl.port</code> and then decode the (already decrypted) data. Or you could use that dissector as a "shim" which then just calls the built-in dissector of your choice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '17, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58562" class="comments-container"><span id="58646"></span><div id="comment-58646" class="comment"><div id="post-58646-score" class="comment-score"></div><div class="comment-text"><p>You're absolutely right, thank you and thanks to luffy_koundi as well, all it took was to add the dissector to the <code>ssl.port</code> table and then do the Decode As... (or just register the right port).</p></div><div id="comment-58646-info" class="comment-info"><span class="comment-age">(10 Jan '17, 12:49)</span> <span class="comment-user userinfo">MixMaxMo</span></div></div></div><div id="comment-tools-58562" class="comment-tools"></div><div class="clear"></div><div id="comment-58562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58553"></span>

<div id="answer-container-58553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58553-score" class="post-score" title="current number of votes">1</div><span id="post-58553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>SSL dissector uses the port number to decide on how to dissect the decrypted data. Various protocols register their ports into an "association". So your dissector needs to add itself if it isn't doing it already. In case there is no association found for a particular port, heuristic dissectors are tried which further claim the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '17, 23:12</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p><span>koundi</span><br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jan '17, 04:26</strong> </span></p></div></div><div id="comments-container-58553" class="comments-container"></div><div id="comment-tools-58553" class="comment-tools"></div><div class="clear"></div><div id="comment-58553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

