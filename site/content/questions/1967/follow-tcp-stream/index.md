+++
type = "question"
title = "follow tcp stream"
description = '''hi, i face this error when i tried to get follow TCP stream ((error creating filter for this atream a transport or network layer header is needed)) please help, thanks'''
date = "2011-01-27T04:12:00Z"
lastmod = "2011-01-28T09:21:00Z"
weight = 1967
keywords = [ "sarasara" ]
aliases = [ "/questions/1967" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [follow tcp stream](/questions/1967/follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1967-score" class="post-score" title="current number of votes">0</div><span id="post-1967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>hi, i face this error when i tried to get follow TCP stream ((error creating filter for this atream a transport or network layer header is needed)) please help, thanks</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sarasara" rel="tag" title="see questions tagged &#39;sarasara&#39;">sarasara</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '11, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/6eac8fadcbb2e71600f5343107e8932c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceve&#39;s gravatar image" /><p><span>ceve</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceve has no accepted answers">0%</span></p></div></div><div id="comments-container-1967" class="comments-container"></div><div id="comment-tools-1967" class="comment-tools"></div><div class="clear"></div><div id="comment-1967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1969"></span>

<div id="answer-container-1969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1969-score" class="post-score" title="current number of votes">0</div><span id="post-1969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've never seen this before. Do you see both transport layer headers and network layer headers, IP addresses for example?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '11, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1969" class="comments-container"></div><div id="comment-tools-1969" class="comment-tools"></div><div class="clear"></div><div id="comment-1969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1974"></span>

<div id="answer-container-1974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1974-score" class="post-score" title="current number of votes">0</div><span id="post-1974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This error occurs when you have selected a frame that does not contain TCP and you try to follow-TCP-stream on it. You will have to select a TCP packet first and <em>then</em> use Follow-TCP-Stream to make it work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '11, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1974" class="comments-container"><span id="1981"></span><div id="comment-1981" class="comment"><div id="post-1981-score" class="comment-score"></div><div class="comment-text"><p>When I select a frame that does not contain TCP, "Follow TCP Stream" is grayed out. I can't click on it and I can't duplicate the error the OP is getting.</p></div><div id="comment-1981-info" class="comment-info"><span class="comment-age">(27 Jan '11, 19:18)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="1984"></span><div id="comment-1984" class="comment"><div id="post-1984-score" class="comment-score"></div><div class="comment-text"><p>Good point, menu sensitivity should indeed prevent one from from trying to Follow-TCP-Stream on a non-TCP stream. This might have been broken in some way...</p><p>@ceve: Could you post the output of "Help -&gt; About" of the Wireshark version you are using?</p></div><div id="comment-1984-info" class="comment-info"><span class="comment-age">(28 Jan '11, 00:50)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="1989"></span><div id="comment-1989" class="comment"><div id="post-1989-score" class="comment-score"></div><div class="comment-text"><p>Sorry, typo. That should have been "I CAN'T duplicate the error the OP is getting" not "I can".</p></div><div id="comment-1989-info" class="comment-info"><span class="comment-age">(28 Jan '11, 08:35)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="1990"></span><div id="comment-1990" class="comment"><div id="post-1990-score" class="comment-score"></div><div class="comment-text"><p>That's what I read in the first place :-) But I have corrected your original comment to prevent confusion...</p></div><div id="comment-1990-info" class="comment-info"><span class="comment-age">(28 Jan '11, 09:21)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-1974" class="comment-tools"></div><div class="clear"></div><div id="comment-1974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

