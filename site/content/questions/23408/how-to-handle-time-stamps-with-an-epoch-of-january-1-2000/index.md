+++
type = "question"
title = "how to handle time stamps with an epoch of January 1, 2000?"
description = '''I am working on the zigbee portion of wireshark. Wireshark uses traditional gmtime function, which has epoch year 1970. But Zigbee has its own epoch year 2000 Jan 1st. Hence, when a NTP time 0x00000000 is passed on to wireshark, I expect it to be 2000. Jan .1st. But, when I use tvb_ntp_ts function, ...'''
date = "2013-07-27T21:02:00Z"
lastmod = "2013-07-27T23:54:00Z"
weight = 23408
keywords = [ "zigbee", "timestamps" ]
aliases = [ "/questions/23408" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to handle time stamps with an epoch of January 1, 2000?](/questions/23408/how-to-handle-time-stamps-with-an-epoch-of-january-1-2000)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23408-score" class="post-score" title="current number of votes">0</div><span id="post-23408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on the zigbee portion of wireshark. Wireshark uses traditional gmtime function, which has epoch year 1970. But Zigbee has its own epoch year 2000 Jan 1st. Hence, when a NTP time 0x00000000 is passed on to wireshark, I expect it to be 2000. Jan .1st. But, when I use tvb_ntp_ts function, it gives me errors. How can I resolve this issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zigbee" rel="tag" title="see questions tagged &#39;zigbee&#39;">zigbee</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '13, 21:02</strong></p><img src="https://secure.gravatar.com/avatar/df58e311217ad31c677ccea3e999e616?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xjybentusi&#39;s gravatar image" /><p><span>xjybentusi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xjybentusi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '13, 23:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23408" class="comments-container"></div><div id="comment-tools-23408" class="comment-tools"></div><div class="clear"></div><div id="comment-23408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23411"></span>

<div id="answer-container-23411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23411-score" class="post-score" title="current number of votes">2</div><span id="post-23411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>NTP times use neither the UN*X epoch of January 1, 1970, 00:00:00 UTC nor the Zigbee epoch of January 1, 2000 (presumably also 00:00:00 UTC). It, instead, uses an epoch of January 1, <em>1900</em>, 00:00:00 "UTC", so you can't use any NTP time stamp functions to deal with UN*X times or Zigbee times.</p><p>You would have to convert Zigbee times to UN*X/POSIX times; if you have a count of seconds since January 1, 2000, 00:00:00 UTC, you would have to add to it the number of seconds between January 1, 1970, 00:00:00 UTC and January 1, 2000, 00:00:00 UTC, and you could then use that, plus an optional count of nanoseconds, as a UN*X-style time stamp. (Calculating that number of seconds is left as an exercise to the reader.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '13, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23411" class="comments-container"></div><div id="comment-tools-23411" class="comment-tools"></div><div class="clear"></div><div id="comment-23411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

