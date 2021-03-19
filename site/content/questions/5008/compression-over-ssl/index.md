+++
type = "question"
title = "Compression over SSL"
description = '''Hi everyone. I would like to analyze application-data compressed over SSL. SSL is using &quot;compression method: DEFLATE(1)&quot;. I can decrypt SSL-data since I have private-key. But I can&#x27;t see application-data because of that data is compressed. I have a question. Can I de-compress data over SSL using wir...'''
date = "2011-07-13T00:22:00Z"
lastmod = "2011-07-19T01:23:00Z"
weight = 5008
keywords = [ "ssl" ]
aliases = [ "/questions/5008" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Compression over SSL](/questions/5008/compression-over-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5008-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone.</p><p>I would like to analyze application-data compressed over SSL. SSL is using "compression method: DEFLATE(1)". I can decrypt SSL-data since I have private-key. But I can't see application-data because of that data is compressed.</p><p>I have a question. Can I de-compress data over SSL using wireshark?</p><p>Many thanks.</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '11, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/ae2c2e1fcbe24496169c2e2503367af6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="four_books&#39;s gravatar image" /><p>four_books<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="four_books has no accepted answers">0%</span></p></div></div><div id="comments-container-5008" class="comments-container"><span id="5038"></span><div id="comment-5038" class="comment"><div id="post-5038-score" class="comment-score"></div><div class="comment-text"><p>Additonally, I am working as Network Engineer. I am not a purpose at all for mischievous. Trouble shooting now.</p></div><div id="comment-5038-info" class="comment-info"><span class="comment-age">(13 Jul '11, 22:20)</span> four_books</div></div></div><div id="comment-tools-5008" class="comment-tools"></div><div class="clear"></div><div id="comment-5008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5039"></span>

<div id="answer-container-5039" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5039-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Even though the SSL protocol has long supported compression at the SSL layer, it was not used (see also: <a href="http://www.belshe.com/2010/11/18/ssl-compression-and-you/">http://www.belshe.com/2010/11/18/ssl-compression-and-you/</a>). Unfortunately no-one bothered to add decompression to the SSL dissector, so currently Wreshark can't decompress data that has been compressed at the SSL layer.</p><p>You might want to file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> to have decompression added to the SSL dissector. Please attach a tracefile that contains compressed SSL data to your request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '11, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5039" class="comments-container"><span id="5040"></span><div id="comment-5040" class="comment"><div id="post-5040-score" class="comment-score"></div><div class="comment-text"><p>Hi SYNbit.</p><p>Thank you for your kindly research. I got it. Currenlty Wireshark doesn't have feature that decompressing compressed packet over ssl. What a pity! I have been expected future release.</p></div><div id="comment-5040-info" class="comment-info"><span class="comment-age">(14 Jul '11, 01:19)</span> four_books</div></div><span id="5053"></span><div id="comment-5053" class="comment"><div id="post-5053-score" class="comment-score"></div><div class="comment-text"><p>In order for "decompression at the SSL level" to be included in a future release, someone needs to find the interest in enahncing the SSL dissector. It helps if you can file the enhancement request mentioned earlier.</p></div><div id="comment-5053-info" class="comment-info"><span class="comment-age">(15 Jul '11, 06:46)</span> SYN-bit ♦♦</div></div><span id="5073"></span><div id="comment-5073" class="comment"><div id="post-5073-score" class="comment-score"></div><div class="comment-text"><p>Hi, decompression in the SSL/TLS dissector was implemented about four years ago (svn rev. 21368). As I have not used it for a long time I can not say if it works or if it has been broken meanwhile.</p></div><div id="comment-5073-info" class="comment-info"><span class="comment-age">(16 Jul '11, 04:44)</span> keksa</div></div></div><div id="comment-tools-5039" class="comment-tools"></div><div class="clear"></div><div id="comment-5039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5114"></span>

<div id="answer-container-5114" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5114-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi.</p><blockquote><p>Hi, decompression in the SSL/TLS dissector was implemented about four years ago (svn rev. 21368).</p></blockquote><p>Can we use "decompression in the SSL/TLS dissector" in currently release?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '11, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/ae2c2e1fcbe24496169c2e2503367af6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="four_books&#39;s gravatar image" /><p>four_books<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="four_books has no accepted answers">0%</span></p></div></div><div id="comments-container-5114" class="comments-container"></div><div id="comment-tools-5114" class="comment-tools"></div><div class="clear"></div><div id="comment-5114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

