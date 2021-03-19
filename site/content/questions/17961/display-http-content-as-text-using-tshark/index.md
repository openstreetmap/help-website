+++
type = "question"
title = "Display HTTP content as text using tshark"
description = '''Hi, I am using tshark to monitor http traffic on a server. I would like to display some of the IP fields, some of the HTTP headers and the HTTP content if it is textual. Is there a way to do this with tshark? Thanks David'''
date = "2013-01-26T04:25:00Z"
lastmod = "2013-01-26T07:30:00Z"
weight = 17961
keywords = [ "http", "tshark" ]
aliases = [ "/questions/17961" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display HTTP content as text using tshark](/questions/17961/display-http-content-as-text-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17961-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am using tshark to monitor http traffic on a server. I would like to display some of the IP fields, some of the HTTP headers and the HTTP content if it is textual. Is there a way to do this with tshark? Thanks David</p></div><div id="question-tags" class="tags-container tags">http tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '13, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/0b0ac57ffe8e8e5747c4b0f5595a521f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Sackstein&#39;s gravatar image" /><p>David Sackstein<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Sackstein has no accepted answers">0%</span></p></div></div><div id="comments-container-17961" class="comments-container"></div><div id="comment-tools-17961" class="comment-tools"></div><div class="clear"></div><div id="comment-17961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17963"></span>

<div id="answer-container-17963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17963-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could do something like this:</p><pre><code>tshark -r trace.pcapng  -R &quot;tcp.port==80&quot; -Tfields -e ip.src -e ip.dst -e http.response.code</code></pre><p>The "-R" parameter filters on tcp port 80 to skip all packets that are not on that port - if your HTTP traffic is using another port you could change that, or maybe -R "http" would work just as well in most cases. The "-e" parameters are used to tell tshark what fields you want to see, so you can add all the fields you need (I just added a few as examples)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '13, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jan '13, 07:30</p></div></div><div id="comments-container-17963" class="comments-container"><span id="17964"></span><div id="comment-17964" class="comment"><div id="post-17964-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper Thanks for the quick response. This option does not allow me to see he http content, though. How can I do that? Thanks David</p></div><div id="comment-17964-info" class="comment-info"><span class="comment-age">(26 Jan '13, 08:00)</span> David Sackstein</div></div><span id="17967"></span><div id="comment-17967" class="comment"><div id="post-17967-score" class="comment-score"></div><div class="comment-text"><p>You could try "data-text-lines", but I'm not sure if it will show all content. It should show all HTTP content that Wireshark can determine as such I guess.</p></div><div id="comment-17967-info" class="comment-info"><span class="comment-age">(26 Jan '13, 08:45)</span> Jasper ♦♦</div></div><span id="17969"></span><div id="comment-17969" class="comment"><div id="post-17969-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, Unfortunately this doesnt work. I get lots of empty lines and from time to time this: Line-based text data: text/html But I dont get any text from the content of the http responses. It seems strange that Wireshark is able to display an entire HTTP conversation using the "decode as" option, but tshark doesnt have it. Dumping the packets themselves (using -x or -w) is not good enough because it doesnt handle reassembly. What do you think? David</p></div><div id="comment-17969-info" class="comment-info"><span class="comment-age">(26 Jan '13, 10:21)</span> David Sackstein</div></div><span id="17970"></span><div id="comment-17970" class="comment"><div id="post-17970-score" class="comment-score"></div><div class="comment-text"><p>Maybe it has to do with the http data being gzipped. I'm not sure if tshark can display the uncompressed content. If you're interested in seeing the content like in "Follow TCP Steam" in Wireshark, maybe SYN-bits answer in this question can help: <a href="http://ask.wireshark.org/questions/17903/how-do-i-view-all-streams-in-follow-tcp-streams">http://ask.wireshark.org/questions/17903/how-do-i-view-all-streams-in-follow-tcp-streams</a></p></div><div id="comment-17970-info" class="comment-info"><span class="comment-age">(26 Jan '13, 11:42)</span> Jasper ♦♦</div></div><span id="17972"></span><div id="comment-17972" class="comment"><div id="post-17972-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, The http data I am working with is not gzipped. I read SYN-bits answer in the link you mentioned. It allows you to decode HTTP content from a previously captured file. But I need to decode this information in a live capture. I think Wireshark also cant do this, because the "follow TCP stream" and "decode as" options are indeed on packets that have already been captured. From what I read, tcpflow can do what I need - but tcpflow doesnt support IP fragmentation. So, do you think I need to write my own HTTP/TCP/IP sniffer for this? David</p></div><div id="comment-17972-info" class="comment-info"><span class="comment-age">(26 Jan '13, 14:07)</span> David Sackstein</div></div><span id="17974"></span><div id="comment-17974" class="comment not_top_scorer"><div id="post-17974-score" class="comment-score"></div><div class="comment-text"><p>The real time part is a problem, I can see that. Before starting the long and hard work of writing your own sniffer you should wait a little more to see if any tshark expert has another idea. Tshark scripting isn't exactly my specialty, but maybe @Landi, @SYN-Bit or @Kurt can help - they are the command line pro's :-)</p></div><div id="comment-17974-info" class="comment-info"><span class="comment-age">(26 Jan '13, 18:01)</span> Jasper ♦♦</div></div><span id="19136"></span><div id="comment-19136" class="comment not_top_scorer"><div id="post-19136-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks for your help on this. In the end this is what I used:</p><p>This is the command line I am using:</p><p>tshark.exe -i3 -l -f "tcp port 80" -O http -d tcp.port==80,http -o "ip.use_geoip:FALSE" -R "not tcp.analysis.duplicate_ack" -T fields -e ip.host -e tcp.port -e http.request.full_uri -e http.request.method -e http.response.code -e http.response.phrase -e http.content_length -e data -e text -E separator=;2&gt;&amp;0</p><p>-e data gets me the POST parameters and -e text gets me the content of the response.</p><p>David</p></div><div id="comment-19136-info" class="comment-info"><span class="comment-age">(04 Mar '13, 13:01)</span> David Sackstein</div></div><span id="19176"></span><div id="comment-19176" class="comment not_top_scorer"><div id="post-19176-score" class="comment-score"></div><div class="comment-text"><p>Wow, that is quite some parameter zoo you've got... congratulations, and thanks for the feedback!</p></div><div id="comment-19176-info" class="comment-info"><span class="comment-age">(05 Mar '13, 12:34)</span> Jasper ♦♦</div></div></div><div id="comment-tools-17963" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-17963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

