+++
type = "question"
title = "Can I use Wireshark to monitor simple traffic usage?"
description = '''My ISP provides a very questionable data usage tracking on it&#x27;s website and I have been searching for alternatives, but so far have not been able to find one that is free and suitable for me. With all the features of wireshark, is it possible to use it to simply monitor how much data I use up when I...'''
date = "2013-11-24T12:32:00Z"
lastmod = "2013-11-24T17:12:00Z"
weight = 27322
keywords = [ "bandwidth" ]
aliases = [ "/questions/27322" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I use Wireshark to monitor simple traffic usage?](/questions/27322/can-i-use-wireshark-to-monitor-simple-traffic-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27322-score" class="post-score" title="current number of votes">0</div><span id="post-27322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My ISP provides a very questionable data usage tracking on it's website and I have been searching for alternatives, but so far have not been able to find one that is free and suitable for me.</p><p>With all the features of wireshark, is it possible to use it to simply monitor how much data I use up when I'm online?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '13, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/c3557d4c68ea7dc5335086f3c1ce17d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Garry%20Wong&#39;s gravatar image" /><p><span>Garry Wong</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Garry Wong has no accepted answers">0%</span></p></div></div><div id="comments-container-27322" class="comments-container"></div><div id="comment-tools-27322" class="comment-tools"></div><div class="clear"></div><div id="comment-27322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27323"></span>

<div id="answer-container-27323" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27323-score" class="post-score" title="current number of votes">0</div><span id="post-27323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can, but it's really not recommended. Wireshark (and the command line version tshark) maintain state as packets are captured, so eventually they will run out of memory.</p><p>I achieve your required functionality by running custom firmware on my wireless router (<a href="http://www.polarcloud.com/tomato">Tomato</a>) that shows my really nice graphs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '13, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27323" class="comments-container"></div><div id="comment-tools-27323" class="comment-tools"></div><div class="clear"></div><div id="comment-27323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27329"></span>

<div id="answer-container-27329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27329-score" class="post-score" title="current number of votes">0</div><span id="post-27329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Or get bandwidth meter pro, that tiny software is a machine!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '13, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/599929aa65406761d15533f022ed2d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctxsvc&#39;s gravatar image" /><p><span>ctxsvc</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctxsvc has one accepted answer">33%</span></p></div></div><div id="comments-container-27329" class="comments-container"></div><div id="comment-tools-27329" class="comment-tools"></div><div class="clear"></div><div id="comment-27329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

