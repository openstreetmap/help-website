+++
type = "question"
title = "How can i know how much time it took to file to get downloaded with wireshark."
description = '''HI all , I downloaded a file and in wireshark i saw the GET request of the filename , i want to know how much time it took to the file to get downloaded to my computer . How can i see that throw wireshark , can anyone please help me ? '''
date = "2013-03-05T07:16:00Z"
lastmod = "2013-03-07T02:51:00Z"
weight = 19152
keywords = [ "download", "timestamp" ]
aliases = [ "/questions/19152" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can i know how much time it took to file to get downloaded with wireshark.](/questions/19152/how-can-i-know-how-much-time-it-took-to-file-to-get-downloaded-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19152-score" class="post-score" title="current number of votes">1</div><span id="post-19152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI all ,</p><p>I downloaded a file and in wireshark i saw the GET request of the filename , i want to know how much time it took to the file to get downloaded to my computer . How can i see that throw wireshark ,</p><p>can anyone please help me ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '13, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/7546a5dc6967574e6c3c9923ace6240e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alon%20Fox&#39;s gravatar image" /><p><span>Alon Fox</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alon Fox has no accepted answers">0%</span></p></div></div><div id="comments-container-19152" class="comments-container"></div><div id="comment-tools-19152" class="comment-tools"></div><div class="clear"></div><div id="comment-19152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19156"></span>

<div id="answer-container-19156" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19156-score" class="post-score" title="current number of votes">3</div><span id="post-19156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alon Fox has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are several ways to do that, depending on the accuracy you need.</p><p><strong>most accurate method</strong></p><ul><li>find the HTTP GET that requests the file. Filter: <code>http.request.uri contains file.exe</code></li><li>right click that packet and select "Follow TCP Stream"</li><li>then find the first data packet (from the server) in that stream, that belongs to the specific GET request. Please remember how HTTP/1.1 works. There may be several consecutive requests in one TCP connection. The response data from the server (downloaded content) will appear in the same order.</li><li>set a time reference on that packet (CTRL-T)</li><li>Find the last data packet that belongs to that download (the one with 'HTTP/1.x 200 OK' in the info column)</li><li>The time you see for that packet in the Time column, is your 'download time'</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19156" class="comments-container"></div><div id="comment-tools-19156" class="comment-tools"></div><div class="clear"></div><div id="comment-19156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19257"></span>

<div id="answer-container-19257" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19257-score" class="post-score" title="current number of votes">0</div><span id="post-19257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you just need an approximate number fast in a capture where the flow you care about is the biggest one: Go to Statistics -&gt; Conversation List -&gt; TCP, click the "Bytes" column twice to sort decreasing, and then look at the "Duration" value for the top row.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '13, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/f1f99b071794213796dcb33e787c5772?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakslice&#39;s gravatar image" /><p><span>rakslice</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakslice has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Mar '13, 18:56</strong> </span></p></div></div><div id="comments-container-19257" class="comments-container"><span id="19268"></span><div id="comment-19268" class="comment"><div id="post-19268-score" class="comment-score"></div><div class="comment-text"><p>That will <strong>not</strong> show the download time of a <strong>single</strong> object <strong>if HTTP/1.1 was used</strong>. It will show the duration of the TCP connection which could have been used to download several objects!</p></div><div id="comment-19268-info" class="comment-info"><span class="comment-age">(07 Mar '13, 02:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-19257" class="comment-tools"></div><div class="clear"></div><div id="comment-19257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

