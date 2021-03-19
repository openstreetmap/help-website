+++
type = "question"
title = "Chunked gzip woes"
description = '''Topic says it...I&#x27;ve been having a really hard time getting chunked gzip to show correctly. The first issue is that with &quot;Allow subdissector to reassemble TCP streams&quot; check I only see the HTTP GET, not the response. So with &quot;Allow subdissector to reassemble TCP streams&quot; uncheck I at least see: HTTP...'''
date = "2016-01-04T13:11:00Z"
lastmod = "2016-01-06T13:16:00Z"
weight = 48852
keywords = [ "gzip", "chunked" ]
aliases = [ "/questions/48852" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Chunked gzip woes](/questions/48852/chunked-gzip-woes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48852-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Topic says it...I've been having a really hard time getting chunked gzip to show correctly. The first issue is that with "Allow subdissector to reassemble TCP streams" check I only see the HTTP GET, not the response. So with "Allow subdissector to reassemble TCP streams" uncheck I at least see:</p><p>HTTP/1.1 200 OK [Unreassembled Packet]</p><p>and can follow the stream. But I don't see an option show the de-chunked data. Is there something I'm missing? Thank you.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2016-01-04_14_12_54-teststream0.pcapng_%5BWireshark_2.0.1_(v2.0.1-0-g59ea380_from_master-2.0)%5D.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">gzip chunked</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '16, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/feeceb13b3a434a147fa2c173ad18db8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngelXX&#39;s gravatar image" /><p>DigiAngelXX<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngelXX has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '16, 13:15</p></div></div><div id="comments-container-48852" class="comments-container"><span id="48854"></span><div id="comment-48854" class="comment"><div id="post-48854-score" class="comment-score"></div><div class="comment-text"><p>This is a good workaround for this, but it would be nice to see this built in:</p><p><a href="https://github.com/morhekil/wireshark-http-gunzip">https://github.com/morhekil/wireshark-http-gunzip</a></p></div><div id="comment-48854-info" class="comment-info"><span class="comment-age">(04 Jan '16, 13:54)</span> DigiAngelXX</div></div><span id="48926"></span><div id="comment-48926" class="comment"><div id="post-48926-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response. Some I could see, but the above I could not. wireshark-http-gunzip was what allowed me to see the data, alas though not within wireshark.</p></div><div id="comment-48926-info" class="comment-info"><span class="comment-age">(06 Jan '16, 13:39)</span> DigiAngelXX</div></div><span id="48927"></span><div id="comment-48927" class="comment"><div id="post-48927-score" class="comment-score"></div><div class="comment-text"><p>It it possible that your stream is incomplete? When the connection is cut short (partial HTTP response), then no response is shown.</p></div><div id="comment-48927-info" class="comment-info"><span class="comment-age">(06 Jan '16, 14:21)</span> Lekensteyn</div></div><span id="48928"></span><div id="comment-48928" class="comment"><div id="post-48928-score" class="comment-score"></div><div class="comment-text"><p>Negative...what you see in the screenshot is what I had...packets are fine...I've just started seeing this in the last....like 4 months.</p></div><div id="comment-48928-info" class="comment-info"><span class="comment-age">(06 Jan '16, 14:24)</span> DigiAngelXX</div></div><span id="48929"></span><div id="comment-48929" class="comment"><div id="post-48929-score" class="comment-score"></div><div class="comment-text"><p>Are you able to isolate a TCP session (Follow TCP Stream) and share the capture? You can mail a link/capture privately if you prefer that.</p></div><div id="comment-48929-info" class="comment-info"><span class="comment-age">(06 Jan '16, 14:45)</span> Lekensteyn</div></div><span id="48931"></span><div id="comment-48931" class="comment not_top_scorer"><div id="post-48931-score" class="comment-score"></div><div class="comment-text"><p>I can share it privately...just let me know who/where to send to :) Thank you.</p></div><div id="comment-48931-info" class="comment-info"><span class="comment-age">(06 Jan '16, 15:29)</span> DigiAngelXX</div></div><span id="48940"></span><div id="comment-48940" class="comment not_top_scorer"><div id="post-48940-score" class="comment-score"></div><div class="comment-text"><p>You can find my contact details in my profile, but please test it yourself with Wireshark 2.0.1 first and a new configuration profile (because that is the first thing I'll do ;)).</p></div><div id="comment-48940-info" class="comment-info"><span class="comment-age">(07 Jan '16, 04:33)</span> Lekensteyn</div></div><span id="48944"></span><div id="comment-48944" class="comment not_top_scorer"><div id="post-48944-score" class="comment-score"></div><div class="comment-text"><p>Thanks...I'll send the pcap your way.</p></div><div id="comment-48944-info" class="comment-info"><span class="comment-age">(07 Jan '16, 07:36)</span> DigiAngelXX</div></div><span id="48947"></span><div id="comment-48947" class="comment not_top_scorer"><div id="post-48947-score" class="comment-score"></div><div class="comment-text"><p>In the pcap you send me I can see the OK response in frame 33 (tested with an empty configuration profile in 2.0.1 and the latest development code (master)).</p></div><div id="comment-48947-info" class="comment-info"><span class="comment-age">(07 Jan '16, 08:16)</span> Lekensteyn</div></div></div><div id="comment-tools-48852" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-48852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48925"></span>

<div id="answer-container-48925" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48925-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>@DigiAngelXX Tested with Wireshark 2.0.1 and I can see the uncompressed, chunked response just fine. What version are you using? Can you share the pcap if it still occurs with 2.0.1? Try the http-chunked-gzip.pcap from <a href="https://wiki.wireshark.org/SampleCaptures#HyperText_Transport_Protocol_.28HTTP.29">https://wiki.wireshark.org/SampleCaptures#HyperText_Transport_Protocol_.28HTTP.29</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '16, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-48925" class="comments-container"><span id="48948"></span><div id="comment-48948" class="comment"><div id="post-48948-score" class="comment-score"></div><div class="comment-text"><p>Well I'll be...I installed the latest WS in a vm and I got your same results...I'm not sure what I've done to break my config...thanks a bunch for this info.</p></div><div id="comment-48948-info" class="comment-info"><span class="comment-age">(07 Jan '16, 08:33)</span> DigiAngelXX</div></div><span id="48952"></span><div id="comment-48952" class="comment"><div id="post-48952-score" class="comment-score"></div><div class="comment-text"><p>Once I enabled the TCP preference <em>Allow subdissector to reassemble TCP streams</em> in the configuration profile you sent me, your packet shows just fine.</p></div><div id="comment-48952-info" class="comment-info"><span class="comment-age">(07 Jan '16, 12:08)</span> Lekensteyn</div></div><span id="48958"></span><div id="comment-48958" class="comment"><div id="post-48958-score" class="comment-score"></div><div class="comment-text"><p>I converted the comment to an answer as it seemed to be the answer so @DigiAngelXX could mark it as so.</p></div><div id="comment-48958-info" class="comment-info"><span class="comment-age">(07 Jan '16, 15:56)</span> grahamb ♦</div></div></div><div id="comment-tools-48925" class="comment-tools"></div><div class="clear"></div><div id="comment-48925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

