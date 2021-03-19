+++
type = "question"
title = "Inbound and Outbound traffic"
description = '''Hi, I&#x27;m writing a Lua program to process data that captured by tshark, and I&#x27;m in need for a filter to separate inbound traffic from outbound traffic in our network to process each group alone. Can some one help me in this, because I&#x27;m new in both: Lua and Wireshark. Thanks'''
date = "2012-01-25T22:39:00Z"
lastmod = "2012-02-02T18:53:00Z"
weight = 8615
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/8615" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Inbound and Outbound traffic](/questions/8615/inbound-and-outbound-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8615-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm writing a Lua program to process data that captured by tshark, and I'm in need for a filter to separate inbound traffic from outbound traffic in our network to process each group alone. Can some one help me in this, because I'm new in both: Lua and Wireshark. Thanks</p></div><div id="question-tags" class="tags-container tags">lua tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '12, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p>Leena<br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jan '12, 00:46</p></div></div><div id="comments-container-8615" class="comments-container"></div><div id="comment-tools-8615" class="comment-tools"></div><div class="clear"></div><div id="comment-8615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8796"></span>

<div id="answer-container-8796" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8796-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming you're interested in IP traffic only.</p><p>You would create two taps (aka "<a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Listener.html#lua_class_Listener">Listeners</a>") -- one filtered for incoming packets to your host and another for outgoing:</p><pre><code>local HOST_IP = &#39;1.2.3.4&#39;

local tap_in = Listener.new(nil, &#39;ip.dst==&#39;..HOST_IP)
local tap_out = Listener.new(nil, &#39;ip.src==&#39;..HOST_IP)

-- handles packets going to $HOST_IP
function tap_in.packet(pinfo, buf)
    print(&#39;#&#39;..pinfo.number, &#39;&lt;IN&gt;&#39;, tostring(buf))
end

-- handles packets going out from $HOST_IP
function tap_out.packet(pinfo, buf)
    print(&#39;#&#39;..pinfo.number, &#39;&lt;OUT&gt;&#39;, tostring(buf))
end</code></pre><p><br />
Copy this file to a temporary directory (e.g., <code>/tmp/test.lua</code>), and run it from TShark as follows:</p><pre><code>$ tshark -Xlua_script:/tmp/test.lua</code></pre><p>You can also load this from Wireshark (as shown in a recent <a href="http://www.wireshark.org/lists/wireshark-users/201201/msg00048.html">post</a>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '12, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></p></div></div><div id="comments-container-8796" class="comments-container"></div><div id="comment-tools-8796" class="comment-tools"></div><div class="clear"></div><div id="comment-8796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

