+++
type = "question"
title = "streaming url"
description = '''Can one use wireshark to find the correct streaming url of a webradio, like http://www.chanson.ru/on-line.html? I would like to record their songs with audial one. If one can find the url, how does one do it specifically (in detail please, I&#x27;m a newbie here)? Thanks in advance gfheiche'''
date = "2012-08-07T07:51:00Z"
lastmod = "2016-06-28T05:04:00Z"
weight = 13425
keywords = [ "url", "streaming" ]
aliases = [ "/questions/13425" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [streaming url](/questions/13425/streaming-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13425-score" class="post-score" title="current number of votes">0</div><span id="post-13425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can one use wireshark to find the correct streaming url of a webradio, like <a href="http://www.chanson.ru/on-line.html?">http://www.chanson.ru/on-line.html?</a> I would like to record their songs with audial one.</p><p>If one can find the url, how does one do it specifically (in detail please, I'm a newbie here)?</p><p>Thanks in advance gfheiche</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-streaming" rel="tag" title="see questions tagged &#39;streaming&#39;">streaming</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '12, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/e5441987e8a183d45944176acf57f667?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gfheiche&#39;s gravatar image" /><p><span>gfheiche</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gfheiche has no accepted answers">0%</span></p></div></div><div id="comments-container-13425" class="comments-container"></div><div id="comment-tools-13425" class="comment-tools"></div><div class="clear"></div><div id="comment-13425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13464"></span>

<div id="answer-container-13464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13464-score" class="post-score" title="current number of votes">0</div><span id="post-13464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Close all other applications, except the browser</li><li>Close all tabs in the browser, except the one that loads the web radio page</li><li>Capture the whole traffic of your system, while you listen to the radio stream. <strong>HINT:</strong> You must start the capture before you click on the "Play" button/link. Don't use any capture filter!</li><li>Look at the TCP statstics (<code>Statistics -&gt; Conversation List -&gt; TCP</code>)</li><li>Sort the out for "Bytes" or "Packets"</li><li>The connection with the most Bytes/Packets is most certainly the audio stream</li><li>Click on that connection and then click on "Follow Stream"</li><li>At the beginning of the TCP connection, you should see the URL (if it was streamed via HTTP).</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '12, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13464" class="comments-container"><span id="13469"></span><div id="comment-13469" class="comment"><div id="post-13469-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, it did not give me the streaming url. It seems from the stations <a href="http://www.chanson.ru/on-line.html">http://www.chanson.ru/on-line.html</a> page source that it is written in java. Thank you very much for your detailed and clear help</p><p>Regards gfheiche</p></div><div id="comment-13469-info" class="comment-info"><span class="comment-age">(08 Aug '12, 06:25)</span> <span class="comment-user userinfo">gfheiche</span></div></div><span id="13473"></span><div id="comment-13473" class="comment"><div id="post-13473-score" class="comment-score"></div><div class="comment-text"><p>it is using a flash player (<a href="http://www.longtailvideo.com/players/jw-flv-player">JW Player</a>) to stream the music. The URL is:</p><blockquote><p><code>http://chanson.cdnvideo.ru/rr/chanson.stream/playlist.m3u8</code><br />
</p></blockquote><p>You can find it by using the following display filter:</p><blockquote><p><code>http.request or http.response</code></p></blockquote><p>then look into the HTML code to find the URL.</p></div><div id="comment-13473-info" class="comment-info"><span class="comment-age">(08 Aug '12, 07:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13508"></span><div id="comment-13508" class="comment"><div id="post-13508-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt, You solved the problem, thank you very much for your great help and patience Regards gfheiche</p></div><div id="comment-13508-info" class="comment-info"><span class="comment-age">(09 Aug '12, 04:23)</span> <span class="comment-user userinfo">gfheiche</span></div></div><span id="13509"></span><div id="comment-13509" class="comment"><div id="post-13509-score" class="comment-score"></div><div class="comment-text"><p>you are welcome. good luck with recording the music.</p></div><div id="comment-13509-info" class="comment-info"><span class="comment-age">(09 Aug '12, 04:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28296"></span><div id="comment-28296" class="comment"><div id="post-28296-score" class="comment-score"></div><div class="comment-text"><p>Hi. I'm looking for the URL, but it is using a flash player, when i look in the "Follow TPC stream" i get this:</p><p>GET /WRADIOAAC?uuid=bf9b2e80-e3cc-4f6b-9024-72d5c1c535b6 HTTP/1.1 Host: 3653.live.streamtheworld.com User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,<em>/</em>;q=0.8 Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate DNT: 1 Referer: <a href="http://player.tritondigital.com/api/swf/tdplayer-api-1.0.swf?cb_1387476401319">http://player.tritondigital.com/api/swf/tdplayer-api-1.0.swf?cb_1387476401319</a> Cookie: uuid=bf9b2e80-e3cc-4f6b-9024-72d5c1c535b6; a2x-an-uid=7425422285700592210 Connection: keep-alive</p><p>HTTP/1.0 200 OK Expires: Thu, 17 Jan 2031 16:00:00 GMT Cache-Control: no-cache, must-revalidate Pragma: no-cache Content-Length: 2100000000 Set-Cookie: uuid=bf9b2e80-e3cc-4f6b-9024-72d5c1c535b6; expires=Sat, 22-Dec-2029 21:30:41 GMT; path=/; domain=.live.streamtheworld.com Content-Type: application/flv</p><p>I DONT SEE THE HTML CODE AFTER apply "http.request or http.response"</p><p>Thnks for the support, greeting from Colombia.</p></div><div id="comment-28296-info" class="comment-info"><span class="comment-age">(19 Dec '13, 10:34)</span> <span class="comment-user userinfo">Juankof Enri...</span></div></div><span id="53697"></span><div id="comment-53697" class="comment not_top_scorer"><div id="post-53697-score" class="comment-score"></div><div class="comment-text"><p>I got my url doing this, ty so much</p><p><a href="http://14093.live.streamtheworld.com:80/CRP_PLAAAC_SC">http://14093.live.streamtheworld.com:80/CRP_PLAAAC_SC</a></p><p><a href="http://planeta.pe/radioenvivo">http://planeta.pe/radioenvivo</a></p><ul><li>GET <strong>/CRP_PLAAAC</strong>?banners=swf%2Cvpaid&amp;uuid=f07a40e0-8721-4f1b-a6fb-aa0aa4e4bd3c HTTP/1.1</li></ul><p>Host: <strong>14093.live.streamtheworld.com</strong></p><p>Connection: keep-alive User-Agent:</p><p>Mozilla/5.0 (Windows NT 10.0; WOW64)</p><p>AppleWebKit/537.36 (KHTML, like</p><p>Gecko) Chrome/51.0.2704.103</p><p>Safari/537.36 X-Requested-With:</p><p>ShockwaveFlash/22.0.0.192 Accept: <em>/</em></p><p>Referer:</p><p><a href="http://planeta.pe/radioenvivo">http://planeta.pe/radioenvivo</a></p><p>Accept-Encoding: gzip, deflate, sdch</p><p>Accept-Language: es,en;q=0.8,ko;q=0.6</p><p>Cookie:</p><p>uuid=f07a40e0-8721-4f1b-a6fb-aa0aa4e4bd3c</p><p>HTTP/1.0 200 OK Expires: Thu, 01 Dec</p><p>2003 16:00:00 GMT Cache-Control:</p><p>no-cache, must-revalidate Pragma:</p><p>no-cache</p><p>Access-Control-Allow-Methods: GET,</p><p>HEAD Access-Control-Allow-Origin: *</p><p>Access-Control-Allow-Credentials:</p><p>true Set-Cookie:</p><p>uuid=f07a40e0-8721-4f1b-a6fb-aa0aa4e4bd3c;</p><p>expires=Sat, 22-Dec-2029 21:30:41</p><p>GMT; path=/;</p><p>domain=.live.streamtheworld.com</p><p>Content-Type: application/flv</p></div><div id="comment-53697-info" class="comment-info"><span class="comment-age">(28 Jun '16, 05:04)</span> <span class="comment-user userinfo">Milumon</span></div></div></div><div id="comment-tools-13464" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-13464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

