+++
type = "question"
title = "How do I save one VOIP call easily?"
description = '''I use tcpdump to capture traffic from my asterisk server that has multiple simultaneous calls on it at the same time. When I use wireshark I can easily listen to one call by clicking Telephony -&amp;gt; Voip calls. But when I want to take that one call and save it as it&#x27;s own stream, I continually have ...'''
date = "2012-11-16T08:45:00Z"
lastmod = "2015-03-18T13:45:00Z"
weight = 15971
keywords = [ "voip" ]
aliases = [ "/questions/15971" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I save one VOIP call easily?](/questions/15971/how-do-i-save-one-voip-call-easily)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15971-score" class="post-score" title="current number of votes">0</div><span id="post-15971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use tcpdump to capture traffic from my asterisk server that has multiple simultaneous calls on it at the same time. When I use wireshark I can easily listen to one call by clicking Telephony -&gt; Voip calls.</p><p>But when I want to take that one call and save it as it's own stream, I continually have problems. It's not easy. I have to grab the ssrc for both calls, and create a filter and then export.... It's a PITA. Is there an easier way to do this? If not why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '12, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/ab47015051ae86b5c2868538cdd36cc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="technonick&#39;s gravatar image" /><p><span>technonick</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="technonick has no accepted answers">0%</span></p></div></div><div id="comments-container-15971" class="comments-container"></div><div id="comment-tools-15971" class="comment-tools"></div><div class="clear"></div><div id="comment-15971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15979"></span>

<div id="answer-container-15979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15979-score" class="post-score" title="current number of votes">0</div><span id="post-15979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, try this for a change. Use menu Telephono|VoIP Calls, select the call you want. Get its flow and look for the associated media flow (thick RTP marked lines). Click that line and your packet list jumps to that packet. It's the RTP stream you're looking for. Now go to menu Telephony|RTP|Stream Analysis. This shows you the analysis of the RTP stream of the call, with the option to play, save, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '12, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-15979" class="comments-container"><span id="15996"></span><div id="comment-15996" class="comment"><div id="post-15996-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap, but unfortunately that doesn't help, but thank you for trying. I'm looking to save the VOIP call data for the that individual call. What you suggested is close, but the options to save are a "raw" format and a .au format. I suspect these are audio formats. Not pcap steams. I'm trying to isolate the call in it's entirety.</p></div><div id="comment-15996-info" class="comment-info"><span class="comment-age">(16 Nov '12, 16:44)</span> <span class="comment-user userinfo">technonick</span></div></div><span id="16033"></span><div id="comment-16033" class="comment"><div id="post-16033-score" class="comment-score"></div><div class="comment-text"><p>So the question was "... and save it as its own <em>packet</em> stream,...". That's something for the wishlist or enhancement bug, I can't remember ever seeing such request. That should be a request for a "Prepare filter" on the RTP Stream Analysis window.</p></div><div id="comment-16033-info" class="comment-info"><span class="comment-age">(18 Nov '12, 22:54)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="40277"></span><div id="comment-40277" class="comment"><div id="post-40277-score" class="comment-score"></div><div class="comment-text"><p>Not really an answer but I've made a guide on doing this just in case anybody out there isn't sure:</p><p><a href="https://ask.wireshark.org/questions/40276/how-to-extract-a-voip-call-using-the-display-filter">https://ask.wireshark.org/questions/40276/how-to-extract-a-voip-call-using-the-display-filter</a></p><p>Does anybody know how we raise this as a feature request/if one has been raised?</p></div><div id="comment-40277-info" class="comment-info"><span class="comment-age">(05 Mar '15, 04:17)</span> <span class="comment-user userinfo">tarmongaidon</span></div></div><span id="40279"></span><div id="comment-40279" class="comment"><div id="post-40279-score" class="comment-score"></div><div class="comment-text"><p>I think your "question" would have been much better placed as an answer to this question or even a question of your own, then folks could have voted your answer up and other folks searching for help might have found the "answer".</p><p>To make a feature request, first check, and then if there isn't an existing item, raise a new item on the <a href="http://bugs.wireshark.org">Wireshark Bugzilla</a> marking it as an enhancement.</p></div><div id="comment-40279-info" class="comment-info"><span class="comment-age">(05 Mar '15, 04:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="40658"></span><div id="comment-40658" class="comment"><div id="post-40658-score" class="comment-score"></div><div class="comment-text"><p>Changed my question to an answer. Thanks Grahamb, I'll take a look.</p></div><div id="comment-40658-info" class="comment-info"><span class="comment-age">(18 Mar '15, 07:36)</span> <span class="comment-user userinfo">tarmongaidon</span></div></div></div><div id="comment-tools-15979" class="comment-tools"></div><div class="clear"></div><div id="comment-15979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40664"></span>

<div id="answer-container-40664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40664-score" class="post-score" title="current number of votes">0</div><span id="post-40664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://ask.wireshark.org/questions/40276/how-to-extract-a-voip-call-using-the-display-filter">https://ask.wireshark.org/questions/40276/how-to-extract-a-voip-call-using-the-display-filter</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/d84edda6d7ff1f34a88b26a9b8fbcc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tarmongaidon&#39;s gravatar image" /><p><span>tarmongaidon</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tarmongaidon has no accepted answers">0%</span></p></div></div><div id="comments-container-40664" class="comments-container"></div><div id="comment-tools-40664" class="comment-tools"></div><div class="clear"></div><div id="comment-40664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40674"></span>

<div id="answer-container-40674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40674-score" class="post-score" title="current number of votes">0</div><span id="post-40674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With pcapsipdump you can capture each call in one file. Open it afterwards with wireshark. Maybe this is a comfortable way for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/bced0dff4042b22e438a09048feadbf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voiplover&#39;s gravatar image" /><p><span>voiplover</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voiplover has no accepted answers">0%</span></p></div></div><div id="comments-container-40674" class="comments-container"></div><div id="comment-tools-40674" class="comment-tools"></div><div class="clear"></div><div id="comment-40674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

