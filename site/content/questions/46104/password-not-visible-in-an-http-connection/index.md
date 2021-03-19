+++
type = "question"
title = "Password not visible in an http connection"
description = '''Hello, i&#x27;m little late in this conversation but i need some help. i tried today to connect to my Box outside from my network &amp;amp; realized that the connection is in http:// once come home i tried the same from a VM &amp;amp; captured the traffic to see if the password is &quot; clear text &quot; the problem is t...'''
date = "2015-09-24T05:28:00Z"
lastmod = "2015-09-24T06:30:00Z"
weight = 46104
keywords = [ "password", "http" ]
aliases = [ "/questions/46104" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Password not visible in an http connection](/questions/46104/password-not-visible-in-an-http-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46104-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i'm little late in this conversation but i need some help. i tried today to connect to my Box outside from my network &amp; realized that the connection is in http:// once come home i tried the same from a VM &amp; captured the traffic to see if the password is " clear text " the problem is that i don't know in which frame to see. (which ones contains login / password ?) Tried "frame contains abc123 " &gt; doesn't work (why ? it's http:// , why would be crypted ?) Tried "http.request.method == "POST" shows something &amp; finaly tried frame contains "password". I got the frame which contains Key: Password and it's crypted.</p><p>8b7cc159a165e6d1dc23c96a83e4822690d737cb</p><p>base64 give's me this result ñ¾Üs^}k^¹{§uuÍ·sÞšów¸ómº÷G{ß·</p><p>and that's no my password.</p><p>have the same probleme with capturing email / password (in a hoeme lab)</p><p>thanks for your help</p></div><div id="question-tags" class="tags-container tags">password http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/75b1235cdca6afc5f90f1b32bcdd2cce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tome80&#39;s gravatar image" /><p>tome80<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tome80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '15, 10:05</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-46104" class="comments-container"></div><div id="comment-tools-46104" class="comment-tools"></div><div class="clear"></div><div id="comment-46104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46105"></span>

<div id="answer-container-46105" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46105-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are using HTTP the password will be within a POST request method. Since you know the password, follow the relevant tcp stream and search for it. It can be that the password is hashed. The one in your description looks like SHA1. If you want us to have a look, create a test account and upload a packet capture to cloudshark or similar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-46105" class="comments-container"><span id="46115"></span><div id="comment-46115" class="comment"><div id="post-46115-score" class="comment-score">1</div><div class="comment-text"><p>It would be worth determining if the authentication uses one of the browser schemes or if it's an application-based mechanism. If it's browser based you should see an HTTP status code 401 as a response to the first access to the host.</p><p>If you see the 401 you will be using:</p><ul><li>Basic authentication</li><li>MD5 hash</li><li>One of the Integrated Windows Authentication mechanisms - see Wikipedia</li></ul><p>If you have no 401s then the web app is handling authentication. This may still use a hash and I must admit your password value looks like a hash such as MD5. Unfortunately you would need to find the seed value to generate say an MD5 hash from yor password. You may be able to work it out from the login page source code or included Javascript.</p></div><div id="comment-46115-info" class="comment-info"><span class="comment-age">(24 Sep '15, 10:47)</span> PaulOfford</div></div><span id="46182"></span><div id="comment-46182" class="comment"><div id="post-46182-score" class="comment-score"></div><div class="comment-text"><p>You can't upload the file here, use cloudshark or some file hosting service.</p></div><div id="comment-46182-info" class="comment-info"><span class="comment-age">(25 Sep '15, 12:57)</span> Roland</div></div><span id="46210"></span><div id="comment-46210" class="comment"><div id="post-46210-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>I will close the post, seems to much for me but i'll retry properly and follow your advice. if need some help i'll be back.</p><p>thank's a lot.</p></div><div id="comment-46210-info" class="comment-info"><span class="comment-age">(28 Sep '15, 01:23)</span> tome80</div></div><span id="46224"></span><div id="comment-46224" class="comment"><div id="post-46224-score" class="comment-score"></div><div class="comment-text"><p>If a question has been solved for your, please <strong>don't</strong> mark the title with '[resolves]'!</p><p>Instead please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-46224-info" class="comment-info"><span class="comment-age">(28 Sep '15, 10:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46105" class="comment-tools"></div><div class="clear"></div><div id="comment-46105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

