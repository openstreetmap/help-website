+++
type = "question"
title = "packetizing the data"
description = '''Hi all, I am working to implement a protocol dissector in wireshark. I have the sample data of this protocol in some format which has data in the form of continuous bits not packets. Now to import this sample data and dissector I am planning to convert this data file into .pcap format. But now the p...'''
date = "2012-02-01T10:03:00Z"
lastmod = "2012-02-02T02:11:00Z"
weight = 8750
keywords = [ "packets" ]
aliases = [ "/questions/8750" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [packetizing the data](/questions/8750/packetizing-the-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8750-score" class="post-score" title="current number of votes">0</div><span id="post-8750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am working to implement a protocol dissector in wireshark. I have the sample data of this protocol in some format which has data in the form of continuous bits not packets. Now to import this sample data and dissector I am planning to convert this data file into .pcap format. But now the problem is that in .pcap format, there are packets of data. But the data file I am having doesn't contains information in packets form. It just contains the data in form of bits as it comes on the bus.</p><p>How shall I proceed? Does wireshark supports any such kind of concept of making packets from bits coming.</p><p>P.S : To form the packets from my sample data file. I will have to see when <strong>Start of packet</strong> arrives and when <strong>end of packet</strong> and packetize the whole data between these two packets.</p><p><strong>Update :</strong> Now that I have written a tool to convert my data into .pcap format. How to proceed with the writing my protocol for decoding that data and How wireshark will know which protocol to use to decode the the content of this .pcap file??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p><span>ashish_goel</span><br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Feb '12, 19:18</strong> </span></p></div></div><div id="comments-container-8750" class="comments-container"></div><div id="comment-tools-8750" class="comment-tools"></div><div class="clear"></div><div id="comment-8750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8752"></span>

<div id="answer-container-8752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8752-score" class="post-score" title="current number of votes">1</div><span id="post-8752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One way:</p><p>Write s program to convert your data into a (packetized) format which can be read by text2pcap. text2pcap is a Wireshark tool: See the <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">test2pcap man page</a>.</p><p>See <a href="http://wiki.wireshark.org/HowToDissectAnything">How to dissect anything</a> for the details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '12, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-8752" class="comments-container"><span id="8765"></span><div id="comment-8765" class="comment"><div id="post-8765-score" class="comment-score"></div><div class="comment-text"><p>thanks for the reply bill.</p><p>But a confusion. Why do I need the test2pcap tool in between. If I have to write a tool at first to packetize data then I can write the complete tool converting my data file to .pcap format directly.</p></div><div id="comment-8765-info" class="comment-info"><span class="comment-age">(01 Feb '12, 22:12)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8767"></span><div id="comment-8767" class="comment"><div id="post-8767-score" class="comment-score"></div><div class="comment-text"><p>You are correct. Have your packet framer write out a pcap file straight away, easy enough.</p></div><div id="comment-8767-info" class="comment-info"><span class="comment-age">(01 Feb '12, 23:34)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="8771"></span><div id="comment-8771" class="comment"><div id="post-8771-score" class="comment-score"></div><div class="comment-text"><p>thanks jaap. And how is this link "http://wiki.wireshark.org/HowToDissectAnything" useful for my problem?</p></div><div id="comment-8771-info" class="comment-info"><span class="comment-age">(02 Feb '12, 02:11)</span> <span class="comment-user userinfo">ashish_goel</span></div></div></div><div id="comment-tools-8752" class="comment-tools"></div><div class="clear"></div><div id="comment-8752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

