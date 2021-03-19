+++
type = "question"
title = "SSL Decrypt works depending on the used browser"
description = '''Hello all, I have a &quot;strange&quot; problem with SSL decoding and I don&#x27;t know how to explain it. I have a test server (apache+ssl) and I access that server with IE 8. Wireshark configured with the corect server SSL key, everything is working fine and I can see the SSL stream decoded. Same scenario, but I...'''
date = "2012-08-24T06:17:00Z"
lastmod = "2012-08-24T06:25:00Z"
weight = 13874
keywords = [ "decode", "ssl", "decrypt", "browser" ]
aliases = [ "/questions/13874" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decrypt works depending on the used browser](/questions/13874/ssl-decrypt-works-depending-on-the-used-browser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13874-score" class="post-score" title="current number of votes">0</div><span id="post-13874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I have a "strange" problem with SSL decoding and I don't know how to explain it. I have a test server (apache+ssl) and I access that server with IE 8. Wireshark configured with the corect server SSL key, everything is working fine and I can see the SSL stream decoded.</p><p>Same scenario, but I use Firefox 14. In this case I cannot see anything being decoded.</p><p>Does anybody has an explanation for this or a point to start looking for a possible solution?</p><p>Just to avoid any useless discussions, on both test I start the Wireshark and then the browser so I capture the entire stream with initial SSL handshake.</p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '12, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/ee83b9c32de82946addc7285abfae34b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yotis&#39;s gravatar image" /><p><span>yotis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yotis has no accepted answers">0%</span></p></div></div><div id="comments-container-13874" class="comments-container"></div><div id="comment-tools-13874" class="comment-tools"></div><div class="clear"></div><div id="comment-13874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13875"></span>

<div id="answer-container-13875" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13875-score" class="post-score" title="current number of votes">1</div><span id="post-13875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is it that Firefox permits the DH cipher and IE 8 doesn't? SSL decryption requires use of an RSA cipher not a DH one. The client and the server negotiate on the cipher to be used. See the answers to this <a href="http://ask.wireshark.org/questions/13721/decrypt-ssl-traffic-problem-because-of-dhe-cipher">question</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '12, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13875" class="comments-container"></div><div id="comment-tools-13875" class="comment-tools"></div><div class="clear"></div><div id="comment-13875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

