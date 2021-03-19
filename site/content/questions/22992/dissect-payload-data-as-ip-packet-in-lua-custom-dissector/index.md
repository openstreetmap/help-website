+++
type = "question"
title = "Dissect payload data as IP packet in Lua custom dissector"
description = '''Hi, I have a packet which has some header fields and some payload. I&#x27;ve successfully written a dissector for the packet. So now I can see my own protocol&#x27;s and field values in Wireshark. Now, the payload data for my protocol is basically an IP Packet data. I want to parse that data as IP Packet and ...'''
date = "2013-07-16T02:20:00Z"
lastmod = "2013-07-16T03:36:00Z"
weight = 22992
keywords = [ "parsing", "ip", "dissector", "packet", "lua" ]
aliases = [ "/questions/22992" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dissect payload data as IP packet in Lua custom dissector](/questions/22992/dissect-payload-data-as-ip-packet-in-lua-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22992-score" class="post-score" title="current number of votes">0</div><span id="post-22992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a packet which has some header fields and some payload. I've successfully written a dissector for the packet. So now I can see my own protocol's and field values in Wireshark. Now, the payload data for my protocol is basically an IP Packet data. I want to parse that data as IP Packet and show as a subtree inside my protocol.</p><p>Can somebody tell me how to parse my data with a pre defined IP Packet parser/dissector which wireshark already uses to parse IP Packets.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '13, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/714464c8e18484edca8112221abd666d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atanudey&#39;s gravatar image" /><p><span>atanudey</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atanudey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jul '13, 03:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-22992" class="comments-container"></div><div id="comment-tools-22992" class="comment-tools"></div><div class="clear"></div><div id="comment-22992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22994"></span>

<div id="answer-container-22994" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22994-score" class="post-score" title="current number of votes">2</div><span id="post-22994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="atanudey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can somebody tell me how to parse my data with a pre defined IP Packet parser/dissector which wireshark already uses to parse IP Packets.</p></blockquote><p>You call the standard IP dissector with the remaining bytes of your payload.</p><p>See the l2tp dissector for an example:</p><blockquote><p>call_dissector(ip_handle, next_tvb, pinfo, tree);</p></blockquote><p>See also these similar questions.</p><blockquote><p><a href="http://ask.wireshark.org/questions/2334/calling-another-dissector">http://ask.wireshark.org/questions/2334/calling-another-dissector</a><br />
<a href="http://ask.wireshark.org/questions/11608/use-of-call_dissector">http://ask.wireshark.org/questions/11608/use-of-call_dissector</a></p></blockquote><p><strong>UPDATE</strong></p><blockquote><p>I've written my dissector in LUA. Will this work in LUA? When I'm trying it says -</p></blockquote><p>In Lua it works differently. See the following sample code.</p><blockquote><p><a href="http://www.wireshark.org/docs/wsug_html_chunked/wslua_dissector_example.html">http://www.wireshark.org/docs/wsug_html_chunked/wslua_dissector_example.html</a></p></blockquote><p>First you create a variable and assign it a dissector reference. Then you call the dissector like this:</p><blockquote><p>variable:call()</p></blockquote><p>In your case, something like this:</p><pre><code>local ip_dissector = Dissector.get(&quot;ip&quot;)
ip_dissector:call(...)</code></pre><p>See the Lua docs for more information about dissector calling and also this similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/18517/calling-lua-dissectors-from-lua-dissector">http://ask.wireshark.org/questions/18517/calling-lua-dissectors-from-lua-dissector</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jul '13, 05:40</strong> </span></p></div></div><div id="comments-container-22994" class="comments-container"><span id="22997"></span><div id="comment-22997" class="comment"><div id="post-22997-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your quick reply. I've written my dissector in LUA. Will this work in LUA? When I'm trying it says -</p><p>Lua Error: ...\Program Files\Wireshark\plugins\netcode\netcode.lua:372: attempt to call global 'call_dissector' (a nil value)</p><p>Thanks</p></div><div id="comment-22997-info" class="comment-info"><span class="comment-age">(16 Jul '13, 03:04)</span> <span class="comment-user userinfo">atanudey</span></div></div><span id="23000"></span><div id="comment-23000" class="comment"><div id="post-23000-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt, Thanks a lot. It's working perfectly :)</p></div><div id="comment-23000-info" class="comment-info"><span class="comment-age">(16 Jul '13, 03:35)</span> <span class="comment-user userinfo">atanudey</span></div></div><span id="23001"></span><div id="comment-23001" class="comment"><div id="post-23001-score" class="comment-score">1</div><div class="comment-text"><p>Great.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-23001-info" class="comment-info"><span class="comment-age">(16 Jul '13, 03:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22994" class="comment-tools"></div><div class="clear"></div><div id="comment-22994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

