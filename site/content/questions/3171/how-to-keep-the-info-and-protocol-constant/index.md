+++
type = "question"
title = "How to keep the info and protocol constant"
description = '''I have 2 dissectors X and Y. If Y is present X calls Y or else it shows it as X. Now everything works fine. I have X and Y displaying on the PROTOCOL column in wireshark.  Now I wanna see only X so I click on protocol button but now everything changes and only Y appears  How do I make the COL_INFO a...'''
date = "2011-03-28T02:46:00Z"
lastmod = "2011-03-29T06:14:00Z"
weight = 3171
keywords = [ "info", "protocol", "columns" ]
aliases = [ "/questions/3171" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to keep the info and protocol constant](/questions/3171/how-to-keep-the-info-and-protocol-constant)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3171-score" class="post-score" title="current number of votes">0</div><span id="post-3171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 2 dissectors X and Y. If Y is present X calls Y or else it shows it as X. Now everything works fine. I have X and Y displaying on the PROTOCOL column in wireshark. Now I wanna see only X so I click on protocol button but now everything changes and only Y appears How do I make the COL_INFO and COL_PROTOCOL values unchangeable? They change every time i click on the "PROTOCOL" or "INFO" button. thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '11, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p><span>niks3089</span><br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-3171" class="comments-container"><span id="3176"></span><div id="comment-3176" class="comment"><div id="post-3176-score" class="comment-score"></div><div class="comment-text"><p>Can you be more specific? Are you writing a dissector which has a subdissector that may or may not be present, or one that is called if and only if a certain field has a specific value, or something else? Additionally, what buttons are you talking about? If you mean the column headers, then what is happening is a sort, not a relabeling.</p></div><div id="comment-3176-info" class="comment-info"><span class="comment-age">(28 Mar '11, 09:24)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="3177"></span><div id="comment-3177" class="comment"><div id="post-3177-score" class="comment-score"></div><div class="comment-text"><p>It is not sorting. The protcol X is not present. I am calling the Y sub dissector from only X . So if X is present then so is Y . But when press the column headers all the protocols other than X and Y sort but Y replaces the occurances of X . hope you understood</p></div><div id="comment-3177-info" class="comment-info"><span class="comment-age">(28 Mar '11, 09:35)</span> <span class="comment-user userinfo">niks3089</span></div></div><span id="3187"></span><div id="comment-3187" class="comment"><div id="post-3187-score" class="comment-score"></div><div class="comment-text"><p>So do you mean that when you read in a capture, or perform a capture, packets that have protocol Y running atop protocol X show protocol X's name in the Protocol column and the info for protocol X in the Info column, but when you try to sort on the Info or Protocol columns the Protocol column for those packets changes to show protocol Y's name and the Info column for those packets changes to show protocol Y's info?</p></div><div id="comment-3187-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-3171" class="comment-tools"></div><div class="clear"></div><div id="comment-3171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3178"></span>

<div id="answer-container-3178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3178-score" class="post-score" title="current number of votes">0</div><span id="post-3178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you click on the Protocol or Info column headers, you are only causing Wireshark to sort the packets by whichever column header you selected. You are not filtering out any packets by doing this. If you only want to see packets displayed that are X, but not packets in which X calls Y, then you can use a display filter to do this, such as, "<code>X and not Y</code>"</p><p>Now if you don't want Y replacing the contents of either the Protocol or Info columns when X does call Y, then you might want to have a look at some of the column utility functions, like <code>col_set_fence()</code>, which is documented in both epan/column-utils.h and section 1.5.8 of doc/README.developer. Alternatively, you could try calling <code>col_set_writable(pinfo-&gt;cinfo, FALSE);</code> before X calls Y.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '11, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3178" class="comments-container"><span id="3198"></span><div id="comment-3198" class="comment"><div id="post-3198-score" class="comment-score"></div><div class="comment-text"><p>Actually I made a mistake. Its Y that is getting replaced by X. The above solution is not working</p></div><div id="comment-3198-info" class="comment-info"><span class="comment-age">(29 Mar '11, 00:00)</span> <span class="comment-user userinfo">niks3089</span></div></div></div><div id="comment-tools-3178" class="comment-tools"></div><div class="clear"></div><div id="comment-3178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3199"></span>

<div id="answer-container-3199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3199-score" class="post-score" title="current number of votes">0</div><span id="post-3199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Make sure you set the COL_INFO and COL_PROTOCOL columns regardless of whether the "tree" argument to your dissector is null or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '11, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3199" class="comments-container"><span id="3200"></span><div id="comment-3200" class="comment"><div id="post-3200-score" class="comment-score"></div><div class="comment-text"><p>It is set but the content keeps on changing</p></div><div id="comment-3200-info" class="comment-info"><span class="comment-age">(29 Mar '11, 06:14)</span> <span class="comment-user userinfo">niks3089</span></div></div></div><div id="comment-tools-3199" class="comment-tools"></div><div class="clear"></div><div id="comment-3199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

