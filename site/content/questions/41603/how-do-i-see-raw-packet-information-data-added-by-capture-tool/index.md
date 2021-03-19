+++
type = "question"
title = "How do I see raw packet information data added by Capture tool?"
description = '''Hi, I&#x27;ve captured wireless traffic using tool Omnipeek. This tool adds so much information about each packet (wireless flags and timestamps). And the capture gets saves as .pkt format by default. If I open the capture in wireshark, I don&#x27;t see as much information I would see in omnipeek, but just ba...'''
date = "2015-04-20T10:12:00Z"
lastmod = "2015-04-22T11:08:00Z"
weight = 41603
keywords = [ "tshark" ]
aliases = [ "/questions/41603" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I see raw packet information data added by Capture tool?](/questions/41603/how-do-i-see-raw-packet-information-data-added-by-capture-tool)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41603-score" class="post-score" title="current number of votes">1</div><span id="post-41603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've captured wireless traffic using tool Omnipeek. This tool adds so much information about each packet (wireless flags and timestamps). And the capture gets saves as .pkt format by default. If I open the capture in wireshark, I don't see as much information I would see in omnipeek, but just basic information like packet length, data rate etc.</p><p>I understand, wireshark may not have decoding information for what Omnipeek embedded for each packet. But I would like to create a dissector to see the same. But how do I first see that packet information as raw data, atleast? Then I would like to start working on dissecting that.</p><p>In Summary: How do I see raw packet data added by wireshark/omnipeek/any-other-tool along with original packet?</p><p>-ram</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '15, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/5c59321a66976ba615e1a50b46a4d209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramprasad&#39;s gravatar image" /><p><span>Ramprasad</span><br />
<span class="score" title="20 reputation points">20</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramprasad has no accepted answers">0%</span></p></div></div><div id="comments-container-41603" class="comments-container"></div><div id="comment-tools-41603" class="comment-tools"></div><div class="clear"></div><div id="comment-41603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41647"></span>

<div id="answer-container-41647" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41647-score" class="post-score" title="current number of votes">0</div><span id="post-41647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ramprasad has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>In Summary: How do I see raw packet data added by wireshark/omnipeek/any-other-tool along with original packet?</p></blockquote><p>by opening the *.pkt file with a HEX editor and by reverse engineering that information.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '15, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41647" class="comments-container"><span id="41702"></span><div id="comment-41702" class="comment"><div id="post-41702-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. It worked.</p><p>Thanks Guy Harris</p></div><div id="comment-41702-info" class="comment-info"><span class="comment-age">(22 Apr '15, 11:08)</span> <span class="comment-user userinfo">Ramprasad</span></div></div></div><div id="comment-tools-41647" class="comment-tools"></div><div class="clear"></div><div id="comment-41647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41605"></span>

<div id="answer-container-41605" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41605-score" class="post-score" title="current number of votes">0</div><span id="post-41605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do I see raw packet data added by wireshark/omnipeek/any-other-tool along with original packet?</p></blockquote><p>Wireshark? Use, err, umm, Wireshark.</p><p>OmniPeek? Use Wireshark 1.99.x, which handles a lot more of the OmniPeek metadata.</p><p>Other tool? That depends on the tool.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '15, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41605" class="comments-container"></div><div id="comment-tools-41605" class="comment-tools"></div><div class="clear"></div><div id="comment-41605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

