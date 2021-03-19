+++
type = "question"
title = "How the Protocol Hierarchy Statistics works?"
description = '''Dear all, Please, anyone could explain how the Protocol Hierarchy Statistics works?  Could the dissectors distinguish every single protocol (of course, included in the available list)? If there is any kind of protocol that happens but hidden within other, can wireshark detect? Does the Wireshark dis...'''
date = "2010-10-11T20:30:00Z"
lastmod = "2010-10-12T03:27:00Z"
weight = 480
keywords = [ "phs", "hierarchy", "dissector", "protocol", "statistics" ]
aliases = [ "/questions/480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How the Protocol Hierarchy Statistics works?](/questions/480/how-the-protocol-hierarchy-statistics-works)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-480-score" class="post-score" title="current number of votes">0</div><span id="post-480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>Please, anyone could explain how the Protocol Hierarchy Statistics works? Could the dissectors distinguish every single protocol (of course, included in the available list)? If there is any kind of protocol that happens but hidden within other, can wireshark detect? Does the Wireshark dissect based on ports or on the structure of the protocols?</p><p>Thanks for your attention. Emilio</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-phs" rel="tag" title="see questions tagged &#39;phs&#39;">phs</span> <span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '10, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/db1f3be1fb1f27798a7c720142f80c6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emiliohonorio&#39;s gravatar image" /><p><span>emiliohonorio</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emiliohonorio has no accepted answers">0%</span></p></div></div><div id="comments-container-480" class="comments-container"></div><div id="comment-tools-480" class="comment-tools"></div><div class="clear"></div><div id="comment-480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="483"></span>

<div id="answer-container-483" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-483-score" class="post-score" title="current number of votes">1</div><span id="post-483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark tries to recognize protocols in several ways:</p><ul><li>By Identifiers. There are well-known identifiers within each protocol layer (Ethertype, IP protocol, TCP port, etc).</li><li>By previous traffic. Some protocols prepare the involved systems for new connections, Wireshark snoops on these control packets to add decoding of the dynamic sessions (example: The PORT command on an FTP control channel).</li><li>By Heuristics. Some protocols don't have a distinct Identifier, but they do have a recognizable pattern by which they can be Identified.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '10, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-483" class="comments-container"><span id="485"></span><div id="comment-485" class="comment"><div id="post-485-score" class="comment-score"></div><div class="comment-text"><p>On a side note: there are settings that can modify the results of the Protocol Hierarchy Statistics, for example the TCP Stream Reassembly. I have traces where the percentage of HTTP goes from 65% with reassembly turned off down to 13% with reassembly turned on. This is in direct relation to the protocol column in the packet list showing either HTTP or TCP, depending on this setting.</p><p>Another standard question is, why the percentage at some point doesn't add up to 100% anymore. This is because Wireshark has no "other" percentage for the remaining packets it cannot determine any further.</p></div><div id="comment-485-info" class="comment-info"><span class="comment-age">(12 Oct '10, 03:27)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-483" class="comment-tools"></div><div class="clear"></div><div id="comment-483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

