+++
type = "question"
title = "PCAP file format/structure (GSM MAP protocol)"
description = '''Hello to all, First time asking question in this forum. In summary: I&#x27;m trying to look for PCAP file format/structure to try to decode files containing GSM MAP protocol. I need to identify what are the hexadecimal values that say where begins/ends a packet, where begins/ends a especific parameter or...'''
date = "2015-11-12T11:12:00Z"
lastmod = "2015-11-13T11:43:00Z"
weight = 47548
keywords = [ "file-format", "gsm-map", "binary-estructure" ]
aliases = [ "/questions/47548" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [PCAP file format/structure (GSM MAP protocol)](/questions/47548/pcap-file-formatstructure-gsm-map-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47548-score" class="post-score" title="current number of votes">0</div><span id="post-47548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello to all,</p><p>First time asking question in this forum.</p><p>In summary: I'm trying to look for PCAP file format/structure to try to decode files containing GSM MAP protocol. I need to identify what are the hexadecimal values that say where begins/ends a packet, where begins/ends a especific parameter or if it is in a fix position with a predefined offset.</p><p>I'm not sure is a tool exists for something like this.</p><p>In detail:</p><p>I look for way to print several parameters from huge pcap files containing GSM MAP protocol messages, for example Timestamp, OPC, DPC, Source IP, Destination IP, SCCP Calling Party, SCCP Called Party based on if field SCCP Called party has certain length.</p><p>What I've done so far is open the files in Wireshark and export them as CSV, then I post process the file to select the lines that match the condition.</p><p>But since the files are more than 300 MB in size and I need to do it for several files, is not a practical task and I think if I open the pcap file in binary mode and I know the estructure of the pcap file, I could do it faster and in batch mode analyzing in binary mode.</p><p>Many thanks for any help.</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-file-format" rel="tag" title="see questions tagged &#39;file-format&#39;">file-format</span> <span class="post-tag tag-link-gsm-map" rel="tag" title="see questions tagged &#39;gsm-map&#39;">gsm-map</span> <span class="post-tag tag-link-binary-estructure" rel="tag" title="see questions tagged &#39;binary-estructure&#39;">binary-estructure</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '15, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/11103cc9b10ea69c717d91c7337e93fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cgkmal&#39;s gravatar image" /><p><span>cgkmal</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cgkmal has no accepted answers">0%</span></p></div></div><div id="comments-container-47548" class="comments-container"></div><div id="comment-tools-47548" class="comment-tools"></div><div class="clear"></div><div id="comment-47548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="47555"></span>

<div id="answer-container-47555" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47555-score" class="post-score" title="current number of votes">3</div><span id="post-47555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I look for way to print several parameters from huge pcap files containing GSM MAP protocol messages, for example Timestamp, OPC, DPC, Source IP, Destination IP, SCCP Calling Party, SCCP Called Party based on if field SCCP Called party has certain length.</p></blockquote><p>You might want to look at using TShark with the <code>-T fields</code> option, using the <code>-e</code> option to select certain fields to print.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47555" class="comments-container"><span id="47581"></span><div id="comment-47581" class="comment"><div id="post-47581-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy for share the tshark options. It works and get info for each packet in one file.</p></div><div id="comment-47581-info" class="comment-info"><span class="comment-age">(13 Nov '15, 11:43)</span> <span class="comment-user userinfo">cgkmal</span></div></div></div><div id="comment-tools-47555" class="comment-tools"></div><div class="clear"></div><div id="comment-47555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47549"></span>

<div id="answer-container-47549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47549-score" class="post-score" title="current number of votes">1</div><span id="post-47549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>these are actually two questions.</p><p>Answer 1: the .pcap file format is described for example <a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">here</a>.</p><p>Answer 2: some of the information elements you mention (e.g. OPC, DPC) have a fixed length and position within the packet, some don't (e.g. SCCP Calling Party, SCCP Called Party). So while it is enough to take N bytes starting from offset M in the packet to get the former ones, you have to properly decode the protocol tree in order to get the latter ones. The exact position of the fixed place and size elements also depends on the transport protocol (MTP2 or SIGTRAN).</p><p>Pavel</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-47549" class="comments-container"><span id="47550"></span><div id="comment-47550" class="comment"><div id="post-47550-score" class="comment-score"></div><div class="comment-text"><p>Hello Pavel,</p><p>Thanks for answer and link shared.</p><p>I see from pcap format that header has a fixed length and you mention that to know size and position for opc, dpc depends of transport.</p><p>Currently the pcap has mtp transport, then, let's say I'm able to isolate the data bytes, then how to know a little bit more about the restructure of this map data?. Do you know where can I look the format(lenght, position) for map parameters?</p><p>Thanks again</p></div><div id="comment-47550-info" class="comment-info"><span class="comment-age">(12 Nov '15, 11:46)</span> <span class="comment-user userinfo">cgkmal</span></div></div><span id="47559"></span><div id="comment-47559" class="comment"><div id="post-47559-score" class="comment-score"></div><div class="comment-text"><p>Hi cgkmal,</p><p>please make clear what you want:<br />
</p><ul><li><p>either you need to extract some protocol fields from each packet into text, one line per packet, with no effort spent. If so, the answer of <a href="https://ask.wireshark.org/users/79/guy-harris">Guy Harris</a> mentioning <a href="https://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> is your best bet<br />
</p></li><li><p>or you want to write your own dissector for MTP3 and SCCP (at least). In such case, the <a href="http://www.itu.int/ITU-T/recommendations/index.aspx?ser=Q">ITU-T library of recommendations</a> is your best starting point (and your question belongs to this web only very loosely).<br />
</p></li></ul><p>Pavel</p></div><div id="comment-47559-info" class="comment-info"><span class="comment-age">(13 Nov '15, 02:26)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="47579"></span><div id="comment-47579" class="comment"><div id="post-47579-score" class="comment-score"></div><div class="comment-text"><p>Hi Pavel, Thanks for the ITU link.</p><p>I've tested with tshark already, the thing is that since I need to process with tshark, then another script to process the output given by tshark and do this for big files and many times. Due to this I thought in ask in order to know a way to process the pcap directly.</p><p>I found the explanation about pcap format <a href="http://www.kroosec.com/2012/10/a-look-at-pcap-file-format.html">http://www.kroosec.com/2012/10/a-look-at-pcap-file-format.html</a> and I have more clear the escenario that matches with wath you mentioned. This is pcap packets have Global header, section headers of fixed lenght and data is variable. But to understand that packet data is needed to follow what ITU says depending the protocol to decode.</p><p>Thanks for the help.</p></div><div id="comment-47579-info" class="comment-info"><span class="comment-age">(13 Nov '15, 11:15)</span> <span class="comment-user userinfo">cgkmal</span></div></div></div><div id="comment-tools-47549" class="comment-tools"></div><div class="clear"></div><div id="comment-47549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47554"></span>

<div id="answer-container-47554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47554-score" class="post-score" title="current number of votes">1</div><span id="post-47554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I think if I open the pcap file in binary mode</p></blockquote><p>I think if you open the pcap file with libpcap or WinPcap, you'll be even happier, as you won't have to <em>care</em> about the pcap file format. :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-47554" class="comments-container"><span id="47557"></span><div id="comment-47557" class="comment"><div id="post-47557-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>Thanks for the suggestion. I´ve been searching about libpcap and winpcap as you said. It seems it works with C, my knowdledge in C are not the bests hehe. But I haven´t found a good example in how to open o manipulate desired info with winpcap so far. Do you know or have experience with that to give me a start point?</p><p>Open the pcap with a hex editor I can see the point codes, SCCP callin/called parties but I still don´t know size, position, offset etc to identify where those parameters begin or end.</p><p>Thanks for the help so far.</p><p>Regards</p></div><div id="comment-47557-info" class="comment-info"><span class="comment-age">(12 Nov '15, 22:07)</span> <span class="comment-user userinfo">cgkmal</span></div></div></div><div id="comment-tools-47554" class="comment-tools"></div><div class="clear"></div><div id="comment-47554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

