+++
type = "question"
title = "How do I track UDP packets from localhost?"
description = '''Greetings, Gentlemen! I am totally new to Wireshark and Networks too. Please help me to do a simple exercise. I have coded a simple UDP server-client pair according to Java tutorials: http://docs.oracle.com/javase/tutorial/networking/datagrams/clientServer.html It works. The server is running on my ...'''
date = "2013-06-19T08:37:00Z"
lastmod = "2013-06-20T09:09:00Z"
weight = 22172
keywords = [ "filter", "udp", "localhost" ]
aliases = [ "/questions/22172" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I track UDP packets from localhost?](/questions/22172/how-do-i-track-udp-packets-from-localhost)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22172-score" class="post-score" title="current number of votes">0</div><span id="post-22172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings, Gentlemen! I am totally new to Wireshark and Networks too. Please help me to do a simple exercise.</p><p>I have coded a simple UDP server-client pair according to Java tutorials: <a href="http://docs.oracle.com/javase/tutorial/networking/datagrams/clientServer.html">http://docs.oracle.com/javase/tutorial/networking/datagrams/clientServer.html</a> It works. The server is running on my machine and client too. What I want now is to track the packets I send using my fantastic software setup. How can I find them?</p><p>So here are 2 questions:</p><p>1) how can I find "my" messages?</p><p>2) how can I decode there content into normal text to be sure it is mine?<br />
</p><p>UPDATE: finally I did it! on Macos by specifying lo0 address for Wireshark. Here is a 'data' from my message I have captured.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/udp_capture.jpg" alt="alt text" /></p><p>The questions are:</p><p>1) In which format the message shown in the picture is encoded?</p><p>2) Why my message in the right column (which I suppose to be the decoded data) is split by dots and has some strange symbols before?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '13, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/cabc9ca0f4fd8402d6615ddcc7dea73f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymytry&#39;s gravatar image" /><p><span>Dymytry</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymytry has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '13, 03:09</strong> </span></p></div></div><div id="comments-container-22172" class="comments-container"></div><div id="comment-tools-22172" class="comment-tools"></div><div class="clear"></div><div id="comment-22172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22202"></span>

<div id="answer-container-22202" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22202-score" class="post-score" title="current number of votes">0</div><span id="post-22202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dymytry has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Now you've managed to capture the traffic you must use Wireshark's facilities to inspect it. According to the link you gave the server operates on udp port 4445, so you should set a <strong>capture filter</strong> of <code>udp port 4445</code>.</p><p>Having done that and captured some traffic you can inspect it. Wireshark has lots of built-in dissectors for many types of traffic, but doesn't have one for the Java test application you are using, so at best the traffic may be displayed as plain "data", and you'll just see the hex bytes, or a dissector may mistake the data for another protocol and attempt to dissect it and will fail with possible errors.</p><p>If the "data" view is sufficient then you're done, if, however, you want to have a proper protocol dissection of your traffic then you'll need to create a dissector for that. There are a few options for doing that and as it happens, that was the topic of my presentation at <a href="http://sharkfest.wireshark.org/agenda.html">SharkFest'13</a> - PA10: Writing a dissector, and the PowerPoint, capture and example dissectors will be available at the SharkFest site shortly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '13, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22202" class="comments-container"></div><div id="comment-tools-22202" class="comment-tools"></div><div class="clear"></div><div id="comment-22202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22177"></span>

<div id="answer-container-22177" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22177-score" class="post-score" title="current number of votes">0</div><span id="post-22177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What is your OS? Capturing loopback traffic is very difficult on Windows. If you are using Windows then the simplest solution will be to run the client and server on different machines.</p><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">loopback capture</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22177" class="comments-container"><span id="22192"></span><div id="comment-22192" class="comment"><div id="post-22192-score" class="comment-score"></div><div class="comment-text"><p>I have Macos Lion, but if necessary I can run the same setup at home on Windows 7.</p></div><div id="comment-22192-info" class="comment-info"><span class="comment-age">(20 Jun '13, 01:27)</span> <span class="comment-user userinfo">Dymytry</span></div></div><span id="22193"></span><div id="comment-22193" class="comment"><div id="post-22193-score" class="comment-score"></div><div class="comment-text"><p>Got it! grahamb, could you please revisit my topic for updates!</p></div><div id="comment-22193-info" class="comment-info"><span class="comment-age">(20 Jun '13, 01:52)</span> <span class="comment-user userinfo">Dymytry</span></div></div></div><div id="comment-tools-22177" class="comment-tools"></div><div class="clear"></div><div id="comment-22177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

