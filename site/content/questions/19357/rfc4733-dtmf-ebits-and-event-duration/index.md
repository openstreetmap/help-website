+++
type = "question"
title = "RFC4733 DTMF ebits and event duration"
description = '''I have seen an issue where the DTMF digits that were being press, some of the digits were being triplicated. Example: user presses 79546 and what it was being interpretted as was 77795. The only thing different we could find was that the event duration increases by 80 on each of the three end bits f...'''
date = "2013-03-11T10:54:00Z"
lastmod = "2013-03-11T16:00:00Z"
weight = 19357
keywords = [ "rfc4733" ]
aliases = [ "/questions/19357" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RFC4733 DTMF ebits and event duration](/questions/19357/rfc4733-dtmf-ebits-and-event-duration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19357-score" class="post-score" title="current number of votes">0</div><span id="post-19357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have seen an issue where the DTMF digits that were being press, some of the digits were being triplicated. Example: user presses 79546 and what it was being interpretted as was 77795. The only thing different we could find was that the event duration increases by 80 on each of the three end bits for the 7. A patch was put in to mask the last two digits, and it worked. I didn't see anything specific in the RFC stating that the digits rely on the event duration staying the same. And when I look at calls that work, the event duration never changes. Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rfc4733" rel="tag" title="see questions tagged &#39;rfc4733&#39;">rfc4733</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '13, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/6d53ced35e08594df25eaad48076bd2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Engineer1976&#39;s gravatar image" /><p><span>Engineer1976</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Engineer1976 has no accepted answers">0%</span></p></div></div><div id="comments-container-19357" class="comments-container"><span id="19363"></span><div id="comment-19363" class="comment"><div id="post-19363-score" class="comment-score"></div><div class="comment-text"><p>Is the equpment detecting the tones on the IP side or after coversion to TDM? if it's the later the duration mathers.</p></div><div id="comment-19363-info" class="comment-info"><span class="comment-age">(11 Mar '13, 12:36)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="19364"></span><div id="comment-19364" class="comment"><div id="post-19364-score" class="comment-score"></div><div class="comment-text"><p>So, this is on an Avaya Experience Portal. It appears to be being presented to it with the different durations. And in the pcap file that is pulled off, when looking at the DTMF tones I see the event duration increasing on the end bits of the first digit. So the AEP is interpretting that as three different 7's.</p></div><div id="comment-19364-info" class="comment-info"><span class="comment-age">(11 Mar '13, 14:43)</span> <span class="comment-user userinfo">Engineer1976</span></div></div></div><div id="comment-tools-19357" class="comment-tools"></div><div class="clear"></div><div id="comment-19357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19367"></span>

<div id="answer-container-19367" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19367-score" class="post-score" title="current number of votes">0</div><span id="post-19367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>RTP events are funny things. The idea is that at the start the RTP timestamp is fixed and a duration is incremented with the RTP packet rate. The '..' indicates the packetizing delay.</p><pre><code>RTP TS:         640 .. 720 .. 800 .. 800 .. 800 .. 800 ..
event duration:                 0     80    160    240</code></pre><p>In this way you can encode the duration of the keypress, without knowing it in advance, or interrupt the RTP stream for the duration, which doesn't help the receiver.</p><p>There's a specific way to annotate the end of a keypress. There's a marker in the RTP event signaling the end, and to prevent it from getting lost (it's UDP after all) it is advised to repeat the final RTP event three times. So that would look something like this.</p><pre><code>RTP TS:           800 .. 800  800  800 .. 1200 .. 1280 .. 1360 ..
event duration:   240    320! 320! 320!  </code></pre><p>Three RTP event packets with the final marker (!) set, in rapid succession, there's no packetizing delay, nor increment of the timestamp or duration. After that the the normal RTP time stamping resumes, adjusted for the time consumed by the event.</p><p>If your RTP event source doesn't work this way you should talk to the supplier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '13, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19367" class="comments-container"></div><div id="comment-tools-19367" class="comment-tools"></div><div class="clear"></div><div id="comment-19367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

