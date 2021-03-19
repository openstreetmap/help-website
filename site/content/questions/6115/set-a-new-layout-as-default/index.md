+++
type = "question"
title = "set a new layout as default"
description = '''Hi Everyone, I would like change the layout from default to layout_type_4. I tried changing epan/prefs.c line 1400+ (Wireshark 1.6.1), but that&#x27;s not working.'''
date = "2011-09-06T01:21:00Z"
lastmod = "2011-09-12T23:50:00Z"
weight = 6115
keywords = [ "development", "preferences" ]
aliases = [ "/questions/6115" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [set a new layout as default](/questions/6115/set-a-new-layout-as-default)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6115-score" class="post-score" title="current number of votes">0</div><span id="post-6115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone,</p><p>I would like change the layout from default to layout_type_4. I tried changing epan/prefs.c line 1400+ (Wireshark 1.6.1), but that's not working.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '11, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '11, 16:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6115" class="comments-container"><span id="6125"></span><div id="comment-6125" class="comment"><div id="post-6125-score" class="comment-score">1</div><div class="comment-text"><p>Did you remove your user preferences before using the new Wireshark? It's possible that settings you had created previously are taking precedence over the defaults of your new version.</p></div><div id="comment-6125-info" class="comment-info"><span class="comment-age">(06 Sep '11, 05:29)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="6130"></span><div id="comment-6130" class="comment"><div id="post-6130-score" class="comment-score">4</div><div class="comment-text"><p>Why not just go to Edit -&gt; Preferences and select layout 4? Why do you need to change it in the code?</p></div><div id="comment-6130-info" class="comment-info"><span class="comment-age">(06 Sep '11, 11:00)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-6115" class="comment-tools"></div><div class="clear"></div><div id="comment-6115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6310"></span>

<div id="answer-container-6310" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6310-score" class="post-score" title="current number of votes">1</div><span id="post-6310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Terrestrial shark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In epan/prefs.c ...change prefs.gui_layout_type to your requirement it will solve your problem</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6310" class="comments-container"></div><div id="comment-tools-6310" class="comment-tools"></div><div class="clear"></div><div id="comment-6310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

