+++
type = "question"
title = "Preferences TCP - providing WindowScale factor"
description = '''Just came across the new fantastic feature of telling wireshark what the windowscale factor was when the 3-way handshake is not captured. Edit - Preferences -&amp;gt; Protocols -&amp;gt; TCP  What can I do when the window scaling factor is not the same at both ends? Looks like I can only specify one. '''
date = "2013-08-05T23:10:00Z"
lastmod = "2013-08-07T01:04:00Z"
weight = 23573
keywords = [ "windowscale", "preferences", "tcp" ]
aliases = [ "/questions/23573" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Preferences TCP - providing WindowScale factor](/questions/23573/preferences-tcp-providing-windowscale-factor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23573-score" class="post-score" title="current number of votes">0</div><span id="post-23573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just came across the new fantastic feature of telling wireshark what the windowscale factor was when the 3-way handshake is not captured. Edit - Preferences -&gt; Protocols -&gt; TCP <img src="https://osqa-ask.wireshark.org/upfiles/wscale2.png" alt="alt text" /></p><p>What can I do when the window scaling factor is not the same at both ends? Looks like I can only specify one.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windowscale" rel="tag" title="see questions tagged &#39;windowscale&#39;">windowscale</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '13, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-23573" class="comments-container"></div><div id="comment-tools-23573" class="comment-tools"></div><div class="clear"></div><div id="comment-23573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23575"></span>

<div id="answer-container-23575" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23575-score" class="post-score" title="current number of votes">2</div><span id="post-23575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can not set the scaling factor differently for each direction, nor can you set it differently for multiple TCP sessions in the capture file as preferences are agnostic to specific contents of the capture file.</p><p>But in practice, the window scaling is most important in large transfers in one direction, so setting a global scaling factor to analyze one flow of the session works pretty well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '13, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23575" class="comments-container"><span id="23604"></span><div id="comment-23604" class="comment"><div id="post-23604-score" class="comment-score"></div><div class="comment-text"><p>Not what I was hoping for but thanks for the explanation! Maybe in a future release the user can add that information as a keyword in a packet comment on any 2 packets of a single tcp connection (one in every direction) for wireshark to read and process.</p></div><div id="comment-23604-info" class="comment-info"><span class="comment-age">(07 Aug '13, 01:04)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-23575" class="comment-tools"></div><div class="clear"></div><div id="comment-23575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

