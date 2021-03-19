+++
type = "question"
title = "Wireshark 1.8.3 x64 phoning home?"
description = '''I have Wireshark 1.8.3 on two machines, one a Win7 x64 box and the other Win XP SP3 (32-bit). Between 1 and 3 times per day the Win7 X64 machine tries to connect to TCP port 61899 of www.wireshark.org (174.137.42.75). My routers firewall blocks these attempts but WTF? Is there some option to disable...'''
date = "2012-11-08T05:57:00Z"
lastmod = "2012-11-09T08:07:00Z"
weight = 15711
keywords = [ "home", "phoning" ]
aliases = [ "/questions/15711" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 1.8.3 x64 phoning home?](/questions/15711/wireshark-183-x64-phoning-home)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15711-score" class="post-score" title="current number of votes">0</div><span id="post-15711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark 1.8.3 on two machines, one a Win7 x64 box and the other Win XP SP3 (32-bit).</p><p>Between 1 and 3 times per day the Win7 X64 machine tries to connect to TCP port 61899 of <a href="http://www.wireshark.org">www.wireshark.org</a> (174.137.42.75). My routers firewall blocks these attempts but WTF?</p><p>Is there some option to disable this "phoning home"?</p><p>BTW Wireshark is NOT running during these attempts.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-home" rel="tag" title="see questions tagged &#39;home&#39;">home</span> <span class="post-tag tag-link-phoning" rel="tag" title="see questions tagged &#39;phoning&#39;">phoning</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/4321c6421d4eb0b7e3143e1319ae2d60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnnoyedOne&#39;s gravatar image" /><p><span>AnnoyedOne</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnnoyedOne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '12, 05:58</strong> </span></p></div></div><div id="comments-container-15711" class="comments-container"></div><div id="comment-tools-15711" class="comment-tools"></div><div class="clear"></div><div id="comment-15711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15714"></span>

<div id="answer-container-15714" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15714-score" class="post-score" title="current number of votes">3</div><span id="post-15714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AnnoyedOne has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>BTW Wireshark is NOT running during these attempts.</p></blockquote><p>I don't think that there is such feature in Wireshark itself (at least I cannot find anything in the source code). Furthermore: If Wireshark is not running how could it cause those requests?</p><p>Most certainly something else on your system tries to create that connection (maybe a browser).</p><p><strong>INTERESTINGLY</strong> that port (61899) is actually open on <a href="http://www.wireshark.org">www.wireshark.org</a> and if you connect to it with a browser, you will see something that's called Riverbed <strong>FlyRUM</strong>.</p><p><strong>What is this??</strong></p><p><img src="https://osqa-ask.wireshark.org/upfiles/FlyRUMsmall.png" alt="alt text" /></p><p><strong>UPDATE:</strong> It's javascript code hosted on <a href="http://www.wireshark.org">www.wireshark.org</a> that connects to that port. As soon as you browse to <a href="http://www.wireshark.org">www.wireshark.org</a>, the script in your browser tries to establish a connection to that port. So, my first assumption (see above) was right.</p><p>So, <strong>NO</strong> Wireshark is <strong>NOT phoning home</strong>!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '12, 07:11</strong> </span></p></div></div><div id="comments-container-15714" class="comments-container"><span id="15717"></span><div id="comment-15717" class="comment"><div id="post-15717-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that.</p><p><a href="http://www.wireshark.org:61899/beacon/1x1.gif">http://www.wireshark.org:61899/beacon/1x1.gif</a></p><p>That'll be (silently) blocked once I post this.</p></div><div id="comment-15717-info" class="comment-info"><span class="comment-age">(08 Nov '12, 06:39)</span> <span class="comment-user userinfo">AnnoyedOne</span></div></div><span id="15718"></span><div id="comment-15718" class="comment"><div id="post-15718-score" class="comment-score"></div><div class="comment-text"><p>looks like a tracking/web bug.</p></div><div id="comment-15718-info" class="comment-info"><span class="comment-age">(08 Nov '12, 06:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15734"></span><div id="comment-15734" class="comment"><div id="post-15734-score" class="comment-score"></div><div class="comment-text"><p>Yup. That bug is now "squashed" :-)</p></div><div id="comment-15734-info" class="comment-info"><span class="comment-age">(08 Nov '12, 09:03)</span> <span class="comment-user userinfo">AnnoyedOne</span></div></div></div><div id="comment-tools-15714" class="comment-tools"></div><div class="clear"></div><div id="comment-15714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15737"></span>

<div id="answer-container-15737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15737-score" class="post-score" title="current number of votes">0</div><span id="post-15737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Current and past versions of Wireshark shouldn't phone home on their own. A future version might do so if we ever get around to adding a "check for updates" feature.</p><p>The connections to <a href="http://www.wireshark.org:61899">www.wireshark.org:61899</a> and the page that Kurt found are for upcoming Riverbed product enhancements (called FlyScript) that a team is working on inside Riverbed. They needed a real-world environment for testing and I agreed to let them use the Wireshark web servers. They aren't quite ready for public consumption and a team of sharks equipped with lasers will be visiting Kurt momentarily.</p><p>As The 1x1.gif URL implies, it's a beacon used to measure the performance of connections to <a href="http://www.wireshark.org">www.wireshark.org</a>. It isn't used to track visits beyond <a href="http://www.wireshark.org">www.wireshark.org</a> and it's not really accurate to call it a tracking/web bug. I use Google Analytics on the various <a href="http://wireshark.org">wireshark.org</a> sites and have used WebTuna in the past. Both use "web bugs" in the traditional sense.</p><p><span><span>@AnnoyedOne</span></span> Can you confirm whether or not you had <a href="http://www.wireshark.org">www.wireshark.org</a> open in a browser when the connection to <a href="http://www.wireshark.org:61899">www.wireshark.org:61899</a>? It might be helpful to the team developing the new feature set.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '12, 10:42</strong> </span></p></div></div><div id="comments-container-15737" class="comments-container"><span id="15746"></span><div id="comment-15746" class="comment"><div id="post-15746-score" class="comment-score">1</div><div class="comment-text"><p>no time... sharks everywhere ... two of them eliminated ... fire, fire!</p><p>see you tomorrow.. HOPEFULLY !!!</p></div><div id="comment-15746-info" class="comment-info"><span class="comment-age">(08 Nov '12, 18:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15775"></span><div id="comment-15775" class="comment"><div id="post-15775-score" class="comment-score"></div><div class="comment-text"><p><span>@Gerald Combs</span></p><p>It took me a few days of Googling etc to figure out, thanks to Kurt, that it was the Wireshark website trying to use port 61899. It was difficult to determine that because my router is configured to send me warning email when something attempts to use a non-standard and/or non-allowed port. Those log only told me what machine was sending the requests not what process/webpage etc.</p><p>I've now configure my router to silently drop all <a href="http://www.wireshark.org:61899">www.wireshark.org:61899</a> attempts.</p><p>Please allow any auto-update feature to be disabled. And I mean off-entirely. No phoning home.</p></div><div id="comment-15775-info" class="comment-info"><span class="comment-age">(09 Nov '12, 08:07)</span> <span class="comment-user userinfo">AnnoyedOne</span></div></div></div><div id="comment-tools-15737" class="comment-tools"></div><div class="clear"></div><div id="comment-15737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

