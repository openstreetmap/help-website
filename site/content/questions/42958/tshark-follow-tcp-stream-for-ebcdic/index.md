+++
type = "question"
title = "tshark follow tcp stream for EBCDIC"
description = '''Hello, I was able to follow tcp stream with the newest releases of tshark: tshark -r file.cap -q -z follow,tcp,ascii,0 . Unfortunately my traffic is EBCDIC encoded and while I can read it with Wireshark I can&#x27;t with tshark, it miss the ebcdic format while still has hex and raw. Anyone can help me fi...'''
date = "2015-06-07T22:29:00Z"
lastmod = "2015-06-08T12:40:00Z"
weight = 42958
keywords = [ "ebcdic", "follow", "tcp_stream", "tshark", "for" ]
aliases = [ "/questions/42958" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tshark follow tcp stream for EBCDIC](/questions/42958/tshark-follow-tcp-stream-for-ebcdic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42958-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I was able to follow tcp stream with the newest releases of tshark: tshark -r file.cap -q -z follow,tcp,ascii,0 . Unfortunately my traffic is EBCDIC encoded and while I can read it with Wireshark I can't with tshark, it miss the ebcdic format while still has hex and raw. Anyone can help me find a solution?</p></div><div id="question-tags" class="tags-container tags">ebcdic follow tcp_stream tshark for</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '15, 22:29</strong></p><img src="https://secure.gravatar.com/avatar/b79727deacc72fbf0e78a11cd2a9df7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pippo&#39;s gravatar image" /><p>pippo<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pippo has no accepted answers">0%</span></p></div></div><div id="comments-container-42958" class="comments-container"><span id="42964"></span><div id="comment-42964" class="comment"><div id="post-42964-score" class="comment-score"></div><div class="comment-text"><p>What are you trying to do? Print the EBCDIC encoded "text" on your DOS box screen with tshark?</p></div><div id="comment-42964-info" class="comment-info"><span class="comment-age">(08 Jun '15, 01:15)</span> Kurt Knochner ♦</div></div><span id="42969"></span><div id="comment-42969" class="comment"><div id="post-42969-score" class="comment-score"></div><div class="comment-text"><p>I just need to read the payload in a tn3270 session. I read it ok with wireshark follow tcp stream selecting ebcdic but I can't from tshark.</p></div><div id="comment-42969-info" class="comment-info"><span class="comment-age">(08 Jun '15, 05:02)</span> pippo</div></div></div><div id="comment-tools-42958" class="comment-tools"></div><div class="clear"></div><div id="comment-42958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42980"></span>

<div id="answer-container-42980" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42980-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is not supported yet, so I uploaded a patch adding this capability to <a href="https://code.wireshark.org/review/#/c/8844/">code review website</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '15, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-42980" class="comments-container"><span id="42991"></span><div id="comment-42991" class="comment"><div id="post-42991-score" class="comment-score"></div><div class="comment-text"><p>The patch is now merged and is available starting from version v1.99.7rc0-135-ge28339e. You can download a nightly build from here: <a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p></div><div id="comment-42991-info" class="comment-info"><span class="comment-age">(08 Jun '15, 22:25)</span> Pascal Quantin</div></div></div><div id="comment-tools-42980" class="comment-tools"></div><div class="clear"></div><div id="comment-42980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42981"></span>

<div id="answer-container-42981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42981-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. by "I need to <strong>read</strong> the payload" you (most certainly) mean, tshark shall print the characters on the console for you to read it, right? If so, you'll have to print the TCP payload with tshark in <strong>hex mode</strong> (-z follow,tcp,hex,0) and then use a Perl script (or any other scripting language you prefer) to convert the hex output to EBCDIC and then convert to ASCII, to be able to print it on the console.</p><blockquote><p><a href="http://search.cpan.org/~cxl/Convert-EBCDIC-0.06/lib/Convert/EBCDIC.pm">http://search.cpan.org/~cxl/Convert-EBCDIC-0.06/lib/Convert/EBCDIC.pm</a></p></blockquote><p>Function: ebcdic2ascii().</p><blockquote><p><a href="http://objectmix.com/perl/20922-hex-ebcdic.html">http://objectmix.com/perl/20922-hex-ebcdic.html</a></p></blockquote><p>As an alternative, you can use one of the online <a href="http://mcraigweaver.com/ebcdic.htm">HEX -&gt; EBCDIC converters</a> (using raw output of tshark), but I guess that won't help you, as it involves a manual step.</p><p>OR, wait until the code change of @Pascal Quantin has been finished ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '15, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42981" class="comments-container"><span id="43016"></span><div id="comment-43016" class="comment"><div id="post-43016-score" class="comment-score"></div><div class="comment-text"><p>I tried it and seem to fail in converting the data into something readable. Unfortunately I can't provide a sample of tn3270 as it contains sensitive infos :(</p></div><div id="comment-43016-info" class="comment-info"><span class="comment-age">(09 Jun '15, 09:55)</span> pippo</div></div></div><div id="comment-tools-42981" class="comment-tools"></div><div class="clear"></div><div id="comment-42981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

