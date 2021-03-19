+++
type = "question"
title = "How to view multiple streams?"
description = '''I&#x27;m aware of the Wireshark feature which allows us to view a single stream that a particular packet is associated with. However, I would like to view multiple streams in the order that they were captured. Is this possible? If so, how?  Edit for clarity  I&#x27;m looking for a way to view multiple streams...'''
date = "2013-01-18T09:29:00Z"
lastmod = "2013-01-18T11:07:00Z"
weight = 17777
keywords = [ "packet-capture", "streams" ]
aliases = [ "/questions/17777" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to view multiple streams?](/questions/17777/how-to-view-multiple-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17777-score" class="post-score" title="current number of votes">0</div><span id="post-17777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm aware of the Wireshark feature which allows us to view a single stream that a particular packet is associated with. However, I would like to view multiple streams in the order that they were captured.</p><p>Is this possible? If so, how?</p><p><strong>Edit for clarity</strong></p><p>I'm looking for a way to view multiple streams in a single "Follow TCP Stream" window. You know how you can right-click on a packet and select "Follow TCP Stream" and new window pops-up showing you the entire stream? - Well, I would like to be able to have multiple streams in that same window.</p><p>My goal is have an easy way of viewing all streams that occurred during a web browser session. So, right now, what I'm doing is doing the following steps:</p><ol><li>Filter: "tcp.stream == <strong>0</strong>"</li><li>Right-click, select "Follow TCP Stream"</li><li>Save the stream to disk (by clicking "Save As")</li><li>Filter: "tcp.stream == <strong>1</strong>", then repeat steps 2 and 3</li><li>Filter: "tcp.stream == <strong>2</strong>", then repeat steps 2 and 3</li><li>Filter: "tcp.stream == <strong>[n]</strong>", then repeat steps 2 and 3</li><li>Using Notepad, combine all the saved streams in sequential order.</li></ol><p>The result of the procedure above will be useful to me, but creating it is a bit cumbersome.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-streams" rel="tag" title="see questions tagged &#39;streams&#39;">streams</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p><span>KTM</span><br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jan '13, 11:04</strong> </span></p></div></div><div id="comments-container-17777" class="comments-container"></div><div id="comment-tools-17777" class="comment-tools"></div><div class="clear"></div><div id="comment-17777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17779"></span>

<div id="answer-container-17779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17779-score" class="post-score" title="current number of votes">1</div><span id="post-17779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can see multiple streams by filtering on the TCP stream index number of the streams you want to see: "tcp.stream==1 || tcp.stream==4 || tcp.stream==5"</p><p>You can see all TCP streams with "tcp".</p><p>However, the <em>packets</em> will be shown in the order they were captured, so packets from different streams will be intermingled in the display if the streams were running simultaneously. To make it clear which packets belong to which stream, you can right-click on a packet in the Packet List and select Colorize Conversation &gt; TCP &gt; [Color 1, Color 2, etc.]. You can colorize up to 10 different conversations. Be careful which colors you pick; some of them are very similar and are difficult to distinguish on the screen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '13, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-17779" class="comments-container"><span id="17781"></span><div id="comment-17781" class="comment"><div id="post-17781-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the colorize tip. I'll definitely use that. However, my goal is to be able to view multiple streams in a single "Follow TCP Stream" window (or something like that).</p><p>I've edited my OP to clarify the intent of my question.</p></div><div id="comment-17781-info" class="comment-info"><span class="comment-age">(18 Jan '13, 11:07)</span> <span class="comment-user userinfo">KTM</span></div></div></div><div id="comment-tools-17779" class="comment-tools"></div><div class="clear"></div><div id="comment-17779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

