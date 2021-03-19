+++
type = "question"
title = "What are the filterable fields for RADIUS?"
description = '''How to filter using calling station id.  I used radius.CallingStationId == XX XX XX XX XX but its not working.  Can anyone help ?'''
date = "2016-06-21T04:16:00Z"
lastmod = "2016-06-21T11:30:00Z"
weight = 53584
keywords = [ "filter", "radius" ]
aliases = [ "/questions/53584" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What are the filterable fields for RADIUS?](/questions/53584/what-are-the-filterable-fields-for-radius)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53584-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to filter using calling station id.</p><p>I used radius.Calling<em>Station</em>Id == XX XX XX XX XX but its not working.</p><p>Can anyone help ?</p></div><div id="question-tags" class="tags-container tags">filter radius</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '16, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/4237edd51e6fdd05b96d8580506f0ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Syd%20Anas&#39;s gravatar image" /><p>Syd Anas<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Syd Anas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 21 Jun '16, 07:01</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53584" class="comments-container"><span id="53588"></span><div id="comment-53588" class="comment"><div id="post-53588-score" class="comment-score"></div><div class="comment-text"><p>@Syd Anas, someone can probably help but the chance will be much higher if you ask a separate Question (and specify in the question title which protocol you are talking about, i.e. radius in your case) rather than sticking it as an Answer to a really loosely related one.</p></div><div id="comment-53588-info" class="comment-info"><span class="comment-age">(21 Jun '16, 06:35)</span> sindy</div></div><span id="53598"></span><div id="comment-53598" class="comment"><div id="post-53598-score" class="comment-score"></div><div class="comment-text"><p>If you meant <code>radius.Calling_Station_Id</code>, what does "not working" mean? Do you have a packet with a Calling-Station-Id field with a value of XX XX XX XX XX XX, which isn't matched by the filter?</p></div><div id="comment-53598-info" class="comment-info"><span class="comment-age">(21 Jun '16, 11:46)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-53584" class="comment-tools"></div><div class="clear"></div><div id="comment-53584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53589"></span>

<div id="answer-container-53589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53589-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the packet list, choose a Radius packet which contains the Calling Station ID AVP.</p><p>In the dissection pane, click open the packet structure until the <code>Calling Station ID</code> AVP is displayed on a single line, and then right-click that line and choose <code>Apply as Filter</code> or <code>Prepare as Filter</code>. The Display filter field will get filled with <code>field_name == value</code>, you are interested in <code>field_name</code>.</p><p>The point is that Radius is an extensible protocol where vendors may contribute their own AVPs so the vendor name became part of the AVP field names.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '16, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53589" class="comments-container"></div><div id="comment-tools-53589" class="comment-tools"></div><div class="clear"></div><div id="comment-53589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53595"></span>

<div id="answer-container-53595" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53595-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does <code>radius.Calling_Station_Id</code> work?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '16, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53595" class="comments-container"><span id="53596"></span><div id="comment-53596" class="comment"><div id="post-53596-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid that <code>radius.Calling_Station_Id</code> is exactly what the OP has posted, except that the site interpreted the underscores as an instruction to print "Station" in italics (possibly my conversion of his Answer to unrelated Question into a new Question has contributed to that).</p></div><div id="comment-53596-info" class="comment-info"><span class="comment-age">(21 Jun '16, 11:39)</span> sindy</div></div><span id="53597"></span><div id="comment-53597" class="comment"><div id="post-53597-score" class="comment-score"></div><div class="comment-text"><p>That's what underscores do in the markup here (which I think is a variant of Markdown). The actual raw content of his question used the "em" tag; I don't know whether he put them there or if it happened as a result of the conversion.</p><p>Underscores can be escaped with a backslash - or you can just put the text in backquotes to make it show up as fixed-width text not interpreted with markup.</p></div><div id="comment-53597-info" class="comment-info"><span class="comment-age">(21 Jun '16, 11:44)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-53595" class="comment-tools"></div><div class="clear"></div><div id="comment-53595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

