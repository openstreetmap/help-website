+++
type = "question"
title = "Why would frame.time_delta = 0 for nearly all packets?"
description = '''Hello, I have completed a few captures on my network and am finding that the frame.time_delta is equal to 0 for nearly all of the packets- it&#x27;s nonzero for under 1% of them. How can I fix this? I have used the frame.time_delta frequently in the past without issue and haven&#x27;t had a problem. In this c...'''
date = "2014-11-11T21:16:00Z"
lastmod = "2014-11-12T17:44:00Z"
weight = 37770
keywords = [ "frame.time.delta" ]
aliases = [ "/questions/37770" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why would frame.time\_delta = 0 for nearly all packets?](/questions/37770/why-would-frametime_delta-0-for-nearly-all-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37770-score" class="post-score" title="current number of votes">0</div><span id="post-37770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have completed a few captures on my network and am finding that the frame.time_delta is equal to 0 for nearly all of the packets- it's nonzero for under 1% of them. How can I fix this? I have used the frame.time_delta frequently in the past without issue and haven't had a problem. In this case, I have connected my PC and the system I'm trying to monitor (a streaming media box) to a hub, which is in turn uplinked to the rest of the network. I get normal deltas when capturing off the wireless NIC in this PC. Is it possible that the hub is causing this?</p><p>I am certain that all of my network traffic is not arriving simultaneously :) so any suggestions would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame.time.delta" rel="tag" title="see questions tagged &#39;frame.time.delta&#39;">frame.time.delta</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '14, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/1cb06a07cd9091e59a08bb4859f44927?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Katb&#39;s gravatar image" /><p><span>Katb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Katb has no accepted answers">0%</span></p></div></div><div id="comments-container-37770" class="comments-container"></div><div id="comment-tools-37770" class="comment-tools"></div><div class="clear"></div><div id="comment-37770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37771"></span>

<div id="answer-container-37771" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37771-score" class="post-score" title="current number of votes">2</div><span id="post-37771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In a busy network with lot's of traffic frame.time_delta will be small (like 0.000145000 seconds) but not zero. Does frame.time_relative look like it is incrementing correctly?</p><p>The timestamp is added by winpcap or libpcap as I understand.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '14, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-37771" class="comments-container"><span id="37801"></span><div id="comment-37801" class="comment"><div id="post-37801-score" class="comment-score"></div><div class="comment-text"><p>Thank you both!</p><p>What I was seeing was true zero; I had my times displayed in nanoseconds. I was using the frame time information, not TCP; I was trying to capture Cobranet traffic, which is a Layer 2 audio distribution protocol. Your comments regarding the timestamp source and network hardware led my to try a fresh install on a newer PC with a better quality NIC, which produced a capture with timestamps that make much more sense. It was surprising to me that the NIC's failure to keep up only affected the time, although having thought through it a bit more, I do understand that a calculated attribute would be low on the priority list.</p><p>Again, thank you for the help! This is really helping me research an entrenched issue with my network.</p></div><div id="comment-37801-info" class="comment-info"><span class="comment-age">(12 Nov '14, 17:44)</span> <span class="comment-user userinfo">Katb</span></div></div></div><div id="comment-tools-37771" class="comment-tools"></div><div class="clear"></div><div id="comment-37771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37774"></span>

<div id="answer-container-37774" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37774-score" class="post-score" title="current number of votes">0</div><span id="post-37774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As marty says, you will see many packets with &gt;1ms times. If your frame.time_delta is using milliseconds, you will see them as 0.000. Make a second column next to the frame delta (Custom tcp.time_delta Instance 0) this will give TCP time in nanoseconds (but you wont see anything on the last 3 digits unless you have pretty good / specialised Hardware. You SHOULD also go into the View | "Time Display Format" Menu and change to Microseconds. You really don't need nanoseconds at home and without the hardware you will never see anything there anyways. Also, your computer is not conencted to a hub, it passes through a hub. Unless it is a switched Hub in which case sub 1ms times are the rule, not the exception.</p><p>I tried uploading an image to show you, but I can't get it uploaded.. But basically.</p><p>Delta Delta (in Microseconds) 0.000 0.000123</p><p>I assume you have enabled TCP | Protocol Preferences | Calculate TCP Timestamps via right click in Packet Details?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '14, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-37774" class="comments-container"></div><div id="comment-tools-37774" class="comment-tools"></div><div class="clear"></div><div id="comment-37774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

