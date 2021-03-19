+++
type = "question"
title = "Retrieve hex values in Lua"
description = '''I&#x27;m extracting values from PDML output of TShark like wlan_mgt.ssid, and I&#x27;d like to change to Lua for efficiency issues. For the moment, I get the hex value in case there&#x27;re weird ASCII characters, directly from the PDML: &amp;lt;field name=&quot;wlan_mgt.ssid&quot; showname=&quot;SSID: Livebox-6325&quot; size=&quot;12&quot; pos=&quot;6...'''
date = "2015-06-24T14:25:00Z"
lastmod = "2015-06-26T07:22:00Z"
weight = 43521
keywords = [ "lua", "pdml" ]
aliases = [ "/questions/43521" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieve hex values in Lua](/questions/43521/retrieve-hex-values-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43521-score" class="post-score" title="current number of votes">0</div><span id="post-43521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm extracting values from PDML output of TShark like wlan_mgt.ssid, and I'd like to change to Lua for efficiency issues.</p><p>For the moment, I get the hex value in case there're weird ASCII characters, directly from the PDML: &lt;field name="wlan_mgt.ssid" showname="SSID: Livebox-6325" size="12" pos="63" show="Livebox-6325" value="4c697665626f782d36333235"/&gt;</p><p>From the few tests I've made with Lua and the Packet Tree in <a href="https://wiki.wireshark.org/Lua/Examples#View_Packet_Tree_of_Fields.2FFieldInfo,">https://wiki.wireshark.org/Lua/Examples#View_Packet_Tree_of_Fields.2FFieldInfo,</a> I just can get the ASCII version of the SSID, not the hexa version.</p><p>-&gt; Is there an easy way to get the hexa version of wlan_mgt.ssid in Lua? (If you have a short piece of code, I take it, I've no idea where to start) -&gt; Or the dissector doesn't have the hexa info, only the ASCII and I have to take the whole hexa and find the offset?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '15, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-43521" class="comments-container"></div><div id="comment-tools-43521" class="comment-tools"></div><div class="clear"></div><div id="comment-43521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43523"></span>

<div id="answer-container-43523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43523-score" class="post-score" title="current number of votes">0</div><span id="post-43523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "string" you're getting is a Lua string, so you can convert it to a string of hex characters by either (1) writing a function to do so in Lua, or (2) if you're running Wireshark 1.12, then use the built-in <code>Struct.tohex()</code> function, for example:</p><pre><code>local orig = myfield.value()
local hex_orig = Struct.tohex(orig)
print(&quot;The hex version of my orig string = &quot; .. hex_orig)</code></pre><p>The full function with other options is documented here: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Struct.html">API doc for Struct</a> in section 11.13.1.5.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '15, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43523" class="comments-container"><span id="43536"></span><div id="comment-43536" class="comment"><div id="post-43536-score" class="comment-score"></div><div class="comment-text"><p>It doesn't work when the string is weird like for ex with original hexa "6b6576696ee2809973206950686f6e6520" String value is "kevin���s iPhone"</p><p>I can't retrieve the original hex version, instead I get "6B6576696EEFBFBDEFBFBDEFBFBD73206950686F6E6520"</p></div><div id="comment-43536-info" class="comment-info"><span class="comment-age">(24 Jun '15, 23:42)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div><span id="43590"></span><div id="comment-43590" class="comment"><div id="post-43590-score" class="comment-score"></div><div class="comment-text"><p>How <em>exactly</em> are you retrieving it? Can you paste a code snippet?</p></div><div id="comment-43590-info" class="comment-info"><span class="comment-age">(26 Jun '15, 07:22)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-43523" class="comment-tools"></div><div class="clear"></div><div id="comment-43523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

