+++
type = "question"
title = "Network compression device, howto match up traces"
description = '''Does anyone have a method or process to match up traces that have gone through a network compression device, that has changed both the datagram ids and seq/ack numbers. We get traces fairly often where we encounter this issue, it would be great if we could somehow match up the traces from both sides...'''
date = "2017-03-28T07:24:00Z"
lastmod = "2017-03-28T12:41:00Z"
weight = 60386
keywords = [ "matches", "compression" ]
aliases = [ "/questions/60386" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Network compression device, howto match up traces](/questions/60386/network-compression-device-howto-match-up-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60386-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone have a method or process to match up traces that have gone through a network compression device, that has changed both the datagram ids and seq/ack numbers.</p><p>We get traces fairly often where we encounter this issue, it would be great if we could somehow match up the traces from both sides.</p></div><div id="question-tags" class="tags-container tags">matches compression</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '17, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/8e19bba7e40a62154983610c3a42edd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mnmoose&#39;s gravatar image" /><p>mnmoose<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mnmoose has no accepted answers">0%</span></p></div></div><div id="comments-container-60386" class="comments-container"></div><div id="comment-tools-60386" class="comment-tools"></div><div class="clear"></div><div id="comment-60386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60390"></span>

<div id="answer-container-60390" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60390-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A compression device changes basically every bit and byte that you could use to match, so the only thing you might still be able to do is to work on meta information. E.g. "when an unencrypted packet arrives with x bytes, we see y bytes coming out of the device z milliseconds later, so chances are high that those two match" (with y &lt; x within reasonable compression rates). Other than that, it's just guesswork I'm afraid.</p><p>Out of curiosity - why do you need to do that "fairly often"? I always never have to do that except for HTTP proxies, trying to match multiplexed connections...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '17, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60390" class="comments-container"><span id="60392"></span><div id="comment-60392" class="comment"><div id="post-60392-score" class="comment-score"></div><div class="comment-text"><p>I work lots of remote journaling(RJ) issues, customers uses compression devices before the WAN. So I end up with a source system trace and Remote system trace. They are complaining about RJ issues, backlogs and slow performance. Most of the time it's a network issues either retrans, or latency issues. But to prove it I need to match the traces up and try show their network team packets 1-7 leaving the source but only packets 1,3,4,6,7 make it to the target.</p></div><div id="comment-60392-info" class="comment-info"><span class="comment-age">(28 Mar '17, 14:08)</span> mnmoose</div></div></div><div id="comment-tools-60390" class="comment-tools"></div><div class="clear"></div><div id="comment-60390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

