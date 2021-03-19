+++
type = "question"
title = "Analyzing HTTP protocol using Tshark"
description = '''Hello! I&#x27;m trying to analyze HTTP requests and responses using Tshark and following command.  /usr/local/bin/tshark -R &quot;http.response or http.request&quot; &#92;  -T fields -E separator=&quot;|&quot; &#92;  -e frame.time_epoch &#92;  -e ip.src &#92;  -e tcp.srcport &#92;  -e ip.dst &#92;  -e tcp.dstport &#92;  -e http.request.version &#92;  -e h...'''
date = "2012-12-17T03:23:00Z"
lastmod = "2012-12-20T03:07:00Z"
weight = 16964
keywords = [ "http", "tshark" ]
aliases = [ "/questions/16964" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Analyzing HTTP protocol using Tshark](/questions/16964/analyzing-http-protocol-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16964-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I'm trying to analyze HTTP requests and responses using Tshark and following command.</p><pre><code> /usr/local/bin/tshark -R &quot;http.response or http.request&quot; \
                -T fields -E separator=&quot;|&quot; \
                -e frame.time_epoch \
                -e ip.src \
                -e tcp.srcport \
                -e ip.dst \
                -e tcp.dstport \
                -e http.request.version \
                -e http.request.method \
                -e http.host \
                -e http.request.uri \
                -e http.user_agent \
                -e http.response.code \
                -e http.content_type \
                -e http.content_length \
                -e http.location \
                -e http.referer \
                -r input.pcap</code></pre><p>It works fine generally but sometimes it gives a multiple request at the same time. for example,</p><pre><code>1351717925.251286000|xxx.xxx.xx.xx|12345|xxx.xx.xx.xxx|80|
HTTP/1.1,HTTP/1.1|GET,GET|www.aaa.com,www.aaa.com|/upload/xxxxx,/upload/xxxxx|agent1|||||</code></pre><p>Here's my question. If there's a only one user-agent field, how can I know this agent value correspond to which request? Is there any way to put a 'blank mark' for not exist http field like following?</p><pre><code>1351717925.251286000|xxx.xxx.xx.xx|12345|xxx.xx.xx.xxx|80|
HTTP/1.1,HTTP/1.1|GET,GET|www.aaa.com,www.aaa.com|/upload/xxxxx,/upload/xxxxx|agent1, &#39;no value&#39;|||||</code></pre><p>Actual responses come with a single packet but each packet is marked as "tcp segment of a reassembled pdu"</p><p>These packets are not parsed as HTTP protocol by Tshark or Wireshark. Tshark parses reassembled packet. This is why I got this strange result. Do you have any solution for this?</p><p>Thank you for your time.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screenshot.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">http tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/2c33bce451fd8dc3844b351b798cbee1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fates&#39;s gravatar image" /><p>fates<br />
<span class="score" title="35 reputation points">35</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fates has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '12, 04:54</p></div></div><div id="comments-container-16964" class="comments-container"></div><div id="comment-tools-16964" class="comment-tools"></div><div class="clear"></div><div id="comment-16964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16968"></span>

<div id="answer-container-16968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16968-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark prints the fields packet-wise (as far as I know), so there should be only one request per line, unless there are really two requests in one packet. So, either this is a tshark bug or there are really two requests in one packet. The later will happen when the client uses Pipelining. In that case it's the same client software, as it's the same TCP connection (the same IP packet). So, even if the client does not send the User-Agent header twice, it will be the same client software (same User-Agent).</p><p>BTW: What is your tshark version (tshark -v) and OS version?</p><p><strong>UPDATE</strong>:</p><p>I did some tests. tshark (V1.8.4 and V1.6.12) <strong>does</strong> report the HTTP requests packet-wise (as I 'guessed'). Maybe it's also doing reassembly if the request is really large, but I was not able to test that.</p><p>Anyway, reassembly is not related to your 'problem', as tshark will print several http requests in one output line if no reassembly is necessary (several requests in one packet - see below).</p><p>See the following capture file</p><blockquote><p><code>https://www.cloudshark.org/captures/8da00a00215f</code><br />
</p></blockquote><p>and the output of tshark</p><pre><code>4|1355756983.988805000|192.168.158.139|2758|217.13.68.220|80|HTTP/1.1|GET|scripts.zeit.de|/static/js/iqd/adam.js|Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0|||||http://www.zeit.de/index

6|1355756983.996463000|192.168.158.139|2758|217.13.68.220|80|HTTP/1.1,HTTP/1.1,HTTP/1.1|GET,GET,GET|scripts.zeit.de,scripts.zeit.de,scripts.zeit.de|/static/js/jquery/1.4.2/jquery-1.4.2.min.js,/static/js/loader.js?282,/static/js/webtrekk/webtrekk_v3.js|Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0,Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0,Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0|||||http://www.zeit.de/index,http://www.zeit.de/index,http://www.zeit.de/index

9|1355756984.029324000|217.13.68.220|80|192.168.158.139|2758|HTTP/1.1|||||200|application/javascript|962||</code></pre><p>As you can see, there are 3 requests in frame #6, as the client uses pipelining (Firefox -&gt; about:config -&gt; network.http.pipelining -&gt; true).</p><p>As a result, tshark reports those three requests in one output line for frame #6. If you need to separate those three requests, split the output fields (split character: ','). <strong>Beware:</strong> ',' might be used in the URL as well! In that case use a different character: <strong><code>-E aggregator=</code></strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '12, 07:51</p></div></div><div id="comments-container-16968" class="comments-container"><span id="16969"></span><div id="comment-16969" class="comment"><div id="post-16969-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt,</p><p>My Tshark version is 1.6.12. I have open the pcap file with Wireshark. Please see the picture I uploaded again (it's a multiple response case). Actual responses come with a single packet but each packet is marked as "tcp segment of a reassembled pdu"</p><p>These packets are not parsed as HTTP protocol by Tshark or Wireshark. Tshark parses reassembled packet. This is why I got this strange result. Do you have any solution for this?</p></div><div id="comment-16969-info" class="comment-info"><span class="comment-age">(17 Dec '12, 03:46)</span> fates</div></div><span id="16972"></span><div id="comment-16972" class="comment"><div id="post-16972-score" class="comment-score"></div><div class="comment-text"><p>maybe I'm wrong and tshark does reassembly as well when it prints the fields. I'll have to test it myself.</p><blockquote><p>Do you have any solution for this?</p></blockquote><p>O.K. what exactly is the problem you need a solution for?</p></div><div id="comment-16972-info" class="comment-info"><span class="comment-age">(17 Dec '12, 05:14)</span> Kurt Knochner ♦</div></div><span id="16976"></span><div id="comment-16976" class="comment"><div id="post-16976-score" class="comment-score"></div><div class="comment-text"><p>see the <strong>UPDATE</strong> in my answer.</p></div><div id="comment-16976-info" class="comment-info"><span class="comment-age">(17 Dec '12, 07:27)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16968" class="comment-tools"></div><div class="clear"></div><div id="comment-16968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17087"></span>

<div id="answer-container-17087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17087-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @Kurt explained, there can be multiple HTTP requests in one (reassembled) HTTP PDU. If not all the requests contain all fields that you are looking for (like the User-Agent in your example), there is no way to correlate the fields. This is due to how the -T fields operator works. Dissection will populate the fields (and will not populate a field that is not there) and -T fields will just show you the available values for a particular field.</p><p>If you do want to see all fields within context, you will have to either write a <a href="http://wiki.wireshark.org/Lua">LUA</a> script to output the data for you (including "missing" data). Or you might want to use the PDML output and use an XML parser to extract the information you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '12, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Dec '12, 03:07</p></div></div><div id="comments-container-17087" class="comments-container"></div><div id="comment-tools-17087" class="comment-tools"></div><div class="clear"></div><div id="comment-17087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

