+++
type = "question"
title = "How source and destination is identified?"
description = '''If there is a syn bit set seen from an endpoint, this is the source. I am curious about if wireshark defines in some other ways or only the syn bit is enough to identify the source and destination? Secondly,  if my traces has are partial conversations, not any syn bit is seen, which one is the sourc...'''
date = "2011-01-21T13:44:00Z"
lastmod = "2011-01-28T10:58:00Z"
weight = 1863
keywords = [ "source", "destination", "wireshark", "conversation" ]
aliases = [ "/questions/1863" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How source and destination is identified?](/questions/1863/how-source-and-destination-is-identified)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1863-score" class="post-score" title="current number of votes">0</div><span id="post-1863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If there is a syn bit set seen from an endpoint, this is the source. I am curious about if wireshark defines in some other ways or only the syn bit is enough to identify the source and destination? Secondly,</p><p>if my traces has are partial conversations, not any syn bit is seen, which one is the source and destination? port numbers can be used to determine them but what if both port numbers makes sense. server uses 80 and the client uses a port number let say something more than 1024 but it's also possible for servers to give services from that port number as a kind of database queries.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '11, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/bde1409a68745702a5dd0f41c6a544e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="berkey&#39;s gravatar image" /><p><span>berkey</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="berkey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '11, 13:44</strong> </span></p></div></div><div id="comments-container-1863" class="comments-container"></div><div id="comment-tools-1863" class="comment-tools"></div><div class="clear"></div><div id="comment-1863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1867"></span>

<div id="answer-container-1867" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1867-score" class="post-score" title="current number of votes">2</div><span id="post-1867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="berkey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depends on what you mean by “source” and “destination.” The “Source” and “Destination” columns in Wireshark identify the source and destination of each packet. Which endpoint is the source and which is the destination alternates as the two systems exchange packets. I'm guessing that's not what you mean.</p><p>I'm guessing you're asking which endpoint is the source of a particular data flow. The endpoint that sends the initial SYN is the originator of the TCP connection, but that system is not necessarily the source of the subsequent data flows.</p><p>Many networking data flows are primarily unidirectional: Data is flowing mostly in one direction. For example, if I open a command prompt on my computer and type “ftp 192.168.1.10” my computer will send the SYN packet to originate the connection. But then if I download a file, the data flow will be FROM the server TO my computer. The FTP server will be the source and my computer will be the destination for the data transfer. If I upload a file, my computer will be the source and the server will be the destination.</p><p>The source is the system sending the data; the destination is the system receiving the data. In a unidirectional data flow, you will see (relatively) large packets from one endpoint, with tcp.len &gt; 0 (hopefully, maximum segment size, or close to it), and the other side will be sending back relatively small ACK packets with no data, and therefore a tcp.len of 0.</p><p>What ports are used doesn't really identify who is the source. Again, in an FTP session, you can be downloading or uploading. You can be the source or the destination for the data.</p><p>When you click on a link on a web page, your computer is the source of the GET request that is sent to the web server, which will be a relatively small amount of data. Then the web server is the source of the page contents that are sent to your computer, and this will probably be a much larger amount of data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '11, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-1867" class="comments-container"><span id="1883"></span><div id="comment-1883" class="comment"><div id="post-1883-score" class="comment-score"></div><div class="comment-text"><p>@jaragon, you simply mean that if i have a trace without payloads by looking the data sizes less than MSS, will help me determine if i don't have any syn bit seen, so do you have any official reference or webpage talks about these related to wireshark.. thanks</p></div><div id="comment-1883-info" class="comment-info"><span class="comment-age">(22 Jan '11, 14:50)</span> <span class="comment-user userinfo">berkey</span></div></div><span id="1885"></span><div id="comment-1885" class="comment"><div id="post-1885-score" class="comment-score"></div><div class="comment-text"><p>If you do not see either the SYN or the SYN/ACK, then you cannot tell which device initiated the TCP connection.</p></div><div id="comment-1885-info" class="comment-info"><span class="comment-age">(22 Jan '11, 19:39)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="1895"></span><div id="comment-1895" class="comment"><div id="post-1895-score" class="comment-score"></div><div class="comment-text"><p>@jaragon, but wireshark can give me results of the conversations by identifying the source and destination without any syn ?</p></div><div id="comment-1895-info" class="comment-info"><span class="comment-age">(23 Jan '11, 10:05)</span> <span class="comment-user userinfo">berkey</span></div></div><span id="1996"></span><div id="comment-1996" class="comment"><div id="post-1996-score" class="comment-score"></div><div class="comment-text"><p>Where does Wireshark "identify the source and destination"? Do <em>NOT</em> assume that, in a list of conversations, the first address it shows for the conversation is the source and the second address is the destination; there is no guarantee that's the case.</p></div><div id="comment-1996-info" class="comment-info"><span class="comment-age">(28 Jan '11, 10:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1867" class="comment-tools"></div><div class="clear"></div><div id="comment-1867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

