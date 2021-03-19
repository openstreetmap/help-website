+++
type = "question"
title = "Decrypting a Wireshark capture without the private key"
description = '''Good afternoon, I have being assigned the task of decrypting a wireshark capture between a user and a server. The transaction is an e-mail with an attachment. I have not being provided with the private key and as such I am unsure how to proceed can anyone help? Kind Regards'''
date = "2015-11-29T07:00:00Z"
lastmod = "2015-11-30T16:23:00Z"
weight = 48056
keywords = [ "ssl", "ssl_decrypt" ]
aliases = [ "/questions/48056" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting a Wireshark capture without the private key](/questions/48056/decrypting-a-wireshark-capture-without-the-private-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48056-score" class="post-score" title="current number of votes">0</div><span id="post-48056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good afternoon,</p><p>I have being assigned the task of decrypting a wireshark capture between a user and a server. The transaction is an e-mail with an attachment. I have not being provided with the private key and as such I am unsure how to proceed can anyone help?</p><p>Kind Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '15, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/65b6dc2b0d119651916aa9d5a6fca704?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArdenUK&#39;s gravatar image" /><p><span>ArdenUK</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArdenUK has no accepted answers">0%</span></p></div></div><div id="comments-container-48056" class="comments-container"><span id="48061"></span><div id="comment-48061" class="comment"><div id="post-48061-score" class="comment-score"></div><div class="comment-text"><p>Haha, Interesting.. I have being given a challenge to complete (job interview) and it is a puzzling one! Only thing I have managed to do some far is convert the subject text to plain text from a ceasar cypher but the attachment which I presume has the private key is still a mystery!</p></div><div id="comment-48061-info" class="comment-info"><span class="comment-age">(29 Nov '15, 12:26)</span> <span class="comment-user userinfo">ArdenUK</span></div></div></div><div id="comment-tools-48056" class="comment-tools"></div><div class="clear"></div><div id="comment-48056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48111"></span>

<div id="answer-container-48111" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48111-score" class="post-score" title="current number of votes">0</div><span id="post-48111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <strong>idea of encryption</strong> is to keep data secure and "hideen" and that only those who own the key are able to decrypt the data set. So, a work assignment as described above ("Decrypting a capture without the private key"), does not make any sense, unless you omited the relevant parts in your question (see comment of <span><span>@ArdenUK</span></span> about caesar cipher).</p><p>So, I see the following possible reasons for such a 'work assignment'.</p><ul><li>The person who asked for it, tries to probe you to see if you understand encryption</li><li>You misunderstood the work assignment and in reality it's about <strong>decoding</strong> a pcap file that contains SMTP traffic and/or POP3/IMAP, and <strong>not decrypting data</strong></li><li>The person who asked for it has zero knowledge of encryption and does not understand that he/she is asking for the impossible</li><li>You are working for an ultra secure TLA (three letter agency) and you are trained with alien technology to crack even the hardest encryption algorithms. In that case, you failed miserably in several ways (Nr #1: not being able to do what you have been trained for, Nr #2: Posting about this in a public Q&amp;A site, Nr #3: not creating your own business with such a skill set).</li></ul><p>Please choose the most likely reason for you.</p><p>If you'd ask me, I's say item #1 and/or item #2.</p><p><span><span>@ArdenUK</span></span>: similar for you, although you actually mentioned a real encryption system (caesar cipher). <strong>However</strong>: Without any information about the work assignment, how are we supposed to help or even comment on your question/problem?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-48111" class="comments-container"></div><div id="comment-tools-48111" class="comment-tools"></div><div class="clear"></div><div id="comment-48111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

