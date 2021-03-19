+++
type = "question"
title = "Get XHR response data from network traffic"
description = '''I am monitoring one website that as far I know refreshes data on page through ajax queries. At least I do not see the data inside the page source (html) but I see the data that I need to capture and analyze for example in  Chrome browser:  -&amp;gt; Developer tools  -&amp;gt; Network  -&amp;gt; XHR  -&amp;gt; pick/...'''
date = "2013-06-26T13:49:00Z"
lastmod = "2013-06-26T16:47:00Z"
weight = 22373
keywords = [ "ajax", "xmlhttprequest" ]
aliases = [ "/questions/22373" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get XHR response data from network traffic](/questions/22373/get-xhr-response-data-from-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22373-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am monitoring one website that as far I know refreshes data on page through ajax queries. At least I do not see the data inside the page source (html) but I see the data that I need to capture and analyze for example in Chrome browser: -&gt; Developer tools -&gt; Network -&gt; XHR -&gt; pick/click one ajax-link that appears to the list -&gt; response Chrome developer tools setting Log XMLHttpRequest must be checked.</p><p>How can I see it in wireshark or better in tshark (so I push it to the text file)?</p></div><div id="question-tags" class="tags-container tags">ajax xmlhttprequest</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/66592dd3f77b9981c53cf43697a7f8d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ristop&#39;s gravatar image" /><p>ristop<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ristop has no accepted answers">0%</span></p></div></div><div id="comments-container-22373" class="comments-container"></div><div id="comment-tools-22373" class="comment-tools"></div><div class="clear"></div><div id="comment-22373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22380"></span>

<div id="answer-container-22380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22380-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The request could be encrypted or scrambled (via javascript) or compressed and that's the reason why you cannot <strong>identify</strong> the requests in Wireshark.</p><p>Is if possible to post a sample capture somewhere (google docs, dropbox, etc.)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22380" class="comments-container"><span id="22405"></span><div id="comment-22405" class="comment"><div id="post-22405-score" class="comment-score"></div><div class="comment-text"><p>I post my comment as answer because comment is classified as spam.</p><p>Thanks for you quick answer. I updated the captured file to <a href="https://docs.google.com/file/d/0B84i2-8sFHT1WllJRVNEMVRzNW8/edit?usp=sharing">https://docs.google.com/file/d/0B84i2-8sFHT1WllJRVNEMVRzNW8/edit?usp=sharing</a></p><p>I captured data with filter ip.addr = &lt;site_ip_address&gt;. I hope it is correct because I can't read it in Wireshark window. It should look like html with line breaks (\n).</p></div><div id="comment-22405-info" class="comment-info"><span class="comment-age">(27 Jun '13, 07:35)</span> ristop</div></div><span id="22414"></span><div id="comment-22414" class="comment"><div id="post-22414-score" class="comment-score"></div><div class="comment-text"><p>There are a lot of TCP connections. Only a few are to external addresses and most connections a SSL/TLS. As I don't know the address of your server (please add that information) and there is no HTTP protocol on those connections (on ports other than 80,443), I guess your ajax connection uses SSL/TLS and that's why you cannot see anything in Wireshark. If the destination server is your own and you have access to the private key of the server, you can decrypt the communication in Wireshark. Otherwise, you will have to use already mentions tools <strong>within</strong> the browser, as those tools will see the unencrypted communication.</p><p>Another option is to use a HTTP proxy with SSL/TLS interception (google for fiddler2, or similar tools).</p></div><div id="comment-22414-info" class="comment-info"><span class="comment-age">(27 Jun '13, 08:29)</span> Kurt Knochner ♦</div></div><span id="22482"></span><div id="comment-22482" class="comment"><div id="post-22482-score" class="comment-score"></div><div class="comment-text"><p>Maybe the Ip.addr filter was not correct and data that I am interested in was transferred through other IP addresses. What I did was: - opened <a href="https://tonybet.com/live_events">https://tonybet.com/live_events</a> in Chrome browser - on the top of the page clicked "Bet type filter" and checked all types - opened wireshark and started to capture IP aadress 92.61.38.58 (ip.addr="92.61.38.58")</p><p>Depending on chenging frequency the data is updated in every 1-10 seconds. In Chrome Developer tools -&gt; Netweork -&gt; XHR -&gt; Response the data looks like (this is only fragment):</p><p><code> table class=\"events singleRow capsTable pushedLeft capsTableDouble running-live\"&gt;\n                          tr&gt;\n                            td class=\"sepThin\"&gt; /td&gt;\n                              td class=\"toSlip\"&gt;\n                                a class=\"price\" href=\"#\" data-event-odd-id=\"7913362\" id=\"event_odd_id_7913362\"&gt;\n                                  span&gt;6.50/span&gt;\n                                  Total UNDER\n                                    em class=\"var purple\"&gt; 1.5/em&gt;\n                                /a&gt;\n                              /td&gt;\n\n\n                              td class=\"toSlip\"&gt;\n                                a class=\"price\" href=\"#\" data-event-odd-id=\"7913361\" id=\"event_odd_id_7913361\"&gt;\n                                  span&gt;1.08/span&gt;\n</code></p></div><div id="comment-22482-info" class="comment-info"><span class="comment-age">(30 Jun '13, 01:31)</span> ristop</div></div></div><div id="comment-tools-22380" class="comment-tools"></div><div class="clear"></div><div id="comment-22380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

