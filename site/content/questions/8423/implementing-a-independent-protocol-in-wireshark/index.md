+++
type = "question"
title = "Implementing a independent protocol in wireshark."
description = '''Hi, I want to implement a protocol in wireshark and decode its packets according to what is mentioned in the protocol specification. The protocol needs not to be a networking protocol. I will provide the data to decode in form of .csv file format. I have read the developers guide on implementing cus...'''
date = "2012-01-17T00:37:00Z"
lastmod = "2012-01-29T02:25:00Z"
weight = 8423
keywords = [ "protocol" ]
aliases = [ "/questions/8423" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Implementing a independent protocol in wireshark.](/questions/8423/implementing-a-independent-protocol-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8423-score" class="post-score" title="current number of votes">0</div><span id="post-8423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to implement a protocol in wireshark and decode its packets according to what is mentioned in the protocol specification. The protocol needs not to be a networking protocol. I will provide the data to decode in form of .csv file format.</p><p>I have read the developers guide on implementing custom dissector on top of some other protocol like tcp/udp etc. But here in my case it is completely different because firstly the protocol data comes from csv and it will run independently not top of any other existing protocol.</p><p>Is it feasible to implement such customizations in wireshark?? How shall I proceed with the development? What all modules I need to change My purpose of such kind of implementation is to analyze protocol data through wireshark.</p><p>Looking for a reply. Thanks in advance :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '12, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p><span>ashish_goel</span><br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div></div><div id="comments-container-8423" class="comments-container"><span id="8425"></span><div id="comment-8425" class="comment"><div id="post-8425-score" class="comment-score"></div><div class="comment-text"><p>If your protocol "[runs] independently not top of any other existing protocol", that means it's a link-layer protocol; it cannot be a network-layer protocol, as those run on top of link-layer protocols such as Ethernet or PPP, and it cannot be a transport-layer protocol, as those run on top of network-layer protocols such as IPv4 or IPv6, and it cannot be a higher-level protocol, as those ultimately run on top of transport-layer protocols such as TCP or UDP.</p><p>On what type of physical network does your protocol run?</p></div><div id="comment-8425-info" class="comment-info"><span class="comment-age">(17 Jan '12, 01:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="8426"></span><div id="comment-8426" class="comment"><div id="post-8426-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris thanks for the reply...</p><p>For my protocol it is not about the layer.. My requirement is that I have some data and I have to display that in a meaning full way like displaying the packet type, its payload etc. So in all i can say that I want to use wireshark as the decoder and display tool for the raw data.</p><p>For example assume the following data comes to wireshark as per my protocol:</p><p>Example Data : 01 00001101 0101</p><p>The above represents bits coming to me. Now suppose that according to my protocol specs. first two bit identify type of packet. So lets assume 01 specifies that this is a "PACKET A" then next 8 bits represent payload of this packet "PACKET A" and last 4 bits represents the checksum. So I want it to be displayed as:</p><p>PACKET A : 01 PAYLOAD : 00001101 CHECKSUM : 0101</p><p>I guess my requirement is clear to you.</p></div><div id="comment-8426-info" class="comment-info"><span class="comment-age">(17 Jan '12, 02:39)</span> <span class="comment-user userinfo">ashish_goel</span></div></div></div><div id="comment-tools-8423" class="comment-tools"></div><div class="clear"></div><div id="comment-8423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8436"></span>

<div id="answer-container-8436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8436-score" class="post-score" title="current number of votes">0</div><span id="post-8436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can implement a dissector for a protocol that does not run on top of another --as Guy said in his comment, this would be a link-layer protocol. What you cannot do is feed your csv file directly into Wireshark, as this is not a file format Wireshark currently understands. My guess is that this is the output of some other program that you are interested in reviewing. While it is possible to use Wireshark for this task, it will require some additional work. Since you will be doing some sort of additional work to display your data, I might recommend that you go another route to display your data (e.g. write a Python script that examines and displays your data, or a VB form to do the same).</p><p>Since your data files are almost certainly <em>not</em> in binary format (and certainly not one Wireshark already understands), using Wireshark will ultimately require converting your csv files to another format first. One method of doing this that I have used in the past goes like this:</p><ol><li>Create a tool that translates your csv file into something Wireshark can manage, like a <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat" title="Libpcap File Format">pcap</a> file. This could be just about anything, and will run separately from Wireshark for each input csv.</li><li>Implement your dissector so that it is registered on the <code>wtap_encap</code> dissector table for the <code>data_link_type</code> number you selected in writing your first tool.</li><li>Any time you want to view one of your data sets in Wireshark, you must first pass it through the tool you created in step 1 before opening the file in Wireshark.</li></ol><p>This strategy allows you to leverage Wireshark for much of the heavy lifting in terms of display, filtering, searching, and so on without having to write all of that yourself. What it requires is a little translation of your data from one format to another, and, more drastically, learning how to program for Wireshark. Once you get used to it, it is quite simple, but the learning curve can be a little steep at times.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '12, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8436" class="comments-container"><span id="8444"></span><div id="comment-8444" class="comment"><div id="post-8444-score" class="comment-score"></div><div class="comment-text"><p>@ multipleinterfaces.. Your solution looks feasible to me. But rather than building a tool for conversion, can't I add support for my defined .csv format in wireshark import formats??</p></div><div id="comment-8444-info" class="comment-info"><span class="comment-age">(17 Jan '12, 20:36)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8446"></span><div id="comment-8446" class="comment"><div id="post-8446-score" class="comment-score"></div><div class="comment-text"><p>Yes, you could. Look at wiretap/README.developer for what's required.</p></div><div id="comment-8446-info" class="comment-info"><span class="comment-age">(18 Jan '12, 01:48)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="8678"></span><div id="comment-8678" class="comment"><div id="post-8678-score" class="comment-score"></div><div class="comment-text"><p>Has anybody added a new import format in wiretap?? If anybody has done it before plz share how the things went and how exactly you implemented.</p></div><div id="comment-8678-info" class="comment-info"><span class="comment-age">(29 Jan '12, 02:25)</span> <span class="comment-user userinfo">ashish_goel</span></div></div></div><div id="comment-tools-8436" class="comment-tools"></div><div class="clear"></div><div id="comment-8436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

