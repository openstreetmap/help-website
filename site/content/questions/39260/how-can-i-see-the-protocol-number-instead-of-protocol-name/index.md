+++
type = "question"
title = "How can I see the protocol number instead of protocol name?"
description = '''How can I see the protocol number instead of protocol name? In Wireshark I just see the name of the protocol like &quot;SIGCOMP&quot; or &quot;QUIC&quot;. I need the protocol number for ACL. I need to block/disable the &quot;SIGCOMP&quot; and &quot;QUIC&quot; protocol.'''
date = "2015-01-18T21:11:00Z"
lastmod = "2015-01-19T01:14:00Z"
weight = 39260
keywords = [ "protocol", "number" ]
aliases = [ "/questions/39260" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I see the protocol number instead of protocol name?](/questions/39260/how-can-i-see-the-protocol-number-instead-of-protocol-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39260-score" class="post-score" title="current number of votes">0</div><span id="post-39260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I see the protocol number instead of protocol name? In Wireshark I just see the name of the protocol like "SIGCOMP" or "QUIC". I need the protocol number for ACL. I need to block/disable the "SIGCOMP" and "QUIC" protocol.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '15, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/33f35d7902cb0190229646e7ce7d9b1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="appreciated&#39;s gravatar image" /><p><span>appreciated</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="appreciated has no accepted answers">0%</span></p></div></div><div id="comments-container-39260" class="comments-container"></div><div id="comment-tools-39260" class="comment-tools"></div><div class="clear"></div><div id="comment-39260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39261"></span>

<div id="answer-container-39261" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39261-score" class="post-score" title="current number of votes">1</div><span id="post-39261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At least for sigcomp I think the packets are actually over tcp or udp on port 5060 - right? So in fact it's not sigcomp. You should look at blocking port 5060 if you don't have any sip traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '15, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-39261" class="comments-container"></div><div id="comment-tools-39261" class="comment-tools"></div><div class="clear"></div><div id="comment-39261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39267"></span>

<div id="answer-container-39267" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39267-score" class="post-score" title="current number of votes">1</div><span id="post-39267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can always see the port numbers in the UDP/TCP part of the packet details pane.</p><p>If you want to see the numbers in the packet list, you can disable name resolution for the transport layer (View -&gt; Name Resolution -&gt; Enable for transport layer)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '15, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39267" class="comments-container"></div><div id="comment-tools-39267" class="comment-tools"></div><div class="clear"></div><div id="comment-39267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

