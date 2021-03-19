+++
type = "question"
title = "Decrypting SSL packets using Pre Master Key"
description = '''Hello! I need to decrypt outgoing traffic that my browser sends to server. I read that I can use Google Chrome browser which will generate all that SSL data stuff and I just would set path to this file in WireShark preferences. I&#x27;ve done it but there&#x27;s no pane &quot;Decrypted SSL data&quot;. My file contains ...'''
date = "2015-08-01T10:19:00Z"
lastmod = "2015-08-02T20:10:00Z"
weight = 44726
keywords = [ "chrome", "ssl", "premasterkey", "decryption" ]
aliases = [ "/questions/44726" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting SSL packets using Pre Master Key](/questions/44726/decrypting-ssl-packets-using-pre-master-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44726-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I need to decrypt outgoing traffic that my browser sends to server. I read that I can use Google Chrome browser which will generate all that SSL data stuff and I just would set path to this file in WireShark preferences. I've done it but there's no pane "Decrypted SSL data". My file contains strings like: 1) RSA a50214f50efc0ce0 03038488ef47796daeb5b9d1b849e90852ad3ae03aec71576e34b6517bf1e8914624e819aa31f1e97eaf6b82fe6fe1d3 2) CLIENT_RANDOM 05207c73974878df11a3d00dbfb932036fea9458fc638f92c6cd254409f2e3da 7729dcf9d4da029633bbe7da02302110f8cbe6c211e293c378e7a031e73020fbc8c9a236e07196ead5e10004e21acc26 Is this format correct? Should I change something to make decryption work? Also there was line in a guide I read that it will work only when you have specific Cipher Suite. In my case it is Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f). Will this method work for me? Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">chrome ssl premasterkey decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '15, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/5eb0b308d9e410fa76a2c02589113510?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krow7&#39;s gravatar image" /><p>krow7<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krow7 has no accepted answers">0%</span></p></div></div><div id="comments-container-44726" class="comments-container"></div><div id="comment-tools-44726" class="comment-tools"></div><div class="clear"></div><div id="comment-44726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44750"></span>

<div id="answer-container-44750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44750-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I followed the instructions from this guy's site --&gt; jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/ and was able to find some packets that would decrypt. What I have found (and its not really much help to you) is that not every frame or packet will be decrypted. If you want to see if yours is working try opening the page I show above using https. Then start a fresh capture with wireshark, and refresh the page above. and then scroll through the frames until you see the tab you are looking for using a display filter of "ssl &amp;&amp; tcp".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '15, 20:10</strong></p><img src="https://secure.gravatar.com/avatar/0a92214fd94d818059f740cdd56be7af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greenfreq&#39;s gravatar image" /><p>greenfreq<br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greenfreq has one accepted answer">33%</span></p></div></div><div id="comments-container-44750" class="comments-container"><span id="44769"></span><div id="comment-44769" class="comment"><div id="post-44769-score" class="comment-score"></div><div class="comment-text"><p>I tried to check frames from site you mentioned and it worked but not for my frames :( Thanks anyway for your responce. It became more clear to me.</p></div><div id="comment-44769-info" class="comment-info"><span class="comment-age">(03 Aug '15, 05:39)</span> krow7</div></div></div><div id="comment-tools-44750" class="comment-tools"></div><div class="clear"></div><div id="comment-44750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

