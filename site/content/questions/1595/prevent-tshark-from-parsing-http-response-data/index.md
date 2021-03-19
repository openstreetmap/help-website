+++
type = "question"
title = "Prevent tshark from parsing http response data"
description = '''I&#x27;m running tshark on a web-surfing capture and noticed than it parses the http response&#x27;s data (when I choose PDML as the output format). This is somewhat annoying when the response consists of an image. I would rather get a blob of data which I can view later as an image, than the PNG&#x27;s headers an...'''
date = "2011-01-03T07:08:00Z"
lastmod = "2011-01-03T07:55:00Z"
weight = 1595
keywords = [ "pdml", "http", "tshark" ]
aliases = [ "/questions/1595" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Prevent tshark from parsing http response data](/questions/1595/prevent-tshark-from-parsing-http-response-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1595-score" class="post-score" title="current number of votes">0</div><span id="post-1595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running tshark on a web-surfing capture and noticed than it parses the http response's data (when I choose PDML as the output format). This is somewhat annoying when the response consists of an image. I would rather get a blob of data which I can view later as an image, than the PNG's headers and their values. Here's an example:</p><pre><code>&lt;proto name=&quot;png&quot; showname=&quot;Portable Network Graphics&quot; size=&quot;3933&quot; pos=&quot;631&quot;&gt;
&lt;field name=&quot;png.signature&quot; showname=&quot;PNG Signature: 89504E470D0A1A0A&quot; size=&quot;8&quot; pos=&quot;631&quot; show=&quot;89:50:4e:47:0d:0a:1a:0a&quot; value=&quot;89504e470d0a1a0a&quot;/&gt;
&lt;field name=&quot;&quot; show=&quot;IHDR Image Header&quot; size=&quot;33&quot; pos=&quot;639&quot; value=&quot;0000000d49484452000000300000003008060000005702f9870000000467414d41&quot;&gt;
  &lt;field name=&quot;png.chunk.len&quot; showname=&quot;Len: 13&quot; size=&quot;4&quot; pos=&quot;639&quot; show=&quot;13&quot; value=&quot;0000000d&quot;/&gt;
  &lt;field name=&quot;png.chunk.type&quot; showname=&quot;Chunk: IHDR&quot; size=&quot;4&quot; pos=&quot;643&quot; show=&quot;IHDR&quot; value=&quot;49484452&quot;&gt;
    &lt;field name=&quot;png.ihdr.width&quot; showname=&quot;Width: 48&quot; size=&quot;4&quot; pos=&quot;647&quot; show=&quot;48&quot; value=&quot;00000030&quot;/&gt;
    &lt;field name=&quot;png.ihdr.height&quot; showname=&quot;Height: 48&quot; size=&quot;4&quot; pos=&quot;651&quot; show=&quot;48&quot; value=&quot;00000030&quot;/&gt;</code></pre><p>(and it goes on and on)</p><p>Is there a way to get tshark to "dechunk" and decompress the response's data, without it going further and parse the data itself? I Couldn't find this option in Wireshark's config file, but maybe I've missed it.</p><p>Thanks (and a happy new year!)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '11, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/9b7b5e633f7836289c2fc6c3934bffaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r0u1i&#39;s gravatar image" /><p><span>r0u1i</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r0u1i has no accepted answers">0%</span></p></div></div><div id="comments-container-1595" class="comments-container"></div><div id="comment-tools-1595" class="comment-tools"></div><div class="clear"></div><div id="comment-1595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1596"></span>

<div id="answer-container-1596" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1596-score" class="post-score" title="current number of votes">2</div><span id="post-1596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="r0u1i has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try disabling the PNG protocol (under Analyze ! Enabled Protocols ...)</p><p>The above is for Wireshark.</p><p>If you do the above and then run tshark, the protocol will also be disabled in tshark since tshark reads the "disabled_protos" configuration file created when the protocol is disabled in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '11, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jan '11, 07:50</strong> </span></p></div></div><div id="comments-container-1596" class="comments-container"><span id="1600"></span><div id="comment-1600" class="comment"><div id="post-1600-score" class="comment-score"></div><div class="comment-text"><p>Thanks, should have thought about it on my own!</p></div><div id="comment-1600-info" class="comment-info"><span class="comment-age">(03 Jan '11, 07:55)</span> <span class="comment-user userinfo">r0u1i</span></div></div></div><div id="comment-tools-1596" class="comment-tools"></div><div class="clear"></div><div id="comment-1596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

