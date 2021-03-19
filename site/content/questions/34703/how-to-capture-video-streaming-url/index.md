+++
type = "question"
title = "How to capture video streaming url?"
description = '''hi there, It has been few days I am trying to get myself familiar with wireshark. Currently I am on openSUSE and using Wireshark 1.10.8. One of the option I want to trying out it how to capture the streaming url, but failed to get things right so far. This is where the source of the video http://eng...'''
date = "2014-07-16T04:06:00Z"
lastmod = "2014-07-17T10:30:00Z"
weight = 34703
keywords = [ "streamurl" ]
aliases = [ "/questions/34703" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture video streaming url?](/questions/34703/how-to-capture-video-streaming-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34703-score" class="post-score" title="current number of votes">0</div><span id="post-34703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi there,</p><p>It has been few days I am trying to get myself familiar with wireshark. Currently I am on openSUSE and using Wireshark 1.10.8. One of the option I want to trying out it how to capture the streaming url, but failed to get things right so far.</p><p>This is where the source of the video <a href="http://english.astroawani.com/videos/live">http://english.astroawani.com/videos/live</a></p><p>I tried to follow this tutorial <a href="http://ask.wireshark.org/questions/13425/streaming-url">http://ask.wireshark.org/questions/13425/streaming-url</a> After I choose the largest file, follow TCP stream, I am still can't get the http</p><p>Thanks<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-streamurl" rel="tag" title="see questions tagged &#39;streamurl&#39;">streamurl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '14, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/ee9974706f8aeb237373346ba19190d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yazidrus&#39;s gravatar image" /><p><span>yazidrus</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yazidrus has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-34703" class="comments-container"></div><div id="comment-tools-34703" class="comment-tools"></div><div class="clear"></div><div id="comment-34703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34721"></span>

<div id="answer-container-34721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34721-score" class="post-score" title="current number of votes">2</div><span id="post-34721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Open the packet capture and filter for http.request.method == "GET"</p><p>The link will look like this: <a href="http://vdata.astroawani.com/flash/VideoPlayer.swf?v=20140715">http://vdata.astroawani.com/flash/VideoPlayer.swf?v=20140715</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '14, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-34721" class="comments-container"><span id="34722"></span><div id="comment-34722" class="comment"><div id="post-34722-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply but http.request.method == "GET" returned me into "Find text has reached the end of the followed stream,The next search will start from the beginning"</p><p>Will try again</p></div><div id="comment-34722-info" class="comment-info"><span class="comment-age">(17 Jul '14, 03:53)</span> <span class="comment-user userinfo">yazidrus</span></div></div><span id="34730"></span><div id="comment-34730" class="comment"><div id="post-34730-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you are not doing it right. Open the packet capture or take a new one. At the top were it says "Filter:" type in http.request.method == "GET" and press enter. It will only show you http get requests. After that you can select a packet and follow the tcp stream if you want.</p></div><div id="comment-34730-info" class="comment-info"><span class="comment-age">(17 Jul '14, 10:30)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-34721" class="comment-tools"></div><div class="clear"></div><div id="comment-34721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

