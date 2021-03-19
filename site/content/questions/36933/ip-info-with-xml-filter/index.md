+++
type = "question"
title = "IP info with &#x27;xml&#x27; filter?"
description = '''Hi, I&#x27;m trying to extract SOAP payloads with timestamps and source/dest IP addresses and ports with the following code: local tap = Listener.new(nil, &quot;xml&quot;, true) local xml_field = Field.new(&quot;xml&quot;)  function tap.packet(pinfo,tvb,tapinfo)  local xml_string = string.gsub(tostring(xml_field().value), &quot;...'''
date = "2014-10-08T14:47:00Z"
lastmod = "2014-10-09T11:39:00Z"
weight = 36933
keywords = [ "lua" ]
aliases = [ "/questions/36933" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IP info with 'xml' filter?](/questions/36933/ip-info-with-xml-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36933-score" class="post-score" title="current number of votes">0</div><span id="post-36933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to extract SOAP payloads with timestamps and source/dest IP addresses and ports with the following code:</p><pre><code>local tap = Listener.new(nil, &quot;xml&quot;, true)
local xml_field = Field.new(&quot;xml&quot;)

function tap.packet(pinfo,tvb,tapinfo)
    local xml_string = string.gsub(tostring(xml_field().value), &quot;(..)&quot;,
        function(c) c=tonumber(c,16); if c==13 or c==10 then c=0 end; return string.char(c) end)
    print( table.concat( {
              os.date(&quot;%Y-%m-%d %H:%M:%S&quot;, pinfo.abs_ts) .. string.sub(select(2,math.modf(pinfo.abs_ts)), 2,8),
              tostring(ip_dst), --  pinfo.cols.src_port, pinfo.cols.dst, pinfo.cols.dst_port,
              xml_string
            }, &quot;|&quot; ) )
end

function tap.reset()
    -- file:close()
end</code></pre><p>I've succeeded in converting the XML data and timestamps, but <code>tapinfo</code> comes as <code>nil</code>. How can I have the IP addresses+ports?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '14, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/420b05f798587712130e5ed33a3abde0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arielCo&#39;s gravatar image" /><p><span>arielCo</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arielCo has no accepted answers">0%</span></p></div></div><div id="comments-container-36933" class="comments-container"></div><div id="comment-tools-36933" class="comment-tools"></div><div class="clear"></div><div id="comment-36933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36946"></span>

<div id="answer-container-36946" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36946-score" class="post-score" title="current number of votes">1</div><span id="post-36946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="arielCo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Listener tapinfo is only populated for some specific Listener tap types, such as <code>ip</code>, <code>tcp</code>, <code>udp</code>, or <code>http</code> types... but not for a <code>frame</code> tap type, which is what you're creating since you passed <code>nil</code> for the first argument of <code>Listener.new()</code>.</p><p>Is there some specific reason you want to tap the <em>frame</em> instead of the IP packet, or even TCP segment? Because doing "<code>Listener.new("ip", "xml", true)</code>" would get you the tapinfo for IP-layer including addresses, but not port numbers. Doing "<code>Listener.new("tcp", "xml", true)</code>" would get you the tapinfo for TCP-layer, which would include IP addresses as well as TCP port numbers.</p><p>Alternatively, you don't need to get the IP addresses+ports from the tapinfo - you can instead just get them from explicit field extractors, like this:</p><pre><code>local tap = Listener.new(nil, &quot;xml&quot;, true)
local f_ip_src   = Field.new(&quot;ip.src&quot;)
local f_ip_dst   = Field.new(&quot;ip.dst&quot;)
local f_src_port = Field.new(&quot;tcp.srcport&quot;)
local f_dst_port = Field.new(&quot;tcp.dstport&quot;)

function tap.packet(pinfo,tvb)
   local ip_src   = f_ip_src().value
   local ip_dst   = f_ip_dst().value
   local src_port = f_src_port().value
   local dst_port = f_dst_port().value</code></pre><p>...</p><p>Note that the above is just example code - in a real script one would do verification checks to make sure each field extractor returns something before calling its <code>value</code> attribute, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '14, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-36946" class="comments-container"><span id="36947"></span><div id="comment-36947" class="comment"><div id="post-36947-score" class="comment-score"></div><div class="comment-text"><p>Thank you - both approaches work but I'm still somewhat confused. Where can I find a concept-level description of dissectors and listeners? The Wiki starts with code examples and jumps to the API reference, but nothing about what they actually <em>do</em> and their relationship; it's all copying and trial/error.</p></div><div id="comment-36947-info" class="comment-info"><span class="comment-age">(09 Oct '14, 10:17)</span> <span class="comment-user userinfo">arielCo</span></div></div><span id="36948"></span><div id="comment-36948" class="comment"><div id="post-36948-score" class="comment-score"></div><div class="comment-text"><p>Hmmm... it depends on what more you want to know. The <a href="http://wiki.wireshark.org/Lua">main Wireshark Lua wiki page</a> has links to wiki pages about <a href="http://wiki.wireshark.org/Lua/Dissectors">Dissectors</a> and <a href="http://wiki.wireshark.org/Lua/Taps">Listener taps</a>, and also links to the <a href="http://wiki.wireshark.org/Lua/Examples">sample script page</a> which has links to a few tutorial scripts. There's a <a href="http://wiki.wireshark.org/Lua/Examples?action=AttachFile&amp;do=get&amp;target=dissector.lua">dissector tutorial script</a>, for example, with details about how/why things are done.</p><p>So if those places don't answer your questions, I think the best thing would be for you to ask your questions here on the Q&amp;A site (as separate new topics, not inside this topic), and I or others will try answering them; then we can update the wiki's with the answers if it makes sense to.</p></div><div id="comment-36948-info" class="comment-info"><span class="comment-age">(09 Oct '14, 11:39)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-36946" class="comment-tools"></div><div class="clear"></div><div id="comment-36946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

