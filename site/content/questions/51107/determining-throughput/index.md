+++
type = "question"
title = "Determining Throughput"
description = '''I&#x27;m attempting to figure out throughput for a specific application. In my capture I am filtering on the TCP stream and then using Statistics &amp;gt; Protocol Hierarchy. Am I correct in using the Bit/s column for Transmission Control Protocol as my application throughput for that stream?'''
date = "2016-03-22T12:14:00Z"
lastmod = "2016-03-22T12:14:00Z"
weight = 51107
keywords = [ "hierarchy", "protocol", "throughput" ]
aliases = [ "/questions/51107" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Determining Throughput](/questions/51107/determining-throughput)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to figure out throughput for a specific application. In my capture I am filtering on the TCP stream and then using Statistics &gt; Protocol Hierarchy.</p><p>Am I correct in using the Bit/s column for Transmission Control Protocol as my application throughput for that stream?</p></div><div id="question-tags" class="tags-container tags">hierarchy protocol throughput</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '16, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/650d2f94f586cb5cbd3c7192f8bb39a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudoraptor&#39;s gravatar image" /><p>sudoraptor<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudoraptor has no accepted answers">0%</span></p></div></div><div id="comments-container-51107" class="comments-container"><span id="51110"></span><div id="comment-51110" class="comment"><div id="post-51110-score" class="comment-score"></div><div class="comment-text"><p>Possibly, but you have to check the following factors:</p><ul><li><p>some competing traffic may exist on the network between your application and its clients, causing the request rate to the application to be lower than it could be, i.e. the actual throughput of your application may be higher if you could "ask for more". This is if the application sends responses to requests.</p></li><li><p>the client of your application may throttle its output by indicating a small receive window. This is if the application sends a continuous stream as a response to a single request.</p></li><li><p>there must be no packet loss between the application and its clients, as then again the Bit/s value would be skewed and the actual throughput of the application throttled by the TCP stack's retransmissions of the lost packets.</p></li></ul><p>So without more details about the expected behaviour of the application and of what exactly you mean by "throughput", it is hard to answer properly.</p></div><div id="comment-51110-info" class="comment-info"><span class="comment-age">(22 Mar '16, 13:30)</span> sindy</div></div></div><div id="comment-tools-51107" class="comment-tools"></div><div class="clear"></div><div id="comment-51107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

