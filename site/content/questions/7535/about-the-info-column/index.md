+++
type = "question"
title = "About the info column."
description = '''Can somebody tell me how to avoid, in the info column, the display of source port and destination port? I&#x27;m checking megaco traces and it is not easy to follow the call due to this not necesary info in the info column: Source port: h248-binary Destination port: megaco-h248 or  Source port: h248-bina...'''
date = "2011-11-21T09:33:00Z"
lastmod = "2011-11-22T09:15:00Z"
weight = 7535
keywords = [ "info", "column" ]
aliases = [ "/questions/7535" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [About the info column.](/questions/7535/about-the-info-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7535-score" class="post-score" title="current number of votes">0</div><span id="post-7535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can somebody tell me how to avoid, in the info column, the display of source port and destination port? I'm checking megaco traces and it is not easy to follow the call due to this not necesary info in the info column: Source port: h248-binary Destination port: megaco-h248<br />
or Source port: h248-binary Destination port: megaco-h248 I noticed this behaviour starting from release 1.6.0</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '11, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/beced2d25419ada1b1879cb55d8da7a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rubik001&#39;s gravatar image" /><p><span>rubik001</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rubik001 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-7535" class="comments-container"><span id="7537"></span><div id="comment-7537" class="comment"><div id="post-7537-score" class="comment-score"></div><div class="comment-text"><p>Have you checked if any of the protocol preferences influence output to the info column? Is the output to the info column important to your analysis? If not, you could just hide the column.</p></div><div id="comment-7537-info" class="comment-info"><span class="comment-age">(21 Nov '11, 09:42)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="7540"></span><div id="comment-7540" class="comment"><div id="post-7540-score" class="comment-score"></div><div class="comment-text"><p>Is Wireshark actually dissecting the packet as MEGACO? Those are put into the Info column by the UDP dissector (there's no option to disable that), but, if Wireshark is dissecting the packets as MEGACO packets, the MEGACO dissector should replace the Info column with its own information, overwriting that information. If it's not doing so, that's a bug.</p></div><div id="comment-7540-info" class="comment-info"><span class="comment-age">(21 Nov '11, 12:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7553"></span><div id="comment-7553" class="comment"><div id="post-7553-score" class="comment-score"></div><div class="comment-text"><p>The output info is important for analysis, having this info it is more simple to analyse the traces, you can see the message type, transaction and context numbers. When the "source and destination port" info is added, the indicated info is shifted to the rigth out of the screen. The packets are correctly displayed in the packet Details windows. And it is interesting not all the packets are showed in the "info column" with "source and destination port" info. Due to this "feature" I have to unistall the 1.6.x release and back to release 1.4.10. If this is a bug, how to report it to the developers?</p></div><div id="comment-7553-info" class="comment-info"><span class="comment-age">(22 Nov '11, 02:12)</span> <span class="comment-user userinfo">rubik001</span></div></div><span id="7554"></span><div id="comment-7554" class="comment"><div id="post-7554-score" class="comment-score"></div><div class="comment-text"><p>The best bet would be to raise an issue on the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a>, adding a capture illustrating the issue. You can mark the attachment private if you don't want it to be publicly visible.</p><p>You should also check for an existing bug report first, and add a comment (and capture) to that if you find one.</p></div><div id="comment-7554-info" class="comment-info"><span class="comment-age">(22 Nov '11, 02:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-7535" class="comment-tools"></div><div class="clear"></div><div id="comment-7535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7558"></span>

<div id="answer-container-7558" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7558-score" class="post-score" title="current number of votes">0</div><span id="post-7558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I infer from your comment (converted to a comment - it doesn't answer <em>your</em> question, so it should be a comment, not an answer; this is a Q&amp;A site, not a forum, as the first item in <a href="http://ask.wireshark.org/faq/">the FAQ for the site</a> says) that Wireshark <em>is</em> dissecting the packets as MEGACO.</p><p>If so, that means that this is a problem with the MEGACO dissector, <em>NOT</em> with the UDP dissector; the UDP dissector is doing what it should do when it adds that information to the Info column, because that means that if the UDP dissector <em>doesn't</em> find a subdissector to dissect the payload the Info column indicates what's in the UDP header, but the MEGACO dissector is <em>NOT</em> doing what it should do when it <em>appends</em> to the Info column rather than overwriting it.</p><p>Please file a bug in <a href="https://bugs.wireshark.org/bugzilla/">the Wireshark Bugzilla</a> against the MEGACO dissector as per grahamb's comment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '11, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7558" class="comments-container"></div><div id="comment-tools-7558" class="comment-tools"></div><div class="clear"></div><div id="comment-7558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

