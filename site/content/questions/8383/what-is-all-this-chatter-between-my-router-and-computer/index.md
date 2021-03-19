+++
type = "question"
title = "what is all this chatter between my router and computer"
description = '''what is all this chatter between my router and computer endless obscure names continuously exchanged between router and computer. no outside IPs just names like websphere, arkivio, spiral, ironmail, embrace, galileolog, odeumservlink, starquiz-port, raven-rmp, voispeed-port etc. etc. ad nauseum. Wha...'''
date = "2012-01-13T20:00:00Z"
lastmod = "2012-01-14T07:19:00Z"
weight = 8383
keywords = [ "and", "router", "computer", "chatter", "between" ]
aliases = [ "/questions/8383" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what is all this chatter between my router and computer](/questions/8383/what-is-all-this-chatter-between-my-router-and-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8383-score" class="post-score" title="current number of votes">0</div><span id="post-8383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what is all this chatter between my router and computer endless obscure names continuously exchanged between router and computer. no outside IPs just names like websphere, arkivio, spiral, ironmail, embrace, galileolog, odeumservlink, starquiz-port, raven-rmp, voispeed-port etc. etc. ad nauseum.</p><p>What is all this stuff? Is it necessary? Where is it coming from? Can/should I be concerned about it?</p><p>Hope for some insight. Love having eyes with wireshark but way too much information.</p><p>Don</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-computer" rel="tag" title="see questions tagged &#39;computer&#39;">computer</span> <span class="post-tag tag-link-chatter" rel="tag" title="see questions tagged &#39;chatter&#39;">chatter</span> <span class="post-tag tag-link-between" rel="tag" title="see questions tagged &#39;between&#39;">between</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '12, 20:00</strong></p><img src="https://secure.gravatar.com/avatar/5cf7c56e4ec37e5e30567eb77e618617?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dorsalfin&#39;s gravatar image" /><p><span>dorsalfin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dorsalfin has no accepted answers">0%</span></p></div></div><div id="comments-container-8383" class="comments-container"></div><div id="comment-tools-8383" class="comment-tools"></div><div class="clear"></div><div id="comment-8383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8385"></span>

<div id="answer-container-8385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8385-score" class="post-score" title="current number of votes">1</div><span id="post-8385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you're looking at the service names that Wireshark determines from the port numbers in use by the nodes communicating with each other (for example, port 80 is replaced with "http"). Problem here is that a client uses ephemeral ports, but Wireshark still replaces them with the service name officially assigned to that port by IANA. You can get rid of the name resolution by disabling "Transport Layer Name Resolution", either in the preferences or in the View Menu. Or you could open the "services" file in the Wireshark installation directory and edit it until only ports that you want to be replaced are left.</p><p>And no, it is nothing to be concerned about, it's pretty normal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '12, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8385" class="comments-container"></div><div id="comment-tools-8385" class="comment-tools"></div><div class="clear"></div><div id="comment-8385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

