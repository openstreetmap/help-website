+++
type = "question"
title = "Relative Sequence Number"
description = '''I have been reading the questiins and answer&#x27;s tothis question but none of them seem to help me. I was under the impression that I could follow a relative sequence number say 551 all the way through and get a complete conversation. Am I mistaken.  Thanks  steve.'''
date = "2010-11-11T09:38:00Z"
lastmod = "2010-11-12T01:32:00Z"
weight = 913
keywords = [ "numbers", "sequence" ]
aliases = [ "/questions/913" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Relative Sequence Number](/questions/913/relative-sequence-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-913-score" class="post-score" title="current number of votes">0</div><span id="post-913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been reading the questiins and answer's tothis question but none of them seem to help me. I was under the impression that I could follow a relative sequence number say 551 all the way through and get a complete conversation. Am I mistaken. Thanks steve.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-numbers" rel="tag" title="see questions tagged &#39;numbers&#39;">numbers</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '10, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/5d5eb4a95de90cab0b0001875f4dacf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfkseb413&#39;s gravatar image" /><p><span>jfkseb413</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfkseb413 has no accepted answers">0%</span></p></div></div><div id="comments-container-913" class="comments-container"><span id="916"></span><div id="comment-916" class="comment"><div id="post-916-score" class="comment-score"></div><div class="comment-text"><p>Thanks folks......I did what you said and got both ends of the conversation....</p></div><div id="comment-916-info" class="comment-info"><span class="comment-age">(11 Nov '10, 10:37)</span> <span class="comment-user userinfo">jfkseb413</span></div></div></div><div id="comment-tools-913" class="comment-tools"></div><div class="clear"></div><div id="comment-913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="914"></span>

<div id="answer-container-914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-914-score" class="post-score" title="current number of votes">2</div><span id="post-914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Relative sequence number is there to make it easy for people to follow the conversation. It's easier on the eyes to track 1,000 to 3000 (relative seq#) rather than 3223..65983453 to 3223...65985453 (absolute seq numbers). So whether you use relative seq# or not has no bearing on the analysis.</p><p>Also, TCP involves two conversations. One from the sender and one from the receiver. So it's important to keep track of sequence numbers from both sides.<br />
</p><p>Finally, you can right click on the packet and use "follow tcp stream" to isolate your conversation from other traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-914" class="comments-container"><span id="929"></span><div id="comment-929" class="comment"><div id="post-929-score" class="comment-score"></div><div class="comment-text"><p>I agree, even though sometimes I revert to absolute seq numbers: it is easy to confuse one self with the two sequence number rows of both communication parties (especially if they are still pretty low). Absolute numbers are often completely different with no way to mistake one for the other. The other reason is if I'm tracking down packets that are from a multi point capture and I need to find the same packets in both (or even three to five different) traces.</p></div><div id="comment-929-info" class="comment-info"><span class="comment-age">(12 Nov '10, 01:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-914" class="comment-tools"></div><div class="clear"></div><div id="comment-914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="915"></span>

<div id="answer-container-915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-915-score" class="post-score" title="current number of votes">0</div><span id="post-915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok... here's the scoop on using relative sequence numbers.</p><p>Let's say you have two Wireshark systems - #1 is capturing traffic at a client and #2 is capturing traffic at a server.</p><p>If you start both analyzers and then launch a web browsing session at the client (to the server), both Wireshark systems (using relative sequence numbers) will show the same starting sequence number (0) at the beginning of the connection. In this case, your sequence numbers should match up on both analyzers.</p><p>If you see a packet from the client to the server that has sequence number 4532 for example, you should see a packet with that same sequence number at the server. If, for some reason, you missed part of the connection process at Wireshark #2 though - the relative numbers will be off.</p><p>What is your goal here? As Hanseng said, if you right click on one of the packets in that connection and select Follow X stream, Wireshark will reassemble the conversation and automatically filter on that conversation only.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-915" class="comments-container"></div><div id="comment-tools-915" class="comment-tools"></div><div class="clear"></div><div id="comment-915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

