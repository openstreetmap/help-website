+++
type = "question"
title = "catch all the HTTP requests to a certain domain"
description = '''Is there a filter to get all HTTP requests to certain domain? For example, all the HTTP requests whose &quot;Host&quot; header is like xxxx.mydomain.com. Thanks.'''
date = "2015-05-11T10:25:00Z"
lastmod = "2015-05-11T14:13:00Z"
weight = 42310
keywords = [ "wireshark" ]
aliases = [ "/questions/42310" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [catch all the HTTP requests to a certain domain](/questions/42310/catch-all-the-http-requests-to-a-certain-domain)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a filter to get all HTTP requests to certain domain? For example, all the HTTP requests whose "Host" header is like xxxx.mydomain.com.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '15, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-42310" class="comments-container"><span id="42311"></span><div id="comment-42311" class="comment"><div id="post-42311-score" class="comment-score"></div><div class="comment-text"><p>Do you mean capture or display filters?</p></div><div id="comment-42311-info" class="comment-info"><span class="comment-age">(11 May '15, 13:28)</span> Christian_R</div></div><span id="42312"></span><div id="comment-42312" class="comment"><div id="post-42312-score" class="comment-score"></div><div class="comment-text"><p>Yes. Don't think it's possible with capture filter, display filter is the best hope. Thanks.</p></div><div id="comment-42312-info" class="comment-info"><span class="comment-age">(11 May '15, 13:36)</span> pktUser1001</div></div></div><div id="comment-tools-42310" class="comment-tools"></div><div class="clear"></div><div id="comment-42310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42315"></span>

<div id="answer-container-42315" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42315-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What about this filter? (http.host == "xxx.mydomain.com") &amp;&amp; (http.request.method == "GET")</p><p>You can generate your own complex filters very easily. You only have to right click the value for what you are interested in the packet detail view and then you can either choose "prepare a filter" or "apply as a filter" in the context menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '15, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '15, 14:10</p></div></div><div id="comments-container-42315" class="comments-container"><span id="42316"></span><div id="comment-42316" class="comment"><div id="post-42316-score" class="comment-score"></div><div class="comment-text"><p>That's a good start, but the issue is, we don't know what are the possible host names are. xxx is a place holder. Thanks.</p></div><div id="comment-42316-info" class="comment-info"><span class="comment-age">(11 May '15, 14:11)</span> pktUser1001</div></div></div><div id="comment-tools-42315" class="comment-tools"></div><div class="clear"></div><div id="comment-42315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42317"></span>

<div id="answer-container-42317" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42317-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use this display filter:</p><p>http.host matches "mydomain\.com"</p><p>This will match on "mydomain.com" anywhere in the http.host field. Because the matches operator uses regular expression syntax, you have to escape the period with a backslash.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '15, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-42317" class="comments-container"><span id="42319"></span><div id="comment-42319" class="comment"><div id="post-42319-score" class="comment-score"></div><div class="comment-text"><p>Thanks, this is the best possibility so far. The corner cases are: To prevent xmydomain.com from being matched, we better use ".mydomain.com". However, that may miss http request to "mydomain.com".</p></div><div id="comment-42319-info" class="comment-info"><span class="comment-age">(11 May '15, 14:16)</span> pktUser1001</div></div><span id="42320"></span><div id="comment-42320" class="comment"><div id="post-42320-score" class="comment-score"></div><div class="comment-text"><p>Then I think this could work (http.host matches "\.mydomain\.com") || (http.host matches "^mydomain\.com")</p></div><div id="comment-42320-info" class="comment-info"><span class="comment-age">(11 May '15, 14:33)</span> Christian_R</div></div><span id="42324"></span><div id="comment-42324" class="comment"><div id="post-42324-score" class="comment-score"></div><div class="comment-text"><blockquote><p>http.host matches "([^\.]+\.)*domain\.com"</p></blockquote><p>Matches:</p><ul><li>domain.com</li><li>aaa.domain.com</li><li>aaa.bbb.domain.com</li><li>aaa.bbb.ccc.domain.com</li><li>etc.</li></ul><p>If you only want the first two:</p><blockquote><p>http.host matches "([^\.]+\.)?domain\.com"</p></blockquote><p>Regards Kurt</p></div><div id="comment-42324-info" class="comment-info"><span class="comment-age">(12 May '15, 04:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-42317" class="comment-tools"></div><div class="clear"></div><div id="comment-42317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

