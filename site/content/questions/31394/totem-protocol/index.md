+++
type = "question"
title = "Totem Protocol"
description = '''My Wireshark doesn&#x27;t decode Totem Protocol, Totem doesn&#x27;t exit in protocols under Analyze --&amp;gt; &quot;Decode As&quot;.  Any ideas how do I view it (any known plugins ... etc)?'''
date = "2014-04-02T07:39:00Z"
lastmod = "2014-04-02T09:53:00Z"
weight = 31394
keywords = [ "plugin" ]
aliases = [ "/questions/31394" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Totem Protocol](/questions/31394/totem-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31394-score" class="post-score" title="current number of votes">0</div><span id="post-31394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Wireshark doesn't decode Totem Protocol, Totem doesn't exit in protocols under Analyze --&gt; "Decode As". Any ideas how do I view it (any known plugins ... etc)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/1eb1a96fa00cc1af851c399e9173be58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim_Zhang&#39;s gravatar image" /><p><span>Jim_Zhang</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim_Zhang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Apr '14, 08:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-31394" class="comments-container"></div><div id="comment-tools-31394" class="comment-tools"></div><div class="clear"></div><div id="comment-31394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31396"></span>

<div id="answer-container-31396" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31396-score" class="post-score" title="current number of votes">2</div><span id="post-31396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a current Gerrit <a href="https://code.wireshark.org/review/#/c/725/">change</a> in progress for <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3232">bug 3232</a> that adds totemnet and totemsrp. Are they the same things as you are looking for, or am I barking up the wrong pole.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31396" class="comments-container"><span id="31402"></span><div id="comment-31402" class="comment"><div id="post-31402-score" class="comment-score"></div><div class="comment-text"><p>Thats exactly what i am looking for. But am new to the world of wireshark (amongst many other things:) ). So was wondering, when do we expect to be part of wireshark, any ideas?</p></div><div id="comment-31402-info" class="comment-info"><span class="comment-age">(02 Apr '14, 09:37)</span> <span class="comment-user userinfo">Jim_Zhang</span></div></div><span id="31405"></span><div id="comment-31405" class="comment"><div id="post-31405-score" class="comment-score"></div><div class="comment-text"><p>The change has to be approved by core developers, which may take some rework, then it will be merged.</p><p>At that point you can then grab an automated pre-built binary, if there is one for your platform, or attempt to build it yourself using the source code.</p><p>It will eventually appear in the next "release" version of Wireshark at some future date, probably before June if the change is approved.</p><p>If you are really desperate, you could also just grab the change from Gerrit and build it yourself now. Note that this may not work correctly as the change might be in a broken state, but feedback about that would help.</p></div><div id="comment-31405-info" class="comment-info"><span class="comment-age">(02 Apr '14, 09:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-31396" class="comment-tools"></div><div class="clear"></div><div id="comment-31396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

