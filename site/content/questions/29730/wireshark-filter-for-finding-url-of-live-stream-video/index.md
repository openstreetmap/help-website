+++
type = "question"
title = "wireshark filter for finding url of live stream video"
description = '''I have an url: http://www.mayapur.tv/newTemples/index.php?stream=Chowpatty/@Chowpatty If i open in the browser it shows the the streaming video. I cant get the url of the stream video from the http headers or the html code. I there any way to find the address of the streamvideo comming using wiresha...'''
date = "2014-02-11T22:15:00Z"
lastmod = "2014-02-13T15:05:00Z"
weight = 29730
keywords = [ "livecapturetcp" ]
aliases = [ "/questions/29730" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark filter for finding url of live stream video](/questions/29730/wireshark-filter-for-finding-url-of-live-stream-video)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29730-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an url: <a href="http://www.mayapur.tv/newTemples/index.php?stream=Chowpatty/@Chowpatty">http://www.mayapur.tv/newTemples/index.php?stream=Chowpatty/@Chowpatty</a></p><p>If i open in the browser it shows the the streaming video. I cant get the url of the stream video from the http headers or the html code.</p><p>I there any way to find the address of the streamvideo comming using wireshark. I dont know how to check tcp things in wireshark</p></div><div id="question-tags" class="tags-container tags">livecapturetcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 22:15</strong></p><img src="https://secure.gravatar.com/avatar/ac549b7ce4f69e6ab255a137107c506b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Santhosh&#39;s gravatar image" /><p>Santhosh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Santhosh has no accepted answers">0%</span></p></div></div><div id="comments-container-29730" class="comments-container"></div><div id="comment-tools-29730" class="comment-tools"></div><div class="clear"></div><div id="comment-29730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29848"></span>

<div id="answer-container-29848" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29848-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I there any way to find the address of the streamvideo comming using wireshark.</p></blockquote><p>sure.</p><ul><li>start Wireshark capture</li><li>load the video and let it play for 30 seconds</li><li>stop Wireshark capture</li><li>Load statistics: Statistics -&gt; Conversations -&gt; TCP [Tab]</li><li>sort the list of connections and find the connection with the longest duration or max. bytes transferred</li><li>get the destination ip address</li><li>filter for <strong><code>dns</code></strong> in wireshark and find the request that matches the IP address. <strong>Hint:</strong> this step will only work if the client has <strong>not cached</strong> the DNS response from an earlier request!</li><li>take that name and build a filter like this: <strong><code>frame contains mtvnyc.dyndns.tv</code></strong></li><li>you will find some RTMP connections. Look for <span>rtmp://mtvnyc.dyndns.tv/xxxxx</span> in those frames to get the full URL</li></ul><p>Done.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '14, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '14, 15:13</p></div></div><div id="comments-container-29848" class="comments-container"><span id="37348"></span><div id="comment-37348" class="comment"><div id="post-37348-score" class="comment-score"></div><div class="comment-text"><p>Hi, I just would like to say thank you very much to Kurt. I start to study video streams in the end of 2011 and since today I never saw an explanation about how we can get adress of a streamvideo using Wireshark. I'd learn some today, so thanks again regards Roberto Diaz</p></div><div id="comment-37348-info" class="comment-info"><span class="comment-age">(26 Oct '14, 07:00)</span> cenahum</div></div><span id="37356"></span><div id="comment-37356" class="comment"><div id="post-37356-score" class="comment-score"></div><div class="comment-text"><p>you're welcome!</p></div><div id="comment-37356-info" class="comment-info"><span class="comment-age">(26 Oct '14, 15:28)</span> Kurt Knochner ♦</div></div><span id="41471"></span><div id="comment-41471" class="comment"><div id="post-41471-score" class="comment-score"></div><div class="comment-text"><p>I'm getting frames but how do I find the entry point? These seem to be chunks of .mp4 but there must be some index or entry point url.</p></div><div id="comment-41471-info" class="comment-info"><span class="comment-age">(15 Apr '15, 20:48)</span> John Doyle</div></div></div><div id="comment-tools-29848" class="comment-tools"></div><div class="clear"></div><div id="comment-29848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

