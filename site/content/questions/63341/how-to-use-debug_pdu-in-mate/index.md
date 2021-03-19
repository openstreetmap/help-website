+++
type = "question"
title = "How to use Debug_Pdu in MATE"
description = '''How to use Debug_Pdu in MATE? The MATE Reference Manual does not provide enough guidance. Thanks in advance.'''
date = "2017-08-02T07:55:00Z"
lastmod = "2017-08-02T13:59:00Z"
weight = 63341
keywords = [ "debug", "mate" ]
aliases = [ "/questions/63341" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use Debug\_Pdu in MATE](/questions/63341/how-to-use-debug_pdu-in-mate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63341-score" class="post-score" title="current number of votes">0</div><span id="post-63341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to use Debug_Pdu in MATE?</p><p>The MATE Reference Manual does not provide enough guidance.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '17, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/7e50c86ac4ee2038257acc83ccb1ce21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juandering&#39;s gravatar image" /><p><span>juandering</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juandering has one accepted answer">100%</span></p></div></div><div id="comments-container-63341" class="comments-container"></div><div id="comment-tools-63341" class="comment-tools"></div><div class="clear"></div><div id="comment-63341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63342"></span>

<div id="answer-container-63342" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63342-score" class="post-score" title="current number of votes">1</div><span id="post-63342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="juandering has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry mate (can't resist that),</p><p>I've completely missed the <strong>Debugging stuff</strong> chapter of the reference manual when updating it to the new syntax. You need to place at the beginning of your MATE script something similar to the example below. Formally none of the items is mandatory, but</p><ul><li>without defining a filename you won't see anything in GUI Wireshark (no console available),</li><li>the default level is 0 (full silence) for both the global and individual levels.</li></ul><p>And don't expect too much from the levels, using 9 will not flood you as much as you might be afraid according to the manual.</p><p><code>Debug {     Filename "C:\mate_debug.txt";     Level 2;     Pdu Level 9;     Gop Level 3;     Gog Level 4;  };</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '17, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63342" class="comments-container"><span id="63357"></span><div id="comment-63357" class="comment"><div id="post-63357-score" class="comment-score"></div><div class="comment-text"><p>I've just updated the relevant part of MATE reference manual.</p></div><div id="comment-63357-info" class="comment-info"><span class="comment-age">(02 Aug '17, 13:59)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-63342" class="comment-tools"></div><div class="clear"></div><div id="comment-63342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

