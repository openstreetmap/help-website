+++
type = "question"
title = "Exporting multiple audio/mpeg packets"
description = '''I&#x27;m new to writing Lua scripts in Wireshark, so maybe my question is stupid, but is it possible to write a Lua script that will export all audio/mpeg packets from a capture? I can do this manually in Wireshark by applying a display filter (http.content_type == &quot;audio/mpeg&quot;), then right-clicking each...'''
date = "2011-08-02T05:41:00Z"
lastmod = "2011-08-02T17:14:00Z"
weight = 5397
keywords = [ "listener", "lua", "tap", "export" ]
aliases = [ "/questions/5397" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting multiple audio/mpeg packets](/questions/5397/exporting-multiple-audiompeg-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5397-score" class="post-score" title="current number of votes">0</div><span id="post-5397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to writing Lua scripts in Wireshark, so maybe my question is stupid, but is it possible to write a Lua script that will export all audio/mpeg packets from a capture? I can do this manually in Wireshark by applying a display filter (<code>http.content_type == "audio/mpeg"</code>), then right-clicking each Media Type in the Packet Details window, and then selecting <code>'Export selected packet bytes'</code>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-listener" rel="tag" title="see questions tagged &#39;listener&#39;">listener</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '11, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/efb8199151deace5e386a3a21b0dad2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesper&#39;s gravatar image" /><p><span>Jesper</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesper has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '11, 17:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5397" class="comments-container"></div><div id="comment-tools-5397" class="comment-tools"></div><div class="clear"></div><div id="comment-5397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5411"></span>

<div id="answer-container-5411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5411-score" class="post-score" title="current number of votes">0</div><span id="post-5411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it's possible. See another <a href="http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload#answer-container-4835">post</a> where Lua was used to extract the XML payload from TCP into a file. In your case, your tap would be defined as:</p><pre><code>Listener.new(nil, &#39;http.content_type == &quot;audio/mpeg&quot;&#39;)</code></pre><p>If your capture contains multiple audio/mpeg streams, you'd also have to modify that Lua to separate the streams into their own files (assuming that's detectable from your protocol).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '11, 17:14</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-5411" class="comments-container"></div><div id="comment-tools-5411" class="comment-tools"></div><div class="clear"></div><div id="comment-5411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

