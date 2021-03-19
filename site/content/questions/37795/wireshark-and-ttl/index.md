+++
type = "question"
title = "Wireshark and TTL"
description = '''Do all captured packets have a TTL (time-to-live)?'''
date = "2014-11-12T08:36:00Z"
lastmod = "2014-11-12T08:43:00Z"
weight = 37795
keywords = [ "packet-capture", "ttl" ]
aliases = [ "/questions/37795" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark and TTL](/questions/37795/wireshark-and-ttl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37795-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Do all captured packets have a TTL (time-to-live)?</p></div><div id="question-tags" class="tags-container tags">packet-capture ttl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '14, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/416a674ed40560b7da546111781bff02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolf1937&#39;s gravatar image" /><p>wolf1937<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolf1937 has no accepted answers">0%</span></p></div></div><div id="comments-container-37795" class="comments-container"></div><div id="comment-tools-37795" class="comment-tools"></div><div class="clear"></div><div id="comment-37795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37796"></span>

<div id="answer-container-37796" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37796-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>All IP packets do, it's part of the IP Protocol and can be found in the IP Header. See <a href="http://www.rfc-editor.org/rfc/rfc791.txt">RFC 791</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '14, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37796" class="comments-container"><span id="37805"></span><div id="comment-37805" class="comment"><div id="post-37805-score" class="comment-score"></div><div class="comment-text"><p><strong>Sheldon Mode on</strong>: Well, technically IPv6 doesn't, it's "HopCount" not "TTL" for those :-))</p></div><div id="comment-37805-info" class="comment-info"><span class="comment-age">(13 Nov '14, 00:55)</span> Jasper ♦♦</div></div><span id="37810"></span><div id="comment-37810" class="comment"><div id="post-37810-score" class="comment-score"></div><div class="comment-text"><p><strong>Bernadette mode on</strong>: Actually its "Hop Limit". See <a href="https://www.ietf.org/rfc/rfc2460.txt">RFC 2460</a>.</p></div><div id="comment-37810-info" class="comment-info"><span class="comment-age">(13 Nov '14, 02:09)</span> grahamb ♦</div></div><span id="37830"></span><div id="comment-37830" class="comment"><div id="post-37830-score" class="comment-score"></div><div class="comment-text"><p>Meh. You win :)</p></div><div id="comment-37830-info" class="comment-info"><span class="comment-age">(13 Nov '14, 10:17)</span> Jasper ♦♦</div></div></div><div id="comment-tools-37796" class="comment-tools"></div><div class="clear"></div><div id="comment-37796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

