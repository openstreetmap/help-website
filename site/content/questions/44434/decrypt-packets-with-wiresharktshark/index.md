+++
type = "question"
title = "Decrypt packets with wireshark/tshark"
description = '''I&#x27;m reading how to decrypt packets from this article https://wiki.wireshark.org/HowToDecrypt802.11 is it possible to specifify which key corresponds to which SSID? And, is there an equivalent in tshark?'''
date = "2015-07-24T10:17:00Z"
lastmod = "2015-07-24T10:43:00Z"
weight = 44434
keywords = [ "encryption", "tshark", "decryption", "wireshark" ]
aliases = [ "/questions/44434" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypt packets with wireshark/tshark](/questions/44434/decrypt-packets-with-wiresharktshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44434-score" class="post-score" title="current number of votes">0</div><span id="post-44434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm reading how to decrypt packets from this article</p><p><a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>is it possible to specifify which key corresponds to which SSID? And, is there an equivalent in tshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/f8e9cc3c86f1d1814aa3a51408d9e4b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob328080&#39;s gravatar image" /><p><span>Bob328080</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob328080 has no accepted answers">0%</span></p></div></div><div id="comments-container-44434" class="comments-container"></div><div id="comment-tools-44434" class="comment-tools"></div><div class="clear"></div><div id="comment-44434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44435"></span>

<div id="answer-container-44435" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44435-score" class="post-score" title="current number of votes">0</div><span id="post-44435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bob328080 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is it possible to specifify which key corresponds to which SSID?</p></blockquote><p>as written on that page: wpa-pwd:MyPassword:MySSID</p><blockquote><p>And, is there an equivalent in tshark?</p></blockquote><p>no, if you want to specify the keys on the tshark CLI.</p><p>BTW: take a look at the following article. It might help you.</p><blockquote><p><a href="http://www.lovemytool.com/blog/2010/05/wireshark-and-tshark-decrypt-sample-capture-file-by-joke-snelders.html">http://www.lovemytool.com/blog/2010/05/wireshark-and-tshark-decrypt-sample-capture-file-by-joke-snelders.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44435" class="comments-container"></div><div id="comment-tools-44435" class="comment-tools"></div><div class="clear"></div><div id="comment-44435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

