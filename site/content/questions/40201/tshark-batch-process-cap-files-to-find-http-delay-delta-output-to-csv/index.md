+++
type = "question"
title = "TShark Batch-process .Cap files to find HTTP delay delta &amp; output to CSV"
description = '''Hi Guys, first post here so be gentle! I&#x27;ve written a script to capture traffic over our 2x new &amp;amp; 2x old Proxy Appliances. It simply sets a static IP, applies a Proxy, starts a 60 second capture and navigates to 3 content heavy websites, saving a cap file per scenario tested. I&#x27;m generating 39 c...'''
date = "2015-03-03T03:27:00Z"
lastmod = "2015-03-03T04:41:00Z"
weight = 40201
keywords = [ "http.response", "wireshark", "http", "cli", "tshark" ]
aliases = [ "/questions/40201" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TShark Batch-process .Cap files to find HTTP delay delta & output to CSV](/questions/40201/tshark-batch-process-cap-files-to-find-http-delay-delta-output-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40201-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys, first post here so be gentle!</p><p>I've written a script to capture traffic over our 2x new &amp; 2x old Proxy Appliances. It simply sets a static IP, applies a Proxy, starts a 60 second capture and navigates to 3 content heavy websites, saving a cap file per scenario tested. I'm generating 39 cap files a day.</p><p>What i basically want is the ability to process a directory full of cap files into a csv file detailing the http response delta of even just one http request per cap file, so i can can build a map of delays at certain times of the day on certain devices. preferably from command line. though at this stage I'm not fussed!</p><p>I've tried tcpdump for win, and bash for win following <a href="http://blog.9minutesnooze.com/analyzing-http-traffic-tcpdump-perconas-pttcpmodel/">this guide.</a></p><p>As insane as that sounds its the closest guide i can find to help me out here, though i keep getting syntax errors which is possibly a porting problem. i also don't understand bash well enough to rewrite the command without the escape operators</p><p>I've got the Solarwinds Response Timeviewer for Wireshark, which does almost exactly what i want, however it only processes 1 cap file at a time and has no export results or cli, requiring a fairly laborious copy and paste into excel per cap file, and to do nearly 200 a week manually will cause me to go insane.<br />
</p><p><em>EDIT</em></p><p>I tried the following from <a href="https://ask.wireshark.org/questions/23168/capturing-http-response-delays">this article</a></p><pre><code>tshark -nr input.pcapng -y &quot;ip.addr eq 172.16.10.230 and (http.request or http.response)&quot; -T fields -e frame.number -e frame.time_relative  -e ip.src -e ip.dst -e tcp.stream -e http.request.full_uri -e http.response.code -e http.response.phrase</code></pre><p><em>(the specified IP being my machines IP)</em></p><p>i got the following error:</p><pre><code>Parsing Http Responses
tshark: The specified data link type &quot;ip.addr eq 172.16.10.230 and (http.request
 or http.response)&quot; isn&#39;t valid</code></pre><p>Any help is very much appreciated!</p><p>Thanks very much in advance,</p></div><div id="question-tags" class="tags-container tags">http.response wireshark http cli tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '15, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/d3c2b30c48854d26331717bc1e0dbc8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bumpudll3&#39;s gravatar image" /><p>Bumpudll3<br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bumpudll3 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Mar '15, 03:55</p></div></div><div id="comments-container-40201" class="comments-container"></div><div id="comment-tools-40201" class="comment-tools"></div><div class="clear"></div><div id="comment-40201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40208"></span>

<div id="answer-container-40208" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40208-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use an uppercase <code>-Y</code> parameter for your filter.</p><p>If you list the exact values you need from the capture, then we may be able to help with a better filter and fields selection.</p><p>What version of tshark are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40208" class="comments-container"><span id="40211"></span><div id="comment-40211" class="comment"><div id="post-40211-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the response. All I'm after is how long in seconds it takes between http request &amp; response when i navigate to a particular external website, for example msn.com. I would like to then export this to a single line in a CSV so i can compare results over the course of a week.</p><p>I'm using the newest version (1.12.3)</p><p>When i change the -y to uppercase, i no longer get any errors, &amp; it exports to CSV happily :)</p><p>the formatting of the CSV is very hard to read as IP,response time &amp; hostname are all squashed into one line with no spaces.</p><p>can help me out with formatting?</p><p>Thanks!</p></div><div id="comment-40211-info" class="comment-info"><span class="comment-age">(03 Mar '15, 05:34)</span> Bumpudll3</div></div><span id="40212"></span><div id="comment-40212" class="comment"><div id="post-40212-score" class="comment-score">1</div><div class="comment-text"><p>Try this:</p><p><code>tshark-nr yourfile.pcapng -2 -Y "http.time || http.request.full_uri" -T fields -e frame.number -e http.request.full_uri -e http.response_in -e http.response.code -e http.time -e http.request_in</code></p><p>This gives you the frame number, then for a request the uri and the frame number of the response, or for a response, the status code and the response time and the frame number of the request.</p></div><div id="comment-40212-info" class="comment-info"><span class="comment-age">(03 Mar '15, 06:44)</span> grahamb ♦</div></div><span id="40213"></span><div id="comment-40213" class="comment"><div id="post-40213-score" class="comment-score"></div><div class="comment-text"><p>You sir are a Hero!!! thanks v much. That's looking fantastic, can i ask 1 further question. How do I amend your response to just return 1 x particular url response time? presumably via a string filter?</p><p>Also while i have your support - is it possible to return the NAME of the source input cap file into the csv on the same line? thanks!</p><p>James</p></div><div id="comment-40213-info" class="comment-info"><span class="comment-age">(03 Mar '15, 06:56)</span> Bumpudll3</div></div><span id="40220"></span><div id="comment-40220" class="comment"><div id="post-40220-score" class="comment-score">1</div><div class="comment-text"><p>I don't think that you can easily filter on a single request uri, as that filter would then exclude the response which has the response time. I think you'll just have to post-process that.</p><p>I'm not aware of anyway to get the filename into tshark output, again a post-processing task.</p><p>There is some formatting control for the fields, have a look at the <code>-E</code> parameter, e.g. <code>-E "separator=," -E "quote=d"</code> to double quote values and add a comma separator.</p></div><div id="comment-40220-info" class="comment-info"><span class="comment-age">(03 Mar '15, 08:24)</span> grahamb ♦</div></div></div><div id="comment-tools-40208" class="comment-tools"></div><div class="clear"></div><div id="comment-40208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

