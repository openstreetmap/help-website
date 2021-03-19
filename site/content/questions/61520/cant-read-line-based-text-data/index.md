+++
type = "question"
title = "Cant read line based text data"
description = '''I&#x27;m trying to read a post request which got captured using wireshark. Now i was wondering, if there&#x27;s a way to make the packet content readable, such as requests in fiddler to have readable data? I would appreciate any kind of suggestions. The Line-based Text data: application/json isnt readable als...'''
date = "2017-05-21T05:59:00Z"
lastmod = "2017-05-22T15:33:00Z"
weight = 61520
keywords = [ "wireshark" ]
aliases = [ "/questions/61520" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cant read line based text data](/questions/61520/cant-read-line-based-text-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61520-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to read a post request which got captured using wireshark.</p><p>Now i was wondering, if there's a way to make the packet content readable, such as requests in fiddler to have readable data?</p><p>I would appreciate any kind of suggestions.</p><p>The Line-based Text data: application/json isnt readable also as you can see in this screenshot:</p><p><img src="https://gyazo.com/ee53e0921c3cb9c6f40ec259d55c8190.png" alt="alt text" /></p><p>I would appreciate any kind of suggestions.</p><p>The captures packet(Wireshark-&gt;Follow TCP Stream) looks like the following: <a href="https://pastebin.com/h2kvaBYY">https://pastebin.com/h2kvaBYY</a></p><p>I would appreciate any kind of suggestions.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '17, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/3197b86c942898bad1161eb3a6af5dbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d4ne&#39;s gravatar image" /><p>d4ne<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d4ne has no accepted answers">0%</span></p></img></div></div><div id="comments-container-61520" class="comments-container"><span id="61524"></span><div id="comment-61524" class="comment"><div id="post-61524-score" class="comment-score"></div><div class="comment-text"><p>Could we either see more of the dissection, or the raw packet capture (not the results of Follow TCP Stream)? That way we can determine whether, for example, the data in question is encrypted, or compressed, or transformed in some other fashion that turns JSON text into binary data, as that's what appears to have happened.</p></div><div id="comment-61524-info" class="comment-info"><span class="comment-age">(21 May '17, 17:45)</span> Guy Harris ♦♦</div></div><span id="61536"></span><div id="comment-61536" class="comment"><div id="post-61536-score" class="comment-score"></div><div class="comment-text"><p>Heres one: <a href="https://pastebin.com/rE61rReD">https://pastebin.com/rE61rReD</a> and <a href="https://pastebin.com/0RvEP7p0">https://pastebin.com/0RvEP7p0</a> and a response to that request: <a href="https://pastebin.com/bBETmND4">https://pastebin.com/bBETmND4</a></p></div><div id="comment-61536-info" class="comment-info"><span class="comment-age">(22 May '17, 03:58)</span> d4ne</div></div></div><div id="comment-tools-61520" class="comment-tools"></div><div class="clear"></div><div id="comment-61520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61521"></span>

<div id="answer-container-61521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61521-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go to menu File | Export Objects | HTTP... That gives you the opportunity to save the object in a file, to be opened with the applicable program for that MIME type.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '17, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61521" class="comments-container"><span id="61522"></span><div id="comment-61522" class="comment"><div id="post-61522-score" class="comment-score"></div><div class="comment-text"><p>Yes, i did that before also. Some of those show up perfectly, others sadly like this:</p><p><em>*”cRkü´)ý¢ˆ?VóSN‘ÇLè5–Í Çî?ö\D~hƒöuvÁÙéuy\ŒIJ–ÍOá“I[›”&amp;Qu”LééiúDÈÛî¨aKˆ„-NF”t¹UgT&lt;Ë·Þ|–÷fKªÿjõâj?bÅÁoäZÍçwºÌBwUã}¼Ñz&amp;??Œ3œé?øˆAKL’ãutb‚¶?R`?¨å&gt;Œº!Ýªù^éQ'Pka ˜Ìßú-æ,^–mo«´¨ª´'Lëùåš£èzê»7ÿ»±p˜ú.PW˜Ý7µrÍ(­Ï<a href="https://ask.wireshark.org/users/12340/neajules">@ñe</a>†ÞéAšb ¶dþ~.Or§çàñ|è™üv-+ê†rîôèj§Ä4¦Ý´&gt;ÎSD¹M‚èÒO}=úÂ˜R´p½…Ü£DCŠ ±7çmš"ÙM¤[email protected]¼†èî~Ê[email protected]½‡&lt;qÍ‡ò±˜„I</em>™ìJÐžO¸?k«ÏwbÍ¨¸ôgû?ÉÎˆœ J»ÕýIÆ»6«¶·¶‰4?ª/§£S7àáŒÔTv</p><p>What could cause this? Maybe beeing json files at all transfered as byte?</p></div><div id="comment-61522-info" class="comment-info"><span class="comment-age">(21 May '17, 07:10)</span> d4ne</div></div></div><div id="comment-tools-61521" class="comment-tools"></div><div class="clear"></div><div id="comment-61521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61563"></span>

<div id="answer-container-61563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61563-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe it's <em>not</em> line-based text data; perhaps it's a binary encoding of JSON, such as the one given in the <a href="http://ubjson.org">Universal Binary JSON Specification</a>. One of your pastebin posts has "Content-Type: application/json", and <em>nothing</em> indicating that it's compressed. However, <a href="http://ubjson.org/#mime-type">the UBJSON people recommend application/ubjson</a>, so perhaps it's some other encoding, and perhaps both the client and server have an out-of-band arrangement to use some binary encoding. The first two pastebin posts have "Dalvik" in the User-Agent, so it's presumably coming from an Android phone or tablet - perhaps some app is communicating with a server from the app vendor, so it knows that the server can accept some binary form of JSON and will send a binary form of JSON back.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '17, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61563" class="comments-container"><span id="61568"></span><div id="comment-61568" class="comment"><div id="post-61568-score" class="comment-score"></div><div class="comment-text"><p>Hey, your right it's a app communicating with a server. The request is sent as Content-Type: application/octet-stream and the response is Content-Type: application/json</p><p>Also found the following code in the apk:</p><p><a href="https://pastebin.com/Demn2n4S">https://pastebin.com/Demn2n4S</a></p><p>This could be the encode/decode right?</p></div><div id="comment-61568-info" class="comment-info"><span class="comment-age">(23 May '17, 02:30)</span> d4ne</div></div></div><div id="comment-tools-61563" class="comment-tools"></div><div class="clear"></div><div id="comment-61563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

