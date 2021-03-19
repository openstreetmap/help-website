+++
type = "question"
title = "Monitor network traffic by user"
description = '''Hey there-  I&#x27;m giving myself a crash course in Wireshark this morning, as a client (I&#x27;m an IT consultant) is looking to have us analyze their network traffic to see what users are hogging bandwidth, and if possible, to see what host they are going to (e.g. Pandora). I&#x27;m not sure if Wireshark has th...'''
date = "2011-05-02T09:32:00Z"
lastmod = "2011-05-02T12:43:00Z"
weight = 3880
keywords = [ "graph", "users" ]
aliases = [ "/questions/3880" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor network traffic by user](/questions/3880/monitor-network-traffic-by-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3880-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there- I'm giving myself a crash course in Wireshark this morning, as a client (I'm an IT consultant) is looking to have us analyze their network traffic to see what users are hogging bandwidth, and if possible, to see what host they are going to (e.g. Pandora). I'm not sure if Wireshark has this capability out of the box, though I get the impression it does if I know how and where to look. I am trying to master the application as quickly as possible this morning, but if anyone can tell me how to graph the above info, I would be eternally grateful. Cheers!</p><p>R</p></div><div id="question-tags" class="tags-container tags">graph users</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '11, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/854b9b26a9f09b7cab45049fe9b7a2fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ikarian&#39;s gravatar image" /><p>Ikarian<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ikarian has no accepted answers">0%</span></p></div></div><div id="comments-container-3880" class="comments-container"></div><div id="comment-tools-3880" class="comment-tools"></div><div class="clear"></div><div id="comment-3880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3882"></span>

<div id="answer-container-3882" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3882-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatistics.html">Statistics</a> menu.</p><p>These stats can be used "real-time" by opening them during a capture session; or can be used to analyze already-captured data. In your case, some stats of interest might include:</p><ul><li><a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatIOGraphs.html">IO Graphs</a> (used with <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDefineFilterSection.html#FiltersDialog">Display Filters</a>...<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">more on display filters</a>)</li><li><a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatEndpoints.html">Endpoints list</a></li><li><a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatConversations.html">Conversations list</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '11, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 May '11, 12:47</p></div></div><div id="comments-container-3882" class="comments-container"></div><div id="comment-tools-3882" class="comment-tools"></div><div class="clear"></div><div id="comment-3882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

