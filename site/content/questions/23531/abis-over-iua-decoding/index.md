+++
type = "question"
title = "Abis over IUA decoding"
description = '''Hi! I have capture file with Abis packets over IUA/SCTP. But the Abis packets are decoded incorrectly because Q.921 SAPI values are used by default in DLCI Parameter of IUA packets. I can&#x27;t find how to use the GSM SAPI values in DLCI Parameter of IUA packet. How the Abis messages that contained in I...'''
date = "2013-08-03T19:04:00Z"
lastmod = "2013-08-07T00:04:00Z"
weight = 23531
keywords = [ "abis", "gsm" ]
aliases = [ "/questions/23531" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Abis over IUA decoding](/questions/23531/abis-over-iua-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23531-score" class="post-score" title="current number of votes">0</div><span id="post-23531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I have capture file with Abis packets over IUA/SCTP. But the Abis packets are decoded incorrectly because Q.921 SAPI values are used by default in DLCI Parameter of IUA packets. I can't find how to use the GSM SAPI values in DLCI Parameter of IUA packet.</p><p>How the Abis messages that contained in IUA packets can be correctly decoded?</p><p>Thank You!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-abis" rel="tag" title="see questions tagged &#39;abis&#39;">abis</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '13, 19:04</strong></p><img src="https://secure.gravatar.com/avatar/a965e9524efdfd058c12cde67daf0f6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Volodymyr&#39;s gravatar image" /><p><span>Volodymyr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Volodymyr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '13, 01:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23531" class="comments-container"></div><div id="comment-tools-23531" class="comment-tools"></div><div class="clear"></div><div id="comment-23531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23537"></span>

<div id="answer-container-23537" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23537-score" class="post-score" title="current number of votes">0</div><span id="post-23537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try to change the preference of LAPD to use GSM SAPI:s</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '13, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-23537" class="comments-container"><span id="23545"></span><div id="comment-23545" class="comment"><div id="post-23545-score" class="comment-score"></div><div class="comment-text"><p>I tried this for LAPD but it doesn't changes the SAPI settings for IUA and Abis packets still displayed incorrectly. So IUA needs it's own option for SAPI.</p></div><div id="comment-23545-info" class="comment-info"><span class="comment-age">(05 Aug '13, 01:29)</span> <span class="comment-user userinfo">Volodymyr</span></div></div><span id="23550"></span><div id="comment-23550" class="comment"><div id="post-23550-score" class="comment-score">1</div><div class="comment-text"><p>Open a bug report supplying an example capture file.</p></div><div id="comment-23550-info" class="comment-info"><span class="comment-age">(05 Aug '13, 02:58)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="23597"></span><div id="comment-23597" class="comment"><div id="post-23597-score" class="comment-score"></div><div class="comment-text"><p>The abillity to dissect Abis over IUA was added in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=51171">http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=51171</a></p></div><div id="comment-23597-info" class="comment-info"><span class="comment-age">(06 Aug '13, 21:52)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="23601"></span><div id="comment-23601" class="comment"><div id="post-23601-score" class="comment-score"></div><div class="comment-text"><p>I've opened a bug report <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9017">#9017</a> an now it resolved and fixed. Thanks a lot!</p></div><div id="comment-23601-info" class="comment-info"><span class="comment-age">(07 Aug '13, 00:04)</span> <span class="comment-user userinfo">Volodymyr</span></div></div></div><div id="comment-tools-23537" class="comment-tools"></div><div class="clear"></div><div id="comment-23537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

