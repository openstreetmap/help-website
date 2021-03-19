+++
type = "question"
title = "How can i get private key (RSA) from SSL traffic?"
description = '''Hi, I have SSL packet capture and i want wireshark to decode the SSL traffic, for that i need RSA private key.Can anyone help me how to get that key from my SSL capture. Thanks JK'''
date = "2011-09-04T20:33:00Z"
lastmod = "2011-09-04T23:45:00Z"
weight = 6082
keywords = [ "ssl", "rsa", "key" ]
aliases = [ "/questions/6082" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can i get private key (RSA) from SSL traffic?](/questions/6082/how-can-i-get-private-key-rsa-from-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6082-score" class="post-score" title="current number of votes">0</div><span id="post-6082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have SSL packet capture and i want wireshark to decode the SSL traffic, for that i need RSA private key.Can anyone help me how to get that key from my SSL capture.</p><p>Thanks JK</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-rsa" rel="tag" title="see questions tagged &#39;rsa&#39;">rsa</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '11, 20:33</strong></p><img src="https://secure.gravatar.com/avatar/01febacc45af8ecf743c4f575d428326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JK7&#39;s gravatar image" /><p><span>JK7</span><br />
<span class="score" title="31 reputation points">31</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JK7 has no accepted answers">0%</span></p></div></div><div id="comments-container-6082" class="comments-container"></div><div id="comment-tools-6082" class="comment-tools"></div><div class="clear"></div><div id="comment-6082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6083"></span>

<div id="answer-container-6083" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6083-score" class="post-score" title="current number of votes">3</div><span id="post-6083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The private key cannot be extracted from the captured trace. It must be provided by you to decrypt the traffic. The private key is, um, 'private', and must be provided by the owner of the key, or obtained through some other means.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '11, 21:53</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div></div><div id="comments-container-6083" class="comments-container"><span id="6084"></span><div id="comment-6084" class="comment"><div id="post-6084-score" class="comment-score"></div><div class="comment-text"><p>Hi Griff , Can you guide me, how to obtain RSA key..</p></div><div id="comment-6084-info" class="comment-info"><span class="comment-age">(04 Sep '11, 22:15)</span> <span class="comment-user userinfo">JK7</span></div></div><span id="6085"></span><div id="comment-6085" class="comment"><div id="post-6085-score" class="comment-score"></div><div class="comment-text"><p>Hi Griff , Can you guide me, how to obtain RSA key..</p></div><div id="comment-6085-info" class="comment-info"><span class="comment-age">(04 Sep '11, 22:18)</span> <span class="comment-user userinfo">JK7</span></div></div><span id="6087"></span><div id="comment-6087" class="comment"><div id="post-6087-score" class="comment-score">1</div><div class="comment-text"><p>You have to call the administrator of the server and explain why you need the key. Depending on the purpose of the site and the security policy you will either get the key or not.</p><p>You may want to use common sense to determine whether a call to the administrator is worth it or not (or even harmful to your carreer).</p></div><div id="comment-6087-info" class="comment-info"><span class="comment-age">(04 Sep '11, 23:45)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-6083" class="comment-tools"></div><div class="clear"></div><div id="comment-6083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

