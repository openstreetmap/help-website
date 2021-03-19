+++
type = "question"
title = "Mac OS X 1.99.9 Follow TCP Stream - &quot;Raw&quot; format Not Available for Save as"
description = '''Hello- Using the latest development version for Mac OS X which does NOT require x-windows ie 1.99.9. When I follow a tcp stream and want to save the data, there is no &quot;Raw&quot; format available, only:  The below documentation for version 1.99.9 indicates it should be available. Am I missing something? I...'''
date = "2015-09-07T18:24:00Z"
lastmod = "2015-09-08T13:35:00Z"
weight = 45684
keywords = [ "raw", "follow.tcp.stream", "mac.os.x" ]
aliases = [ "/questions/45684" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS X 1.99.9 Follow TCP Stream - "Raw" format Not Available for Save as](/questions/45684/mac-os-x-1999-follow-tcp-stream-raw-format-not-available-for-save-as)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45684-score" class="post-score" title="current number of votes">0</div><span id="post-45684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello-</p><p>Using the latest development version for Mac OS X which does NOT require x-windows ie 1.99.9. When I follow a tcp stream and want to save the data, there is no "Raw" format available, only:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/show-sata-as-format.jpg" alt="alt text" /></p><p>The below documentation for version 1.99.9 indicates it should be available. Am I missing something? Is "raw" going to be available in a future release? Is there something I can do in the mean time to be able to save it in "raw" format?<br />
</p><p>The doc below still has the x-windows look in the images rather than the normal Mac GUI.</p><p><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowTCPSection.html">https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowTCPSection.html</a></p><p>7.2. Following TCP streams</p><p>If you are working with TCP based protocols it can be very helpful to see the data from a TCP stream in the way that the application layer sees it. Perhaps you are looking for passwords in a Telnet stream, or you are trying to make sense of a data stream. Maybe you just need a display filter to show only the packets of that TCP stream. If so, Wireshark’s ability to follow a TCP stream will be useful to you.</p><p>Simply select a TCP packet in the packet list of the stream/connection you are interested in and then select the Follow TCP Stream menu item from the Wireshark Tools menu (or use the context menu in the packet list). Wireshark will set an appropriate display filter and pop up a dialog box with all the data from the TCP stream laid out in order, as shown in Figure 7.1, “The “Follow TCP Stream” dialog box”.</p><p>[Note] Note Opening the “Follow TCP Stream” installs a display filter to select all the packets in the TCP stream you have selected.</p><p>7.2.1. The “Follow TCP Stream” dialog box</p><p>Figure 7.1. The “Follow TCP Stream” dialog box wsug_graphics/ws-follow-stream.png</p><p>The stream content is displayed in the same sequence as it appeared on the network. Traffic from A to B is marked in red, while traffic from B to A is marked in blue. If you like, you can change these colors in the “Colors” page if the “Preferences” dialog.</p><p>Non-printable characters will be replaced by dots.</p><p>The stream content won’t be updated while doing a live capture. To get the latest content you’ll have to reopen the dialog.</p><p>You can choose from the following actions:</p><p>Save As: Save the stream data in the currently selected format. Print: Print the stream data in the currently selected format. Direction: Choose the stream direction to be displayed (“Entire conversation”, “data from A to B only” or “data from B to A only”). Filter out this stream: Apply a display filter removing the current TCP stream data from the display. Close: Close this dialog box, leaving the current display filter in effect. You can choose to view the data in one of the following formats:</p><p>ASCII: In this view you see the data from each direction in ASCII. Obviously best for ASCII based protocols, e.g. HTTP. EBCDIC: For the big-iron freaks out there. HEX Dump: This allows you to see all the data. This will require a lot of screen space and is best used with binary protocols. C Arrays: This allows you to import the stream data into your own C program. Raw: This allows you to load the unaltered stream data into a different program for further examination. The display will look the same as the ASCII setting, but “Save As” will result in a binary file.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-raw" rel="tag" title="see questions tagged &#39;raw&#39;">raw</span> <span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span> <span class="post-tag tag-link-mac.os.x" rel="tag" title="see questions tagged &#39;mac.os.x&#39;">mac.os.x</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '15, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/63df608f94c34d0cb6d199eadec36269?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="securitysam&#39;s gravatar image" /><p><span>securitysam</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="securitysam has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-45684" class="comments-container"></div><div id="comment-tools-45684" class="comment-tools"></div><div class="clear"></div><div id="comment-45684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45691"></span>

<div id="answer-container-45691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45691-score" class="post-score" title="current number of votes">1</div><span id="post-45691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is already tracked by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11118">bug 11118</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-45691" class="comments-container"><span id="45713"></span><div id="comment-45713" class="comment"><div id="post-45713-score" class="comment-score"></div><div class="comment-text"><p>Well at least is is on the record as being missing then. Thanks!</p></div><div id="comment-45713-info" class="comment-info"><span class="comment-age">(08 Sep '15, 12:32)</span> <span class="comment-user userinfo">securitysam</span></div></div></div><div id="comment-tools-45691" class="comment-tools"></div><div class="clear"></div><div id="comment-45691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45711"></span>

<div id="answer-container-45711" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45711-score" class="post-score" title="current number of votes">0</div><span id="post-45711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A quick look at the code suggests that the Qt version may have renamed the option from "Raw" to "UTF-8". Try that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '15, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45711" class="comments-container"><span id="45712"></span><div id="comment-45712" class="comment"><div id="post-45712-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy, that was the first thing I tried. Unfortunately, I'm trying to extract a base64 encoded pdf from a pcap and saving it in UTF-8 does not allow the base64 -d command to decode it properly and it does not have the proper format for a pdf. The Linux version which still has the RAW format available does come out properly.</p></div><div id="comment-45712-info" class="comment-info"><span class="comment-age">(08 Sep '15, 12:31)</span> <span class="comment-user userinfo">securitysam</span></div></div><span id="45715"></span><div id="comment-45715" class="comment"><div id="post-45715-score" class="comment-score"></div><div class="comment-text"><p>It's not "Linux vs. OS X", it's "GTK+ vs. Qt" - the Linux Qt version won't have it either.</p></div><div id="comment-45715-info" class="comment-info"><span class="comment-age">(08 Sep '15, 12:43)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="45717"></span><div id="comment-45717" class="comment"><div id="post-45717-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the correction, and my apologies for using incorrect terminology; by Linux I meant GTK+ as I don't run, nor did I know until now, that it was possible to run Qt on Linux. When I wrote the reply I was in a bit of a rush, and could not recall the full acronym for GTK (I was thinking GT, but it didn't sound right, so I went with Linux).</p></div><div id="comment-45717-info" class="comment-info"><span class="comment-age">(08 Sep '15, 13:14)</span> <span class="comment-user userinfo">securitysam</span></div></div><span id="45718"></span><div id="comment-45718" class="comment"><div id="post-45718-score" class="comment-score"></div><div class="comment-text"><p>The current official releases are GTK+ on all OSes, which is GTK+-on-X11 on OS X. The intent is that the 2.0 release will be Qt on all OSes, without require X11 on OS X.</p></div><div id="comment-45718-info" class="comment-info"><span class="comment-age">(08 Sep '15, 13:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-45711" class="comment-tools"></div><div class="clear"></div><div id="comment-45711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

