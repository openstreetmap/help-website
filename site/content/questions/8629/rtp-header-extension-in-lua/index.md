+++
type = "question"
title = "RTP Header extension in Lua"
description = '''I want to write a dissector to manage some header extensions for RTP protocol. Searching in code, I saw that we need to write a sub-dissector and that it would be called instead of the generic header extension, but how do I register my dissector to the list of sub-dissectors in Lua? Update Where is ...'''
date = "2012-01-26T12:04:00Z"
lastmod = "2012-01-27T05:44:00Z"
weight = 8629
keywords = [ "lua", "dissector", "rtp" ]
aliases = [ "/questions/8629" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [RTP Header extension in Lua](/questions/8629/rtp-header-extension-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8629-score" class="post-score" title="current number of votes">1</div><span id="post-8629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write a dissector to manage some header extensions for RTP protocol. Searching in code, I saw that we need to write a sub-dissector and that it would be called instead of the generic header extension, but how do I register my dissector to the list of sub-dissectors in Lua?</p><h2 id="update">Update</h2><p>Where is the payload type string locate?</p><p>In the packet I want to analyses, it said that payload type is <code>DinamicRTP-Type-98 (98)</code>.</p><p>I think the real payload type is defined in a RTSP/SDF packet I received a fiew packets ago. Here is it's RTSP content:</p><pre><code>RTSP/1.0 200 OK
CSeq: 2
Connection: Keep-Alive
Content-Base: rtsp://10.2.23.28/Storage/
Content-Type: application/sdp
Content-Length: 166

v=0o=- 1 1 IN IP4 10.2.23.28
s=Media Presentation
e=NONE
c=IN IP4 0.0.0.0
t=0 0
a=control:*
m=video 0 RTP/AVP 98
a=rtpmap:98 H264/90000
a=control:trackID=1</code></pre><p>With that said, what should be the payload_str_type?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '12, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/a916d30b27a92a26b4144a88b2791471?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdesharnais&#39;s gravatar image" /><p><span>mdesharnais</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdesharnais has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jan '12, 06:05</strong> </span></p></div></div><div id="comments-container-8629" class="comments-container"></div><div id="comment-tools-8629" class="comment-tools"></div><div class="clear"></div><div id="comment-8629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8641"></span>

<div id="answer-container-8641" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8641-score" class="post-score" title="current number of votes">1</div><span id="post-8641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mdesharnais has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This should work:</p><pre><code>local proto_foo = Proto(&quot;foo&quot;, &quot;Foo Protocol&quot;)
function proto_foo.dissector(buf, pinfo, tree)
  -- ...
end
DissectorTable.get(&#39;rtp_hdr_ext&#39;):add(&#39;payload_type_str&#39;, proto_foo)</code></pre><p>where <em><code>payload_type_str</code></em>, in your case, is the encoding name, which is parsed from the <code>rtpmap</code> media attribute (the text between the space and slash):</p><pre><code>a=rtpmap:98 H264/90000</code></pre><p>So, you would use:</p><pre><code>DissectorTable.get(&#39;rtp_hdr_ext&#39;):add(&#39;H264&#39;, proto_foo)</code></pre><p>Unfortunately, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5208">Bug 5208</a> prevents this subdissector from being called.</p><p><strong>UPDATE:</strong> According to <del><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6783">Bug 6783</a></del>, this dissector table is actually supposed to key off the RTP header extension ID (a 16-bit integer) instead of the encoding name (a string). Thus, <code>rtp_hdr_ext</code> has been changed from a string table to an integer table, and example usage would be:</p><pre><code>DissectorTable.get(&#39;rtp_hdr_ext&#39;):add(0xA123, proto_foo)</code></pre><p>You can try SVN 40834 (or later) or download an <a href="http://www.wireshark.org/download/automated/">automated build</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '12, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Feb '12, 10:28</strong> </span></p></div></div><div id="comments-container-8641" class="comments-container"><span id="8653"></span><div id="comment-8653" class="comment"><div id="post-8653-score" class="comment-score"></div><div class="comment-text"><p>Tanks for your answer. But I am not sure what the payload_type_str is suppose to be in my case. I've just edit my initial question to explain further my situation. Can you please have a look?</p></div><div id="comment-8653-info" class="comment-info"><span class="comment-age">(27 Jan '12, 05:44)</span> <span class="comment-user userinfo">mdesharnais</span></div></div></div><div id="comment-tools-8641" class="comment-tools"></div><div class="clear"></div><div id="comment-8641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

