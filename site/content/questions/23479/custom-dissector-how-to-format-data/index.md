+++
type = "question"
title = "Custom dissector - How to format data?"
description = '''I followed the online example here: http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html and managed to get my custom dissector working correctly. My results look like this in wireshark: Status Protocol Serial Number: 0x0000001a57004eaf Reserved: 0 Product ID: Radio Module (3) Capabilit...'''
date = "2013-07-31T08:21:00Z"
lastmod = "2013-07-31T09:09:00Z"
weight = 23479
keywords = [ "dissector", "wireshark", "custom" ]
aliases = [ "/questions/23479" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Custom dissector - How to format data?](/questions/23479/custom-dissector-how-to-format-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23479-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I followed the online example here: <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html">http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html</a> and managed to get my custom dissector working correctly. My results look like this in wireshark:</p><p>Status Protocol</p><p>Serial Number: 0x0000001a57004eaf</p><p>Reserved: 0</p><p>Product ID: Radio Module (3)</p><p>Capabilities: Unknown (52)</p><p><strong>Is there a way I can format 0x0000001a57004eaf to look like 00:00:00:1a:57:00:4e:af ?</strong></p><p>If I can turn the 8 bytes in a string and format it that might work. I'm just not sure where to stick such a function to make it work with the foo example in the tutorial above. It's all still "magic" to me since I blindly followed the tutorial.</p><p><strong>My other problem is the packets have a varying amount of capabilities.</strong> The packets can have any amount of capabilities from 1 to 5. Right now, I'm just reading the first capability because I'm not sure how to get the others. Is there a way to loop to the end of the packet, then <em>proto_tree_add_item</em> the entire array of capabilities? I'd like the capabilities to be on one line, if possible, like this: Capabilities: Human (4), Mobile (3), Trackable (1)</p><p>But even if they have to be on separate lines, I still need a way to loop through a varying amount of capabilities.</p></div><div id="question-tags" class="tags-container tags">dissector wireshark custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '13, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/477c22aa68350514a3d320929b588791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arwen17&#39;s gravatar image" /><p>Arwen17<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arwen17 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jul '13, 08:35</p></div></div><div id="comments-container-23479" class="comments-container"></div><div id="comment-tools-23479" class="comment-tools"></div><div class="clear"></div><div id="comment-23479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23480"></span>

<div id="answer-container-23480" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23480-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might get away with calling <code>proto_tree_add_item()</code> using a field type of FT_IPv6 but I don't know if that might lead to odd filtering issues (your serial number matching an IPv6 filter string), or you can create any string you like and then use <code>proto_tree_add_text()</code> or you can use <code>proto_tree_add_bytes_format()</code> and supply your own formatting string and values.</p><p>Assuming you know the length of your overall message and the length of each of your capability items, just loop over them reading data from the tvb, adding the item to the tree and incrementing your byte count (the variable offset in most cases) until the byte count you have read matches the total message length.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '13, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23480" class="comments-container"><span id="23488"></span><div id="comment-23488" class="comment"><div id="post-23488-score" class="comment-score"></div><div class="comment-text"><p>Thank you, that did help me.</p><p><a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/tvbuff.c">http://anonsvn.wireshark.org/wireshark/trunk/epan/tvbuff.c</a></p><p><a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/tvbuff.h">http://anonsvn.wireshark.org/wireshark/trunk/epan/tvbuff.h</a></p><p>Here's what worked for me:</p><pre><code>gint length = tvb_length(tvb);
while (offset != length) {
 proto_tree_add_item(...capability...)
 offset += 2;
}</code></pre><p>FT_IPv6 cheat didn't work for me so I have to write my own string. I'm still trying to figure this out. Can I pass a string directly to <code>proto_tree_add_text()</code> or <code>proto_tree_add_bytes_format()</code> ? Or do I need to have it stored in a <code>tvbuff_t</code> type?</p><p>Some example syntax of <code>proto_tree_add_text()</code> or <code>proto_tree_add_bytes_format()</code> would be nice.</p><p>I wish I could just: <code>proto_tree_add_text(tree, hf_serial_num, "String!");</code></p><p>EDIT: ok halfway there:</p><pre><code>proto_tree_add_string(tree, hf_serial_num, tvb, 0, 11, &quot;Your String&quot;);</code></pre><p>with 0 and 11 being the length of the string and NOT the serial_num.</p><p>I used <code>FT_STRING, BASE_NONE</code> for serial_num registration.</p></div><div id="comment-23488-info" class="comment-info"><span class="comment-age">(31 Jul '13, 10:55)</span> Arwen17</div></div><span id="23509"></span><div id="comment-23509" class="comment"><div id="post-23509-score" class="comment-score"></div><div class="comment-text"><p>Here's what finally worked for me:</p><pre><code>char* hexString(tvbuff_t *tvb)
{
   char s[25];
   guint8 *bytes = tvb_get_string(tvb, 0, 8);

   sprintf(s, &quot;%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x&quot;, bytes[0], bytes[1],bytes[2],bytes[3],
                             bytes[4],bytes[5],bytes[6],bytes[7]);

   return s;
}</code></pre><p>and</p><pre><code>const char* test = hexString(tvb);
proto_tree_add_string_format_value(tree, hf_serial_num, tvb, 0, 8, &quot;%s&quot;, test);</code></pre></div><div id="comment-23509-info" class="comment-info"><span class="comment-age">(01 Aug '13, 11:55)</span> Arwen17</div></div><span id="23520"></span><div id="comment-23520" class="comment"><div id="post-23520-score" class="comment-score"></div><div class="comment-text"><p>After kicking it some more, this made things more beautiful:</p><pre><code>proto_tree_add_string(tree, hf_serial_num, tvb, 0, 8, test);</code></pre></div><div id="comment-23520-info" class="comment-info"><span class="comment-age">(02 Aug '13, 11:11)</span> Arwen17</div></div></div><div id="comment-tools-23480" class="comment-tools"></div><div class="clear"></div><div id="comment-23480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

