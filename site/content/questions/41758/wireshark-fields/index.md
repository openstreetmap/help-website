+++
type = "question"
title = "Wireshark  fields"
description = '''We understand that fields enclosed in square brackets [ ] are calculated by Wireshark. What type of fields are enclosed in “greater than / less than” &amp;lt; &amp;gt; signs? An example is shown below. We have two Wireshark installs (same version). One Wireshark instance is displaying these two true/false v...'''
date = "2015-04-23T14:47:00Z"
lastmod = "2015-04-23T14:59:00Z"
weight = 41758
keywords = [ "ftp", "request", "response" ]
aliases = [ "/questions/41758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark fields](/questions/41758/wireshark-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41758-score" class="post-score" title="current number of votes">0</div><span id="post-41758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We understand that fields enclosed in square brackets [ ] are calculated by Wireshark. What type of fields are enclosed in “greater than / less than” &lt; &gt; signs?</p><p>An example is shown below. We have two Wireshark installs (same version). One Wireshark instance is displaying these two true/false values for FTP, the other is not. We are using the same trace file in both. We cannot locate the Wireshark setting that controls the display of these &lt; &gt; lines.</p><p>File Transfer Protocol (FTP) &lt;request: true=""&gt; &lt;response: false=""&gt;</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '15, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/20c1984de1fcb73b692e3f05632f041a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David99&#39;s gravatar image" /><p><span>David99</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David99 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '15, 14:49</strong> </span></p></div></div><div id="comments-container-41758" class="comments-container"></div><div id="comment-tools-41758" class="comment-tools"></div><div class="clear"></div><div id="comment-41758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41760"></span>

<div id="answer-container-41760" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41760-score" class="post-score" title="current number of votes">1</div><span id="post-41760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to Edit &gt; Preferences &gt; Protocols and uncheck "Display hidden protocol items" to return Wireshark to the default setting and turn off display of those fields.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '15, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-41760" class="comments-container"><span id="41762"></span><div id="comment-41762" class="comment"><div id="post-41762-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jim, that fixed the issue.</p></div><div id="comment-41762-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:59)</span> <span class="comment-user userinfo">David99</span></div></div></div><div id="comment-tools-41760" class="comment-tools"></div><div class="clear"></div><div id="comment-41760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

