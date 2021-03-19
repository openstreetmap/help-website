+++
type = "question"
title = "Latency issues, ISP says possibly a malicious source and to download wireshark and take a look at my traffic. Any help on looking?"
description = '''So I have very limited experience with wireshark, but my isp is telling me that my latency issues aren&#x27;t coming from them and that it&#x27;s possibly malicious, DoS or DDoS or somesuch. I&#x27;m trying to teach myself the basics, and the wiki is a great resource, but I was hoping for some expert opinions. Sch...'''
date = "2014-11-06T18:55:00Z"
lastmod = "2014-11-07T12:10:00Z"
weight = 37631
keywords = [ "dos", "ddos", "malicious", "imnewatthis" ]
aliases = [ "/questions/37631" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Latency issues, ISP says possibly a malicious source and to download wireshark and take a look at my traffic. Any help on looking?](/questions/37631/latency-issues-isp-says-possibly-a-malicious-source-and-to-download-wireshark-and-take-a-look-at-my-traffic-any-help-on-looking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I have very limited experience with wireshark, but my isp is telling me that my latency issues aren't coming from them and that it's possibly malicious, DoS or DDoS or somesuch. I'm trying to teach myself the basics, and the wiki is a great resource, but I was hoping for some expert opinions. School is pretty hectic atm, so I don't have a lot of time to learn this stuff, though I'm trying. You can download my capture file here, if anyone feels up to it -&gt; <a href="http://tinyurl.com/ozptvm5">http://tinyurl.com/ozptvm5</a> Already sanitized, I think.</p><p>Any pointers on figuring this out for myself if no one feels up to scanning through my cap?</p></div><div id="question-tags" class="tags-container tags">dos ddos malicious imnewatthis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '14, 18:55</strong></p><img src="https://secure.gravatar.com/avatar/195e92f650378f4a0c5170d34b868ace?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dewbydo&#39;s gravatar image" /><p>dewbydo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dewbydo has no accepted answers">0%</span></p></div></div><div id="comments-container-37631" class="comments-container"></div><div id="comment-tools-37631" class="comment-tools"></div><div class="clear"></div><div id="comment-37631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37666"></span>

<div id="answer-container-37666" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37666-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The only latency issue that I see in the trace is for client port <code>tcp.port eq 58403</code> where your SYN packet gets dropped and your windows takes 3 seconds for the first retransmission.<br />
All other delays <code>tcp.analysis.ack_rtt ge 0.2</code> are caused by delayed acknowledgments.</p><p>There is a hotfix out there that allows to reduce the minRTO value in Windows: <a href="http://support.microsoft.com/kb/2472264">http://support.microsoft.com/kb/2472264</a></p><p>After you install this hotfix, you can configure the following TCP configurations by using the netsh command:</p><p>Configuration 1: Initial RTO</p><pre><code>netsh interface tcp set global &lt;for help&gt;
netsh interface tcp set global initialRto=&lt;value in msec&gt;
netsh interface tcp show global

Note This command displays the values that are set.</code></pre><p>Warning : Setting a low value of Initial RTO could result in failure to connect.</p><hr /><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-37666" class="comments-container"><span id="37679"></span><div id="comment-37679" class="comment"><div id="post-37679-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I'll look into this. Any idea what a good iRTO time would be? Or this an experimentation thing?</p></div><div id="comment-37679-info" class="comment-info"><span class="comment-age">(07 Nov '14, 16:45)</span> dewbydo</div></div><span id="37684"></span><div id="comment-37684" class="comment"><div id="post-37684-score" class="comment-score"></div><div class="comment-text"><p>A better - still conservative - iRTO is probably 200 ms. It is a matter of the average RTT of your connections. As they will vary depending on where you are connecting to, there is no 'one size fits all' iRTO though.</p></div><div id="comment-37684-info" class="comment-info"><span class="comment-age">(07 Nov '14, 22:43)</span> mrEEde</div></div><span id="37699"></span><div id="comment-37699" class="comment"><div id="post-37699-score" class="comment-score"></div><div class="comment-text"><p>hey i have the same issue but and worse for me it stems from a video game on ps4 and theses trying to be so slick and constantly guys are trying to hack manipulate and some how mess with my connection i run wire shark and it will say for some reason it shut down my laptop and ps4 all of a sudden sounds like their are working so hard ive been trying get rid of these guys for several months its been so aggravating ive been looking for hackers to get them back but i really just want my connection fixed it always dropps drastically im supposed to get 100 upload and 20 down i only get 10 and under all kinds of errors ive had 7 technitians from my provider switched modems countless times and switched providers and still i could use anyone's help thank you<br />
</p></div><div id="comment-37699-info" class="comment-info"><span class="comment-age">(08 Nov '14, 10:51)</span> MostUnlikedO...</div></div></div><div id="comment-tools-37666" class="comment-tools"></div><div class="clear"></div><div id="comment-37666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

