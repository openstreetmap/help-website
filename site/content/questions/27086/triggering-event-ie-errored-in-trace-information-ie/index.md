+++
type = "question"
title = "Triggering-Event IE errored in Trace-Information IE"
description = '''I am using wireshark version 1.11.0. I am facing problem while decoding the Triggering-Events IE sent in Create Session Request in GTPv2 protocol.  The size of the decoded IE by Wireshark is 8 bytes long but as per specification-32.422-ab0 the size should be 9 bytes long. Can any one have a look and...'''
date = "2013-11-18T23:46:00Z"
lastmod = "2013-11-20T18:14:00Z"
weight = 27086
keywords = [ "information", "ie", "trace" ]
aliases = [ "/questions/27086" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Triggering-Event IE errored in Trace-Information IE](/questions/27086/triggering-event-ie-errored-in-trace-information-ie)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27086-score" class="post-score" title="current number of votes">0</div><span id="post-27086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark version 1.11.0. I am facing problem while decoding the Triggering-Events IE sent in Create Session Request in GTPv2 protocol. The size of the decoded IE by Wireshark is 8 bytes long but as per specification-32.422-ab0 the size should be 9 bytes long.</p><p>Can any one have a look and please let me know.</p><p>Hope for your cooperation. Thanks in advance.</p><p>-- Regards Mrinal Aich Software Engineer-1, Dynamic Digital Technology, Kolkata</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-information" rel="tag" title="see questions tagged &#39;information&#39;">information</span> <span class="post-tag tag-link-ie" rel="tag" title="see questions tagged &#39;ie&#39;">ie</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '13, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/6ac0d9e777e77faa8d859fc0f335919a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mrinal&#39;s gravatar image" /><p><span>Mrinal</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mrinal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '13, 03:27</strong> </span></p></div></div><div id="comments-container-27086" class="comments-container"><span id="27090"></span><div id="comment-27090" class="comment"><div id="post-27090-score" class="comment-score"></div><div class="comment-text"><p>I can't find any "Triggering-Events" ary you talking about a Diameter message with an AVP "Triggering-Events"? If so what vendor id and what AVP number? If not which protocol, protocol messge and IE are you refering to? A bug report with a trace file is an alternative :-)</p></div><div id="comment-27090-info" class="comment-info"><span class="comment-age">(19 Nov '13, 01:56)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-27086" class="comment-tools"></div><div class="clear"></div><div id="comment-27086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27186"></span>

<div id="answer-container-27186" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27186-score" class="post-score" title="current number of votes">1</div><span id="post-27186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Section 8.31 of 3GPP TS 29.274 is where the GTPv2 IE specifically is defined. Mrinal is correct, it's defined as a nine byte field.</p><p>My C is rusty but I believe the problem is line 2411 of file epan/dissectors/gtpv2.c in Wireshark's source code. Looks like it defines that IE as 8 bytes (that "8" is there the byte length is given for the other IEs as you go along):</p><pre><code>trigg = proto_tree_add_text(tree, tvb, offset, 8, &quot;Trigging Events&quot;);</code></pre><p>It also misspells "triggering", at least in the source for Wireshark 1.10.2.</p><p>Mrinal, I recommend posting this issue as a bug at: <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 18:14</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '13, 18:25</strong> </span></p></div></div><div id="comments-container-27186" class="comments-container"></div><div id="comment-tools-27186" class="comment-tools"></div><div class="clear"></div><div id="comment-27186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

