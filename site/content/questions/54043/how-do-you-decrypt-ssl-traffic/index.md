+++
type = "question"
title = "How do you decrypt SSL traffic?"
description = '''I&#x27;m practicing session hijacking on my Facebook account and when I attempt to locate the authentication cookie I am unable to, presumably because the packets are SSL encrypted. My question is how to I decrypt this traffic so I can read the packets??'''
date = "2016-07-13T11:46:00Z"
lastmod = "2016-07-17T05:10:00Z"
weight = 54043
keywords = [ "facebook", "ssl_decrypt" ]
aliases = [ "/questions/54043" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you decrypt SSL traffic?](/questions/54043/how-do-you-decrypt-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54043-score" class="post-score" title="current number of votes">0</div><span id="post-54043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm practicing session hijacking on my Facebook account and when I attempt to locate the authentication cookie I am unable to, presumably because the packets are SSL encrypted. My question is how to I decrypt this traffic so I can read the packets??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-facebook" rel="tag" title="see questions tagged &#39;facebook&#39;">facebook</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '16, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/0a1d53d4f9c0fff6e9b9c2a5de95942a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kieran%20John%20Gallicker-Irvine&#39;s gravatar image" /><p><span>Kieran John ...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kieran John Gallicker-Irvine has no accepted answers">0%</span></p></div></div><div id="comments-container-54043" class="comments-container"></div><div id="comment-tools-54043" class="comment-tools"></div><div class="clear"></div><div id="comment-54043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54113"></span>

<div id="answer-container-54113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54113-score" class="post-score" title="current number of votes">0</div><span id="post-54113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To decrypt the SSL Session you have to find a way to get the needed Pre Shared Key.</p><p>The <a href="https://wiki.wireshark.org/SSL">Wireshark Wiki entry for SSL</a> has everything you need, especially the paragraph "Using the (Pre)-Master-Secret". Besides other options it's also linking to a <a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">Detailed guide how to extract and use the Keys from some browsers.</a></p><p>But that's overkill if you just need the Cookie, which can be much simpler extracted from the browser cache (or plugins like Live HTTP Headers).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '16, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/18515a703aba0eefe60e68fcec7ba929?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Wetzel&#39;s gravatar image" /><p><span>Alexander We...</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Wetzel has no accepted answers">0%</span></p></div></div><div id="comments-container-54113" class="comments-container"></div><div id="comment-tools-54113" class="comment-tools"></div><div class="clear"></div><div id="comment-54113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

