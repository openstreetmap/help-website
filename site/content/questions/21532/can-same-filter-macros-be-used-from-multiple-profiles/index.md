+++
type = "question"
title = "Can same filter macros be used from multiple profiles?"
description = '''I am getting into the habit of switching between various profiles while examining a single capture, but doing so changes the set of defined filter macros. Can a single macro definition be setup to be accessible from multiple profiles? '''
date = "2013-05-28T11:12:00Z"
lastmod = "2013-05-29T09:29:00Z"
weight = 21532
keywords = [ "profiles", "display-filter" ]
aliases = [ "/questions/21532" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can same filter macros be used from multiple profiles?](/questions/21532/can-same-filter-macros-be-used-from-multiple-profiles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21532-score" class="post-score" title="current number of votes">0</div><span id="post-21532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting into the habit of switching between various profiles while examining a single capture, but doing so changes the set of defined filter macros. Can a single macro definition be setup to be accessible from multiple profiles?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-profiles" rel="tag" title="see questions tagged &#39;profiles&#39;">profiles</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '13, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/dd7ccbff7bb78e38074d113186debea3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EngAtWork&#39;s gravatar image" /><p><span>EngAtWork</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EngAtWork has no accepted answers">0%</span></p></div></div><div id="comments-container-21532" class="comments-container"></div><div id="comment-tools-21532" class="comment-tools"></div><div class="clear"></div><div id="comment-21532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21534"></span>

<div id="answer-container-21534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21534-score" class="post-score" title="current number of votes">0</div><span id="post-21534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Manually, yes. Copy the file "dfilter_macros" into each profile directory. As far as I know there is now way of creating a macro within Wireshark that is available in all profiles automatically, so you have to create it and then copy it to each profile directory yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '13, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 May '13, 11:19</strong> </span></p></div></div><div id="comments-container-21534" class="comments-container"></div><div id="comment-tools-21534" class="comment-tools"></div><div class="clear"></div><div id="comment-21534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21571"></span>

<div id="answer-container-21571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21571-score" class="post-score" title="current number of votes">0</div><span id="post-21571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While there is no way yet to share parts of the configuration between profiles from within WIreshark, you could of course use shortcuts (windows) or symbolic/hard links (osx/linux/*nix) to have the same file available between profiles. If you do that for your filter macros file (dfilter_macros), you will be able to access and edit your filter macros from all profiles in which you have linked the file :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21571" class="comments-container"></div><div id="comment-tools-21571" class="comment-tools"></div><div class="clear"></div><div id="comment-21571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

