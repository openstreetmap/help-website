+++
type = "question"
title = "GRE Protocol Type 0x8909"
description = '''The GRE Protocol Type 0x8909 is used by Cisco gear to encapsulate Cisco MetaData frames inside GRE. What would be the easiest way to modify the GRE Decode As option to interpret the Data within the GRE payload as a Cisco MetaData frame when the GRE Protocol Type is 0x8909? WireShark can decode nativ...'''
date = "2017-06-15T12:48:00Z"
lastmod = "2017-06-17T13:28:00Z"
weight = 62051
keywords = [ "gre" ]
aliases = [ "/questions/62051" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [GRE Protocol Type 0x8909](/questions/62051/gre-protocol-type-0x8909)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62051-score" class="post-score" title="current number of votes">0</div><span id="post-62051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The GRE Protocol Type 0x8909 is used by Cisco gear to encapsulate Cisco MetaData frames inside GRE. What would be the easiest way to modify the GRE Decode As option to interpret the Data within the GRE payload as a Cisco MetaData frame when the GRE Protocol Type is 0x8909? WireShark can decode native Cisco MetaData frames already, but GRE encapsulated Cisco MetaData frames are shown as unknown.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gre" rel="tag" title="see questions tagged &#39;gre&#39;">gre</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '17, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/dba76c2c3a6d2ebd20cc7d21b9ffc630?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rmcguilicuddy&#39;s gravatar image" /><p><span>rmcguilicuddy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rmcguilicuddy has no accepted answers">0%</span></p></div></div><div id="comments-container-62051" class="comments-container"></div><div id="comment-tools-62051" class="comment-tools"></div><div class="clear"></div><div id="comment-62051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62053"></span>

<div id="answer-container-62053" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62053-score" class="post-score" title="current number of votes">1</div><span id="post-62053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rmcguilicuddy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Currently there is no support for this.</p><p>To get Cisco MetaData dissected as GRE payload the source code of epan/dissectors/packet-gre.c and epan/dissectors/packet-cisco-metadata.c has to be modified.</p><p>If you want this feature in some future Wireshark version open an <a href="https://bugs.wireshark.org/bugzilla/">enhancement bug</a> (including sample capture(s)).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '17, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jun '17, 13:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-62053" class="comments-container"><span id="62056"></span><div id="comment-62056" class="comment"><div id="post-62056-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info, I filed <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13804">Enhancement 13804</a> request with a packet capture attached.</p></div><div id="comment-62056-info" class="comment-info"><span class="comment-age">(16 Jun '17, 06:58)</span> <span class="comment-user userinfo">rmcguilicuddy</span></div></div><span id="62057"></span><div id="comment-62057" class="comment"><div id="post-62057-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-62057-info" class="comment-info"><span class="comment-age">(16 Jun '17, 07:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="62086"></span><div id="comment-62086" class="comment"><div id="post-62086-score" class="comment-score">1</div><div class="comment-text"><p>The changes in question were made in change I0d96122a0c7f39315316e4da32c29977e147d3d6 in the master branch and change I0d96122a0c7f39315316e4da32c29977e147d3d6 in the 2.4 branch, so this capability should be in the 2.4 release when it comes out.</p></div><div id="comment-62086-info" class="comment-info"><span class="comment-age">(17 Jun '17, 13:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-62053" class="comment-tools"></div><div class="clear"></div><div id="comment-62053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

