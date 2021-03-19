+++
type = "question"
title = "Decrypting website accessed through internet explorer"
description = '''First of all apologies if the following question is unclear as I am unfamiliar with network security. I can view tabular data on a website after logging into my account. The website has TLS encryption and can only be accessed using Internet Explorer. I need to set up Wireshark to decrypt the data an...'''
date = "2017-05-30T06:37:00Z"
lastmod = "2017-05-30T07:10:00Z"
weight = 61698
keywords = [ "ssl", "internet", "explorer", "decription" ]
aliases = [ "/questions/61698" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting website accessed through internet explorer](/questions/61698/decrypting-website-accessed-through-internet-explorer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61698-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First of all apologies if the following question is unclear as I am unfamiliar with network security.</p><p>I can view tabular data on a website after logging into my account. The website has TLS encryption and can only be accessed using Internet Explorer.</p><p>I need to set up Wireshark to decrypt the data and write into a text file. I need the data to perform some analysis. Found some material to log ssl session key but the method only works with Chrome and Firefox.</p><p>Not sure where to start. Can someone point me in the right direction?</p><p>I'm also open to hiring a consultant to help me with this. Again can someone point me where to look for such consultants?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">ssl internet explorer decription</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '17, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/2686140deae3cf1d3f3d6ae21e0dad33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benctr&#39;s gravatar image" /><p>benctr<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benctr has no accepted answers">0%</span></p></div></div><div id="comments-container-61698" class="comments-container"></div><div id="comment-tools-61698" class="comment-tools"></div><div class="clear"></div><div id="comment-61698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61699"></span>

<div id="answer-container-61699" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61699-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use <a href="http://www.telerik.com/fiddler">Fiddler</a>, it can work with any browser.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '17, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61699" class="comments-container"><span id="61709"></span><div id="comment-61709" class="comment"><div id="post-61709-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb. Is WireShark out of the question because the website must be accessed using Internet Explorer?</p></div><div id="comment-61709-info" class="comment-info"><span class="comment-age">(31 May '17, 07:22)</span> benctr</div></div><span id="61711"></span><div id="comment-61711" class="comment"><div id="post-61711-score" class="comment-score"></div><div class="comment-text"><p>Yep, unless someone else knows how to get keying material out of IE.</p></div><div id="comment-61711-info" class="comment-info"><span class="comment-age">(31 May '17, 07:31)</span> grahamb ♦</div></div><span id="61775"></span><div id="comment-61775" class="comment"><div id="post-61775-score" class="comment-score"></div><div class="comment-text"><p>It can be done, but it is not easy: <a href="https://www.blackhat.com/docs/us-16/materials/us-16-Kambic-Cunning-With-CNG-Soliciting-Secrets-From-SChannel.pdf">https://www.blackhat.com/docs/us-16/materials/us-16-Kambic-Cunning-With-CNG-Soliciting-Secrets-From-SChannel.pdf</a></p></div><div id="comment-61775-info" class="comment-info"><span class="comment-age">(04 Jun '17, 09:51)</span> Lekensteyn</div></div><span id="61776"></span><div id="comment-61776" class="comment"><div id="post-61776-score" class="comment-score"></div><div class="comment-text"><p>Oooh, access to SChannel secrets. Obviously requires elevated privs, but given that I think something could be done at run-time to give a Wireshark plugin access to the keys.</p></div><div id="comment-61776-info" class="comment-info"><span class="comment-age">(04 Jun '17, 12:00)</span> grahamb ♦</div></div></div><div id="comment-tools-61699" class="comment-tools"></div><div class="clear"></div><div id="comment-61699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

