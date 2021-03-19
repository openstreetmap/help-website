+++
type = "question"
title = "can&#x27;t find rtmp from this stream"
description = '''hey i use wireshark to find the rtmp and i dont find it. in this site :  http://www.goalim4u.site/p/2_28.html there is live video streaming how i use wireshark to find the rtmp that can work if i play it here:  http://www.vlc.eu.pn/ (enter this site with firefox) can someone help me ...'''
date = "2015-12-15T09:07:00Z"
lastmod = "2015-12-15T15:32:00Z"
weight = 48538
keywords = [ "wireshark" ]
aliases = [ "/questions/48538" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can't find rtmp from this stream](/questions/48538/cant-find-rtmp-from-this-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48538-score" class="post-score" title="current number of votes">0</div><span id="post-48538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey i use wireshark to find the rtmp and i dont find it. in this site : <a href="http://www.goalim4u.site/p/2_28.html">http://www.goalim4u.site/p/2_28.html</a> there is live video streaming how i use wireshark to find the rtmp that can work if i play it here: <a href="http://www.vlc.eu.pn/">http://www.vlc.eu.pn/</a> (enter this site with firefox)</p><p>can someone help me ...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/f938321e77a154b0e2732cda009bdd7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="israel&#39;s gravatar image" /><p><span>israel</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="israel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '15, 12:06</strong> </span></p></div></div><div id="comments-container-48538" class="comments-container"></div><div id="comment-tools-48538" class="comment-tools"></div><div class="clear"></div><div id="comment-48538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48550"></span>

<div id="answer-container-48550" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48550-score" class="post-score" title="current number of votes">0</div><span id="post-48550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot find it because it is not using the default port. The rtmp is there but because it uses tcp port 80 at server side, Wireshark dissects it as http. It is enough to choose any packet of that tcp session in the captured file, right-click it, choose "Decode as" from the context menu, and choose "rtmpt" in the rightmost column. However, I assume it won't help you much to watch the game for free as I believe that the banner hiding the middle of the picture is put there already at the sending side. And VLC does not seem to ask for the stream properly - the negotiation is part of the rtmp as you'll be able to see if you first start the capture and only then open the <a href="http://deltatv.co/stream.php?id=144991&amp;width=660&amp;height=390">real link</a> to the stream in a browser. Something is telling me that you'd have to provide the right keyword so that deltatv would be sending you the picture without the banner.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '15, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48550" class="comments-container"><span id="48552"></span><div id="comment-48552" class="comment"><div id="post-48552-score" class="comment-score"></div><div class="comment-text"><p>thanks you... i need the direct link to stream to kodi addons there is a way to get it form deltatv? with other software?</p></div><div id="comment-48552-info" class="comment-info"><span class="comment-age">(15 Dec '15, 15:32)</span> <span class="comment-user userinfo">israel</span></div></div></div><div id="comment-tools-48550" class="comment-tools"></div><div class="clear"></div><div id="comment-48550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

