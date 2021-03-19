+++
type = "question"
title = "Community Feedback Request: Should DHCP analysis be separated from BOOTP?"
description = '''Since its inception, Wireshark has had a dissector for BOOTP. When DHCP became a commonly-used protocol, that was built into the BOOTP dissector since it was built upon the BOOTP protocol. At this point, though, most network users have no idea what BOOTP is. While some of us may be familiar with it ...'''
date = "2016-06-13T10:38:00Z"
lastmod = "2016-06-14T02:06:00Z"
weight = 53411
keywords = [ "dhcp", "dissector", "bootp" ]
aliases = [ "/questions/53411" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Community Feedback Request: Should DHCP analysis be separated from BOOTP?](/questions/53411/community-feedback-request-should-dhcp-analysis-be-separated-from-bootp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53411-score" class="post-score" title="current number of votes">-1</div><span id="post-53411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Since its inception, Wireshark has had a dissector for BOOTP. When DHCP became a commonly-used protocol, that was built into the BOOTP dissector since it was built upon the BOOTP protocol.</p><p>At this point, though, most network users have no idea what BOOTP is. While some of us may be familiar with it because many things (tools, instruments, printers, etc.) still operate with BOOTP, we recognize that DHCP in itself can and should be wholly separated from BOOTP, especially when it comes to analysis. By this, I mean that when I filter on "bootp," I expect to see only BOOTP traffic and no DHCP, and there needs to be a DHCP filter that shows either DHCP and BOOTP traffic, or exclusively DHCP traffic.</p><p>I personally believe this needs to be done in order to best support those of us who regularly analyze DHCP and BOOTP traffic, and that Wireshark <em>needs</em> to support DHCP as independent from BOOTP.</p><p>So, the question: does anyone in the community believe that DHCP needs to be or should <em>not</em> be separated from BOOTP? Why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-bootp" rel="tag" title="see questions tagged &#39;bootp&#39;">bootp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '16, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/b468e4e16e13d50e47e4eda1e7b6ca02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael_Romans&#39;s gravatar image" /><p><span>Michael_Romans</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael_Romans has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '16, 10:46</strong> </span></p></div></div><div id="comments-container-53411" class="comments-container"><span id="53415"></span><div id="comment-53415" class="comment"><div id="post-53415-score" class="comment-score">1</div><div class="comment-text"><p>For the sake of completeness:</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12516">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12516</a> is discussing this issue too.</p></div><div id="comment-53415-info" class="comment-info"><span class="comment-age">(13 Jun '16, 11:39)</span> <span class="comment-user userinfo">Uli</span></div></div></div><div id="comment-tools-53411" class="comment-tools"></div><div class="clear"></div><div id="comment-53411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53432"></span>

<div id="answer-container-53432" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53432-score" class="post-score" title="current number of votes">3</div><span id="post-53432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From a protocol design point of view <a href="https://tools.ietf.org/html/rfc2131">DHCP</a> is no more than an <a href="https://tools.ietf.org/html/rfc2132">extension</a> of <a href="https://tools.ietf.org/html/rfc951">BOOTP</a>. Therefore it uses the BOOTP messages (BOOTREQUEST, BOOTREPLY) and uses the BOOTP UDP port. It uses the BOOTP message layout (to allow for interoperability between BOOTP, DHCP, BOOTP relay) and its overloading features. So where does BOOTP end and DHCP start? After the DHCP cookie? What to do with overloaded BOOTP fields?</p><p>It becomes clear that the protocol stack look like this: <code>DL / IP / UDP / BOOTP + DHCP extensions</code>.</p><p>And that the DHCP 'protocol' is no more than a profile of the use of the BOOTP protocol. In itself this profile has become a predominant player in host configuration. But from a protocol analysis point of view, it's just BOOTP (+extensions).</p><p>With Wireshark packet dissection trying to reflecting the pure protocol stack it's clear that the protocol stack as shown is reflected in this dissection. Therefore there is no DHCP protocol to speak of.</p><p>Is there nothing else possible? There is. Thanks to the display filter engine it is possible to correlate various protocol fields to determine if we have a pure BOOTP or BOOTP + DHCP extensions packet at hand. Wrapping such expressions into display filter macro's provides the desired functionality, while preserving the integrity of the protocol dissectors.</p><p>In short this is a vote against the notion of separation, because there is none.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '16, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-53432" class="comments-container"></div><div id="comment-tools-53432" class="comment-tools"></div><div class="clear"></div><div id="comment-53432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

