+++
type = "question"
title = "Session Reconstruction"
description = '''I know different tools use different techniques when reconstructing sessions from packets. How does Wireshark reconstruct a session? Or How does it determine which packets go with each other?'''
date = "2014-07-22T08:33:00Z"
lastmod = "2014-07-23T00:29:00Z"
weight = 34829
keywords = [ "session", "reconstruction" ]
aliases = [ "/questions/34829" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Session Reconstruction](/questions/34829/session-reconstruction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34829-score" class="post-score" title="current number of votes">0</div><span id="post-34829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know different tools use different techniques when reconstructing sessions from packets. How does Wireshark reconstruct a session? Or How does it determine which packets go with each other?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-reconstruction" rel="tag" title="see questions tagged &#39;reconstruction&#39;">reconstruction</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '14, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/2e8541bf4054689eec96dbf983c0048b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewking1116&#39;s gravatar image" /><p><span>andrewking1116</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewking1116 has no accepted answers">0%</span></p></div></div><div id="comments-container-34829" class="comments-container"></div><div id="comment-tools-34829" class="comment-tools"></div><div class="clear"></div><div id="comment-34829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34831"></span>

<div id="answer-container-34831" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34831-score" class="post-score" title="current number of votes">0</div><span id="post-34831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It uses several pieces of information from the frames</p><ul><li>socket 5-tupel: protocol (UDP,TCP, etc.), src ip, dst ip, src port, dst port</li><li>TCP sequence numbers</li><li>Protocol request/response 'flow' (like in HTTP/FTP/SMTP, etc.)</li><li>many other things, all very dependent on the specific protocols</li></ul><p>That's all implemented in the protocol dissectors and the Wireshark dissection engine in general.</p><p>Is there any specific reason for your question?</p><p>Maybe there is a more detailed answer, if you are looking for a specific protocol.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '14, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34831" class="comments-container"><span id="34836"></span><div id="comment-34836" class="comment"><div id="post-34836-score" class="comment-score"></div><div class="comment-text"><p>I'm working on a requirements project. I just wanted a little more clarification on the technical aspect of different tools and how they process data.</p><p>I guess more specifically, Say the initial syn packet was dropped and you collected the rest of the data. Or, if you see a high port to high port. Some reconstruction tools rely on standard ports 0-1023 to be the server. How would would Wireshark process this? Would it just make a best guess or only use the sequence number?</p></div><div id="comment-34836-info" class="comment-info"><span class="comment-age">(22 Jul '14, 12:31)</span> <span class="comment-user userinfo">andrewking1116</span></div></div><span id="34842"></span><div id="comment-34842" class="comment"><div id="post-34842-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How would would Wireshark <strong>process</strong> this?</p></blockquote><p>'process' in terms of what?</p><p>Wireshark will still be able to identify a 'conversation' based on the socket 5-tupel and/or the TCP sequence numbers, no matter if the SYN is there or not.</p><p>As Wireshark won't tell you who is the 'client' and who is the 'server' (that's just a logical concept), it won't need the SYN anyway.</p><p>Wireshark also relies on ports to identify protocols (HTTP, SMTP, etc.) as Wireshark needs a criteria to call the right dissectors on a packet. However, there are also heuristic dissectors (trying to identify some protocols regardless of the port). Furthermore the user can overrule Wiresharks decision be telling it to dissect a certain frame/conversation/port/etc. with a different dissector ("Decode As").</p></div><div id="comment-34842-info" class="comment-info"><span class="comment-age">(23 Jul '14, 00:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34831" class="comment-tools"></div><div class="clear"></div><div id="comment-34831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

