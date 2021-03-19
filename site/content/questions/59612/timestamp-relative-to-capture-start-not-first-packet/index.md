+++
type = "question"
title = "Timestamp relative to capture start, not first packet"
description = '''I am doing some captures of boot-up sequences and I want the timestamps to be relative to the time in which the connected hardware is turned on. I am starting the capture at the same time that I power the hardware on. I have &quot;seconds since beginning of capture&quot; selected for the Time Display Format, ...'''
date = "2017-02-22T08:20:00Z"
lastmod = "2017-02-22T11:57:00Z"
weight = 59612
keywords = [ "timestamp" ]
aliases = [ "/questions/59612" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Timestamp relative to capture start, not first packet](/questions/59612/timestamp-relative-to-capture-start-not-first-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59612-score" class="post-score" title="current number of votes">0</div><span id="post-59612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am doing some captures of boot-up sequences and I want the timestamps to be relative to the time in which the connected hardware is turned on. I am starting the capture at the same time that I power the hardware on. I have "seconds since beginning of capture" selected for the Time Display Format, but it seems that this actually means time since first packet. As a result, instead of the timestamps being relative to power up, they are relative to the first packet sent to/from the NIC, which is seconds later (significant for my application)</p><p>Is there a way to have the timestamp be relative to time at which the capture is actually triggered?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '17, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/1b60b5bed9129282c3f057795c077b69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="broadcastgear&#39;s gravatar image" /><p><span>broadcastgear</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="broadcastgear has no accepted answers">0%</span></p></div></div><div id="comments-container-59612" class="comments-container"></div><div id="comment-tools-59612" class="comment-tools"></div><div class="clear"></div><div id="comment-59612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59617"></span>

<div id="answer-container-59617" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59617-score" class="post-score" title="current number of votes">2</div><span id="post-59617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>Is there a way to have the timestamp be relative to time at which the capture is actually triggered?</em></p><p>No, this isn't currently possible. If absolute time stamps work for you, you could add an absolute timestamp column; otherwise you could try to "seed" the capture file with a packet that you generate and capture immediately after wireshark is started - that way, the <em>"time since first packet"</em> and <em>"time since capturing started"</em> will essentially be the same, or hopefully close enough for your purposes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '17, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59617" class="comments-container"><span id="59619"></span><div id="comment-59619" class="comment"><div id="post-59619-score" class="comment-score"></div><div class="comment-text"><p>Ok, thanks for the reply! Not a bad idea with the seeded packet in tandem with the capture.</p></div><div id="comment-59619-info" class="comment-info"><span class="comment-age">(22 Feb '17, 11:47)</span> <span class="comment-user userinfo">broadcastgear</span></div></div><span id="59620"></span><div id="comment-59620" class="comment"><div id="post-59620-score" class="comment-score"></div><div class="comment-text"><p>If you decide to "seed" the capture with a packet, then of course you can send whatever you like, but here's a little script I use to send myself little syslog markers in the traces at various stages of capturing (e.g., <em>"About to test feature xyz"</em>, <em>"OK, things just failed."</em>, ...) which you might find useful:</p><pre><code>#!/bin/sh

if (( ${#} &lt; 1 ))
then
        echo &quot;Usage: $0 message [host]&quot;
        exit 0
fi

if (( ${#} &lt; 2 ))
then
        # Send a syslog message $1 to host 1.1.1.1
        echo &quot;${1}&quot; | nc -w 1 -u 1.1.1.1 514
else
        # Send a syslog message $1 to the host $2
        echo &quot;${1}&quot; | nc -w 1 -u ${2} 514
fi</code></pre></div><div id="comment-59620-info" class="comment-info"><span class="comment-age">(22 Feb '17, 11:57)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-59617" class="comment-tools"></div><div class="clear"></div><div id="comment-59617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

