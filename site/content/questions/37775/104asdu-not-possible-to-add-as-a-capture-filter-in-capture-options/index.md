+++
type = "question"
title = "104asdu not possible to add as a Capture Filter in Capture Options"
description = '''Hi, It seems to not be possible to add 104asdu as a capture filter in the capture options window. Any ideas of how to get this working or can someone confirm that it is a bug? Maybe we can add it to a list of bugs?  It takes up so much disk space if I can&#x27;t use a capture filter :/  Best regards, Ric...'''
date = "2014-11-12T01:07:00Z"
lastmod = "2014-11-12T03:44:00Z"
weight = 37775
keywords = [ "60870-5-104", "capture-filter", "104" ]
aliases = [ "/questions/37775" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [104asdu not possible to add as a Capture Filter in Capture Options](/questions/37775/104asdu-not-possible-to-add-as-a-capture-filter-in-capture-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37775-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>It seems to not be possible to add 104asdu as a capture filter in the capture options window. Any ideas of how to get this working or can someone confirm that it is a bug? Maybe we can add it to a list of bugs?</p><p>It takes up so much disk space if I can't use a capture filter :/</p><p>Best regards,</p><p>Richard</p></div><div id="question-tags" class="tags-container tags">60870-5-104 capture-filter 104</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '14, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/2da7626bca6ecbaec3578637d5221972?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Prendiville&#39;s gravatar image" /><p>Richard Pren...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Prendiville has no accepted answers">0%</span></p></div></div><div id="comments-container-37775" class="comments-container"></div><div id="comment-tools-37775" class="comment-tools"></div><div class="clear"></div><div id="comment-37775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37781"></span>

<div id="answer-container-37781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37781-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a high-level protocol (IEC60870-5-104) field, the capture filter system has no knowledge of that protocol (it stops around tcp\udp) so you can't create a capture filter for the field. See the Wiki page on <a href="http://wiki.wireshark.org/CaptureFilters">Capture Filters</a> for more info.</p><p>You can filter the capture by IP\port, which might help, but if the volume of traffic for the device is still too high, you might be able to create a capture filter by matching bytes at specific offsets in the packet, if the relevant IEC fields always appear at the same offset.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '14, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37781" class="comments-container"><span id="37793"></span><div id="comment-37793" class="comment"><div id="post-37793-score" class="comment-score"></div><div class="comment-text"><p>Thanks Grahamb,</p><p>I just find it strange because I can filter for 104asdu in the main window (Filter field). Here I can filter all kinds of parameters which are very useful (e.g. 104asdu.ioa, 104asdu.typeid, 104asdu.addr etc). I thought because it is possible to filter here that it would be possible to filter in the capture options (using the same filters).</p><p>Best regards,</p><p>Richard</p></div><div id="comment-37793-info" class="comment-info"><span class="comment-age">(12 Nov '14, 08:24)</span> Richard Pren...</div></div><span id="37794"></span><div id="comment-37794" class="comment"><div id="post-37794-score" class="comment-score"></div><div class="comment-text"><p>Capture Filters and <a href="http://wiki.wireshark.org/DisplayFilters">Display Filters</a> are two quite different beasts, that often confuse folks. The users guide has lots of useful information about the two types of filters, but basically Capture Filters are lean and efficient to operate with high traffic rates, so they only "know" about a limited set of protocols and filter options, whereas Display Filters can handle any field in Wireshark with many different comparison options.</p></div><div id="comment-37794-info" class="comment-info"><span class="comment-age">(12 Nov '14, 08:31)</span> grahamb ♦</div></div></div><div id="comment-tools-37781" class="comment-tools"></div><div class="clear"></div><div id="comment-37781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

