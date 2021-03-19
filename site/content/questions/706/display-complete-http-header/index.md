+++
type = "question"
title = "Display complete HTTP header"
description = '''Wireshark displays [truncated] preceding the HTTP Cookie header. How can I make it capture and display the entire Cookie header?'''
date = "2010-10-27T08:07:00Z"
lastmod = "2010-10-28T15:40:00Z"
weight = 706
keywords = [ "cookie", "truncated", "http", "header" ]
aliases = [ "/questions/706" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display complete HTTP header](/questions/706/display-complete-http-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-706-score" class="post-score" title="current number of votes">1</div><span id="post-706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark displays [truncated] preceding the HTTP Cookie header. How can I make it capture and display the entire Cookie header?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cookie" rel="tag" title="see questions tagged &#39;cookie&#39;">cookie</span> <span class="post-tag tag-link-truncated" rel="tag" title="see questions tagged &#39;truncated&#39;">truncated</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '10, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/7055c5f5253d54724373553372514768?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthewlmcclure&#39;s gravatar image" /><p><span>matthewlmcclure</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthewlmcclure has no accepted answers">0%</span></p></div></div><div id="comments-container-706" class="comments-container"><span id="715"></span><div id="comment-715" class="comment"><div id="post-715-score" class="comment-score"></div><div class="comment-text"><p>Can you use http.cookie as a display filter to see all packets that contain an HTTP cookie and then right-click on one of those packets and select Follow TCP stream? Do you see the entire cookie now?</p></div><div id="comment-715-info" class="comment-info"><span class="comment-age">(27 Oct '10, 20:16)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-706" class="comment-tools"></div><div class="clear"></div><div id="comment-706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="736"></span>

<div id="answer-container-736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-736-score" class="post-score" title="current number of votes">2</div><span id="post-736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark DID capture the whole Cookie Header (assuming that no snaplength was used during capture). However, it has a limit on the length of text to show for one particular item in the protocol detail pane.</p><p>When you select the Cookie Header, you can see the whole Cookie Header in HEX &amp; Ascii in the packet bytes pane. Or you can use "Copy Value" to extract the whole Cookie Header into the copy buffer and paste it in a text editor of your choice to view.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '10, 15:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-736" class="comments-container"></div><div id="comment-tools-736" class="comment-tools"></div><div class="clear"></div><div id="comment-736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

