+++
type = "question"
title = "Wireshark WCCP interpretation"
description = '''Hi Wireshark-er, This topic is not about the bug or question, is the interpretation is a bit confusing for WCCP;  From my view it should display IP.address before encap with WCCP GRE tunnel but wireshark 2.2.4 display the source of the original host '''
date = "2017-02-23T02:18:00Z"
lastmod = "2017-02-23T19:04:00Z"
weight = 59630
keywords = [ "wccp" ]
aliases = [ "/questions/59630" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark WCCP interpretation](/questions/59630/wireshark-wccp-interpretation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59630-score" class="post-score" title="current number of votes">0</div><span id="post-59630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Wireshark-er,</p><p>This topic is not about the bug or question, is the interpretation is a bit confusing for WCCP;</p><p>From my view it should display IP.address before encap with WCCP GRE tunnel but wireshark 2.2.4 display the source of the original host</p><p><img src="https://osqa-ask.wireshark.org/upfiles/test_proxy.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wccp" rel="tag" title="see questions tagged &#39;wccp&#39;">wccp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '17, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/ee15000690effb5f7ee000775e3bfe76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="limvuihan&#39;s gravatar image" /><p><span>limvuihan</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="limvuihan has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59630" class="comments-container"></div><div id="comment-tools-59630" class="comment-tools"></div><div class="clear"></div><div id="comment-59630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59632"></span>

<div id="answer-container-59632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59632-score" class="post-score" title="current number of votes">1</div><span id="post-59632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When analyzing encapsulated traffic, it can be useful to add extra IP source and destination columns to display both the outer and the encapsulated source and destination IP addresses. How?</p><p>Here's an example for adding the outer source IPv4 address: Navigate to <em>Edit -&gt; Preferences -&gt;Columns</em>, then click <em>Add</em>. For the "Field type", choose <em>Custom</em> and then enter <code>ip.src</code> for the "Field name", but (and this is the important part) change the "Field occurrence" value from 0 to 1, which will cause only the first occurrence of the field to be displayed. Rename the title from <em>"New Column"</em> to something more useful, such as <em>"OuterSrcIP"</em> and drag it into your desired column position.</p><p>Repeat for <code>ip.dst</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '17, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59632" class="comments-container"><span id="59651"></span><div id="comment-59651" class="comment"><div id="post-59651-score" class="comment-score"></div><div class="comment-text"><p>Hi cmaynard,</p><p>Thanks for the guide it work perfectly</p><p><img src="https://osqa-ask.wireshark.org/upfiles/success.jpg" alt="alt text" /></p></div><div id="comment-59651-info" class="comment-info"><span class="comment-age">(23 Feb '17, 19:04)</span> <span class="comment-user userinfo">limvuihan</span></div></div></div><div id="comment-tools-59632" class="comment-tools"></div><div class="clear"></div><div id="comment-59632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

