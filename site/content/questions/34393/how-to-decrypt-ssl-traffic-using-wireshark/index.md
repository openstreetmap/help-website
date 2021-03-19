+++
type = "question"
title = "How to decrypt SSL Traffic using wireshark"
description = '''I got an SSL trace file ran on a traffic generator which is copied to my local machine. I know the way to navigate wireshark for decrypting the SSL traffic but confused with what key/cert i need to feed as input to wireshark(RSA KEY LIST/Keys) in this case . Here is the bunch of information i got. C...'''
date = "2014-07-03T15:39:00Z"
lastmod = "2014-07-04T01:22:00Z"
weight = 34393
keywords = [ "ssl", "ssl_decrypt" ]
aliases = [ "/questions/34393" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decrypt SSL Traffic using wireshark](/questions/34393/how-to-decrypt-ssl-traffic-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34393-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I got an SSL trace file ran on a traffic generator which is copied to my local machine. I know the way to navigate wireshark for decrypting the SSL traffic but confused with what key/cert i need to feed as input to wireshark(RSA KEY LIST/Keys) in this case . Here is the bunch of information i got.</p><p>Client certificate</p><p>Client Private key</p><p>Server ca cert</p><p>I came to know that the file should be converted to .pem for wireshark to decrypt. Please let me know which one to pick from above 3 for decryption.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ssl ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '14, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-34393" class="comments-container"></div><div id="comment-tools-34393" class="comment-tools"></div><div class="clear"></div><div id="comment-34393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34397"></span>

<div id="answer-container-34397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34397-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <a href="http://wiki.wireshark.org/SSL#Wireshark">the Wireshark wiki on SSL</a>. You need to add a private key. The certificates (both CA and client/server) are useless as they are already sent over the wire and do not contains decryption keys anyway.</p><p>Be aware of some possible limitations. In particular the choice of cipher suites, PFS cipher suites (the (EC)DHE ones) cannot be decrypted even if you posess the private key. If you have access to the Pre-Master secrets, then you do not have this limitation, but it will require cooperation from the application to get these keys.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '14, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-34397" class="comments-container"></div><div id="comment-tools-34397" class="comment-tools"></div><div class="clear"></div><div id="comment-34397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

