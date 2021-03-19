+++
type = "question"
title = "changing the preference using tshark"
description = '''Hi I need to the change the preference settings so that the tshark will dissect the heuristic dissector first and i need to give a command for that since i cant use the gui (manager has told me to try using only cli so cant help) please help! '''
date = "2011-04-18T06:33:00Z"
lastmod = "2011-04-18T06:40:00Z"
weight = 3556
keywords = [ "tshark", "preferences" ]
aliases = [ "/questions/3556" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [changing the preference using tshark](/questions/3556/changing-the-preference-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3556-score" class="post-score" title="current number of votes">0</div><span id="post-3556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I need to the change the preference settings so that the tshark will dissect the heuristic dissector first and i need to give a command for that since i cant use the gui (manager has told me to try using only cli so cant help) please help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p><span>niks3089</span><br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-3556" class="comments-container"></div><div id="comment-tools-3556" class="comment-tools"></div><div class="clear"></div><div id="comment-3556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3557"></span>

<div id="answer-container-3557" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3557-score" class="post-score" title="current number of votes">3</div><span id="post-3557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark -o</code> will do the trick.</p><p>-o name:value ... override preference setting</p><p>Use <code>tshark -G defaultprefs</code> to find the name of the pref you wish to change.</p><p><code>tshark -G defaultprefs</code> gives a complete list of the default prefs</p><p><code>tshark -G currentprefs</code> give a list of the currentprefs</p><hr /><p>I expect that in this case you'll want to do</p><p><code>tshark -o tcp.try_heuristic-first:TRUE</code></p><p>Also: you can use <code>tshark -C</code> to specify a particular profile to be used.</p><p>-C config_profile start with specified configuration profile</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '11, 06:55</strong> </span></p></div></div><div id="comments-container-3557" class="comments-container"></div><div id="comment-tools-3557" class="comment-tools"></div><div class="clear"></div><div id="comment-3557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

