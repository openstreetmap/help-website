+++
type = "question"
title = "Realtime Analysis with WireShark GUI"
description = '''Has anyone tried real-time packet analysis using wiresharks GUI with high volumes of traffic(&amp;gt;1Gbps)? Is this even possible with Wireshark?'''
date = "2012-05-22T09:26:00Z"
lastmod = "2012-05-22T10:15:00Z"
weight = 11217
keywords = [ "analysis", "packet", "real-time" ]
aliases = [ "/questions/11217" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Realtime Analysis with WireShark GUI](/questions/11217/realtime-analysis-with-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11217-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Has anyone tried real-time packet <strong>analysis</strong> using wiresharks GUI with high volumes of traffic(&gt;1Gbps)? Is this even possible with Wireshark?</p></div><div id="question-tags" class="tags-container tags">analysis packet real-time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/9d141f99918df47932149d44ef1d36bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kfryklund&#39;s gravatar image" /><p>kfryklund<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kfryklund has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '12, 17:38</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-11217" class="comments-container"></div><div id="comment-tools-11217" class="comment-tools"></div><div class="clear"></div><div id="comment-11217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11218"></span>

<div id="answer-container-11218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11218-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>if you say <strong>&gt; 1 GBit/s</strong>. Do you mean 10 GBit/s? If so, there have been talks about this at several sharkfest events:</p><blockquote><p><code>http://www.google.de/#hl=de&amp;site=&amp;source=hp&amp;q=sharkfest+10+GBit&amp;btnK=Google-Suche&amp;oq=&amp;aq=&amp;aqi=&amp;aql=&amp;gs_l=&amp;bav=on.2,or.r_gc.r_pw.,cf.osb&amp;fp=abbb4046b845e521&amp;biw=1440&amp;bih=754</code></p></blockquote><p>Maybe someone here has even personal experience with 10 GBit analysis.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '12, 10:16</p></div></div><div id="comments-container-11218" class="comments-container"><span id="11221"></span><div id="comment-11221" class="comment"><div id="post-11221-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the suggestions. I'm capturing at 10Gbit/s (but I have the ability to capture up to 40Gbit/s). I already have an appliance that can handle 20Gbps of traffic capture, but I don't have a way to analyze the realtime traffic with Wireshark.<br />
</p><p>Based on the sharkfest events, wireshark builds there own appliances (up to 7Gbps capture/record), but I still can't tell if the wireshark user is capable of monitoring/analysis of large amounts of realtime traffic as it's being captured.</p></div><div id="comment-11221-info" class="comment-info"><span class="comment-age">(22 May '12, 12:07)</span> kfryklund</div></div><span id="11222"></span><div id="comment-11222" class="comment"><div id="post-11222-score" class="comment-score"></div><div class="comment-text"><p>You say:</p><blockquote><p>is capable of monitoring/analysis of large amounts of realtime traffic as it's being captured.</p></blockquote><p>Why do you need to analyze the data while it is being captured (at that speed)?<br />
What are you looking for?</p></div><div id="comment-11222-info" class="comment-info"><span class="comment-age">(22 May '12, 12:11)</span> Kurt Knochner ♦</div></div><span id="11268"></span><div id="comment-11268" class="comment"><div id="post-11268-score" class="comment-score"></div><div class="comment-text"><p>BTW: If you try to analyze 10GBit/s traffic in realtime in wireshark (gui or tshark), you will end up with enormous memory consumption in a very short period of time. 10Gbit/s is roughly 1Gbyte/s data. Wireshark builds internal data structures to store that data in memory. Internal memory requirement is somewhat larger than the raw captured data. So, within just 10 seconds you would end up with &gt;&gt; 10 GByte RAM consumption and it's not getting any better if wireshark runs longer ;-)</p><p>So, again: What are you looking for? Maybe there is a better way (if any) to analyze that much data in realtime.</p></div><div id="comment-11268-info" class="comment-info"><span class="comment-age">(23 May '12, 10:29)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11218" class="comment-tools"></div><div class="clear"></div><div id="comment-11218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

