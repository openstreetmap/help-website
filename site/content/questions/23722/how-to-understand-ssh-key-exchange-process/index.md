+++
type = "question"
title = "How to understand SSH Key exchange process?"
description = '''Hi all, I want to understand basic functional aspects behind SSH key exchange. I tried to understand looking at RFC but felt little complex for me to comprehend from it. Here are the 7 Packets I got from t-shark using display filter &quot;ssh.message_code&quot; SSHv2 Client: Key Exchange Init SSHv2 Server: Ke...'''
date = "2013-08-12T17:28:00Z"
lastmod = "2013-08-14T14:44:00Z"
weight = 23722
keywords = [ "ssh" ]
aliases = [ "/questions/23722" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to understand SSH Key exchange process?](/questions/23722/how-to-understand-ssh-key-exchange-process)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23722-score" class="post-score" title="current number of votes">0</div><span id="post-23722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I want to understand basic functional aspects behind SSH key exchange. I tried to understand looking at RFC but felt little complex for me to comprehend from it.</p><p>Here are the 7 Packets I got from t-shark using display filter "ssh.message_code"</p><p>SSHv2 Client: Key Exchange Init</p><p>SSHv2 Server: Key Exchange Init</p><p>SSHv2 Client: Diffie-Hellman Key Exchange Init</p><p>SSHv2 Server: Diffie-Hellman Key Exchange Reply</p><p>SSHv2 Client: Diffie-Hellman GEX Init</p><p>SSHv2 Server: Diffie-Hellman GEX Reply</p><p>SSHv2 Client: New Keys</p><p>If you find some time to reply please help me understand what each packet means to client/server</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '13, 17:28</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Aug '13, 17:29</strong> </span></p></div></div><div id="comments-container-23722" class="comments-container"></div><div id="comment-tools-23722" class="comment-tools"></div><div class="clear"></div><div id="comment-23722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23742"></span>

<div id="answer-container-23742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23742-score" class="post-score" title="current number of votes">2</div><span id="post-23742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This question is actually not really to Wireshark (although you used tshark) and thus it is a bit off-topic for this Q&amp;A site.</p><p>A quick google search for <strong><a href="http://bit.ly/13gV1jk">ssh protocol explained</a></strong> returned several pages that explain the ssh protocol in detail.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '13, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23742" class="comments-container"><span id="23748"></span><div id="comment-23748" class="comment"><div id="post-23748-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, When it comes to troubleshooting TCP , we start our conversation with their conversation(3-way handshake).Like wise i felt this is also a part of conversation in it's own approach(Key exchange)and hence i raised a question to understand it better from experts. Yah, thanks for your suggestion.I will look in to the material mentioned.</p></div><div id="comment-23748-info" class="comment-info"><span class="comment-age">(13 Aug '13, 08:56)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="23770"></span><div id="comment-23770" class="comment"><div id="post-23770-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>i raised a question to understand it better from experts</p></blockquote><p>well, here are some Wireshark and networking/protocol experts and I'm sure someone would be able to explain the SSH protocol. But how much sense does it make to do that, while there are great resources available out there. After you have studied those resources you are more than welcome to come back and ask specific questions ;-)</p></div><div id="comment-23770-info" class="comment-info"><span class="comment-age">(14 Aug '13, 04:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23785"></span><div id="comment-23785" class="comment"><div id="post-23785-score" class="comment-score"></div><div class="comment-text"><p>Sound good:)</p></div><div id="comment-23785-info" class="comment-info"><span class="comment-age">(14 Aug '13, 14:44)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div></div><div id="comment-tools-23742" class="comment-tools"></div><div class="clear"></div><div id="comment-23742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

