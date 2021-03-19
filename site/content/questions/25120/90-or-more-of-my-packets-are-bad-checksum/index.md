+++
type = "question"
title = "90% or more of my Packets are BAD CHECKSUM"
description = '''Please excuse the newbie nature of my post. I have spent a few weeks trying to &quot;Learn my way&quot; into understanding my issue. But I could use a little mentoring here. I am the &quot;Tech guy&quot; at a small operation. Whenever anyone tries to grab a a larger web page ( Or requests a series of pages in tabs) the...'''
date = "2013-09-23T09:15:00Z"
lastmod = "2013-09-23T16:47:00Z"
weight = 25120
keywords = [ "badchecksum" ]
aliases = [ "/questions/25120" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [90% or more of my Packets are BAD CHECKSUM](/questions/25120/90-or-more-of-my-packets-are-bad-checksum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25120-score" class="post-score" title="current number of votes">0</div><span id="post-25120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please excuse the newbie nature of my post. I have spent a few weeks trying to "Learn my way" into understanding my issue. But I could use a little mentoring here.</p><p>I am the "Tech guy" at a small operation. Whenever anyone tries to grab a a larger web page ( Or requests a series of pages in tabs) the network slows to a halt for everyone. We can send thru small requests: no problem. But we can't request a number of complex pages. (We get the index.html page back: but once the included CSS, js, google analytic, Olark etc are asked for. Then they just just stop)</p><p>What I have noticed when this "stop" happens is that the entire network is flooded with TCP packed with a bad Checksum.<br />
</p><p>When I examine them a number of packets have a checksum of 0X00.</p><p>My neighbors are seeing the same checksum problems on their networks.<br />
</p><p>Im pointing the finger at my ISP, But they simply come out an do a speed test (UDP!) and declare things to just be fine.</p><p>What can I do to help my poorly trained ISP techs to solve my issue? WHat am i missing/ Am I barking up the wrong tree?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-badchecksum" rel="tag" title="see questions tagged &#39;badchecksum&#39;">badchecksum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '13, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/45decaf3095d56a783c8d3036643d14c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jvmx_tx&#39;s gravatar image" /><p><span>jvmx_tx</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jvmx_tx has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-25120" class="comments-container"></div><div id="comment-tools-25120" class="comment-tools"></div><div class="clear"></div><div id="comment-25120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25122"></span>

<div id="answer-container-25122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25122-score" class="post-score" title="current number of votes">1</div><span id="post-25122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With that many CRC errors it is most likely that your procedure of capturing packets is faulty. Where do you capture the packets? If you capture them on the host sending and receiving them (kind of a "piggy backed capture") by installing Wireshark on every single system you test, you will see lots and lots of strange things like bad checksums. What is happening is that you're picking up packets that are not completely finalized before sending them out - the fact that you mention them to have a checksum of 0x00 is a typical sign here. Today's network cards do a lot of work on the packet (like calculating checksums, or segmenting the data into the correct packet sizes), which will not yet have taken place when you pick them up with Wireshark.</p><p>You should try to do a capture on a SPAN port (see the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Wiki</a>), which should show you no CRC errors because you'll pick up finalized packets at that location.</p><p>Also, try to use the I/O graph in the statistics menu to see if your bandwidth touches the maximum of whatever line speed you have bought from your ISP (don't forget to set the Y-Axis unit to "bits per tick"). If so, you're just maxing out your connection. If not, filter on tcp.analysis.flags to see if there are plenty of lost packets, retransmissions etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '13, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25122" class="comments-container"></div><div id="comment-tools-25122" class="comment-tools"></div><div class="clear"></div><div id="comment-25122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25140"></span>

<div id="answer-container-25140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25140-score" class="post-score" title="current number of votes">0</div><span id="post-25140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most of the time that I see this, it turns out that TCP Checksum off load is enabled for the Capturing NIC and I have TCP Checksum validation enabled in Wiresharek.</p><p>This issue is described / discussed in this previous answer <a href="http://ask.wireshark.org/questions/19013/ip-checksum-offload-error.">http://ask.wireshark.org/questions/19013/ip-checksum-offload-error.</a></p><p>There are 2 options that I have found. 1) disable TCP Checksum validation in Wireshark under 'Edit -&gt; Preferences -&gt; Protocols -&gt; TCP -&gt; Validate the TCP checksum if possigle' This 'Removes' the error by not validating the checksums 2) Disable TCP Checksum off load on your NIC. This "Fixes" this issue,but on heavily used interfaces you may see some performance degradation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '13, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/c89893c29e1be2a892a4bbce28d53a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="astrader&#39;s gravatar image" /><p><span>astrader</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="astrader has no accepted answers">0%</span></p></div></div><div id="comments-container-25140" class="comments-container"></div><div id="comment-tools-25140" class="comment-tools"></div><div class="clear"></div><div id="comment-25140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

