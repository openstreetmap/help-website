+++
type = "question"
title = "Will capture size have bearing on throuput measurement?"
description = '''When I limit the capture of packet to about 100 bytes (paer packet), there is visible change in throuput measurement (as indicated in the summary). Why would this happen?'''
date = "2011-01-13T01:28:00Z"
lastmod = "2011-01-13T13:19:00Z"
weight = 1729
keywords = [ "packet", "size" ]
aliases = [ "/questions/1729" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Will capture size have bearing on throuput measurement?](/questions/1729/will-capture-size-have-bearing-on-throuput-measurement)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1729-score" class="post-score" title="current number of votes">0</div><span id="post-1729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I limit the capture of packet to about 100 bytes (paer packet), there is visible change in throuput measurement (as indicated in the summary). Why would this happen?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '11, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/33118c8a09ea35e6cb17b03515968e35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raghav&#39;s gravatar image" /><p><span>Raghav</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raghav has no accepted answers">0%</span></p></div></div><div id="comments-container-1729" class="comments-container"><span id="1735"></span><div id="comment-1735" class="comment"><div id="post-1735-score" class="comment-score"></div><div class="comment-text"><p>Can you describe the actual difference (and confirm the traffic you are monitoring hasn't changed)?</p><p>That sounds like a bug.</p></div><div id="comment-1735-info" class="comment-info"><span class="comment-age">(13 Jan '11, 03:03)</span> <span class="comment-user userinfo">martyvis</span></div></div></div><div id="comment-tools-1729" class="comment-tools"></div><div class="clear"></div><div id="comment-1729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1742"></span>

<div id="answer-container-1742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1742-score" class="post-score" title="current number of votes">1</div><span id="post-1742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The only thing I can imagine is that as soon as you limit the frame size to say 100 bytes that your throughput get better (you didn't mention if it goes up or down, but I think "up" is the only realistic thing to happen).</p><p>This is why: your link might really really be crowded with frames, and when Wireshark tries to capture those there is too much data too fast to be written to disk, resulting in dropped frames. As soon as you reduce the capture size to 100 byte there is much less data volume to be written to disk, so Wireshark can "record" more frames, and this results in a higher throughput reading.</p><p>If your throughput readings go down on 100 bytes per frame I'd agree with Martyvis that this is probably a bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1742" class="comments-container"></div><div id="comment-tools-1742" class="comment-tools"></div><div class="clear"></div><div id="comment-1742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1733"></span>

<div id="answer-container-1733" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1733-score" class="post-score" title="current number of votes">0</div><span id="post-1733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would imagine that it is actually calculating this based on the frame as seen in the capture. You could still get some idea of usage by opening "IO Graphs" under "Statistics". Set the units to "Advanced" and use Sum(x) and ip.len. Its a different view, but should be relative to frame size and throughput as long as most of your traffic is IP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1733" class="comments-container"></div><div id="comment-tools-1733" class="comment-tools"></div><div class="clear"></div><div id="comment-1733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1743"></span>

<div id="answer-container-1743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1743-score" class="post-score" title="current number of votes">0</div><span id="post-1743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I experimented with this unscientifically and without a huge load. I actually found that only the "File" section of the summary screen seemed to be affected by limiting the packet size. I ran two instances of wireshark for about the same amount of time. The Avg bytes/sec were pretty consistent between the copy that was limiting the packet size and the one that wasn't. The pcap format might actually have a field for frame length even when it does not record the entire frame. I'm using 1.4.2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1743" class="comments-container"></div><div id="comment-tools-1743" class="comment-tools"></div><div class="clear"></div><div id="comment-1743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

