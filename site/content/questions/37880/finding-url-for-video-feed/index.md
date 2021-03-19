+++
type = "question"
title = "Finding URL for Video Feed"
description = '''I&#x27;m trying to find the source URL for a video feed. When I view the image information, I&#x27;ll see a URL such as: http://img7.insecam.com:8080/NNNNNN/0/nocache/ where NNNNNN is presumably some internal number assigned to the feed. Can anyone give me step by step instructions using Wireshark to find the...'''
date = "2014-11-15T10:56:00Z"
lastmod = "2014-11-17T16:08:00Z"
weight = 37880
keywords = [ "videostream" ]
aliases = [ "/questions/37880" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Finding URL for Video Feed](/questions/37880/finding-url-for-video-feed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37880-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to find the source URL for a video feed. When I view the image information, I'll see a URL such as:</p><p><a href="http://img7.insecam.com:8080/NNNNNN/0/nocache/">http://img7.insecam.com:8080/NNNNNN/0/nocache/</a> where NNNNNN is presumably some internal number assigned to the feed.</p><p>Can anyone give me step by step instructions using Wireshark to find the original source URL that the feed is coming from?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">videostream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '14, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/d0e1b5c584e73c262754bf8df14f4873?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jr2468&#39;s gravatar image" /><p>jr2468<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jr2468 has no accepted answers">0%</span></p></div></div><div id="comments-container-37880" class="comments-container"></div><div id="comment-tools-37880" class="comment-tools"></div><div class="clear"></div><div id="comment-37880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37920"></span>

<div id="answer-container-37920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37920-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>see my answers for a similar questions:</p><blockquote><p><a href="https://ask.wireshark.org/questions/29730/wireshark-filter-for-finding-url-of-live-stream-video">https://ask.wireshark.org/questions/29730/wireshark-filter-for-finding-url-of-live-stream-video</a><br />
<a href="https://ask.wireshark.org/questions/13425/streaming-url">https://ask.wireshark.org/questions/13425/streaming-url</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Nov '14, 16:09</p></div></div><div id="comments-container-37920" class="comments-container"><span id="37923"></span><div id="comment-37923" class="comment"><div id="post-37923-score" class="comment-score"></div><div class="comment-text"><p>Kurt, Firstly, thank you for the help.<br />
</p><p>I found those 2 threads previously, but I run into trouble at the "filter for dns in wireshark and find the request that matches the IP address." step. When I filter for DNS, none of the IPs that come back match the destination IP associated with the largest number of bytes from the prior step.</p></div><div id="comment-37923-info" class="comment-info"><span class="comment-age">(17 Nov '14, 16:37)</span> jr2468</div></div><span id="37927"></span><div id="comment-37927" class="comment"><div id="post-37927-score" class="comment-score"></div><div class="comment-text"><p>did you clear the DNS cache on the client, before you started capturing?</p><blockquote><p>ipconfig /flushdns</p></blockquote></div><div id="comment-37927-info" class="comment-info"><span class="comment-age">(17 Nov '14, 17:34)</span> Kurt Knochner ♦</div></div><span id="37954"></span><div id="comment-37954" class="comment"><div id="post-37954-score" class="comment-score"></div><div class="comment-text"><p>I did and still no luck. If it’s not too much to ask, could you run through an example using this URL:</p><p><a href="http://www.insecam.cc/cam/view/106106/">http://www.insecam.cc/cam/view/106106/</a></p><p>Again, appreciate the help.</p></div><div id="comment-37954-info" class="comment-info"><span class="comment-age">(18 Nov '14, 16:21)</span> jr2468</div></div><span id="37972"></span><div id="comment-37972" class="comment"><div id="post-37972-score" class="comment-score"></div><div class="comment-text"><p>There is no video feed. It's a javascript repload a certain link (you posted that already in your question) to get a refreshed image of the camera!</p><p>Maybe I'm misunderstanding your request. What is it your are actually asking for? The link? Well, then you already have it.</p></div><div id="comment-37972-info" class="comment-info"><span class="comment-age">(19 Nov '14, 09:20)</span> Kurt Knochner ♦</div></div><span id="37985"></span><div id="comment-37985" class="comment"><div id="post-37985-score" class="comment-score"></div><div class="comment-text"><p>No, I'm looking for the original IP address of the video feed, In other words, where is that website getting the feed from.</p></div><div id="comment-37985-info" class="comment-info"><span class="comment-age">(19 Nov '14, 16:30)</span> jr2468</div></div><span id="37998"></span><div id="comment-37998" class="comment not_top_scorer"><div id="post-37998-score" class="comment-score"></div><div class="comment-text"><p>As I mentioned, the is no <strong>video feed</strong> and the site the images get loaded is the one you mentioned in your question.</p></div><div id="comment-37998-info" class="comment-info"><span class="comment-age">(20 Nov '14, 01:31)</span> Kurt Knochner ♦</div></div><span id="38012"></span><div id="comment-38012" class="comment not_top_scorer"><div id="post-38012-score" class="comment-score"></div><div class="comment-text"><p>Again, thanks for the help.<br />
</p><p>IP Camera --&gt; Website/java--&gt; me</p><p>This website, like shodan, searches for open IP cameras. I was hoping that by examining the java reload using wireshark, I could determine the IP address of the camera that the website found in its search.</p></div><div id="comment-38012-info" class="comment-info"><span class="comment-age">(20 Nov '14, 02:59)</span> jr2468</div></div><span id="38013"></span><div id="comment-38013" class="comment not_top_scorer"><div id="post-38013-score" class="comment-score"></div><div class="comment-text"><p>@jr2468</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-38013-info" class="comment-info"><span class="comment-age">(20 Nov '14, 03:14)</span> grahamb ♦</div></div><span id="38029"></span><div id="comment-38029" class="comment not_top_scorer"><div id="post-38029-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I was hoping that by examining the java reload using wireshark, I could determine the IP address of the camera that the website found in its search.</p></blockquote><p>That's not possible, because they load the images from their own servers. Unless they tell you where they got it from (IP address of the camera), there is no way for you to retrieve that information.</p></div><div id="comment-38029-info" class="comment-info"><span class="comment-age">(20 Nov '14, 10:40)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37920" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-37920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

