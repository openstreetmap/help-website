+++
type = "question"
title = "Wireshark 2.0.2 not reassembling segments of HTTP as 1.12.10 does"
description = '''I am testing an embedded web server which generally sends the HTTP header in one TCP segment, and the data in subsequent segments. Previous versions of Wireshark through 1.12.10 would reassemble the segments and show &quot;HTTP&quot; in the protocol column for the frame with the last segment along with &quot;N rea...'''
date = "2016-04-14T12:06:00Z"
lastmod = "2016-04-25T15:09:00Z"
weight = 51674
keywords = [ "http", "reassemble" ]
aliases = [ "/questions/51674" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0.2 not reassembling segments of HTTP as 1.12.10 does](/questions/51674/wireshark-202-not-reassembling-segments-of-http-as-11210-does)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51674-score" class="post-score" title="current number of votes">0</div><span id="post-51674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am testing an embedded web server which generally sends the HTTP header in one TCP segment, and the data in subsequent segments. Previous versions of Wireshark through 1.12.10 would reassemble the segments and show "HTTP" in the protocol column for the frame with the last segment along with "N reassembled segments".</p><p>But Wireshark 2.0.2 shows "HTTP" in the protocol column for the frame with the FIRST data segment - just the header. The other data is there in the later frames. But it is a pain not to filter on "http" and see just the conversation without the TCP overhead.</p><p>I am using the same "preferences" file on the two versions of Wireshark, and the "Reassemble..." options are all checked.</p><p>The guy in the cube next to me sees the same behavior.</p><p>Has anyone else seen this? I have a .pcapng file and screenshots, but I don't see a way to attach them</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '16, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/97396271e105db3494171cf9bd94a521?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nomeekgeek&#39;s gravatar image" /><p><span>nomeekgeek</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nomeekgeek has no accepted answers">0%</span></p></div></div><div id="comments-container-51674" class="comments-container"><span id="51926"></span><div id="comment-51926" class="comment"><div id="post-51926-score" class="comment-score"></div><div class="comment-text"><p>Upload the capture file somewhere publicly accessible, e.g. Cloudshark, Google Drive, DropBox etc. and then edit your question with a link to the capture file.</p></div><div id="comment-51926-info" class="comment-info"><span class="comment-age">(25 Apr '16, 07:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51931"></span><div id="comment-51931" class="comment"><div id="post-51931-score" class="comment-score"></div><div class="comment-text"><p>I have uploaded a sample capture to <a href="https://www.cloudshark.org/captures/9a2309a647ef">https://www.cloudshark.org/captures/9a2309a647ef</a></p><p>There is a GET request in frame 73, with response data in frames 75 (headers) and 76 (body).</p><p>When I load the file in Wireshark 2.0.2 and filter on "tcp &amp;&amp; http" (http alone also shows SSDP over UDP traffic on our network), it shows "HTTP" for frame 75, with only the header data. Frame 76 isn't shown. If I remove the HTTP filter, I can see the data in TCP frame 76, but lack of a rollup makes it clumsy to interpret the response.</p><p>When I load the file in Wireshark 1.12.10 or 2.0.3 and filter on "tcp &amp;&amp; http", it shows "HTTP" for frame 76. Details shows “2 reassembled TCP segments #75 and #76” and the data pane shows the entire message for easy reading.</p><p>Also shows correctly in CloudShark's view.</p><p>I no longer have the 2.0.2 installed, so I can't say whether ALL transactions (such as the GET responses in frames 6 through 12) showed the problem. I believe that it did, but 75/76 is one for which I have got a screen-shot showing the problem (which I now see that CloudShark won't let me upload)</p></div><div id="comment-51931-info" class="comment-info"><span class="comment-age">(25 Apr '16, 11:33)</span> <span class="comment-user userinfo">nomeekgeek</span></div></div></div><div id="comment-tools-51674" class="comment-tools"></div><div class="clear"></div><div id="comment-51674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="51927"></span>

<div id="answer-container-51927" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51927-score" class="post-score" title="current number of votes">1</div><span id="post-51927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Whatever was fixed in 2.0.3 did not include bug 10335. Wireshark still does not correctly identify all HTTP packets. Some HTTP packets are still identified as simply TCP and the contents are not dissected. Bug 10335 affects all versions from 1.12.0, including recently released versions 1.12.11 and 2.0.3.</p><p>For the original poster, you can accomplish the same goal (seeing the conversation without the TCP overhead) using the display filter "tcp.port==80 and tcp.len &gt; 0". Substitute the correct port, of course, if the HTTP traffic uses an alternate port. If this is something you do a lot, you might want to make this a filter expression button on the display filter toolbar so that this display filter can be quickly applied.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '16, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51927" class="comments-container"><span id="51928"></span><div id="comment-51928" class="comment"><div id="post-51928-score" class="comment-score"></div><div class="comment-text"><p>I do not know whether the problem I saw in 2.0.2 is related to 10335. My experience has been that the HTTP re-assembly:</p><ul><li>worked (and still works) in 1.12.10</li><li>did not work in 2.0.2 (multiple installations of 32-bit and 64-bit versions on different PCs)</li><li>works in the 2.0.3 update I installed this morning.</li></ul><p>Jim Aragon's tip about tcp.len&gt;0 is a useful work around if I see the problem again, although it means seeing each chunk-containing frame, rather than the HTTP re-assembly. Better than nothing, though.</p></div><div id="comment-51928-info" class="comment-info"><span class="comment-age">(25 Apr '16, 10:35)</span> <span class="comment-user userinfo">nomeekgeek</span></div></div><span id="51929"></span><div id="comment-51929" class="comment"><div id="post-51929-score" class="comment-score"></div><div class="comment-text"><p><span>@nomeekgeek</span></p><p>Is there any chance of you making the capture available, it's another point in the possible search for a solution for bug 10335?</p></div><div id="comment-51929-info" class="comment-info"><span class="comment-age">(25 Apr '16, 10:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51940"></span><div id="comment-51940" class="comment"><div id="post-51940-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>, I've attached a capture file to bug 10335 that illustrates the problem very dramatically. This is in addition to the one that was previously uploaded when the original bug was filed.</p></div><div id="comment-51940-info" class="comment-info"><span class="comment-age">(25 Apr '16, 15:09)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-51927" class="comment-tools"></div><div class="clear"></div><div id="comment-51927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51678"></span>

<div id="answer-container-51678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51678-score" class="post-score" title="current number of votes">0</div><span id="post-51678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10335">10335</a>, but that reports 1.12.x as broken as well?</p><p>See <a href="https://ask.wireshark.org/questions/35767/packets-marked-as-http-on-1109-are-marked-as-tcp-on-1120">this</a> similar question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51678" class="comments-container"></div><div id="comment-tools-51678" class="comment-tools"></div><div class="clear"></div><div id="comment-51678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51924"></span>

<div id="answer-container-51924" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51924-score" class="post-score" title="current number of votes">0</div><span id="post-51924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Fixed by update to 2.0.3</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '16, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/97396271e105db3494171cf9bd94a521?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nomeekgeek&#39;s gravatar image" /><p><span>nomeekgeek</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nomeekgeek has no accepted answers">0%</span></p></div></div><div id="comments-container-51924" class="comments-container"></div><div id="comment-tools-51924" class="comment-tools"></div><div class="clear"></div><div id="comment-51924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

