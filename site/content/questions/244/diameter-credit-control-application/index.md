+++
type = "question"
title = "Diameter credit control application"
description = '''Dears, I need to know how wireshark dissects diameter protocol and its applications such as ( credit control ). Does wireshark dissects them directly, or uses external tools? Thanks.'''
date = "2010-09-21T06:28:00Z"
lastmod = "2010-09-22T13:14:00Z"
weight = 244
keywords = [ "diameter" ]
aliases = [ "/questions/244" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Diameter credit control application](/questions/244/diameter-credit-control-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-244-score" class="post-score" title="current number of votes">0</div><span id="post-244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dears,</p><p>I need to know how wireshark dissects diameter protocol and its applications such as ( credit control ). Does wireshark dissects them directly, or uses external tools?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '10, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/e2210381631ffc231bad55a0ad4b782a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="caesar_etos&#39;s gravatar image" /><p><span>caesar_etos</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="caesar_etos has no accepted answers">0%</span></p></div></div><div id="comments-container-244" class="comments-container"></div><div id="comment-tools-244" class="comment-tools"></div><div class="clear"></div><div id="comment-244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="247"></span>

<div id="answer-container-247" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-247-score" class="post-score" title="current number of votes">2</div><span id="post-247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="caesar_etos has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To elaborate on Jaaps answer Dimater is dissected with the aid of xml libraries. AVP names and atributes, enum translation, Application ID names etc comes from those libraries. path: ~wireshark/diamter/ you can add your own stuff to those libraries or update them from trunk with the latest stuff. If things ar missing or wrong in trunk we'd apreciate patches trough https://bugs.wireshark.org/bugzilla/ some AVP:s are further dissected by subdissectors, such as OCTET STRINGS containing data defined in specificaions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-247" class="comments-container"><span id="260"></span><div id="comment-260" class="comment"><div id="post-260-score" class="comment-score"></div><div class="comment-text"><p>can you specify more which xml libraries wireshark uses?</p></div><div id="comment-260-info" class="comment-info"><span class="comment-age">(22 Sep '10, 06:18)</span> <span class="comment-user userinfo">caesar_etos</span></div></div></div><div id="comment-tools-247" class="comment-tools"></div><div class="clear"></div><div id="comment-247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="246"></span>

<div id="answer-container-246" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-246-score" class="post-score" title="current number of votes">1</div><span id="post-246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It has a dissector for that which parses the applications from the diameter sub directory under the Wireshark installation directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-246" class="comments-container"></div><div id="comment-tools-246" class="comment-tools"></div><div class="clear"></div><div id="comment-246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="270"></span>

<div id="answer-container-270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-270-score" class="post-score" title="current number of votes">0</div><span id="post-270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can browse the sources here: http://anonsvn.wireshark.org/viewvc/trunk/diameter/ on my win7: C:Program FilesWiresharkdiameter Not sure on Linux. /Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '10, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-270" class="comments-container"></div><div id="comment-tools-270" class="comment-tools"></div><div class="clear"></div><div id="comment-270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

