+++
type = "question"
title = "Statistics--&gt;Service Response Time--&gt;Diameter works?"
description = '''Hello, I am using Wireshark version - 1.10.7 and I want find out response time of diameter requests. I have seen that some perl script can be used for that. But I also see that in wireshark there is an option Statistics--&amp;gt;Service Response Time--&amp;gt;Diameter to get the service response time of the...'''
date = "2014-04-24T22:59:00Z"
lastmod = "2014-04-28T08:12:00Z"
weight = 32168
keywords = [ "diameter", "response", "time" ]
aliases = [ "/questions/32168" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Statistics--&gt;Service Response Time--&gt;Diameter works?](/questions/32168/statistics-service-response-time-diameter-works)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32168-score" class="post-score" title="current number of votes">0</div><span id="post-32168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am using Wireshark version - 1.10.7 and I want find out response time of diameter requests. I have seen that some perl script can be used for that.</p><p>But I also see that in wireshark there is an option Statistics--&gt;Service Response Time--&gt;Diameter to get the service response time of the diameter requests along with other protocols.</p><p>I want to know if this is really working. As the Wireshark documentation says,</p><p>Service response time statistics are currently available for some of the protocols listen in the help.</p><p>But when I use this features, I am able to get service response time but not sure if its correct.</p><p>Can any one help me out with this please?? Statistics--&gt;Service Response Time--&gt;Diameter is really supported?</p><p>Thanks, vidhi.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '14, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/b794b90289cddde7dadc03e91012c605?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vidhi&#39;s gravatar image" /><p><span>Vidhi</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vidhi has no accepted answers">0%</span></p></div></div><div id="comments-container-32168" class="comments-container"></div><div id="comment-tools-32168" class="comment-tools"></div><div class="clear"></div><div id="comment-32168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32209"></span>

<div id="answer-container-32209" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32209-score" class="post-score" title="current number of votes">2</div><span id="post-32209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vidhi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I use this all the time. It's available not only through the GUI, but also through the 'tshark' command line. An entry like this will give you the response time of all the request/answer exchanges, for example. You can adjust the -R display filter if you want to tune it to an application or command type, and you can pipe this to any utility you want to work with the numbers:</p><p><code>tshark -r {capture file} -R 'diameter.flags.request==0' -T fields -e diameter.resp_time</code></p><p>I have eye-balled the response time values of Wireshark version 1.8.6 at least, countless times now for unbelievers and the values have always appeared to be accurate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 17:26</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '14, 17:27</strong> </span></p></div></div><div id="comments-container-32209" class="comments-container"><span id="32229"></span><div id="comment-32229" class="comment"><div id="post-32229-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Quadratic! it has saved lots of my effort!</p></div><div id="comment-32229-info" class="comment-info"><span class="comment-age">(27 Apr '14, 22:48)</span> <span class="comment-user userinfo">Vidhi</span></div></div><span id="32256"></span><div id="comment-32256" class="comment"><div id="post-32256-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-32256-info" class="comment-info"><span class="comment-age">(28 Apr '14, 08:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32209" class="comment-tools"></div><div class="clear"></div><div id="comment-32209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32196"></span>

<div id="answer-container-32196" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32196-score" class="post-score" title="current number of votes">1</div><span id="post-32196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I did a test with a small diameter capture file and I would say the service response times are reasonable. So, to me it looks like the diameter srt stats are working properly.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32196" class="comments-container"><span id="32230"></span><div id="comment-32230" class="comment"><div id="post-32230-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your reapose Kurt Knochner!</p></div><div id="comment-32230-info" class="comment-info"><span class="comment-age">(27 Apr '14, 22:48)</span> <span class="comment-user userinfo">Vidhi</span></div></div></div><div id="comment-tools-32196" class="comment-tools"></div><div class="clear"></div><div id="comment-32196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

