+++
type = "question"
title = "Change alias in src / dest port to actual port number"
description = '''My Wireshark shows src / dest port as cisco-sccp but I want it to show 2000. How can I get Wireshark to show actual port 2000 and not alias cisco-sccp?'''
date = "2017-05-18T12:53:00Z"
lastmod = "2017-05-18T21:05:00Z"
weight = 61492
keywords = [ "alias", "destination", "port", "source" ]
aliases = [ "/questions/61492" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Change alias in src / dest port to actual port number](/questions/61492/change-alias-in-src-dest-port-to-actual-port-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61492-score" class="post-score" title="current number of votes">0</div><span id="post-61492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Wireshark shows src / dest port as cisco-sccp but I want it to show 2000. How can I get Wireshark to show actual port 2000 and not alias cisco-sccp?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-alias" rel="tag" title="see questions tagged &#39;alias&#39;">alias</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '17, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/73b51f0024ff1a0273aa7267f541b234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="major&#39;s gravatar image" /><p><span>major</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="major has no accepted answers">0%</span></p></div></div><div id="comments-container-61492" class="comments-container"><span id="61499"></span><div id="comment-61499" class="comment"><div id="post-61499-score" class="comment-score"></div><div class="comment-text"><p>Is that in the packet list, as a column, or in the packet details?</p></div><div id="comment-61499-info" class="comment-info"><span class="comment-age">(18 May '17, 21:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-61492" class="comment-tools"></div><div class="clear"></div><div id="comment-61492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61494"></span>

<div id="answer-container-61494" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61494-score" class="post-score" title="current number of votes">0</div><span id="post-61494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="major has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to View-&gt;Name Resolution and disable <code>Resolve Transport Addresses</code>.</p><p>Or go into Preferences (Edit-&gt;Preferences), select the Name Resolution section, and disable <code>Resolve transport names</code>.</p><p>(This is just 2 ways of doing the same thing--pick the one that you prefer.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '17, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-61494" class="comments-container"></div><div id="comment-tools-61494" class="comment-tools"></div><div class="clear"></div><div id="comment-61494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

