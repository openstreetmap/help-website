+++
type = "question"
title = "Filter out wildcard domain names"
description = '''I would like to create a display filter that will remove all sub-domains within a known domain. for example. I want to exclude all *.dropbox.com traffic like www.dropbox.com and snt-re4-8d.sjc.dropbox.com along with snt-re3-4b.sjc.dropbox.com and snt-re3-7b.sjc.dropbox.com, etc with one command not ...'''
date = "2014-11-07T15:26:00Z"
lastmod = "2015-02-26T02:29:00Z"
weight = 37673
keywords = [ "wildcard", "dns" ]
aliases = [ "/questions/37673" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Filter out wildcard domain names](/questions/37673/filter-out-wildcard-domain-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37673-score" class="post-score" title="current number of votes">0</div><span id="post-37673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to create a display filter that will remove all sub-domains within a known domain. for example. I want to exclude all *.dropbox.com traffic like www.dropbox.com and snt-re4-8d.sjc.dropbox.com along with snt-re3-4b.sjc.dropbox.com and snt-re3-7b.sjc.dropbox.com, etc with one command not 4+.</p><p>So far !(ip.host == www.dropbox.com) works but *.dropbox.com produces an isnt a valid syntax filter error.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wildcard" rel="tag" title="see questions tagged &#39;wildcard&#39;">wildcard</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/f8a9341a8c9193e7082911ee10a0495d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fa2lerror&#39;s gravatar image" /><p><span>fa2lerror</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fa2lerror has no accepted answers">0%</span></p></div></div><div id="comments-container-37673" class="comments-container"></div><div id="comment-tools-37673" class="comment-tools"></div><div class="clear"></div><div id="comment-37673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="37686"></span>

<div id="answer-container-37686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37686-score" class="post-score" title="current number of votes">1</div><span id="post-37686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just tries <code>!ip.host contains "dropbox.com"</code> and it sieems to achieve what you want.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-107.png" alt="alt text" /></p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-37686" class="comments-container"></div><div id="comment-tools-37686" class="comment-tools"></div><div class="clear"></div><div id="comment-37686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37681"></span>

<div id="answer-container-37681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37681-score" class="post-score" title="current number of votes">0</div><span id="post-37681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's no way to do that. Wireshark doesn't have any code to get all the DNS records for a wildcard domain name and do a filter that compares an IP address field with all IP addresses in the records that match that domain name.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 18:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37681" class="comments-container"></div><div id="comment-tools-37681" class="comment-tools"></div><div class="clear"></div><div id="comment-37681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40089"></span>

<div id="answer-container-40089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40089-score" class="post-score" title="current number of votes">0</div><span id="post-40089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually it’s a record in DNS zone that matches the request for nonexistent <a href="https://domainia.com/popular-domain-names">domain name</a>. If you are having a personal domain along with email configured in it, can filter out the wildcards. However the process is multilevel and quite complex. For convenience you can see slipstick.com/outlook/rules/create-a-rule-with-wildcards/. The source describes all wildcard rules, hence I hope it will be helpful for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '15, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/b4fbd1b8fcd554e01290913e6e01d053?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karltucker&#39;s gravatar image" /><p><span>karltucker</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karltucker has no accepted answers">0%</span></p></div></div><div id="comments-container-40089" class="comments-container"></div><div id="comment-tools-40089" class="comment-tools"></div><div class="clear"></div><div id="comment-40089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

