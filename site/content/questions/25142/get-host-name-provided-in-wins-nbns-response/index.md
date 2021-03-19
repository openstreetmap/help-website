+++
type = "question"
title = "Get host name provided in WINS (Nbns) response"
description = '''I am attempting to generate a list of netbios names and IP addresses from WINS replies. I would like to find a way to either create custom columns in wireshark and / or get the textual output using tshark. I have not been able to include a slice (IE:frame[55:33]) in a display filter. My Second Stumb...'''
date = "2013-09-23T16:56:00Z"
lastmod = "2013-09-25T02:05:00Z"
weight = 25142
keywords = [ "netbios", "nbns", "nbt" ]
aliases = [ "/questions/25142" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Get host name provided in WINS (Nbns) response](/questions/25142/get-host-name-provided-in-wins-nbns-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25142-score" class="post-score" title="current number of votes">0</div><span id="post-25142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to generate a list of netbios names and IP addresses from WINS replies.</p><p>I would like to find a way to either create custom columns in wireshark and / or get the textual output using tshark. I have not been able to include a slice (IE:frame[55:33]) in a display filter. My Second Stumbling block is that windows encodes (MS calls it compression) the hostname in the reply.</p><p>Any assistance with this would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netbios" rel="tag" title="see questions tagged &#39;netbios&#39;">netbios</span> <span class="post-tag tag-link-nbns" rel="tag" title="see questions tagged &#39;nbns&#39;">nbns</span> <span class="post-tag tag-link-nbt" rel="tag" title="see questions tagged &#39;nbt&#39;">nbt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '13, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/c89893c29e1be2a892a4bbce28d53a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="astrader&#39;s gravatar image" /><p><span>astrader</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="astrader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '13, 20:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-25142" class="comments-container"></div><div id="comment-tools-25142" class="comment-tools"></div><div class="clear"></div><div id="comment-25142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25179"></span>

<div id="answer-container-25179" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25179-score" class="post-score" title="current number of votes">1</div><span id="post-25179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="astrader has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, as per my comment, there's really no way to do that. I'll look at fixing that for the next major release; if the fixes aren't too complicated (I don't expect them to be too complicated), it might be worth backporting them to the 1.10 branch, so 1.10.3 or some other future 1.10.x release also lets you do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '13, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-25179" class="comments-container"><span id="25180"></span><div id="comment-25180" class="comment"><div id="post-25180-score" class="comment-score"></div><div class="comment-text"><p>It's a bit more complicated - a NetBIOS name is typically 15 characters of name and one byte of "name type", so we'd need to think about what the right thing to do there is.</p></div><div id="comment-25180-info" class="comment-info"><span class="comment-age">(24 Sep '13, 15:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="25190"></span><div id="comment-25190" class="comment"><div id="post-25190-score" class="comment-score"></div><div class="comment-text"><p>As far as MS is concerned NetBIOS names are definitely 15 characters with a 1 byte suffix. The suffixes are enumerated, e.g. <a href="http://support.microsoft.com/kb/163409">here</a> although that kb article is old so there may be newer values, so I would think two fields, one for the name and one for the suffix.</p><p>Are there any NetBIOS implementations out there that don't follow the MS path and use the full 16 characters for the name that might fall foul of the two fields suggestion?</p></div><div id="comment-25190-info" class="comment-info"><span class="comment-age">(25 Sep '13, 02:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-25179" class="comment-tools"></div><div class="clear"></div><div id="comment-25179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25152"></span>

<div id="answer-container-25152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25152-score" class="post-score" title="current number of votes">1</div><span id="post-25152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark supports columns for every field. Find the field you want to display in the protocol tree, right click it and then select "Apply as Column".</p><p>I haven't looked at WINS in Wireshark lately as we don't use it in our environment, but if you can't get Wireshark do do what you need, then Network Monitor from MS should handle it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '13, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-25152" class="comments-container"><span id="25178"></span><div id="comment-25178" class="comment"><div id="post-25178-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, in 1.10.x and prior releases, there <em>is</em> no field for the NetBIOS names or IP addresses in NBNS packets, so he <em>can't</em> find the field in question.</p><p>Even more unfortunately, that's still true in the trunk, so, unless it's converted to use named fields, that will still be true in 1.12.x.</p></div><div id="comment-25178-info" class="comment-info"><span class="comment-age">(24 Sep '13, 15:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-25152" class="comment-tools"></div><div class="clear"></div><div id="comment-25152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

