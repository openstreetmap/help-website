+++
type = "question"
title = "Decompress gzip POST frame"
description = '''I have the following HTTP frame: POST /Usage/Upload?compression=gzip HTTP/1.1 How can I show it decompressed? Please note: It is a POST (to the server) not a GET (from the server)'''
date = "2013-07-02T10:46:00Z"
lastmod = "2013-07-02T13:04:00Z"
weight = 22560
keywords = [ "gzip" ]
aliases = [ "/questions/22560" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decompress gzip POST frame](/questions/22560/decompress-gzip-post-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22560-score" class="post-score" title="current number of votes">0</div><span id="post-22560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following HTTP frame: POST /Usage/Upload?compression=gzip HTTP/1.1 How can I show it decompressed? Please note: It is a POST (to the server) not a GET (from the server)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gzip" rel="tag" title="see questions tagged &#39;gzip&#39;">gzip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/659f11e281d7a7907695787c55a31e19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hanky&#39;s gravatar image" /><p><span>Hanky</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hanky has no accepted answers">0%</span></p></div></div><div id="comments-container-22560" class="comments-container"></div><div id="comment-tools-22560" class="comment-tools"></div><div class="clear"></div><div id="comment-22560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22561"></span>

<div id="answer-container-22561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22561-score" class="post-score" title="current number of votes">0</div><span id="post-22561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>POST /Usage/Upload?compression=gzip</p></blockquote><p>sounds like your application is doing the compression, so it's (most certainly) not the built in compression available in HTTP. As I don't have a sample capture file, I would say, that it's only possible to show the POST payload uncompressed</p><ul><li>if you know the exact encoding used for the POST payload. It could be not just gzip compressed, but it could contain it's own data structure (length information, structure information), where only parts are compressed.</li><li>if you extract the compressed data manually (or via a script) and then use a command line tool to decompress it. To extract the data, you can use the "Follow TCP Stream" feature of Wireshark (right click the POST request and select that option).</li></ul><p>BTW: If you are able to provide a sample capture file (google docs, dropbox, etc.) we might be able to give more information/details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22561" class="comments-container"><span id="22563"></span><div id="comment-22563" class="comment"><div id="post-22563-score" class="comment-score"></div><div class="comment-text"><p>POST /Usage/Upload?compression=gzip HTTP/1.1</p><p>Host: services.robotstudio.com</p><p>Content-Length: 1388</p><p>Expect: 100-continue</p><p>Connection: Keep-Alive</p><p>HTTP/1.1 100 Continue</p><p>H4sIAAAAAAAEAOy9B2AcSZYlJi9tynt/SvVK1+B0oQiAYBMk2JBAEOzBiM3mkuwdaUcjKasqgcplVmVdZhZAzO2dvPfee++999577733ujudTif33/8/XGZkAWz2zkrayZ4hgKrIHz9+fB8/Iv7Hv/cffFVNqvZ1u54V1VdNdpH/zE/u/sbJNj3fPj1+evoqfXL6+dkL/P0bJ6/zpimq5dnss/Pz3XzvfO98+/4s393ef7CTbx/sne9v39vNHh5k9x7s39slKF9k03mxzNF+crCT55OH2/f3HlD73f2d7cn93U+3s8n+7GC6f29n9nDfwn/dZnX72c6Duzt7d/d2du+luzuP9nYf7d0PW3zVTv1GOwem0Zevz2b5si3Oi7z+7ItiWldNdd6m3y2Ws+qqSV+8ST8d744ffLqzm77O68timqcvs+nbdBev/mReo4fPTJPxp/fv3/sU3zzPlhdrItBn+XL7q9c/c7q8KItmnm59tSzafJYSTm3e3EHLJ0W7JEQ/u7f3Gycnz18ZkPvjnfG9nXu7D8fU0/NqmpU3wjperczb98e798f7Dx/ujfc+pfefrIty9ia7+OxlXc3W05aacPOTarHIlrPnRPfPPjp59PvS1xd1tkifFWXe/L7HT56kZ8vZumnrIivTsze/L09/MW3s78IKKbr7fZ8US//Dcf4u/yjlbvwh0p+3pQ1hM6XXqvqkqvOTar1sP9v1Pn1eXRREFvfF/LrBB1/ki6q+/mx358G9vZ2H9/aJVz4/f3eS1bMX2SJvPvvJL66yOk9f/+Tnx+m9p/zl07q4zOun6Pcz4o+93Z2de94XStXmswfj3X2aampA/b1YL54WzarMrhvBq1hk9bV+9CpvqnINQn+2u3ew8+5gZ+c3Tl7ly1leE589Lep82qLzp9UiK5afPS4xw0c009nyi+OTz3Z2tndOtvcebt+7v/303vZ9YtTv0js0Kw2+frxevl1WV0t6gaZwtW7z+otsuT7Ppu0a8GWII5q96dhrUs3y0gz/ J4u6XdOsviyz9ryqFzSAk9fXTZsv3lyv8s8I2+fE68uGKGJ/fZZngO998jy/JJDP6jwHAfJFsV7oNwzlxTHJdbEkwpRny6bNSmqblQ01fkIyRB9c5CydL8EN9qM32eRFfgW8y6p+M88X9F25zgNFc/riqagZ/Pv8y899zbOz84j+t38wPiDKH9w/+JnTd/mU5mJ5ofz+M+Dv03dF+zPHJAuXNO0z/639e5+6t/JZ9yXXZ4DE6zfHb177aLypaMBvCsLegX6wf0Cg9TvLyV4j0iFg2d094tqXefb2u1X9lhB/nbefPTy4v7Pz6c6BfKHz97r4Qf7ZPfr03r0dvOMwscj9PwEAAP//WtE9aLcFAAA= HTTP/1.1 200 OK</p><p>Cache-Control: private</p><p>Server: Microsoft-IIS/8.0</p><p>X-AspNet-Version: 4.0.30319</p><p>X-Powered-By: ASP.NET</p><p>Date: Tue, 02 Jul 2013 08:34:40 GMT</p><p>Content-Length: 0</p></div><div id="comment-22563-info" class="comment-info"><span class="comment-age">(02 Jul '13, 11:24)</span> <span class="comment-user userinfo">Hanky</span></div></div><span id="22566"></span><div id="comment-22566" class="comment"><div id="post-22566-score" class="comment-score"></div><div class="comment-text"><p>that's not only compressed but also MIME encoded.</p><p>You can decode it on Linux with this command:</p><blockquote><p><code>base64 -d input.txt | gunzip -d</code></p></blockquote><p>Result (part of it):</p><pre><code>RobotStudioUsage|V1
----HEADER BEGIN----
SessionId=ff1e2f2f-5de1-470e-82f4-31a98a374311
MachineId=fb80eeb9-5271-4140-b516-ab4d8c430d94
SessionStart=07/02/2013 10:21:25
SessionStartUtc=07/02/2013 08:21:25
OSIdentifier=Microsoft Windows NT 6.1.7601 Service Pack 1
OSVersion=6.1.7601.65536
OSLanguage=en-US|English (United States)
OSBitness=32
CLRVersion=4.0.30319.1
Locale=en-US|English (United States)
AppVersion=5.15.4992.261
BuildTag=Production
AppCommandLine=&quot;C:\Program Files\ABB Industrial IT\Robotics IT\RobotStudio 5.15\Bin\RobotStudio.exe&quot; 
AppBitness=32
AppLanguage=en-US|English (United States)
ProcessorCoreCount=1
ProcessorLogicalCount=1
PhysicalMemory=1073209344
GfxCardNames=VMware SVGA 3D
GfxDriverDates=20121003
GfxDriverVersions=7.14.1.1211
NumDisplays=1
PrimaryDisplayResolution=1280x800
Renderer=Direct3D
Domain=&lt;local&gt;
LanMAC=00-0C-29-35-D3-55
WirelessMAC=&lt;unknown&gt;
ComputerManufacturer=VMware, Inc.
ComputerModel=VMware </code></pre></div><div id="comment-22566-info" class="comment-info"><span class="comment-age">(02 Jul '13, 11:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22569"></span><div id="comment-22569" class="comment"><div id="post-22569-score" class="comment-score"></div><div class="comment-text"><p>As <span>@Kurt</span> suspected, the compression is done at the (web)application layer, not at the HTTP layer. This means wireshark has no knowledge on how to interpret the data and is therefor not able to decompress it for you.</p></div><div id="comment-22569-info" class="comment-info"><span class="comment-age">(02 Jul '13, 13:04)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-22561" class="comment-tools"></div><div class="clear"></div><div id="comment-22561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

