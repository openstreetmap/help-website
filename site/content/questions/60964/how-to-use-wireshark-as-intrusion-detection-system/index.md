+++
type = "question"
title = "How to use Wireshark as intrusion detection system"
description = '''How to use Wireshark as intrusion detection system on a windows machine ?'''
date = "2017-04-22T03:17:00Z"
lastmod = "2017-04-22T23:13:00Z"
weight = 60964
keywords = [ "detection", "intrusion" ]
aliases = [ "/questions/60964" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use Wireshark as intrusion detection system](/questions/60964/how-to-use-wireshark-as-intrusion-detection-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60964-score" class="post-score" title="current number of votes">0</div><span id="post-60964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to use Wireshark as intrusion detection system on a windows machine ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-detection" rel="tag" title="see questions tagged &#39;detection&#39;">detection</span> <span class="post-tag tag-link-intrusion" rel="tag" title="see questions tagged &#39;intrusion&#39;">intrusion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '17, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/4debf4d644c7320e639547bd1b13c1b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="w_keyboard&#39;s gravatar image" /><p><span>w_keyboard</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="w_keyboard has no accepted answers">0%</span></p></div></div><div id="comments-container-60964" class="comments-container"></div><div id="comment-tools-60964" class="comment-tools"></div><div class="clear"></div><div id="comment-60964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60966"></span>

<div id="answer-container-60966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60966-score" class="post-score" title="current number of votes">0</div><span id="post-60966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not really. It's a packet dissector, for as many protocols as possible, with the highest amount of detail possible. That's not what you want from an IDS. There you want just enough protocol analysis and correlation to process as much data as possible, in order to maintain a high troughput, and raise alarms on detected issues. These are not matching specifications. placing Wireshark in the same realm as IDS's, but not in the same category. It would come into play once IDS alarms have been raised and network logs have been preserved to investigate the occurrence in more detail.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '17, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60966" class="comments-container"><span id="60979"></span><div id="comment-60979" class="comment"><div id="post-60979-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Jaap</span> I am unable to add an image to my response to your reply, so I am adding another answer to my question - the reason to ask if wireshark can be used as IDS is that I get frequent DoS like this <img src="https://osqa-ask.wireshark.org/upfiles/dos_1lMnB67.PNG" alt="alt text" /> and another one <img src="https://osqa-ask.wireshark.org/upfiles/dos1.PNG" alt="alt text" /></p><p>these DoS attacks stop the moment I start wireskark or I login to the router.</p></div><div id="comment-60979-info" class="comment-info"><span class="comment-age">(22 Apr '17, 23:13)</span> <span class="comment-user userinfo">w_keyboard</span></div></div></div><div id="comment-tools-60966" class="comment-tools"></div><div class="clear"></div><div id="comment-60966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

