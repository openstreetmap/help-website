+++
type = "question"
title = "Retrieving &quot;wlan&quot; header length"
description = '''In a Lua script, I&#x27;m looking for the length of the &quot;wlan&quot; header in each packet, and I can&#x27;t find any &quot;wlan.length&quot; value (the value &quot;28 bytes&quot; in attached screenshot) I have frame.len, radiotap.length, data.len if packets are encrypted, and I can do some maths with that. But for example if packets ...'''
date = "2016-02-15T08:12:00Z"
lastmod = "2016-02-16T01:25:00Z"
weight = 50211
keywords = [ "lua", "wlan", "display-filter" ]
aliases = [ "/questions/50211" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Retrieving "wlan" header length](/questions/50211/retrieving-wlan-header-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50211-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a Lua script, I'm looking for the length of the "wlan" header in each packet, and I can't find any "wlan.length" value (the value "28 bytes" in attached screenshot)</p><p>I have frame.len, radiotap.length, data.len if packets are encrypted, and I can do some maths with that.</p><p>But for example if packets are not encrypted data packets with several data headers, I can't do my maths to retrieve the length of wlan header.</p><p>How does Wireshark retrieve that "28 bytes" value?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screenshot80.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">lua wlan display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '16, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p>TomLaBaude<br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></img></div></div><div id="comments-container-50211" class="comments-container"></div><div id="comment-tools-50211" class="comment-tools"></div><div class="clear"></div><div id="comment-50211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50214"></span>

<div id="answer-container-50214" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50214-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The header size is not directly available as a field of the wireless frame but comes out from the frame type <code>wlan.fc_type</code> and subtype <code>wlan.fc_subtype</code> in the frame control field <code>wlan.fc</code>. The existing IEEE 802.11 (wlan) dissector understands that information but does not generate a pseudo-field like <code>wlan.length</code> from it, so your only chance would be to build your own table of header sizes indexed by <code>wlan.fc</code> values (64 in total, ignoring the two bits reserved for version). You can look for information necessary to build that table into the IEEE 802.11 dissector's source code, or into the IEEE 802.11 standard, or you can build it manually from captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '16, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '16, 01:12</p></div></div><div id="comments-container-50214" class="comments-container"><span id="50227"></span><div id="comment-50227" class="comment"><div id="post-50227-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy (at the end, "reading the specs" always win ...)</p></div><div id="comment-50227-info" class="comment-info"><span class="comment-age">(16 Feb '16, 00:58)</span> TomLaBaude</div></div></div><div id="comment-tools-50214" class="comment-tools"></div><div class="clear"></div><div id="comment-50214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50229"></span>

<div id="answer-container-50229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50229-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you can get <code>wlan</code> as a <code>FieldInfo</code> in your Lua script, you can use its <code>len</code> method, according to <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Field.html#lua_class_FieldInfo">the Wireshark LUA API reference</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50229" class="comments-container"><span id="50230"></span><div id="comment-50230" class="comment"><div id="post-50230-score" class="comment-score"></div><div class="comment-text"><p>Interesting, I tried to retrieve length of the tvb, but was not aware of FieldInfo. Gonna try right now</p></div><div id="comment-50230-info" class="comment-info"><span class="comment-age">(16 Feb '16, 01:36)</span> TomLaBaude</div></div><span id="50231"></span><div id="comment-50231" class="comment"><div id="post-50231-score" class="comment-score"></div><div class="comment-text"><p>Something is wrong in FieldInfo length of wlan field, seems like the Frame Check Sequence (located at the end of the packet) interferes:</p><p>Ex for a QoS Data Packet: wlan (38 bytes) - shown on the GUI -&gt; 34 bytes for the wlan header -&gt; 4 bytes for the FCS (end of packet)</p><p>Lua: local wlan_f = Field.new("wlan") ... function .... print(wlan_f().len) -&gt; 26</p><p>26 doesn't represent anything... There's a "jump" in the GUI looking for the FCS at the end, but in the case of a QoS Data packet, there are other fields after the FCS (QoS Control &amp; CCMP parameters)</p><p>It seems that Lua doesn't count fully QoS Control (2 bytes) &amp; CCMP parameters (8 bytes) 26 + 2 + 8 = 36 ... There are 2 bytes somewhere ...</p><p>Bug?</p></div><div id="comment-50231-info" class="comment-info"><span class="comment-age">(16 Feb '16, 02:02)</span> TomLaBaude</div></div></div><div id="comment-tools-50229" class="comment-tools"></div><div class="clear"></div><div id="comment-50229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

