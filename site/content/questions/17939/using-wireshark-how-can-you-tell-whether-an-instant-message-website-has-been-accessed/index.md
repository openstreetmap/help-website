+++
type = "question"
title = "Using Wireshark, how can you tell whether an instant-message Website has been accessed?"
description = '''I have been working on how to find use of online messenger (e.g imo.im, ebuddy) using wireshark. I&#x27;m doing , as i need to build SIEM (security information event management) use-cases which detects usage of online web-messenger. To do little about of research, i went on a few online web-messenger and...'''
date = "2013-01-24T12:07:00Z"
lastmod = "2013-01-24T18:56:00Z"
weight = 17939
keywords = [ "instant-messaging" ]
aliases = [ "/questions/17939" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Using Wireshark, how can you tell whether an instant-message Website has been accessed?](/questions/17939/using-wireshark-how-can-you-tell-whether-an-instant-message-website-has-been-accessed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17939-score" class="post-score" title="current number of votes">0</div><span id="post-17939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been working on how to find use of online messenger (e.g imo.im, ebuddy) using wireshark. I'm doing , as i need to build SIEM (security information event management) use-cases which detects usage of online web-messenger.</p><p>To do little about of research, i went on a few online web-messenger and turned on the wireshark in the background. After a couple of minutes of browsing the online messenger sites , i stopped the wireshark and went straight on analysis. At first, I found nothing special / unique which tells me (as a user) an online messaging service / protocol i used as all these sites works on http or https.</p><p>How using wireshark one can tell IM website has been accessed ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-instant-messaging" rel="tag" title="see questions tagged &#39;instant-messaging&#39;">instant-messaging</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/a5e36ef8cc4416aa199a3a82dcb1deb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazerz&#39;s gravatar image" /><p><span>lazerz</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazerz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted <strong>24 Jan '13, 18:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17939" class="comments-container"></div><div id="comment-tools-17939" class="comment-tools"></div><div class="clear"></div><div id="comment-17939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17951"></span>

<div id="answer-container-17951" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17951-score" class="post-score" title="current number of votes">1</div><span id="post-17951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lazerz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you know the name of the site in question, you can filter on:</p><p>http.host contains imo.im || ssl.handshake.extensions_server_name contains imo.im</p><p>This will return either the Clear Text HTTP command they sent to that page or, depending on browser used by the client, the SSL Client Hello sent during SSL negotiation to the offending website.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/f4567d2db9c9f422c664030ac53a1873?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magnus%20Mortensen&#39;s gravatar image" /><p><span>Magnus Morte...</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magnus Mortensen has one accepted answer">50%</span></p></div></div><div id="comments-container-17951" class="comments-container"></div><div id="comment-tools-17951" class="comment-tools"></div><div class="clear"></div><div id="comment-17951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17948"></span>

<div id="answer-container-17948" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17948-score" class="post-score" title="current number of votes">0</div><span id="post-17948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In general, there is no easy way to do that. To post a message on a Web site, almost any sort of mechanism can be used (posting forms, etc.). You'd have to figure out some patterns in the HTTP requests that suggest that the site is an IM site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17948" class="comments-container"></div><div id="comment-tools-17948" class="comment-tools"></div><div class="clear"></div><div id="comment-17948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

