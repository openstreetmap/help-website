+++
type = "question"
title = "SSL and TLS &quot;Ignored Unknown Record&quot;"
description = '''I have been actively pursuing an issue that seems to have little documentation of reference material on, e.g. Google and TCP/SSL experts. I have been trying to identify why when using SSLv3 and TLSv1.0 that in the Wireshark captures I find excessive &quot;Ignored Unknown Record&quot; and [Unreassembled Packet...'''
date = "2010-10-27T06:51:00Z"
lastmod = "2011-08-24T06:56:00Z"
weight = 703
keywords = [ "ssl" ]
aliases = [ "/questions/703" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL and TLS "Ignored Unknown Record"](/questions/703/ssl-and-tls-ignored-unknown-record)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-703-score" class="post-score" title="current number of votes">0</div><span id="post-703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been actively pursuing an issue that seems to have little documentation of reference material on, e.g. Google and TCP/SSL experts. I have been trying to identify why when using SSLv3 and TLSv1.0 that in the Wireshark captures I find excessive "Ignored Unknown Record" and [Unreassembled Packet] responses in the capture decodes. When using SSLv2 is see nothing to that effect and the full communications between the web client and web server are clean.</p><p>Can anyone speak to the effect that this is either a true issue or a false positive by Wireshark when decoding the captures? I have heard the argument about the TOE (TCP Offloading) and the effects that can have. But if you have verified that TOE is turned off on both the Server and the Client and still find the problem, what next?</p><p>Feed back on this would be greatly appreciated, technical reference material and whitepapers would be ever better.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '10, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/276b7a7613a3953ab8a2962f095dc8ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChipPowell&#39;s gravatar image" /><p><span>ChipPowell</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChipPowell has no accepted answers">0%</span></p></div></div><div id="comments-container-703" class="comments-container"></div><div id="comment-tools-703" class="comment-tools"></div><div class="clear"></div><div id="comment-703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="718"></span>

<div id="answer-container-718" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-718-score" class="post-score" title="current number of votes">3</div><span id="post-718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is showing you traffic that is not reassembled. Let Wireshark do reassembly. Select Edit &gt; Preferences &gt; Protocols &gt; TCP and check Allow Subdissector to Reassemble TCP Streams. Better?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-718" class="comments-container"></div><div id="comment-tools-718" class="comment-tools"></div><div class="clear"></div><div id="comment-718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5839"></span>

<div id="answer-container-5839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5839-score" class="post-score" title="current number of votes">0</div><span id="post-5839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Same problem and went to Select Edit &gt; Preferences &gt; Protocols &gt; TCP &gt; Allow Subdissector to Reassemble TCP Streams....but found its already checked. Should I look at some alternate settings etc as well..?</p><p>Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '11, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/283f091311293e6e59079e6a5e281c8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nine&#39;s gravatar image" /><p><span>nine</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nine has no accepted answers">0%</span></p></div></div><div id="comments-container-5839" class="comments-container"></div><div id="comment-tools-5839" class="comment-tools"></div><div class="clear"></div><div id="comment-5839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

