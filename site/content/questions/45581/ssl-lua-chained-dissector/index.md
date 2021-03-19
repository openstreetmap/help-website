+++
type = "question"
title = "SSL LUA chained dissector"
description = '''Hi everyone, I&#x27;m trying to do something that appears simple enough for HTTP, but seems impossible for SSL/TLS. I would very much appreciate your take on this. What am I trying to do?  I&#x27;m trying to read the ssl fields provided by the ssl dissector so I can add additional information based on cross-s...'''
date = "2015-09-01T17:41:00Z"
lastmod = "2015-09-03T06:44:00Z"
weight = 45581
keywords = [ "dissectortable", "ssl", "postdissector", "chained-dissector", "lua" ]
aliases = [ "/questions/45581" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL LUA chained dissector](/questions/45581/ssl-lua-chained-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45581-score" class="post-score" title="current number of votes">0</div><span id="post-45581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I'm trying to do something that appears simple enough for HTTP, but seems impossible for SSL/TLS. I would very much appreciate your take on this.</p><p><strong>What am I trying to do?</strong></p><ul><li>I'm trying to read the ssl fields provided by the ssl dissector so I can add additional information based on cross-sslrecord content.</li><li>An example: showing on the frame containing a 'ClientHello' message, that renegotiation is not only supported but has also been requested by the server or client (i.e. like there is a HelloRequest message further down the line)</li><li>I need to post-parse the ssl. <em>fields, but they do not fill by default upon pcap load. I need to click a frame containing an SSL record, then I get access, in code, to the ssl.</em> fields of that frame.</li><li>I want the code to run on pcap load, but after the ssl dissector has been run completely. So I thought: post-dissector... but no; then I thought: replacing the ssl dissector with my own and my own dissector calls the original ssl dissector first. This is even a textbook example for 'chained dissector' from the wiki (<a href="https://wiki.wireshark.org/Lua/Dissectors)">https://wiki.wireshark.org/Lua/Dissectors)</a></li></ul><p><strong>The problem?</strong></p><ul><li>Chaining does not seem to work with the SSL dissector.</li><li>my code works perfectly if I choose another port than 443.</li><li>444 works (a port for which the TCP dissector table has no entry yet)</li><li>80 works (a port for which the TCP dissector table has an existing entry, namely 'HTTP')</li><li>443 does not work (the dissector table keeps showing me 'SSL' instead of my 'SSLTS'; on the other ports it does replace the original with mine)</li></ul><p><strong>Here's the code I use:</strong> (change 443 to 80 =&gt; it works, you get extra fields, etc, if you use 443, you need to select 'Decode As...' on a stream)</p><pre><code>do
local sslts = Proto(&quot;sslts&quot;,&quot;SSL/TLS Troubleshooting Information&quot;);
local sslts_issue = ProtoField.string(&quot;sslts.issue&quot;)
sslts.fields = {sslts_issue}
local original_ssl_dissector

function sslts.dissector(tvb,pinfo,tree)
    original_ssl_dissector:call(tvb,pinfo,tree)
    local subtree = tree:add(sslts,tvb)
    subtree:add(sslts_issue,tvb(),&quot;---&quot;)
end

local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
original_ssl_dissector = tcp_dissector_table:get_dissector(443)
tcp_dissector_table:add(443, sslts)

local function heur_dissect_sslts(tvbuf,pktinfo,root)
    sslts.dissector(tvbuf,pktinfo,root)
    pktinfo.conversation = sslts
    return true
end

sslts:register_heuristic(&quot;tcp&quot;,heur_dissect_sslts)</code></pre><p>end</p><p><strong>My questions?</strong></p><ul><li>Can it be done with the SSL dissector and LUA, or am I stuck doing it in C?</li><li>If it can be done and someone did it, can you show/explain me how?</li><li>Next to chained dissectors and post-dissectors, would there be any other way that I am missing at the moment?</li></ul><p>Kind regards and many thanks in advance for when I get a response on this one :D</p><p>Thomas Schockaert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissectortable" rel="tag" title="see questions tagged &#39;dissectortable&#39;">dissectortable</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span> <span class="post-tag tag-link-chained-dissector" rel="tag" title="see questions tagged &#39;chained-dissector&#39;">chained-dissector</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '15, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/effa49fcdd6b45fbb0f385d37134e94b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sstm&#39;s gravatar image" /><p><span>sstm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sstm has no accepted answers">0%</span></p></div></div><div id="comments-container-45581" class="comments-container"><span id="45582"></span><div id="comment-45582" class="comment"><div id="post-45582-score" class="comment-score"></div><div class="comment-text"><p>And lest I forget, my version is this: Version 1.12.7 (v1.12.7-0-g7fc8978 from master-1.12)</p></div><div id="comment-45582-info" class="comment-info"><span class="comment-age">(01 Sep '15, 17:43)</span> <span class="comment-user userinfo">sstm</span></div></div></div><div id="comment-tools-45581" class="comment-tools"></div><div class="clear"></div><div id="comment-45581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45584"></span>

<div id="answer-container-45584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45584-score" class="post-score" title="current number of votes">0</div><span id="post-45584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I haven't investigated your Lua code or original issue, but a quick answer that might or might not be sufficient...</p><p>Change this:</p><pre><code>tcp_dissector_table:add(443, sslts)</code></pre><p>To this:</p><pre><code>tcp_dissector_table:set(443, sslts)</code></pre><p>The <code>add()</code> call adds your dissector but also leaves existing ones in place, whereas the <code>set()</code> one replaces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Sep '15, 19:34</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-45584" class="comments-container"><span id="45586"></span><div id="comment-45586" class="comment"><div id="post-45586-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel,</p><p>Thanks for your response! Unfortunately it doesn't help. The problem remains: I need to manually 'Decode As' to get my fields on a frame containing SSL/TLS, whereas if I use port 80 (with :set and :add) I don't need to do this.</p><p>Kind regards,</p><p>Thomas</p></div><div id="comment-45586-info" class="comment-info"><span class="comment-age">(01 Sep '15, 23:41)</span> <span class="comment-user userinfo">sstm</span></div></div></div><div id="comment-tools-45584" class="comment-tools"></div><div class="clear"></div><div id="comment-45584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45615"></span>

<div id="answer-container-45615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45615-score" class="post-score" title="current number of votes">0</div><span id="post-45615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I tried your script and it works fine for me (I added a "<code>ct_val</code>" field to show the <code>ssl.record.content_type</code> field from the SSL layer, to show the Lua plugin got it):</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2015-09-03_at_9.38.52_AM.png" alt="alt text" /></p><p>Perhaps you have a preference setting wrong? Does your HTTP protocol preference setting for SSL not have 443 for the port?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '15, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '15, 06:44</strong> </span></p></div></div><div id="comments-container-45615" class="comments-container"></div><div id="comment-tools-45615" class="comment-tools"></div><div class="clear"></div><div id="comment-45615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

