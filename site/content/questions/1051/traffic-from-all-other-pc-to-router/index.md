+++
type = "question"
title = "Traffic from all other PC to router"
description = '''There is two type of packets in the wifi network traffic, in one the source is one PC and the destination is a wifi router, in the other one the source is the router and the destination is the PC. In my case I have a wifi card in promiscous mode and when I start tpcdump or wireshark I can see the tr...'''
date = "2010-11-21T15:44:00Z"
lastmod = "2010-11-22T16:10:00Z"
weight = 1051
keywords = [ "wifi", "traffic" ]
aliases = [ "/questions/1051" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Traffic from all other PC to router](/questions/1051/traffic-from-all-other-pc-to-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1051-score" class="post-score" title="current number of votes">0</div><span id="post-1051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is two type of packets in the wifi network traffic, in one the source is one PC and the destination is a wifi router, in the other one the source is the router and the destination is the PC. In my case I have a wifi card in promiscous mode and when I start tpcdump or wireshark I can see the traffic from router to my PC and from the router to all other PC but I can't see the traffic from all other PC to router wifi, why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '10, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/0c7672fa88d2ba50bcab8f6fe4cf9cf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alanp&#39;s gravatar image" /><p><span>alanp</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alanp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Sep '12, 08:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-1051" class="comments-container"></div><div id="comment-tools-1051" class="comment-tools"></div><div class="clear"></div><div id="comment-1051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1072"></span>

<div id="answer-container-1072" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1072-score" class="post-score" title="current number of votes">1</div><span id="post-1072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Thanks Jasper, but I have linux ubuntu and the device is tp-link 
and is in promiscous mode.
I try to explain better:

Source ----&gt; destination of packet

    PC ----&gt; router wifi (I can&#39;t see this type of packet)
 My PC ----&gt; router Wifi (I can see)
Router ----&gt; single PC, single PC, 
             in example another PC of network. I can see this.

And then I can&#39;t see only packet that have as source 
another PC of the wifi network.
I can not understend why?</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '10, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/0c7672fa88d2ba50bcab8f6fe4cf9cf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alanp&#39;s gravatar image" /><p><span>alanp</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alanp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '10, 16:15</strong> </span></p></div></div><div id="comments-container-1072" class="comments-container"></div><div id="comment-tools-1072" class="comment-tools"></div><div class="clear"></div><div id="comment-1072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1063"></span>

<div id="answer-container-1063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1063-score" class="post-score" title="current number of votes">0</div><span id="post-1063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably another case of trying to capture WiFi data with a standard wireless card using a Windows operating system. For this kind of capture you need an Airpcap adapter as sold by Cace Technologies, or use linux instead. Otherwise you won't see the 802.11 layer and data from other stations, just your own.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '10, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1063" class="comments-container"></div><div id="comment-tools-1063" class="comment-tools"></div><div class="clear"></div><div id="comment-1063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

