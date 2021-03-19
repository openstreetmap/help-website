+++
type = "question"
title = "decrypt ldap over ssl"
description = '''Hi guys, I&#x27;m unable to decrypt ldaps traffic using Wireshark. My concern is (not sure about it) I have the private key from the Server but when I open it it begins with -----BEGIN PRIVATE KEY----- and not -----BEGIN RSA PRIVATE KEY----- can this cause problems ? Any help is much appreciated ! Thank ...'''
date = "2015-09-21T04:38:00Z"
lastmod = "2015-09-21T04:51:00Z"
weight = 45999
keywords = [ "ssl", "ldap" ]
aliases = [ "/questions/45999" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [decrypt ldap over ssl](/questions/45999/decrypt-ldap-over-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45999-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I'm unable to decrypt ldaps traffic using Wireshark. My concern is (not sure about it) I have the private key from the Server but when I open it it begins with -----BEGIN PRIVATE KEY----- and not -----BEGIN RSA PRIVATE KEY----- can this cause problems ?</p><p>Any help is much appreciated !</p><p>Thank you and best regards</p><p>Adam</p></div><div id="question-tags" class="tags-container tags">ssl ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '15, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-45999" class="comments-container"><span id="46001"></span><div id="comment-46001" class="comment"><div id="post-46001-score" class="comment-score"></div><div class="comment-text"><p>Also, I was able to decrypt the snakeoil capure file.</p></div><div id="comment-46001-info" class="comment-info"><span class="comment-age">(21 Sep '15, 04:41)</span> adasko</div></div></div><div id="comment-tools-45999" class="comment-tools"></div><div class="clear"></div><div id="comment-45999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46003"></span>

<div id="answer-container-46003" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46003-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it it begins with -----BEGIN PRIVATE KEY----- and not -----BEGIN RSA PRIVATE KEY-----</p></blockquote><p>Try to add the string "RSA" to it. What happens then?</p><blockquote><p>can this cause problems ?</p></blockquote><p>yes. You should see that in the SSL debug file</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; SSL -&gt; SSL debug file</p></blockquote><p>If possible, please upload the ssl debug file somewhere and post the link here.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '15, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46003" class="comments-container"><span id="46010"></span><div id="comment-46010" class="comment"><div id="post-46010-score" class="comment-score"></div><div class="comment-text"><p>thank you Kurt for you comment ! i did now the following. Used openSSL to convert it the correct format. When I open the new key file now, it says BEGIN RSA PRIVATE KEY but still not able to decrypt the data. Just one more what not sure if is ok. I mean when I open the .key file i get the content inside in one long line , not in rows ....</p></div><div id="comment-46010-info" class="comment-info"><span class="comment-age">(21 Sep '15, 05:30)</span> adasko</div></div><span id="46012"></span><div id="comment-46012" class="comment"><div id="post-46012-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I mean when I open the .key file i get the content inside in one long line , not in rows ....</p></blockquote><p>That does not matter.</p><p>Can you please post the ssl debug file. Without that I will have to look into my crystal ball to figure out what's wrong ;-)</p></div><div id="comment-46012-info" class="comment-info"><span class="comment-age">(21 Sep '15, 06:09)</span> Kurt Knochner ♦</div></div><span id="46015"></span><div id="comment-46015" class="comment"><div id="post-46015-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt! Where can i get one :D ?</p><p>I suspect that it's the private key. Customer will provide a new key. For now I consider this to be solved and will mark as resolved. If still issues will report it back !</p><p>Thank you and have a great day !</p><p>BR Adam</p></div><div id="comment-46015-info" class="comment-info"><span class="comment-age">(21 Sep '15, 07:15)</span> adasko</div></div><span id="46024"></span><div id="comment-46024" class="comment"><div id="post-46024-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p></div><div id="comment-46024-info" class="comment-info"><span class="comment-age">(21 Sep '15, 09:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46003" class="comment-tools"></div><div class="clear"></div><div id="comment-46003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

