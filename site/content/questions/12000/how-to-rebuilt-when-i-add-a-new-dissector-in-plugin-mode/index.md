+++
type = "question"
title = "How to rebuilt when I add a new dissector in Plugin mode."
description = '''I have add a new protocol&quot;scoreboard&quot; dissector in plugin,files is located in wireshark1.6.4&#92;plugins&#92;scoreboard. when i rebuilt the dissector in &#92;plugin. as: nmake -f Makefile.nmake all. and then I run the main program, there is nothing changed.  but when i rebuilt all of the project .(need much mor...'''
date = "2012-06-17T23:45:00Z"
lastmod = "2012-06-18T01:45:00Z"
weight = 12000
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/12000" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to rebuilt when I add a new dissector in Plugin mode.](/questions/12000/how-to-rebuilt-when-i-add-a-new-dissector-in-plugin-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12000-score" class="post-score" title="current number of votes">0</div><span id="post-12000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have add a new protocol"scoreboard" dissector in plugin,files is located in wireshark1.6.4\plugins\scoreboard. when i rebuilt the dissector in \plugin. as: nmake -f Makefile.nmake all. and then I run the main program, there is nothing changed. but when i rebuilt all of the project .(need much more time) .the change had been write in code has appeared . why?and how to rebuilt in short time,(best for just rebuilt my plugin dissector),and then get the right result.</p><p>Hope the master give advice or comments please!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '12, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-12000" class="comments-container"></div><div id="comment-tools-12000" class="comment-tools"></div><div class="clear"></div><div id="comment-12000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12003"></span>

<div id="answer-container-12003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12003-score" class="post-score" title="current number of votes">0</div><span id="post-12003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You just compiled your code (and possibly other plugins), but you did NOT link that changed object code to the resulting binary, that's the reason why you did not see any changes.</p><p>Running make in the main directory fixed the problem, as the build process figured out, that your object code had changed and then it performed the required steps to integrate your changes into the binary. Without any further information I guess it was mostly running the linker.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12003" class="comments-container"><span id="12005"></span><div id="comment-12005" class="comment"><div id="post-12005-score" class="comment-score"></div><div class="comment-text"><p>thanks! I have get the answer.just get of the "all". is OK.</p></div><div id="comment-12005-info" class="comment-info"><span class="comment-age">(18 Jun '12, 01:45)</span> <span class="comment-user userinfo">smilezuzu</span></div></div></div><div id="comment-tools-12003" class="comment-tools"></div><div class="clear"></div><div id="comment-12003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

