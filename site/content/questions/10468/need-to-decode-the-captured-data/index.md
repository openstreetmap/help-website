+++
type = "question"
title = "Need to decode the captured data"
description = '''how to decode the captured packets how to view the original message or picture some thing like that  '''
date = "2012-04-26T11:52:00Z"
lastmod = "2012-04-30T16:41:00Z"
weight = 10468
keywords = [ "decodeing" ]
aliases = [ "/questions/10468" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need to decode the captured data](/questions/10468/need-to-decode-the-captured-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10468-score" class="post-score" title="current number of votes">0</div><span id="post-10468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to decode the captured packets how to view the original message or picture some thing like that<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decodeing" rel="tag" title="see questions tagged &#39;decodeing&#39;">decodeing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '12, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/c10742b15beca2fd871828ccdee554bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arasu&#39;s gravatar image" /><p><span>arasu</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arasu has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '12, 13:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-10468" class="comments-container"><span id="10498"></span><div id="comment-10498" class="comment"><div id="post-10498-score" class="comment-score"></div><div class="comment-text"><p>Ok... what exactly is your problem?!</p></div><div id="comment-10498-info" class="comment-info"><span class="comment-age">(28 Apr '12, 05:17)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="10539"></span><div id="comment-10539" class="comment"><div id="post-10539-score" class="comment-score"></div><div class="comment-text"><p>if it's a "text based" protcol, use: Analyze -&gt; Follow TCP/UDP Stream. You will see the transmitted data in text form. If that's not what you need, please add more details to your question.</p><p>Regards Kurt</p></div><div id="comment-10539-info" class="comment-info"><span class="comment-age">(30 Apr '12, 15:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-10468" class="comment-tools"></div><div class="clear"></div><div id="comment-10468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10542"></span>

<div id="answer-container-10542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10542-score" class="post-score" title="current number of votes">1</div><span id="post-10542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"How to decode the captured packets" is a very general question; one simple answer is to use a packet analyzer application. One nice free packet analyzer is called "Wireshark". :-)</p><p>"How to view the original message or picture" is a bit less general question. For some protocols and image formats, Wireshark might support saving images in, for example, mail messages or Web pages. There's no guarantee that it will support it in all protocols (SMTP, POP, IMAP, various Microsoft protocols, etc.) or that it will support it for all image types.</p><p>And if the traffic is running over SSL/TLS (which would be the case for HTTP traffic to an https: URL, and could also be the case for SMTP and POP and probably IMAP), you would need to supply enough information to allow Wireshark to decrypt the encrypted SSL traffic, as discussed in <a href="http://wiki.wireshark.org/SSL">the SSL page on the Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 16:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '12, 16:43</strong> </span></p></div></div><div id="comments-container-10542" class="comments-container"></div><div id="comment-tools-10542" class="comment-tools"></div><div class="clear"></div><div id="comment-10542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

