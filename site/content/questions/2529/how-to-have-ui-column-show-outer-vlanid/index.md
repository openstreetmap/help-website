+++
type = "question"
title = "how to have UI column show outer vlan.id"
description = '''hi, I&#x27;m capturing double 802.1q tagged frames. I&#x27;d like to have columns which display both the outer and inner vlan tag ID in the user interface. the column field type &quot;802.1q VLAN id&quot; shows the inner vlan id. the custom column with vlan.id also shows inner tag. how do i have a column show the outer...'''
date = "2011-02-23T11:45:00Z"
lastmod = "2011-02-23T12:49:00Z"
weight = 2529
keywords = [ "column", "tag", "802.1q", "vlan" ]
aliases = [ "/questions/2529" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to have UI column show outer vlan.id](/questions/2529/how-to-have-ui-column-show-outer-vlanid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2529-score" class="post-score" title="current number of votes">0</div><span id="post-2529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>I'm capturing double 802.1q tagged frames. I'd like to have columns which display both the outer and inner vlan tag ID in the user interface. the column field type "802.1q VLAN id" shows the inner vlan id. the custom column with vlan.id also shows inner tag. how do i have a column show the outer tag vlan id?</p><p>thanks in advance,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-802.1q" rel="tag" title="see questions tagged &#39;802.1q&#39;">802.1q</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '11, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/78003c0762605021d789e3f64b1a9b15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="northernlight&#39;s gravatar image" /><p><span>northernlight</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="northernlight has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '11, 11:53</strong> </span></p></div></div><div id="comments-container-2529" class="comments-container"></div><div id="comment-tools-2529" class="comment-tools"></div><div class="clear"></div><div id="comment-2529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2531"></span>

<div id="answer-container-2531" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2531-score" class="post-score" title="current number of votes">1</div><span id="post-2531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In version 1.5.0 there is the new feature to select a specific occurrence of a field in a custom column. Which version are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '11, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2531" class="comments-container"><span id="2534"></span><div id="comment-2534" class="comment"><div id="post-2534-score" class="comment-score"></div><div class="comment-text"><p>That's great. Thank you SYNbit. I'm using 1.2.6. I'll wait until 1.5.0 is declared stable and give it a try.</p></div><div id="comment-2534-info" class="comment-info"><span class="comment-age">(23 Feb '11, 12:39)</span> <span class="comment-user userinfo">northernlight</span></div></div><span id="2535"></span><div id="comment-2535" class="comment"><div id="post-2535-score" class="comment-score"></div><div class="comment-text"><p>1.5.0 will not be declared stable. It's a development realease, meaning it is an official release, but it contains (many) new features, which means it could be a little less stable than the "stable" branches like 1.2.x and 1.4.x.</p><p>The first "stable" release with this functionality will be 1.6.0</p></div><div id="comment-2535-info" class="comment-info"><span class="comment-age">(23 Feb '11, 12:49)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2531" class="comment-tools"></div><div class="clear"></div><div id="comment-2531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

