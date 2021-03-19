+++
type = "question"
title = "Blocked Port 80 URLs"
description = '''When at a customers review my team did some captures for many users dispersed geographically. Some users tried accessing port 80 sites that were blocked by our network proxies. How can I find all requested HTTP URLs?'''
date = "2013-10-08T10:29:00Z"
lastmod = "2013-10-08T12:28:00Z"
weight = 25751
keywords = [ "http" ]
aliases = [ "/questions/25751" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Blocked Port 80 URLs](/questions/25751/blocked-port-80-urls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25751-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When at a customers review my team did some captures for many users dispersed geographically. Some users tried accessing port 80 sites that were blocked by our network proxies. How can I find all requested HTTP URLs?</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '13, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/9231d57e09cb52e00e39dede07ab6ad3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karl&#39;s gravatar image" /><p>karl<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karl has no accepted answers">0%</span></p></div></div><div id="comments-container-25751" class="comments-container"></div><div id="comment-tools-25751" class="comment-tools"></div><div class="clear"></div><div id="comment-25751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25758"></span>

<div id="answer-container-25758" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25758-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you have a capture file, you can use tshark as follows:</p><pre><code>tshark -Tfields -Yhttp.request.full_uri -ehttp.request.full_uri -r mycapture.pcap &gt; websites.txt</code></pre><p>That will write each requested http URI to the file websites.txt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '13, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-25758" class="comments-container"><span id="25764"></span><div id="comment-25764" class="comment"><div id="post-25764-score" class="comment-score"></div><div class="comment-text"><p>I have tshark v1.8.6. I used the -R instead of -Y.</p></div><div id="comment-25764-info" class="comment-info"><span class="comment-age">(08 Oct '13, 14:17)</span> karl</div></div></div><div id="comment-tools-25758" class="comment-tools"></div><div class="clear"></div><div id="comment-25758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25757"></span>

<div id="answer-container-25757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25757-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I recommend looking at the Proxy logs. Wireshark is a great tool, but sometimes there are other ways to get results faster.</p><p>If you don't have access to the proxy logs you could filter on "http.request.method or http.response.code = 403" (assuming your proxy returns a 403 when the site is blacklisted; replace with whatever code yours is returning). That will give you a list of all requests and response codes, but matching them can be tedious work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '13, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25757" class="comments-container"></div><div id="comment-tools-25757" class="comment-tools"></div><div class="clear"></div><div id="comment-25757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

