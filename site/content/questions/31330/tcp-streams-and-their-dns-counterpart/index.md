+++
type = "question"
title = "TCP Streams and their DNS counterpart..."
description = '''Alright guys, I have multiple clarification questions on DNS connections and TCP Streams...  Does every DNS Query and Response have a corresponding TCP Stream? Does every TCP Stream have a correspodning DNS Query and Response? (I imagine one of these has to be independent). If one of the above isn&#x27;t...'''
date = "2014-03-31T17:59:00Z"
lastmod = "2014-03-31T19:32:00Z"
weight = 31330
keywords = [ "tcp", "tcp.stream", "tshark", "dns", "dnsquery" ]
aliases = [ "/questions/31330" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Streams and their DNS counterpart...](/questions/31330/tcp-streams-and-their-dns-counterpart)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31330-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Alright guys, I have multiple clarification questions on DNS connections and TCP Streams...</p><ol><li>Does every DNS Query and Response have a corresponding TCP Stream?</li><li>Does every TCP Stream have a correspodning DNS Query and Response? (I imagine one of these has to be independent).</li><li>If one of the above isn't true - when do they and when don't they?</li><li>Is it possible in tshark to know which DNS Query and Response goes to which TCP Stream (as in is it possible to set a field for it "tshark -r infile -T Fields -e blah blah" and see their relationship)?</li><li>Im writing a script that measures time from when button is pressed, which posts a message, to when the post is finshed uploading. Would the most accurate way be from the DNS query to the TCP ACK, or would it just be from TCP SYN to TCP ACK? (I suppose this assums that DNS Connections and TCP connections are related).<br />
</li><li>Lastly, is there anything I am missing? (if you know something that is really interesting or useful that is related to this topic - you should pretend like I asked a question here that would solicit your answer : p )<br />
</li></ol><p>Thanks guys, Im excited to finally understand some of these concepts.</p><p>//Z</p></div><div id="question-tags" class="tags-container tags">tcp tcp.stream tshark dns dnsquery</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '14, 17:59</strong></p><img src="https://secure.gravatar.com/avatar/fbc5b3a06e0bdd9408c2356da21566c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nefarii&#39;s gravatar image" /><p>Nefarii<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nefarii has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Mar '14, 18:01</p></div></div><div id="comments-container-31330" class="comments-container"></div><div id="comment-tools-31330" class="comment-tools"></div><div class="clear"></div><div id="comment-31330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31331"></span>

<div id="answer-container-31331" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31331-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does every DNS Query and Response have a corresponding TCP Stream?</p></blockquote><p>No. A DNS query might result from an attempt to look up a host to which to send <em>UDP</em> packets, for example. DNS queries can be used for other purposes, such as translating an <em>IP address</em> to a <em>host name</em>. And looking up an IP address for a host might require <em>more than one</em> DNS query, e.g. "example.com" might require that a DNS server for ".com" be looked up, and then that "example.com" might be looked up on that server.</p><blockquote><p>Does every TCP Stream have a correspodning DNS Query and Response?</p></blockquote><p>No. Somebody might try to connect to a host with a known IP address, or might be getting the IP address for the host from a file, or might be using some other protocol, such as NIS, to look up the IP address for the host. Or the host might already have a cached copy of a previous lookup of a host name.</p><blockquote><p>If one of the above isn't true - when do they and when don't they?</p></blockquote><p><em>Neither</em> is true. See above.</p><blockquote><p>Is it possible in tshark to know which DNS Query and Response goes to which TCP Stream</p></blockquote><p>Given that not all DNS query/response pairs correspond to a TCP stream (and not all TCP streams have a DNS query/response associated with them), no. At best, you can try to find a DNS query/response pair that returned an IP address used in a later TCP stream.</p><blockquote><p>Im writing a script that measures time from when button is pressed, which posts a message, to when the post is finshed uploading. Would the most accurate way be from the DNS query to the TCP ACK, or would it just be from TCP SYN to TCP ACK?</p></blockquote><p>What if it takes 10 seconds (on a slow machine) between the time when the button is pressed and when a DNS query is sent out, <em>if</em> necessary, to find the IP address of the host to which to upload the post? In that case, you can't use <em>any</em> packet sniffer find out the time between the button is pressed and when the post finishes being uploaded, because the first 10 seconds don't necessarily correspond to network traffic - they might be due to the code to handle the button push being paged out and having to be paged in from disk, or due to a lot of CPU time being spent to get to the host name lookup, or something such as that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '14, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31331" class="comments-container"><span id="31332"></span><div id="comment-31332" class="comment"><div id="post-31332-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answers, a few follow up questions though - 1.) If there is an android application that posts something onto facebook (update or picture), would there most likely be a DNS connection before the TCP connection? 2.) Relating to question 6, would it be best then to just take the Round Trip TCP connection time to determine how long it took for an item to post?</p></div><div id="comment-31332-info" class="comment-info"><span class="comment-age">(31 Mar '14, 19:51)</span> Nefarii</div></div><span id="31333"></span><div id="comment-31333" class="comment"><div id="post-31333-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>If there is an android application that posts something onto facebook (update or picture), would there most likely be a DNS connection before the TCP connection?</p></blockquote><p>If they've already been accessing Facebook, the machine probably has an IP address corresponding to www.facebook.com, so there's a good chance that there would <em>not</em> be a DNS query/response.</p><blockquote><p>Relating to question 6, would it be best then to just take the Round Trip TCP connection time to determine how long it took for an item to post?</p></blockquote><p>That depends on what you mean by "how long it took for an item to post". If you're <em>only</em> looking at network delays, the best way to do it is to:</p><ul><li>if there <em>is</em> a DNS lookup for a Facebook domain name, use the DNS query as the starting time, otherwise use the first TCP packet to the Facebook server as the starting time;</li><li>use the time of the last TCP segment of the posted item as the ending time.</li></ul><p><em>However</em>, that doesn't say how long it took the server to <em>do</em> the post, so you'd need to look for the first segment of the <em>response</em> to the POST request to get that.</p><p>You'd also have to worry about, for example, the Facebook app or browser periodically polling the server to update lists of how many friends were online, etc., etc..</p><p>Note that there wouldn't necessarily be a new connection established for the POST, either.</p></div><div id="comment-31333-info" class="comment-info"><span class="comment-age">(31 Mar '14, 19:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-31331" class="comment-tools"></div><div class="clear"></div><div id="comment-31331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

