+++
type = "question"
title = "capture packets,edit and replay"
description = '''Hi, I want to be able to capture packets in a file, edit out certain packets and &quot;replay&quot; the traffic ie simulate as if the traffic was happening in reality - is this possible ?  Thanks.'''
date = "2010-12-20T09:02:00Z"
lastmod = "2010-12-20T17:07:00Z"
weight = 1407
keywords = [ "replay", "traffic", "captured" ]
aliases = [ "/questions/1407" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture packets,edit and replay](/questions/1407/capture-packetsedit-and-replay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1407-score" class="post-score" title="current number of votes">0</div><span id="post-1407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to be able to capture packets in a file, edit out certain packets and "replay" the traffic ie simulate as if the traffic was happening in reality - is this possible ?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-replay" rel="tag" title="see questions tagged &#39;replay&#39;">replay</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-captured" rel="tag" title="see questions tagged &#39;captured&#39;">captured</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '10, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/052cea1a33dd51db67919582594e448b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="codie9002&#39;s gravatar image" /><p><span>codie9002</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="codie9002 has no accepted answers">0%</span></p></div></div><div id="comments-container-1407" class="comments-container"></div><div id="comment-tools-1407" class="comment-tools"></div><div class="clear"></div><div id="comment-1407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1410"></span>

<div id="answer-container-1410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1410-score" class="post-score" title="current number of votes">0</div><span id="post-1410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, use Wireshark to capture your traffic, mark the packets you don't want and save it with these packets suppressed. Then use tools like TCPreplay to playout the capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '10, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1410" class="comments-container"><span id="1415"></span><div id="comment-1415" class="comment"><div id="post-1415-score" class="comment-score"></div><div class="comment-text"><p>And my 2 cents: do not reply captured traffic into a live production environment ;-)</p></div><div id="comment-1415-info" class="comment-info"><span class="comment-age">(20 Dec '10, 17:07)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-1410" class="comment-tools"></div><div class="clear"></div><div id="comment-1410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

