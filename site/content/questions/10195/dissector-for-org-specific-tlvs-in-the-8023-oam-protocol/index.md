+++
type = "question"
title = "Dissector for org specific TLVs in the 802.3 OAM protocol"
description = '''I hope I am asking the right question. I have just started looking into making my own dissector for this.  I&#x27;m trying to write a dissector in LUA that will parse a couple of org specific TLVs in the OAM protocol. I can&#x27;t seem to wrap my head around the steps I&#x27;d need to take to allow the built in di...'''
date = "2012-04-16T11:29:00Z"
lastmod = "2012-04-17T12:12:00Z"
weight = 10195
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/10195" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector for org specific TLVs in the 802.3 OAM protocol](/questions/10195/dissector-for-org-specific-tlvs-in-the-8023-oam-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10195-score" class="post-score" title="current number of votes">0</div><span id="post-10195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I hope I am asking the right question. I have just started looking into making my own dissector for this.</p><p>I'm trying to write a dissector in LUA that will parse a couple of org specific TLVs in the OAM protocol. I can't seem to wrap my head around the steps I'd need to take to allow the built in dissector to do all the work it can, and only run my code when the frame contains the TLVs I care about. And even better would be to only run my dissector on the portion of the frame I need it to.</p><p>How would I write a dissector in LUA that will process a specific part of a frame after the rest of the frame has been processed by a built in dissector? Or do I have to add my dissector to the dissector table in place of the slow protocols dissector?</p><p>Any pointers would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/3cc1df6883bb62a4d19de99aae9647d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mateo&#39;s gravatar image" /><p><span>Mateo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mateo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '12, 16:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-10195" class="comments-container"></div><div id="comment-tools-10195" class="comment-tools"></div><div class="clear"></div><div id="comment-10195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10201"></span>

<div id="answer-container-10201" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10201-score" class="post-score" title="current number of votes">0</div><span id="post-10201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mateo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Currently, you would have to add your dissector in place of the slow protocols dissector, as the OAM dissector does not currently have any mechanism to register a dissector for the Vendor Specific Information in a Local Information TLV in an Information OAMPDU, for the information in an Organization Specific Information TLV in an Information OAMPDU, or for the contents of an Organization Specific OAMPDU.</p><p>It would be better if there <em>were</em> such mechanisms; to request them, you should file a request for enhancement on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10201" class="comments-container"><span id="10221"></span><div id="comment-10221" class="comment"><div id="post-10221-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply. I can certainly enter a request for that. Off the top of your head, do you know of any protocols dissector that does have a mechanism for registering a dissector for a Organization Specific TLV? I can only think of one other protocol that uses them (LLDP) but I'm sure there are others. I wouldn't mind taking a stab at adding the functionality.</p><p>In the short term though, would it be easiest to customize the slow protocols dissector to dissect the parts I care about?</p></div><div id="comment-10221-info" class="comment-info"><span class="comment-age">(17 Apr '12, 10:29)</span> <span class="comment-user userinfo">Mateo</span></div></div><span id="10225"></span><div id="comment-10225" class="comment"><div id="post-10225-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Off the top of your head, do you know of any protocols dissector that does have a mechanism for registering a dissector for a Organization Specific TLV? I can only think of one other protocol that uses them (LLDP) but I'm sure there are others.</p></blockquote><p>Well, looking for calls to <code>register_dissector_table()</code> with a dissector table name that includes "oui", I only found the LLDP dissector, so there might not be others.</p><blockquote><p>In the short term though, would it be easiest to customize the slow protocols dissector to dissect the parts I care about?</p></blockquote><p>Probably.</p></div><div id="comment-10225-info" class="comment-info"><span class="comment-age">(17 Apr '12, 12:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-10201" class="comment-tools"></div><div class="clear"></div><div id="comment-10201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

