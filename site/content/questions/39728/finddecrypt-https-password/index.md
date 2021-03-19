+++
type = "question"
title = "Find/Decrypt HTTPS Password"
description = '''Hello. I need to find a gmail password in a sample capture for a school club using only wireshark. Gmail is obviously encrypted and I have no idea how to do this. There are so many packets with the google IP and I don&#x27;t know which one to choose. Any and all help is appreciated.'''
date = "2015-02-09T15:56:00Z"
lastmod = "2015-02-09T16:07:00Z"
weight = 39728
keywords = [ "ssl", "decryption", "https", "gmail" ]
aliases = [ "/questions/39728" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find/Decrypt HTTPS Password](/questions/39728/finddecrypt-https-password)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39728-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I need to find a gmail password in a sample capture for a school club using only wireshark. Gmail is obviously encrypted and I have no idea how to do this. There are so many packets with the google IP and I don't know which one to choose. Any and all help is appreciated.</p></div><div id="question-tags" class="tags-container tags">ssl decryption https gmail</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '15, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/89a6b6d0fa0f0d6286ac2f4ce377b975?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wire_Shark_Pro&#39;s gravatar image" /><p>Wire_Shark_Pro<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wire_Shark_Pro has no accepted answers">0%</span></p></div></div><div id="comments-container-39728" class="comments-container"></div><div id="comment-tools-39728" class="comment-tools"></div><div class="clear"></div><div id="comment-39728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39731"></span>

<div id="answer-container-39731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39731-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You won't find the password, as gmail uses HTTPS (ssl/tls encryption) by default for some years.</p><p>Without the RSA key of the google servers (I guess you don't have those keys) or a dumped session key of the "attacked" browser (you'll have to dump that while you are accessing gmail) you won't be able to decrypt that communication unless you are a super hacker from an alien planet or you work for the NSA department Str0ngBalls78. In the later case, you will get displaced tomorrow morning at 0600 because you asked silly questions in an open forum ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '15, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Feb '15, 16:09</p></div></div><div id="comments-container-39731" class="comments-container"><span id="39732"></span><div id="comment-39732" class="comment"><div id="post-39732-score" class="comment-score"></div><div class="comment-text"><p>I probably have a dumped session key as the capture file was designed for high school kids to find the gmail password. I am positive I have all the information i just need to know how to find the session key, and use it to decrypt the HTTPS password</p></div><div id="comment-39732-info" class="comment-info"><span class="comment-age">(09 Feb '15, 16:10)</span> Wire_Shark_Pro</div></div><span id="39733"></span><div id="comment-39733" class="comment"><div id="post-39733-score" class="comment-score"></div><div class="comment-text"><p>I probably have a dumped session key as the capture file was designed for high school kids to find the gmail password. I am positive I have all the information i just need to know how to find the session key, and use it to decrypt the HTTPS password</p></div><div id="comment-39733-info" class="comment-info"><span class="comment-age">(09 Feb '15, 16:13)</span> Wire_Shark_Pro</div></div><span id="39734"></span><div id="comment-39734" class="comment"><div id="post-39734-score" class="comment-score"></div><div class="comment-text"><p>Ah, O.K. then please have a look at one of those ssl decryption tutorials:</p><blockquote><p><a href="https://www.google.com/?q=wireshark+ssl+decryption+tutorial">https://www.google.com/?q=wireshark+ssl+decryption+tutorial</a></p></blockquote><p>One of the first 3-5 should help.</p><blockquote><p>There are so many packets with the google IP and I don't know which one to choose</p></blockquote><p>Think about DNS!!</p></div><div id="comment-39734-info" class="comment-info"><span class="comment-age">(09 Feb '15, 16:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-39731" class="comment-tools"></div><div class="clear"></div><div id="comment-39731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

