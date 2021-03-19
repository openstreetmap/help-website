+++
type = "question"
title = "wireshark with tcp segments."
description = '''Hi all, I have a problem with HTTP filter in wireshark where the HTTP Response is displayed first then HTTP Request. This is observed in HTTP GET Request with following headers.  Authorization: xxxx. User-Agent: curl/7.30.0 Accept: / Content-Type: application/json &#92;r&#92;n&#92;r&#92;n Please see the below HTTP....'''
date = "2016-04-19T05:48:00Z"
lastmod = "2016-04-20T00:56:00Z"
weight = 51780
keywords = [ "wireshark" ]
aliases = [ "/questions/51780" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark with tcp segments.](/questions/51780/wireshark-with-tcp-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51780-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have a problem with HTTP filter in wireshark where the HTTP Response is displayed first then HTTP Request. This is observed in HTTP GET Request with following headers.</p><p>Authorization: xxxx. User-Agent: curl/7.30.0 Accept: <em>/</em> Content-Type: application/json \r\n\r\n</p><p>Please see the below HTTP.png file.<img src="https://osqa-ask.wireshark.org/upfiles/http_c8xownA.png" alt="alt text" /></p><p>If the Content-Type header is not present then wireshark is displaying the request and response in proper sequence.</p><p>I think the "Content-type" header should not be used in GET request? Is this the reason for wireshark to fail to decode it in proper sequence?<br />
</p><p>Regards, Swathi.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '16, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/a34282ab2b31d84bc63d5ea83c15d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swathi%20jakkam&#39;s gravatar image" /><p>swathi jakkam<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swathi jakkam has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-51780" class="comments-container"><span id="51781"></span><div id="comment-51781" class="comment"><div id="post-51781-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture somewhere publicly, e.g. Google Drive, Dropbox etc?</p></div><div id="comment-51781-info" class="comment-info"><span class="comment-age">(19 Apr '16, 06:01)</span> grahamb ♦</div></div><span id="51785"></span><div id="comment-51785" class="comment"><div id="post-51785-score" class="comment-score"></div><div class="comment-text"><p>where did you take that capture and <strong>how</strong>?</p></div><div id="comment-51785-info" class="comment-info"><span class="comment-age">(19 Apr '16, 06:29)</span> Kurt Knochner ♦</div></div><span id="51808"></span><div id="comment-51808" class="comment"><div id="post-51808-score" class="comment-score"></div><div class="comment-text"><p>could you please see the http capture in below link.</p><p><a href="https://drive.google.com/file/d/0B_VkVWWaLuj5NnJ3Uk81Sm84ckk/view?usp=sharing">https://drive.google.com/file/d/0B_VkVWWaLuj5NnJ3Uk81Sm84ckk/view?usp=sharing</a></p><p>Regards, Swathi.</p></div><div id="comment-51808-info" class="comment-info"><span class="comment-age">(19 Apr '16, 22:08)</span> swathi jakkam</div></div></div><div id="comment-tools-51780" class="comment-tools"></div><div class="clear"></div><div id="comment-51780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51810"></span>

<div id="answer-container-51810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51810-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please apply the following display filter and take a look at the timestamps of the frames.</p><blockquote><p>tcp.stream eq 0<br />
</p></blockquote><p>They are totally weird. So, there is either something wrong with your capturing system or something changed the timestamps in the pcap file (like anonymizer tools).</p><p>That's why you see the response before the request. So again my question:</p><blockquote><p>where did you take that capture and how?<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '16, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-51810" class="comments-container"><span id="51811"></span><div id="comment-51811" class="comment"><div id="post-51811-score" class="comment-score"></div><div class="comment-text"><p>I am Sending HTTP get request with below url. "http://www.get-utc.appspot.com/getutc". For HTTP get request I added "Authorization: xxxx. User-Agent: curl/7.30.0 Accept: / Content-Type: application/json \r\n\r\n" headers. Then I captured this in wireshark.</p><p>I have one doubt. Content-type header is used in HTTP get method or not?</p><p>Could you please conform when we use content-type header field in HTTP.</p><p>Regrads, Swathi.</p></div><div id="comment-51811-info" class="comment-info"><span class="comment-age">(20 Apr '16, 02:29)</span> swathi jakkam</div></div><span id="51813"></span><div id="comment-51813" class="comment"><div id="post-51813-score" class="comment-score"></div><div class="comment-text"><p>The HTTP RFC defines NO "Content-Type" for GET requests only for HEAD requests and for repsonses (where it makes sense), so "Content-Type" should not appear in GET requests, as there is no "Content" in GET requests. POST requests might have a "Content-Type" as well.</p><p><a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html">https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html</a><br />
Section: 14.17 Content-Type</p><p>Later RFCs might define it differently. I did not check!</p><p>But this still does not explain the weird time stamps in the pcap! Something must be wrong on your capturing system.</p></div><div id="comment-51813-info" class="comment-info"><span class="comment-age">(20 Apr '16, 03:41)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-51810" class="comment-tools"></div><div class="clear"></div><div id="comment-51810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

