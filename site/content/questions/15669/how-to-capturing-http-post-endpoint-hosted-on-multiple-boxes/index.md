+++
type = "question"
title = "How to capturing HTTP POST endpoint hosted on multiple boxes?"
description = '''I am running a Java application upon my Ubuntu box that is making API calls to endpoint https://int.tangocard.com. This endpoint has multiple hosts when I ping-ed it:  54.243.76.183 23.23.233.116 50.17.183.39 54.243.72.138  This API endpoint has DigiCert certificate, and the data communication is us...'''
date = "2012-11-07T16:05:00Z"
lastmod = "2012-11-08T08:22:00Z"
weight = 15669
keywords = [ "capture", "post", "http", "request", "responses" ]
aliases = [ "/questions/15669" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capturing HTTP POST endpoint hosted on multiple boxes?](/questions/15669/how-to-capturing-http-post-endpoint-hosted-on-multiple-boxes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15669-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running a Java application upon my Ubuntu box that is making API calls to endpoint <strong><a href="https://int.tangocard.com">https://int.tangocard.com</a></strong>.</p><p>This endpoint has multiple hosts when I ping-ed it:</p><ul><li>54.243.76.183</li><li>23.23.233.116</li><li>50.17.183.39</li><li>54.243.72.138</li></ul><p>This API endpoint has <strong>DigiCert certificate</strong>, and the data communication is using <strong>HTTP POST using Basic Authentication</strong>, and the body requests and responses are JSON.</p><p>I am trying to capture these HTTP POST requests &amp; responses, I have tried using the following as the filter, but nothing is getting captured:</p><p><em>(ip.addr == 54.243.76.183 || ip.addr == 23.23.233.116 || ip.addr == 50.17.183.39 || ip.addr == 54.243.72.138) &amp;&amp; http</em></p><p>I am use to working with "Fiddler 2" on Windows 7, so I am new to this tool on Ubuntu.</p><p>Thanks</p><p>Jeff in Seattle</p></div><div id="question-tags" class="tags-container tags">capture post http request responses</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 16:05</strong></p><img src="https://secure.gravatar.com/avatar/d43e972a8ca84b9478a814f32e464fd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeff00tangocard&#39;s gravatar image" /><p>jeff00tangocard<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeff00tangocard has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Nov '12, 17:46</p></div></div><div id="comments-container-15669" class="comments-container"></div><div id="comment-tools-15669" class="comment-tools"></div><div class="clear"></div><div id="comment-15669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15728"></span>

<div id="answer-container-15728" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, I am able to capture traffic between a Java app using HttpsURLConnection POST to API endpoint <a href="https://int.tangocard.com">https://int.tangocard.com</a></p><p>Using ping, the discovered IP addresses included in filter are:</p><p>(ip.addr == 54.243.76.183 || ip.addr == 23.23.233.116 || ip.addr == 50.17.183.39 || ip.addr == 54.243.72.138) &amp;&amp; tcp</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/d43e972a8ca84b9478a814f32e464fd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeff00tangocard&#39;s gravatar image" /><p>jeff00tangocard<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeff00tangocard has no accepted answers">0%</span></p></div></div><div id="comments-container-15728" class="comments-container"></div><div id="comment-tools-15728" class="comment-tools"></div><div class="clear"></div><div id="comment-15728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

