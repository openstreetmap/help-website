+++
type = "question"
title = "Wire shark Recording server"
description = '''Hello All Sorry this question has probably already been asked loads of times before! what is the best way to setup wire shark on a server that records all data all the time for problem analysis at a later date? is this actually possible? I would also like to only store a couple weeks worth of traffi...'''
date = "2011-03-21T14:36:00Z"
lastmod = "2011-03-21T19:06:00Z"
weight = 2979
keywords = [ "capture" ]
aliases = [ "/questions/2979" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Wire shark Recording server](/questions/2979/wire-shark-recording-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2979-score" class="post-score" title="current number of votes">0</div><span id="post-2979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All</p><p>Sorry this question has probably already been asked loads of times before! what is the best way to setup wire shark on a server that records all data all the time for problem analysis at a later date? is this actually possible? I would also like to only store a couple weeks worth of traffic!</p><p>currently when a issue is reported we start a capture and try to get the user to reproduce the issue.</p><p>Thanks for any help in advanced.</p><p>James</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/589ba8da5f1add8b184abdf976861ace?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jam3s&#39;s gravatar image" /><p><span>jam3s</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jam3s has no accepted answers">0%</span></p></div></div><div id="comments-container-2979" class="comments-container"></div><div id="comment-tools-2979" class="comment-tools"></div><div class="clear"></div><div id="comment-2979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="2991"></span>

<div id="answer-container-2991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2991-score" class="post-score" title="current number of votes">2</div><span id="post-2991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The command line tool "dumpcap" can help especially if you set a ring buffer that will prevent your disk from running out of space by overwriting older trace files. You'll still need terabytes of disk space I guess if you want to go on for a week or more with full packets captured (otherwise use frame slicing and capture only the first 64-256 bytes depending on what protocol you're looking at).</p><p>If I were you I'd do a capture that is ring buffering for about a day or two and make it clear to the users to report issues rapidly including exact date and time as well as their IP address (if they know how to determine it). That way you can work with smaller disks as long as you get notified quickly enough to stop the capture from overwriting the relevant details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2991" class="comments-container"></div><div id="comment-tools-2991" class="comment-tools"></div><div class="clear"></div><div id="comment-2991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2994"></span>

<div id="answer-container-2994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2994-score" class="post-score" title="current number of votes">1</div><span id="post-2994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As others have already mentioned, use <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> for long-term capturing. When using dumpcap, you will probably want to make use of the ring buffer so you limit both the maximum capture file size and the maximum number of files that are part of the ring buffer. That will ensure you have somewhat manageable capture files as well as ensure that you don't completely consume all of your disk space.</p><p>Keep in mind that using dumpcap doesn't guarantee that you won't drop packets, particularly on very busy links, so here are a few <a href="http://wiki.wireshark.org/Performance">performance</a> related tips to consider.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-2994" class="comments-container"></div><div id="comment-tools-2994" class="comment-tools"></div><div class="clear"></div><div id="comment-2994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2981"></span>

<div id="answer-container-2981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2981-score" class="post-score" title="current number of votes">0</div><span id="post-2981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Search for <strong>dumpcap</strong>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2981" class="comments-container"></div><div id="comment-tools-2981" class="comment-tools"></div><div class="clear"></div><div id="comment-2981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2982"></span>

<div id="answer-container-2982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2982-score" class="post-score" title="current number of votes">0</div><span id="post-2982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>dumpcap</strong> will work for you, but you'd better have TONS of local disk. If you're going to grab "everything", you'll probably need terabytes of disk space.</p><p>If you can narrow your capture down at all (to a particular protocl or particular set of hosts), it will help greatly...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-2982" class="comments-container"></div><div id="comment-tools-2982" class="comment-tools"></div><div class="clear"></div><div id="comment-2982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

