+++
type = "question"
title = "Decrypting your own Tlsv1 packets?"
description = '''Hi everyone. I&#x27;m trying to write a program that interfaces to XYZ service&#x27;s servers. (basically their software is quite buggy and non-optimized so I want to make a client that offers some limited functionality without said bugs etc) The login uses TLSv1 and respectively, I know some of the data that...'''
date = "2011-07-25T13:32:00Z"
lastmod = "2011-07-25T16:57:00Z"
weight = 5232
keywords = [ "tlsv1", "decryption" ]
aliases = [ "/questions/5232" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypting your own Tlsv1 packets?](/questions/5232/decrypting-your-own-tlsv1-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5232-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone.</p><p>I'm trying to write a program that interfaces to XYZ service's servers. (basically their software is quite buggy and non-optimized so I want to make a client that offers some limited functionality without said bugs etc)</p><p>The login uses TLSv1 and respectively, I know some of the data that is getting sent (my username and password for example).<br />
</p><p>It there anyway to 'decrypt' your own packets? As I need the 'structure' of the 'login process' for my application to mimic it... And the original data and key to encrypt it is coming from my end anyway - so would this be possible?</p><p>Any help it greatly appreciated Kind regards, Luke</p></div><div id="question-tags" class="tags-container tags">tlsv1 decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '11, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/722a3e77d4695f7bad60b6d4711ee14a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lukus001&#39;s gravatar image" /><p>lukus001<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lukus001 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-5232" class="comments-container"></div><div id="comment-tools-5232" class="comment-tools"></div><div class="clear"></div><div id="comment-5232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5236"></span>

<div id="answer-container-5236" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5236-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To be able to decrypt SSL/TLS traffic with Wireshark, you need to have the server private key or have an export of the (pre-)master secret (which can be done with a self-compiled version of Chrome or Firefox with some debug options turned on or by using the openssl s_client). It sounds like those might not an option in your setup.</p><p>If you are able to use firefox to access their site, then the easiest way to decrypt the traffic (if it is https) is to use the httpfox add-on, this will give you all the decrypted http traffic.</p><p>If that's not possible, you might be able to do a man-in-the-middle with <a href="http://www.fiddler2.com/fiddler2/">Fiddler</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 16:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5236" class="comments-container"><span id="5262"></span><div id="comment-5262" class="comment"><div id="post-5262-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply SYNbit.</p><p>Their client is actually made in adobe air or more specifically; the login is handled with adobe flash. Looking at fiddler now, hopefully that will work :)</p><p>I believe flash uses TLS built in from windows (in this instance at least, because disabling it in internet options makes their login fail /give errors). Unfortunately their flash file does not load in a browser, so I don't know how it getting treated.</p><p>Anyway, thanks again for taking the time to help out.</p></div><div id="comment-5262-info" class="comment-info"><span class="comment-age">(26 Jul '11, 08:28)</span> lukus001</div></div></div><div id="comment-tools-5236" class="comment-tools"></div><div class="clear"></div><div id="comment-5236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

