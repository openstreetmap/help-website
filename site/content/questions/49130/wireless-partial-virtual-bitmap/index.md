+++
type = "question"
title = "Wireless Partial Virtual Bitmap"
description = '''Does anyone know of an easy way to filter on a specific AID (association ID) for a WLAN client to see if it is in the partial virtual bitmap (PVM)? With a only a limited number of devices and low AID values, I can do some simple comparisons, if I know how large the bitmap could be: ((wlan_mgt.tim.pa...'''
date = "2016-01-12T09:51:00Z"
lastmod = "2016-06-17T16:26:00Z"
weight = 49130
keywords = [ "tim", "beacon", "partialvirtualbitmap" ]
aliases = [ "/questions/49130" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireless Partial Virtual Bitmap](/questions/49130/wireless-partial-virtual-bitmap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49130-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know of an easy way to filter on a specific AID (association ID) for a WLAN client to see if it is in the partial virtual bitmap (PVM)? With a only a limited number of devices and low AID values, I can do some simple comparisons, if I know how large the bitmap could be:</p><pre><code>((wlan_mgt.tim.partial_virtual_bitmap &amp; 02) or (wlan_mgt.tim.partial_virtual_bitmap &amp; 2:00))</code></pre><p>However, on some systems, my AID values could be in the 100s, so I want to filter on AID == 132 (or whatever), and have it match if that bit is high. The problem is the IE for TIM includes a length and an offset, so I may get a couple of bytes or many bytes, depending on how many stations have data waiting for them, and we need the offset to determine where this particular device is. I can decode by hand, but would be great if Wireshark could tell me.</p><p>The natural choice is wlan.aid == 132 (or whatever), but this does not match the partial virtual bitmap. However, this filter works well to pick up the PS-Poll frames, but to verify proper 802.11 operation, I should see the device AID in the PVM, then the PS-Poll frame.<br />
</p><p>Some sample results:<br />
</p><p>One beacon might give this to me as the PVM</p><pre><code>Length: 15
Offset: 4
PVM: 0x020000000000000010002000

 AID   64 -&gt;    01000000
 AID   72 -&gt;    00000000
 AID   80 -&gt;    00000000
 AID   88 -&gt;    00000000
 AID   96 -&gt;    00000000
 AID  104 -&gt;    00000000
 AID  112 -&gt;    00000000
 AID  120 -&gt;    00000000
 AID  128 -&gt;    00001000    &lt;-- device 132 indicates data waiting
 AID  136 -&gt;    00000000
 AID  144 -&gt;    00000100
 AID  152 -&gt;    00000000</code></pre><p>So I know device 132 has data waiting.</p><p>Another beacon a little while later -</p><pre><code>Length: 7
Offset: 8
PVM: 0x10000000

 AID  128 -&gt;    00001000   &lt;-- device 132 indicates data waiting
 AID  136 -&gt;    00000000
 AID  144 -&gt;    00000000
 AID  152 -&gt;    00000000</code></pre><p>Again, device 132 has data waiting.</p><p>Reference: <a href="http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Power_Save">http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Power_Save</a></p></div><div id="question-tags" class="tags-container tags">tim beacon partialvirtualbitmap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div></div><div id="comments-container-49130" class="comments-container"><span id="49134"></span><div id="comment-49134" class="comment"><div id="post-49134-score" class="comment-score"></div><div class="comment-text"><p>can you provide a small sample pcap?</p></div><div id="comment-49134-info" class="comment-info"><span class="comment-age">(12 Jan '16, 10:32)</span> Kurt Knochner ♦</div></div><span id="49142"></span><div id="comment-49142" class="comment"><div id="post-49142-score" class="comment-score"></div><div class="comment-text"><p>Trace is here:</p><p><a href="https://www.cloudshark.org/captures/169a75f46227">https://www.cloudshark.org/captures/169a75f46227</a></p><p>Two packets - a beacon with TIM IE, and a PS Poll frame.<br />
</p><p>For this example, this is what I have for the TIM map:</p><pre><code>     length  15
     offset  4
     pvm     200000000000000010002000
     Bytes:  [12] 8...19
     Bits:   64...159
     pvm as decimal: 9903520314283042199461437440</code></pre><p>AID 64 -&gt; 00000100 AID 72 -&gt; 00000000 AID 80 -&gt; 00000000 AID 88 -&gt; 00000000 AID 96 -&gt; 00000000 AID 104 -&gt; 00000000 AID 112 -&gt; 00000000 AID 120 -&gt; 00000000 AID 128 -&gt; 00001000 &lt;--- device 132, per AID in PS-Poll AID 136 -&gt; 00000000 AID 144 -&gt; 00000100 AID 152 -&gt; 00000000</p><p>None of the anonymizer tools seemed to work on wlan addresses. I had to edit hex manually. Know of a tool like tracewrangler for 802.11 capture files?</p></div><div id="comment-49142-info" class="comment-info"><span class="comment-age">(12 Jan '16, 12:10)</span> Bob Jones</div></div><span id="53211"></span><div id="comment-53211" class="comment"><div id="post-53211-score" class="comment-score"></div><div class="comment-text"><p>Bump.<br />
</p><p>I ran into this again at a customer site last week with a large wifi infrastructure - more than 1200 APs. I have to feed the packet captures into OmniPeek as it decodes the actual AIDs in the TIM map. Any tips for Wireshark, or would this be a new feature request to enhance the TIM IE decoding?</p></div><div id="comment-53211-info" class="comment-info"><span class="comment-age">(05 Jun '16, 10:11)</span> Bob Jones</div></div><span id="53212"></span><div id="comment-53212" class="comment"><div id="post-53212-score" class="comment-score"></div><div class="comment-text"><p>Would a Lua post-dissector creating up to thousands of individual pseudo-fields out of the individual bits of the TIM submap help you? Display filters do not support arithmetic to calculate offsets and protocol fields cannot be organized into arrays.</p><p>Or, as I think about it, rather a duplicate copy of the original bitmap which would be left-stuffed with 0s to allow use of a fixed offset, so for AID 132, you could always use <code>xxx.xxx.my_bitmap[16:1] &amp; 8</code></p></div><div id="comment-53212-info" class="comment-info"><span class="comment-age">(05 Jun '16, 11:45)</span> sindy</div></div><span id="53225"></span><div id="comment-53225" class="comment"><div id="post-53225-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>Or, as I think about it, rather a duplicate copy of the original bitmap which would be left-stuffed with 0s to allow use of a fixed offset, so for AID 132, you could always use xxx.xxx.my_bitmap[16:1] &amp; 8</p></blockquote></blockquote><p>This sounds like it would do. What I observe is something like this...</p><ol><li>There is WiFi data loss</li><li>So I ... capture WiFi traffic</li><li>Notice client stops sending PS-Poll frames for a period off time</li></ol><p>So root cause of data loss is that no data is sent FromDS for this period, as client is not requesting it. But it's not really root cause: client will only send PS-Poll if informed that data is buffered at the AP with the TIM map entry, so to figure which device is at fault, we need to look at the TIM map to see if the AP is indicating data is waiting. If the bit is set, and no PS-Poll, it's a client issue. If not set, then need a wired trace to prove wired data arrives at AP, but it does not set the TIM map.<br />
</p><p>So a Lua dissector, as you describe, would allow me to filter by PS-Poll and then by Beacons that had this bit set, so Wireshark will easily show periods of no PS-Poll - and then whether there are beacons or not during that period.<br />
</p><p>I have not done any Lua with Wireshark before, so sounds like I need to get on it. I'll start the Lua tutorial for a dissector and see how far I get.</p></div><div id="comment-53225-info" class="comment-info"><span class="comment-age">(06 Jun '16, 03:17)</span> Bob Jones</div></div><span id="53227"></span><div id="comment-53227" class="comment not_top_scorer"><div id="post-53227-score" class="comment-score"></div><div class="comment-text"><p>Well, I was afraid of posting an optimistic nonsense so I'd better checked I haven't... so if you don't want to use this as an impulse to dive into Lua, you may have my proof of concept code :-)</p></div><div id="comment-53227-info" class="comment-info"><span class="comment-age">(06 Jun '16, 03:26)</span> sindy</div></div><span id="53233"></span><div id="comment-53233" class="comment not_top_scorer"><div id="post-53233-score" class="comment-score"></div><div class="comment-text"><p>Proof of concept code would be gladly accepted and greatly appreciated, but I don't want to expect that others would just do it if I won't try first. Thanks for any help you could provide, anyway. I am not sure what the learning curve might be...</p></div><div id="comment-53233-info" class="comment-info"><span class="comment-age">(06 Jun '16, 05:19)</span> Bob Jones</div></div><span id="53237"></span><div id="comment-53237" class="comment not_top_scorer"><div id="post-53237-score" class="comment-score"></div><div class="comment-text"><p>OK. So I don't delete those 16 lines of Lua code until you state clearly either that you want them or that you have written your own ones.</p><p>Just an idea if you're going to take Lua programming seriously: I was thinking of an alternative solution consisting in creation of a value-less pseudofield for each bit which has a value of 1. This would make the addressing in the display filter expression more convenient as you wouldn't have to manually calculate the byte offset and bit position, but it could cost quite some CPU time. The display filter condition would then look just like <code>wlan_mgt.tim.data_waiting.aid_132</code> (no <code>== 1</code> necessary).</p></div><div id="comment-53237-info" class="comment-info"><span class="comment-age">(06 Jun '16, 06:13)</span> sindy</div></div><span id="53257"></span><div id="comment-53257" class="comment not_top_scorer"><div id="post-53257-score" class="comment-score"></div><div class="comment-text"><p>Please share!</p></div><div id="comment-53257-info" class="comment-info"><span class="comment-age">(06 Jun '16, 17:37)</span> Bob Jones</div></div></div><div id="comment-tools-49130" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-49130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53258"></span>

<div id="answer-container-53258" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53258-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A Lua post-dissector, creating a pseudo-field which is a duplicate copy of the original bitmap left-stuffed with 0s in order to allow use of a fixed bit address in the display filter, is below.</p><p>The display filter condition is <code>tim.bitmap[X:1]&amp;x</code>, where</p><ul><li><p><code>X</code> is <code>AID div 8</code> in decadic notation (unless specified otherwise using <code>0x</code> or <code>0</code> prefix),</p></li><li><p>if I got the explanation regarding LSB/MSB meaning correctly from the reference, <code>x</code> is <code>2^(AID rem 8)</code>, this time hexadecimal notation is the only possibility and no prefix is required or possible.</p></li></ul><p>So for AID=132, it would be <code>tim.bitmap[16:1]&amp;10</code>.</p><p>The Lua script itself, to be placed into a .lua file in your plugin directory, is:</p><pre><code>-- Define functions to import already dissected values:
OrigBitmap=Field.new(&quot;wlan_mgt.tim.partial_virtual_bitmap&quot;)
OrigOffset=Field.new(&quot;wlan_mgt.tim.bmapctl.offset&quot;)

-- Export &quot;protocol&quot; &#39;tim&#39; and its only field
MyProto = Proto(&quot;tim&quot;,&quot;TIM pseudo-protocol&quot;)
MyBitmap = ProtoField.bytes(&quot;tim.bitmap&quot;,&quot;Extended bitmap&quot;)
MyProto.fields = { MyBitmap }

-- The (post-)dissector function itself
function MyProto.dissector(buffer,pinfo,tree)
    if OrigBitmap() then
        local MyArray = ByteArray.new(&quot;00&quot;)
        MyArray:set_size(2*OrigOffset().value)
        MyArray:append(OrigBitmap().value)
        local MyTvb = ByteArray.tvb(MyArray,&quot;extended bitmap&quot;)
        local subtree = tree:add(MyProto,&quot;TIM buffer expanded&quot;)
        subtree:add(MyBitmap,MyTvb:range(0))
    end
end

-- register the postdissector for our &quot;protocol&quot;
register_postdissector(MyProto)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '16, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '16, 04:18</p></div></div><div id="comments-container-53258" class="comments-container"><span id="53271"></span><div id="comment-53271" class="comment"><div id="post-53271-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I owe you a beer. I'm out of the office this week on business, but I will try this as soon as I get a chance.</p></div><div id="comment-53271-info" class="comment-info"><span class="comment-age">(07 Jun '16, 03:09)</span> Bob Jones</div></div><span id="53356"></span><div id="comment-53356" class="comment"><div id="post-53356-score" class="comment-score"></div><div class="comment-text"><p>I tested this and it looks good. Thanks for your help.</p><p>I validated with a couple of different cases: AID of 16 and AID of 1 - two simple cases I could inspect to be sure, it works.</p></div><div id="comment-53356-info" class="comment-info"><span class="comment-age">(11 Jun '16, 01:21)</span> Bob Jones</div></div></div><div id="comment-tools-53258" class="comment-tools"></div><div class="clear"></div><div id="comment-53258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53546"></span>

<div id="answer-container-53546" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53546-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please open an enhancement bug at bugs.wireshark.org, attach a sample capture that contains (at least) two beacons: one with no offset into the tim map and one with an offset. If you are worried about keeping the information non-public set the attachment to private. Last but not least: assign the bug to me: [email protected] I will add proper decoding and thus filtering but I need some captures to test against.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/f1397f7833ee927f0c26a9fcb92fff11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmayer&#39;s gravatar image" /><p>jmayer<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmayer has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-53546" class="comments-container"><span id="53549"></span><div id="comment-53549" class="comment"><div id="post-53549-score" class="comment-score"></div><div class="comment-text"><p>This is great, thanks. Enhancement request is done:</p><p>Bug 12545 - Enhancement: Decode TIM Map in 802.11 Beacon Frame</p><p>If you need a tester, let me know. I have <em>plenty</em> of traces to test against.</p></div><div id="comment-53549-info" class="comment-info"><span class="comment-age">(18 Jun '16, 02:02)</span> Bob Jones</div></div></div><div id="comment-tools-53546" class="comment-tools"></div><div class="clear"></div><div id="comment-53546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

