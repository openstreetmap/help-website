+++
type = "question"
title = "Why are Wireshark downloads unreasonably slow?"
description = '''20kbps is way too slow. Can this bandwidth be increased some alternate download sites setup?'''
date = "2013-11-14T08:21:00Z"
lastmod = "2013-11-14T09:52:00Z"
weight = 27010
keywords = [ "download", "bandwidth", "throttling" ]
aliases = [ "/questions/27010" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why are Wireshark downloads unreasonably slow?](/questions/27010/why-are-wireshark-downloads-unreasonably-slow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27010-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>20kbps is way too slow. Can this bandwidth be increased some alternate download sites setup?</p></div><div id="question-tags" class="tags-container tags">download bandwidth throttling</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '13, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/2ac32204995b47f3e2e3508a4e2a52e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YouNeedMoreBandwidth&#39;s gravatar image" /><p>YouNeedMoreB...<br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YouNeedMoreBandwidth has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '13, 11:21</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-27010" class="comments-container"></div><div id="comment-tools-27010" class="comment-tools"></div><div class="clear"></div><div id="comment-27010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27012"></span>

<div id="answer-container-27012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27012-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which download server did you happen to use? The download page generates URLs using a weighted random selection from the list that Graham posted. The list is weighted heavily toward wiresharkdownloads.riverbed.com. I don't have any sort of throttling set up on that server or any of the other Wireshark servers but I don't manage the other servers.</p><p>If I download Wireshark directly from wiresharkdownloads.riverbed.com on a machine at home I get about 27 Mbps, which is about the max for my cable connection.</p><p>You might try reloading the download page (which should make it regenerate its URLs) and try again. Otherwise you might try downloading directly from wiresharkdownloads.riverbed.com.</p><p><strong>Update 2013-12-05</strong></p><p>I discovered that the main download server saturates its link (100Mbps) periodically. I'm deploying additional download servers and looking at options for improving latency (e.g. geolocation).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '13, 10:27</p></div></div><div id="comments-container-27012" class="comments-container"></div><div id="comment-tools-27012" class="comment-tools"></div><div class="clear"></div><div id="comment-27012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27011"></span>

<div id="answer-container-27011" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27011-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You mean, like the list of mirrors shown on the download <a href="http://www.wireshark.org/download.html">page</a>?</p><pre><code>askApache (http, us)
Providence University (http, tw)
Riverbed Technology (http, us)
SourceForge.net (http, many)
University of Kaiserslautern (ftp, de)
University of Kaiserslautern (http, de)
University of Seville (http, es)
Wireshark.org (http, us)
Yamagata University (http, jp)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27011" class="comments-container"></div><div id="comment-tools-27011" class="comment-tools"></div><div class="clear"></div><div id="comment-27011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

