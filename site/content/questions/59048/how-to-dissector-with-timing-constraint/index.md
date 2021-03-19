+++
type = "question"
title = "How to Dissector with Timing Constraint"
description = '''I have created a c++ dissector plugin that parses my protocol just fine. My protocol has timing constraints between messages. What is the best way to implement tracking/reporting of time between messages. Is this something that I can handle with of conversations (no experience with) or do I create m...'''
date = "2017-01-25T08:27:00Z"
lastmod = "2017-02-03T09:30:00Z"
weight = 59048
keywords = [ "timing", "dissector", "postdissector" ]
aliases = [ "/questions/59048" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to Dissector with Timing Constraint](/questions/59048/how-to-dissector-with-timing-constraint)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59048-score" class="post-score" title="current number of votes">0</div><span id="post-59048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created a c++ dissector plugin that parses my protocol just fine.</p><p>My protocol has timing constraints between messages. What is the best way to implement tracking/reporting of time between messages.</p><p>Is this something that I can handle with of conversations (no experience with) or do I create my own wmem structure and track inside of the dissector? Should I create a post dissector tap (no experience with them)?</p><p>How would I indicate that the last message did not have a follow on message to satisfy the constraint.</p><p>Thanks for the help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timing" rel="tag" title="see questions tagged &#39;timing&#39;">timing</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '17, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/334b3772ba24e093b1c83a07da9e12c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20B&#39;s gravatar image" /><p><span>Rob B</span><br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob B has no accepted answers">0%</span></p></div></div><div id="comments-container-59048" class="comments-container"></div><div id="comment-tools-59048" class="comment-tools"></div><div class="clear"></div><div id="comment-59048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59056"></span>

<div id="answer-container-59056" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59056-score" class="post-score" title="current number of votes">0</div><span id="post-59056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rob B has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should go and read doc/README.request_response_tracking where it is explained how to do this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '17, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59056" class="comments-container"><span id="59067"></span><div id="comment-59067" class="comment"><div id="post-59067-score" class="comment-score"></div><div class="comment-text"><p>How would I set an expert field in the request stating that no response was seen?</p></div><div id="comment-59067-info" class="comment-info"><span class="comment-age">(25 Jan '17, 13:58)</span> <span class="comment-user userinfo">Rob B</span></div></div><span id="59069"></span><div id="comment-59069" class="comment"><div id="post-59069-score" class="comment-score">1</div><div class="comment-text"><p>In the first pass of dissecting packets, this is obviously impossible, as, when the request was seen, Wireshark/TShark haven't yet read any packets that would <em>be</em> a response.</p><p>In subsequent passes, if you have a data structure to keep track of requests and replies, you can detect whether a response was seen, and add an expert info.</p><p>This means that, in TShark without the <code>-2</code> flag, this will be impossible. It should work in most cases for Wireshark.</p><p>To determine whether you're in the first pass or not, check whether <code>pinfo-&gt;fd-&gt;flags.visited</code> is true or false. If it's false, you're doing the first pass, otherwise you're doing a subsequent pass.</p></div><div id="comment-59069-info" class="comment-info"><span class="comment-age">(25 Jan '17, 14:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="59248"></span><div id="comment-59248" class="comment"><div id="post-59248-score" class="comment-score"></div><div class="comment-text"><p>Guy Harris, Thanks for the help.</p><p>Does Wireshark always do two passes?</p></div><div id="comment-59248-info" class="comment-info"><span class="comment-age">(03 Feb '17, 08:22)</span> <span class="comment-user userinfo">Rob B</span></div></div><span id="59249"></span><div id="comment-59249" class="comment"><div id="post-59249-score" class="comment-score"></div><div class="comment-text"><p>Wireshark is not <em>guaranteed</em> to make more than one complete pass over the packet data unless you run some statistical tap that has to scan all the packet or you run a display filter on the packet list; that first pass happens when you read the file in. If you select a packet, it will re-dissect the packet in order to generate the protocol tree for display, so at <em>that</em> point, the protocol tree can indicate a request without a response.</p></div><div id="comment-59249-info" class="comment-info"><span class="comment-age">(03 Feb '17, 09:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-59056" class="comment-tools"></div><div class="clear"></div><div id="comment-59056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

