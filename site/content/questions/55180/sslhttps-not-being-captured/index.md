+++
type = "question"
title = "SSL/HTTPS not being captured"
description = '''Hello, I have an iMac where i installed WireShark and i am filtering all HTTP traffic, but all i see is normal HTTP, i don&#x27;t see any HTTPS. The same thing is happening in an Ubuntu installation. Any idea what could be wrong?  Thanks'''
date = "2016-08-29T14:25:00Z"
lastmod = "2016-08-30T07:55:00Z"
weight = 55180
keywords = [ "ssl", "https", "capture" ]
aliases = [ "/questions/55180" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL/HTTPS not being captured](/questions/55180/sslhttps-not-being-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55180-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have an iMac where i installed WireShark and i am filtering all HTTP traffic, but all i see is normal HTTP, i don't see any HTTPS. The same thing is happening in an Ubuntu installation.</p><p>Any idea what could be wrong?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-08-30_at_8.36.44_AM_GTEiA90.png" alt="alt text" /></p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ssl https capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '16, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/1b7877c3f563ce8aaa31cbef15456c81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexsmith&#39;s gravatar image" /><p>alexsmith<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexsmith has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '16, 22:38</p></div></div><div id="comments-container-55180" class="comments-container"><span id="55181"></span><div id="comment-55181" class="comment"><div id="post-55181-score" class="comment-score"></div><div class="comment-text"><p>Can you take a picture of the filter you are using?</p></div><div id="comment-55181-info" class="comment-info"><span class="comment-age">(29 Aug '16, 14:30)</span> BruteForce</div></div><span id="55187"></span><div id="comment-55187" class="comment"><div id="post-55187-score" class="comment-score"></div><div class="comment-text"><p>I uploaded the image.</p></div><div id="comment-55187-info" class="comment-info"><span class="comment-age">(29 Aug '16, 22:38)</span> alexsmith</div></div></div><div id="comment-tools-55180" class="comment-tools"></div><div class="clear"></div><div id="comment-55180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55204"></span>

<div id="answer-container-55204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55204-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your display filter "http" is only going to show http traffic from the capture - not filter it out. In order to filter it out you would have to do not http or negate it.</p><p>Looks like this....."!http" or you can spell it out "not http". This will show you all the remaining traffic, after http has been removed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p>BruteForce<br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-55204" class="comments-container"></div><div id="comment-tools-55204" class="comment-tools"></div><div class="clear"></div><div id="comment-55204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55205"></span>

<div id="answer-container-55205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55205-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no protocol HTTPS, https is a URI scheme for http secure, see <a href="https://tools.ietf.org/html/rfc7230#section-2.7.2">RFC 7230</a>.</p><p>If you have captured HTTPS traffic, Wireshark will show TLS\SSL (as appropriate) as the protocol.</p><p>If you then supply the appropriate keying material to Wireshark, the traffic will be decrypted and show up as HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55205" class="comments-container"><span id="55278"></span><div id="comment-55278" class="comment"><div id="post-55278-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer, that helps, although it is not complete. How do i supply the appropriate keying material? What does that mean?</p></div><div id="comment-55278-info" class="comment-info"><span class="comment-age">(02 Sep '16, 03:41)</span> alexsmith</div></div><span id="55282"></span><div id="comment-55282" class="comment"><div id="post-55282-score" class="comment-score"></div><div class="comment-text"><p>See the Wireshark Wiki page on <a href="https://wiki.wireshark.org/SSL">SSL</a> for info on how to add keys to Wireshark.</p></div><div id="comment-55282-info" class="comment-info"><span class="comment-age">(02 Sep '16, 04:11)</span> grahamb ♦</div></div><span id="55375"></span><div id="comment-55375" class="comment"><div id="post-55375-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that makes more sense now. Unfortunately, it is not working for me.. I followed all their steps and it is not working for me for some reason, it does not decrypt.. Please have a look at my video and let me know if you see anything wrong: <a href="http://screencast.com/t/tMM2KBqa">http://screencast.com/t/tMM2KBqa</a> (sorry about the background noise)</p></div><div id="comment-55375-info" class="comment-info"><span class="comment-age">(07 Sep '16, 09:07)</span> alexsmith</div></div><span id="55376"></span><div id="comment-55376" class="comment"><div id="post-55376-score" class="comment-score"></div><div class="comment-text"><p>A video isn't much use, but the SSL debug log is. In the SSL preferences, where you added the key, there is a path to the file to be used for the SSL debug log. Set that accordingly, reload your capture, then edit your question with the debug log, using the "code" button to format it for easier reading.</p></div><div id="comment-55376-info" class="comment-info"><span class="comment-age">(07 Sep '16, 09:26)</span> grahamb ♦</div></div></div><div id="comment-tools-55205" class="comment-tools"></div><div class="clear"></div><div id="comment-55205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

