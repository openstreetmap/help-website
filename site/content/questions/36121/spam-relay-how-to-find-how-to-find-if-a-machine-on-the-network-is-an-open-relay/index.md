+++
type = "question"
title = "spam relay how to find? how to find if a machine on the network is an open relay"
description = '''we received a notice from our ISP that they are going to shut off our mail because we are a open relay for spam. They want to &quot;blacklist&quot; us. How can I find the machine with WIRESHARK? Thank you '''
date = "2014-09-09T11:46:00Z"
lastmod = "2014-09-09T12:52:00Z"
weight = 36121
keywords = [ "blacklist", "virus", "open", "relay", "spam" ]
aliases = [ "/questions/36121" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [spam relay how to find? how to find if a machine on the network is an open relay](/questions/36121/spam-relay-how-to-find-how-to-find-if-a-machine-on-the-network-is-an-open-relay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36121-score" class="post-score" title="current number of votes">0</div><span id="post-36121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we received a notice from our ISP that they are going to shut off our mail because we are a open relay for spam. They want to "blacklist" us. How can I find the machine with WIRESHARK?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-blacklist" rel="tag" title="see questions tagged &#39;blacklist&#39;">blacklist</span> <span class="post-tag tag-link-virus" rel="tag" title="see questions tagged &#39;virus&#39;">virus</span> <span class="post-tag tag-link-open" rel="tag" title="see questions tagged &#39;open&#39;">open</span> <span class="post-tag tag-link-relay" rel="tag" title="see questions tagged &#39;relay&#39;">relay</span> <span class="post-tag tag-link-spam" rel="tag" title="see questions tagged &#39;spam&#39;">spam</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '14, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/b5ed6e5dbbeb0afdde84a5159e43fa64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lenbob&#39;s gravatar image" /><p><span>lenbob</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lenbob has no accepted answers">0%</span></p></div></div><div id="comments-container-36121" class="comments-container"></div><div id="comment-tools-36121" class="comment-tools"></div><div class="clear"></div><div id="comment-36121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36122"></span>

<div id="answer-container-36122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36122-score" class="post-score" title="current number of votes">0</div><span id="post-36122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can use Wireshark to capture the traffic to and from your ISP to see what devices on your network accept SMTP traffic (TCP port 25). It may be simpler to scan your IP range with a nmap for that port though.</p><p>To check if a mail server is an open relay you can test them with one of the free online services that perform those kind of checks, e.g. <a href="http://www.mailradar.com/openrelay/">http://www.mailradar.com/openrelay/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '14, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36122" class="comments-container"></div><div id="comment-tools-36122" class="comment-tools"></div><div class="clear"></div><div id="comment-36122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

