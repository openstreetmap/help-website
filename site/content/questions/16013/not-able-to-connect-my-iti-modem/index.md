+++
type = "question"
title = "Not able to connect my ITI modem"
description = '''HI Team , how can i connect wireshark with ITI modem to get the network sta. to check network utilazation. Thanks Dev'''
date = "2012-11-18T10:41:00Z"
lastmod = "2012-11-19T14:02:00Z"
weight = 16013
keywords = [ "modem", "iti" ]
aliases = [ "/questions/16013" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not able to connect my ITI modem](/questions/16013/not-able-to-connect-my-iti-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16013-score" class="post-score" title="current number of votes">0</div><span id="post-16013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI Team ,</p><p>how can i connect wireshark with ITI modem to get the network sta. to check network utilazation.</p><p>Thanks Dev</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modem" rel="tag" title="see questions tagged &#39;modem&#39;">modem</span> <span class="post-tag tag-link-iti" rel="tag" title="see questions tagged &#39;iti&#39;">iti</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '12, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/cf7d6ed4a1b4fe2fb974ef2c84e73048?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devanshumathur&#39;s gravatar image" /><p><span>devanshumathur</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devanshumathur has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '12, 10:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16013" class="comments-container"><span id="16016"></span><div id="comment-16016" class="comment"><div id="post-16016-score" class="comment-score"></div><div class="comment-text"><p>can you please add some details?</p><ul><li>what is an "ITI modem"?</li><li>how is the modem related to Wireshark?</li></ul></div><div id="comment-16016-info" class="comment-info"><span class="comment-age">(18 Nov '12, 13:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16031"></span><div id="comment-16031" class="comment"><div id="post-16031-score" class="comment-score"></div><div class="comment-text"><p>i have an internet connection which is shared through one ITI modem for 4 Lan users and 5 wireless user , when i am connting to this modem it's asking for port details to connect ,modem details is here DNA-A211 ITI router/modem.</p></div><div id="comment-16031-info" class="comment-info"><span class="comment-age">(18 Nov '12, 21:01)</span> <span class="comment-user userinfo">devanshumathur</span></div></div></div><div id="comment-tools-16013" class="comment-tools"></div><div class="clear"></div><div id="comment-16013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16087"></span>

<div id="answer-container-16087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16087-score" class="post-score" title="current number of votes">0</div><span id="post-16087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. the ITI modem is apparently a DSL modem. If you connect the modem to your PC, they will communicate via PPPoE (or PPPoA).</p><p>So, if you want to monitor the network utilization (to the internet), you should capture on the NIC that is connected to the DSL modem. The Statistics module of Wireshark will give you some information about the utilization on the link.</p><blockquote><p><code>Statistics -&gt; Conversations</code><br />
<code>Statistics -&gt; Summary</code><br />
<code>Statistics -&gt; Protocol Hierarchy</code><br />
<code>Statistics -&gt; IO Graph</code><br />
</p></blockquote><p>I'm not sure what you want to say with the following !?!</p><blockquote><p>when i am connting to this modem it's asking for port details to connect</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16087" class="comments-container"></div><div id="comment-tools-16087" class="comment-tools"></div><div class="clear"></div><div id="comment-16087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

