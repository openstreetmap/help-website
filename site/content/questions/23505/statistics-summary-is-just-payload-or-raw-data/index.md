+++
type = "question"
title = "Statistics summary is just payload or raw data ?"
description = '''Hello, I&#x27;m trying to find payload average for UDP. Can any one explain me whether &quot;Average data rate speed&quot; in Statistics-&amp;gt;Summary-&amp;gt;Traffic is raw data average or just payload average ? Thanks, Mahii'''
date = "2013-08-01T08:16:00Z"
lastmod = "2013-08-01T17:39:00Z"
weight = 23505
keywords = [ "payload", "summary" ]
aliases = [ "/questions/23505" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Statistics summary is just payload or raw data ?](/questions/23505/statistics-summary-is-just-payload-or-raw-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23505-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to find payload average for UDP. Can any one explain me whether "Average data rate speed" in Statistics-&gt;Summary-&gt;Traffic is raw data average or just payload average ?</p><p>Thanks,</p><p>Mahii</p></div><div id="question-tags" class="tags-container tags">payload summary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '13, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/5d48d19fa8c74789854739c3da512b0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mahii&#39;s gravatar image" /><p>mahii<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mahii has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Aug '13, 01:24</p></div></div><div id="comments-container-23505" class="comments-container"></div><div id="comment-tools-23505" class="comment-tools"></div><div class="clear"></div><div id="comment-23505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23513"></span>

<div id="answer-container-23513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23513-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you do a simple export of just one or two UDP frames and then look at Statistics-&gt;Summary you will see the "Captured" and "Display" data values are for the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '13, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-23513" class="comments-container"><span id="23514"></span><div id="comment-23514" class="comment"><div id="post-23514-score" class="comment-score"></div><div class="comment-text"><p>@Marty thank you for the response! but i think you misunderstood my question, please look at image, I want to know "Avg MBit/Sec" is raw data average or just 1514 payload avg? thanks for the response</p></div><div id="comment-23514-info" class="comment-info"><span class="comment-age">(02 Aug '13, 01:25)</span> mahii</div></div><span id="23515"></span><div id="comment-23515" class="comment"><div id="post-23515-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/Test.png" alt="alt text" /></p></div><div id="comment-23515-info" class="comment-info"><span class="comment-age">(02 Aug '13, 01:27)</span> mahii</div></div><span id="23516"></span><div id="comment-23516" class="comment"><div id="post-23516-score" class="comment-score"></div><div class="comment-text"><p>@mahii, @martyvis was showing you a method to work it out for yourself. If you only have two packets in the capture and then look at the summary for that capture you can easily see if the Avg. is calculated from the whole frame, or just the payload.</p></div><div id="comment-23516-info" class="comment-info"><span class="comment-age">(02 Aug '13, 01:55)</span> grahamb ♦</div></div></div><div id="comment-tools-23513" class="comment-tools"></div><div class="clear"></div><div id="comment-23513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

