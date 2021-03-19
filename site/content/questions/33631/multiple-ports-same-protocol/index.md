+++
type = "question"
title = "multiple ports same protocol?"
description = '''I&#x27;m debugging a dicom link between a client and a server. I suspect that there are two instances of dicom SCP on the server on separate ports and two clients on the client machine. Obviously each server is listening on a separate port and the clients are talking to their respective servers. My quest...'''
date = "2014-06-10T20:09:00Z"
lastmod = "2014-06-11T13:28:00Z"
weight = 33631
keywords = [ "dicom" ]
aliases = [ "/questions/33631" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [multiple ports same protocol?](/questions/33631/multiple-ports-same-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33631-score" class="post-score" title="current number of votes">0</div><span id="post-33631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm debugging a dicom link between a client and a server. I suspect that there are two instances of dicom SCP on the server on separate ports and two clients on the client machine. Obviously each server is listening on a separate port and the clients are talking to their respective servers. My question is when I filter by dicom packets how do I know which message 'pairs' are from the same peers? (I don't see the port numbers on the transaction log.)</p><p>Cheers,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dicom" rel="tag" title="see questions tagged &#39;dicom&#39;">dicom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '14, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/6e0f6d1c74f4bc26b86c95e81ad62d8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BJOBrien&#39;s gravatar image" /><p><span>BJOBrien</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BJOBrien has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '14, 06:03</strong> </span></p></div></div><div id="comments-container-33631" class="comments-container"><span id="33672"></span><div id="comment-33672" class="comment"><div id="post-33672-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(I don't see the port numbers on the transaction log.)</p></blockquote><p>Some questions:</p><ul><li>Why (question to the statement above)?</li><li>How did you generate the 'transaction' log?</li><li>Did you try to capture the traffic with Wireshark?</li></ul></div><div id="comment-33672-info" class="comment-info"><span class="comment-age">(11 Jun '14, 13:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33631" class="comment-tools"></div><div class="clear"></div><div id="comment-33631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33641"></span>

<div id="answer-container-33641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33641-score" class="post-score" title="current number of votes">0</div><span id="post-33641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can add source port and destination port as columns to help you differentiate. Right click a port field (src or dst) in the packet details pane and select "Apply as Column", repeat for the other (src or dst) field).</p><p>You can also apply display filters to limit the conversation to a particular port, e.g. <code>tcp.srcport == xyz</code> if your traffic is over TCP for instance (similarly for UDP), or you can select a particular frame, right click and select "Follow xxx Stream" where "xxx" is TCP or UDP as appropriate and that will show the whole converstation on that port for UDP or that connection (SYN -&gt; FIN) for TCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33641" class="comments-container"></div><div id="comment-tools-33641" class="comment-tools"></div><div class="clear"></div><div id="comment-33641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

