+++
type = "question"
title = "In SGsAP Status message the Erroneous message IE showing as extraneous data"
description = '''I am using Wireshark version 1.10.0rc2. In my SGsAP Status message the Erroneous message IE showing as extraneous data. Though by looking at the hex values i think the IE in the packet is right. It is like - 1b 0b XX XX XX XX XX XX XX XX XX XX XX'''
date = "2013-07-05T00:32:00Z"
lastmod = "2013-07-05T09:21:00Z"
weight = 22682
keywords = [ "sgsap" ]
aliases = [ "/questions/22682" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [In SGsAP Status message the Erroneous message IE showing as extraneous data](/questions/22682/in-sgsap-status-message-the-erroneous-message-ie-showing-as-extraneous-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22682-score" class="post-score" title="current number of votes">0</div><span id="post-22682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark version 1.10.0rc2. In my SGsAP Status message the Erroneous message IE showing as extraneous data. Though by looking at the hex values i think the IE in the packet is right. It is like -</p><p>1b 0b XX XX XX XX XX XX XX XX XX XX XX</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sgsap" rel="tag" title="see questions tagged &#39;sgsap&#39;">sgsap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '13, 00:32</strong></p><img src="https://secure.gravatar.com/avatar/5aae92c75bcf159f9da5092d5e7e99a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swap&#39;s gravatar image" /><p><span>swap</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swap has no accepted answers">0%</span></p></div></div><div id="comments-container-22682" class="comments-container"></div><div id="comment-tools-22682" class="comment-tools"></div><div class="clear"></div><div id="comment-22682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22692"></span>

<div id="answer-container-22692" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22692-score" class="post-score" title="current number of votes">0</div><span id="post-22692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you upload the packet in its full context (upload and post URL from: <a href="http://cloudshark.org/)?">http://cloudshark.org/)?</a></p><p>My interpretation of the spec (Table 9.3.1, 3GPP TS 29.118 R9.8.0) would decode that as the "Erroneous message" IE as you say. After those two bytes, your X's should immediately continue with the Message Type field from table 9.2.1, followed by the message in question.</p><p>edit: I did look for this in the bug tracker, but can't seem to find anything on this at the moment unless the search engine has failed me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '13, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jul '13, 09:49</strong> </span></p></div></div><div id="comments-container-22692" class="comments-container"></div><div id="comment-tools-22692" class="comment-tools"></div><div class="clear"></div><div id="comment-22692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

