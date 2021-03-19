+++
type = "question"
title = "SSL decrypting"
description = '''I am trying to decode/decrypt ssl transactions between my laptop and an EC2 on the Amazon Cloud. We have an ssl cert from Verisign (cert, chain, root). How do I take this info and create a key that Wireshark will use to decrypt the data ?? I look at the SSL log file and it tells me that it can&#x27;t loa...'''
date = "2012-03-15T11:16:00Z"
lastmod = "2012-03-20T18:56:00Z"
weight = 9560
keywords = [ "ssl", "cert", "verasign" ]
aliases = [ "/questions/9560" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decrypting](/questions/9560/ssl-decrypting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9560-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decode/decrypt ssl transactions between my laptop and an EC2 on the Amazon Cloud. We have an ssl cert from Verisign (cert, chain, root). How do I take this info and create a key that Wireshark will use to decrypt the data ?? I look at the SSL log file and it tells me that it can't load the pem file. Specifically, the ssl log file says:</p><p>ssl_load_key: can't import pem data</p><p>How do I take the .crt and create a .pem that Wireshark will be happy with ??</p><p>thanks wk</p><p>p.s. I did search thru the site and did not see anything that specifically addressed what I am experiencing.</p></div><div id="question-tags" class="tags-container tags">ssl cert verasign</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '12, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/2b12f1f0687101a1dd8f75db884aed8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakelt&#39;s gravatar image" /><p>wakelt<br />
<span class="score" title="13 reputation points">13</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakelt has no accepted answers">0%</span></p></div></div><div id="comments-container-9560" class="comments-container"></div><div id="comment-tools-9560" class="comment-tools"></div><div class="clear"></div><div id="comment-9560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9668"></span>

<div id="answer-container-9668" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9668-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One additional thing to look out for is that usually a .crt file extension is not used for a key (either public or private.) It just contains an X509 certificate which in turn contains only the public key and other information about you and the Issuer, etc.</p><p>What Verisign sends to you <em>cannot</em> include the private key because you never sent it to them in the first place.</p><p>When you generated a Certificate Signing Request (CSR) to send to Verisign, the private key was probably created at that point or earlier and stored locally. If you are lucky, it will be in a Java keystore or a .key extension file somewhere. If you are unlucky it may be in a secure storage within your OS from which you may not be able to export it.<br />
</p><p>If you cannot find the private key, you will have to start over and generate a new key pair, this time making sure that the private key stays accessible, and then send a new CSR using that key pair.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-9668" class="comments-container"></div><div id="comment-tools-9668" class="comment-tools"></div><div class="clear"></div><div id="comment-9668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9561"></span>

<div id="answer-container-9561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9561-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://wiki.wireshark.org/SSL">SSL</a> Wiki page has some info on converting keys to pem format, although .crt files aren't mentioned. The following link provides lots of answers to the question: <a href="http://lmgtfy.com/?q=.crt+to+pem">.crt to pem</a>, but the best answer seems to be <a href="http://stackoverflow.com/questions/991758/openssl-pem-key">here</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '12, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9561" class="comments-container"><span id="9574"></span><div id="comment-9574" class="comment"><div id="post-9574-score" class="comment-score"></div><div class="comment-text"><p>Yup i agree with grahamb</p></div><div id="comment-9574-info" class="comment-info"><span class="comment-age">(15 Mar '12, 23:55)</span> carolin</div></div></div><div id="comment-tools-9561" class="comment-tools"></div><div class="clear"></div><div id="comment-9561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

