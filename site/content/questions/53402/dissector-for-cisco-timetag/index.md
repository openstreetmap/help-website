+++
type = "question"
title = "Dissector for Cisco TimeTag"
description = '''The Cisco Nexus 3548 has ability to add a ptp clocked time tag to each ingress packet on egress. Has anyone build a dissector to parse this? bytes 13/14 Ethertype 0xBB85 bytes 15-20 6 byte time tick in NS bytes 21/22 actual ethertype (0x0800 for IP or 8100 for dotQ tag). Steve'''
date = "2016-06-13T08:29:00Z"
lastmod = "2016-06-14T00:55:00Z"
weight = 53402
keywords = [ "nexus", "dissector", "cisco" ]
aliases = [ "/questions/53402" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector for Cisco TimeTag](/questions/53402/dissector-for-cisco-timetag)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53402-score" class="post-score" title="current number of votes">0</div><span id="post-53402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The Cisco Nexus 3548 has ability to add a ptp clocked time tag to each ingress packet on egress. Has anyone build a dissector to parse this?<br />
bytes 13/14 Ethertype 0xBB85<br />
bytes 15-20 6 byte time tick in NS<br />
bytes 21/22 actual ethertype (0x0800 for IP or 8100 for dotQ tag).</p><p>Steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nexus" rel="tag" title="see questions tagged &#39;nexus&#39;">nexus</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '16, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/575922bd3f5d72b465eac18a045acfd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve_merc&#39;s gravatar image" /><p><span>steve_merc</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve_merc has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '16, 08:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></br></p></div></div><div id="comments-container-53402" class="comments-container"></div><div id="comment-tools-53402" class="comment-tools"></div><div class="clear"></div><div id="comment-53402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53409"></span>

<div id="answer-container-53409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53409-score" class="post-score" title="current number of votes">1</div><span id="post-53409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please raise an enhancement request on bugzilla with a sample trace file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '16, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-53409" class="comments-container"><span id="53413"></span><div id="comment-53413" class="comment"><div id="post-53413-score" class="comment-score"></div><div class="comment-text"><p>Thank you for info. I will do.</p><p>Steve</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12518">Bug 12518</a></p></div><div id="comment-53413-info" class="comment-info"><span class="comment-age">(13 Jun '16, 11:23)</span> <span class="comment-user userinfo">steve_merc</span></div></div><span id="53417"></span><div id="comment-53417" class="comment"><div id="post-53417-score" class="comment-score"></div><div class="comment-text"><p>(I converted Ander's comment to an answer since it answers the question: no, Wireshark doesn't support this today.)</p></div><div id="comment-53417-info" class="comment-info"><span class="comment-age">(13 Jun '16, 12:18)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="53427"></span><div id="comment-53427" class="comment"><div id="post-53427-score" class="comment-score"></div><div class="comment-text"><p>And if you cannot wait, you may use Lua to cover the time until someone picks up your enhancement request. From the description the dissection of the header doesn't seem to be a complex task.</p></div><div id="comment-53427-info" class="comment-info"><span class="comment-age">(14 Jun '16, 00:55)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-53409" class="comment-tools"></div><div class="clear"></div><div id="comment-53409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

