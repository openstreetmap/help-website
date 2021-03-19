+++
type = "question"
title = "automated save as plain text"
description = '''in my project i need to save the captured packets info as plain text with only packet source ip destionation ip source mac destination mac '''
date = "2014-04-06T22:48:00Z"
lastmod = "2014-04-07T02:15:00Z"
weight = 31584
keywords = [ "wireshark" ]
aliases = [ "/questions/31584" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [automated save as plain text](/questions/31584/automated-save-as-plain-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31584-score" class="post-score" title="current number of votes">0</div><span id="post-31584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in my project i need to save the captured packets info as plain text with only packet source ip destionation ip source mac destination mac</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '14, 22:48</strong></p><img src="https://secure.gravatar.com/avatar/5b9e956a3b928a307b6131162e23c36a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vengatesh&#39;s gravatar image" /><p><span>vengatesh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vengatesh has no accepted answers">0%</span></p></div></div><div id="comments-container-31584" class="comments-container"></div><div id="comment-tools-31584" class="comment-tools"></div><div class="clear"></div><div id="comment-31584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31585"></span>

<div id="answer-container-31585" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31585-score" class="post-score" title="current number of votes">0</div><span id="post-31585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this</p><blockquote><p>tshark -nr input.pcap -T fields -e eth.src -e eth.dst -e ip.src -e ip.dst</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '14, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31585" class="comments-container"><span id="31587"></span><div id="comment-31587" class="comment"><div id="post-31587-score" class="comment-score"></div><div class="comment-text"><p>i need to capture from wireshark not from a pcap file sir input.pcap error:"tshark: The file "input.pcap" doesn't exist." and i have to export packet dissections as plain text automatically</p></div><div id="comment-31587-info" class="comment-info"><span class="comment-age">(07 Apr '14, 00:54)</span> <span class="comment-user userinfo">vengatesh</span></div></div></div><div id="comment-tools-31585" class="comment-tools"></div><div class="clear"></div><div id="comment-31585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31591"></span>

<div id="answer-container-31591" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31591-score" class="post-score" title="current number of votes">0</div><span id="post-31591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i need to capture from wireshark not from a pcap file</p></blockquote><p>Then try</p><pre><code>tshark -i interface -T fields -e eth.src -e eth.dst -e ip.src -e ip.dst</code></pre><p>where "interface" is the network interface on which you're capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '14, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31591" class="comments-container"></div><div id="comment-tools-31591" class="comment-tools"></div><div class="clear"></div><div id="comment-31591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

