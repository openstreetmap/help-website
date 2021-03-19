+++
type = "question"
title = "Noticed a change in how EBCDIC information is presented from /030 to no longer do that."
description = '''I was using the 1.4.4 release of Wireshark and upgraded to the 1.6 release and noticed that for MQ traffic that is talking between Unix and zOS systems the characters are now hidden instead of being shown as octocl information such as (slash) 343 (slash) 342 (slash) 310 type of information.  I was a...'''
date = "2011-06-29T05:03:00Z"
lastmod = "2011-07-03T14:41:00Z"
weight = 4808
keywords = [ "mq", "ebcdic" ]
aliases = [ "/questions/4808" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Noticed a change in how EBCDIC information is presented from /030 to no longer do that.](/questions/4808/noticed-a-change-in-how-ebcdic-information-is-presented-from-030-to-no-longer-do-that)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4808-score" class="post-score" title="current number of votes">0</div><span id="post-4808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was using the 1.4.4 release of Wireshark and upgraded to the 1.6 release and noticed that for MQ traffic that is talking between Unix and zOS systems the characters are now hidden instead of being shown as octocl information such as (slash) 343 (slash) 342 (slash) 310 type of information.<br />
</p><p>I was able to use that for other post processing to actually see traffic interactions bewteen these systems. This was by using the results from the tags like Remote Queue: and notice the 347 type of marking and then translate that to a character. Now I no longer have the option to do that.</p><p>I have had to bad level my wireshark to keep this function. Yet I like the newer features in 1.6 except for that one feature. Could it be an option to use the Octocl or the marker?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mq" rel="tag" title="see questions tagged &#39;mq&#39;">mq</span> <span class="post-tag tag-link-ebcdic" rel="tag" title="see questions tagged &#39;ebcdic&#39;">ebcdic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '11, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/a77b529500bdd2e75849ac5c7c883713?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hsteinhauer&#39;s gravatar image" /><p><span>hsteinhauer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hsteinhauer has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '11, 05:05</strong> </span></p></div></div><div id="comments-container-4808" class="comments-container"></div><div id="comment-tools-4808" class="comment-tools"></div><div class="clear"></div><div id="comment-4808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4811"></span>

<div id="answer-container-4811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4811-score" class="post-score" title="current number of votes">0</div><span id="post-4811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like a bug report to me. Please file it <a href="https://bugs.wireshark.org">here</a>, with a sample capture file for the developers to work/test with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4811" class="comments-container"><span id="4890"></span><div id="comment-4890" class="comment"><div id="post-4890-score" class="comment-score"></div><div class="comment-text"><p>OK - -I opened up a bug report</p></div><div id="comment-4890-info" class="comment-info"><span class="comment-age">(01 Jul '11, 19:01)</span> <span class="comment-user userinfo">hsteinhauer</span></div></div></div><div id="comment-tools-4811" class="comment-tools"></div><div class="clear"></div><div id="comment-4811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4895"></span>

<div id="answer-container-4895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4895-score" class="post-score" title="current number of votes">0</div><span id="post-4895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, the MQ dissector in the SVN trunk translates EBCDIC strings to ASCII before showing them in the Info column or packet details. That's scheduled for backporting to 1.6.1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '11, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4895" class="comments-container"></div><div id="comment-tools-4895" class="comment-tools"></div><div class="clear"></div><div id="comment-4895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

