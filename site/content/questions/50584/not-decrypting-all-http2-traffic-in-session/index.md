+++
type = "question"
title = "Not Decrypting all HTTP/2 traffic in session."
description = '''I cannot seem to decrypt every HTTP/2 packet in a given session using my pre shared keys. Setup  Set SSLKEYLOGFILE environent variable. Open Wireshark + Chrome from terminal. Open desired site in Chrome and watch trace in Wireshark.  Problem It seems that sometimes all the HTTP/2 packets are decrypt...'''
date = "2016-02-29T11:22:00Z"
lastmod = "2016-03-07T12:02:00Z"
weight = 50584
keywords = [ "tls", "ssl", "decryption", "http2" ]
aliases = [ "/questions/50584" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not Decrypting all HTTP/2 traffic in session.](/questions/50584/not-decrypting-all-http2-traffic-in-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50584-score" class="post-score" title="current number of votes">0</div><span id="post-50584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I cannot seem to decrypt every HTTP/2 packet in a given session using my pre shared keys.</p><p><strong>Setup</strong></p><ol><li>Set SSLKEYLOGFILE environent variable.</li><li>Open Wireshark + Chrome from terminal.</li><li>Open desired site in Chrome and watch trace in Wireshark.</li></ol><p><strong>Problem</strong></p><p>It seems that sometimes all the HTTP/2 packets are decrypted, and then other times only ~half of them are. If I open the Statistics -&gt; HTTP2 dialogue the number of packets sent/received can fluctuate from ~350 to ~1050 when loading the same page.</p><p>Occasionally several "Ignored Unknown Record" packets will appear too. I'm assuming these are sometimes being decrypted as HTTP/2 packets, and sometimes they're not for some unknown reason.</p><p><strong>Link to PCAP File &amp; Key</strong></p><p><a href="https://mega.nz/#!yBk2xaQQ!NYeRXY6vHqOrh0wzndMje5dSf0x6cUTCy75ewJvQ5xc">https://mega.nz/#!yBk2xaQQ!NYeRXY6vHqOrh0wzndMje5dSf0x6cUTCy75ewJvQ5xc</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-http2" rel="tag" title="see questions tagged &#39;http2&#39;">http2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '16, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/c313b41d21a690f6d61f835bc8909826?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r0sscon&#39;s gravatar image" /><p><span>r0sscon</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r0sscon has no accepted answers">0%</span></p></div></div><div id="comments-container-50584" class="comments-container"></div><div id="comment-tools-50584" class="comment-tools"></div><div class="clear"></div><div id="comment-50584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50755"></span>

<div id="answer-container-50755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50755-score" class="post-score" title="current number of votes">1</div><span id="post-50755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that wireshark fails to detect all TLS records that start in the middle of a TCP segment when segments are lost or arrive out of order or are re-transmitted. The following filter shows all TLS records with a record length of 1424 bytes including those that are not recognized. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_834_Hsdm3Yi.png" alt="alt text" /><br />
</p><p>It might be worth filing a bug at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a><br />
Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '16, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-50755" class="comments-container"><span id="50756"></span><div id="comment-50756" class="comment"><div id="post-50756-score" class="comment-score"></div><div class="comment-text"><p>Thanks for this, I'd never have guessed that was the problem. I'll raise a bug report for it.</p></div><div id="comment-50756-info" class="comment-info"><span class="comment-age">(07 Mar '16, 09:11)</span> <span class="comment-user userinfo">r0sscon</span></div></div><span id="50759"></span><div id="comment-50759" class="comment"><div id="post-50759-score" class="comment-score"></div><div class="comment-text"><p>WOuld you please accept the answer if it satisfies your question by clicking on the checkmark icon. Thanks</p></div><div id="comment-50759-info" class="comment-info"><span class="comment-age">(07 Mar '16, 12:02)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-50755" class="comment-tools"></div><div class="clear"></div><div id="comment-50755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

