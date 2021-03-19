+++
type = "question"
title = "How wireshark reassembles TCP/SIP segments"
description = '''I have problem in Analyzing a SIP message. The SIP message is fragmented across multiple TCP segments.  This is causing a problem in analyzing the SIP message, due to this, few times our code is reading only half the &quot;phone number&quot; etc. Interesting thing is wireshark is able to reassemble these TCP ...'''
date = "2014-06-03T06:54:00Z"
lastmod = "2014-06-03T07:58:00Z"
weight = 33344
keywords = [ "reassembly", "segments", "tcp", "of" ]
aliases = [ "/questions/33344" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How wireshark reassembles TCP/SIP segments](/questions/33344/how-wireshark-reassembles-tcpsip-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33344-score" class="post-score" title="current number of votes">0</div><span id="post-33344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have problem in Analyzing a SIP message. The SIP message is fragmented across multiple TCP segments. This is causing a problem in analyzing the SIP message, due to this, few times our code is reading only half the "phone number" etc.</p><p>Interesting thing is wireshark is able to reassemble these TCP segments. Just i wanted to know how wireshark is reassembling into one PDU?</p><p>Wireshark decodes as below</p><p>No Source Destination Protocol Length Info</p><ol><li>x.x.x.x y.y.y.y TCP 582 [TCP segment of reassembled PDU]</li><li>x.x.x.x y.y.y.y TCP 582 [TCP segment of reassembled PDU]</li><li>x.x.x.x y.y.y.y TCP 582 [TCP segment of reassembled PDU]</li><li>x.x.x.x y.y.y.y SIP/SDP 562 Request:INVITE:sip <span class="__cf_email__" data-cfemail="b88d88888ef889968996899689">[email protected]</span>; User=phone 1</li></ol><p>here message 4 is assembled 1,2 and 3 TCP segments</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-segments" rel="tag" title="see questions tagged &#39;segments&#39;">segments</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-of" rel="tag" title="see questions tagged &#39;of&#39;">of</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '14, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/7cda6020d163a370ed9996b83257abcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Veer&#39;s gravatar image" /><p><span>Veer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Veer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jun '14, 06:56</strong> </span></p></div></div><div id="comments-container-33344" class="comments-container"></div><div id="comment-tools-33344" class="comment-tools"></div><div class="clear"></div><div id="comment-33344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33346"></span>

<div id="answer-container-33346" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33346-score" class="post-score" title="current number of votes">0</div><span id="post-33346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer:</p><p>There's some amount of code in the Wireshark SIP dissector (epan/packet-sip.c) to handle reassembly of SIP PDUs.</p><p>You'll need to look at the code to see how Wireshark does the reassembly. :)</p><p>As you've seen, since TCP is a streaming protocol, a TCP segment can contain only part of a high-level protocol PDU; thus the higher level protocol must have some way to determine the actual length of the PDU to be able get the data (from 1 or more TCP segments) for the complete PDU.</p><p>This can be done in various ways: e.g., Having a "length" field as the initial part of the PDU.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '14, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jun '14, 08:05</strong> </span></p></div></div><div id="comments-container-33346" class="comments-container"></div><div id="comment-tools-33346" class="comment-tools"></div><div class="clear"></div><div id="comment-33346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

