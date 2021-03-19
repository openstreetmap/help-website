+++
type = "question"
title = "Lua Post Dissector from 1.4 breaks in 1.6"
description = '''I&#x27;ve been building a post dissector in Lua for the last month, and have used pinfo.columns.protocol:set(&quot;G2S&quot;) to assign packets the G2S name in the Protocol column that I&#x27;ve identified as my application protocol. In V1.4.x, this worked just fine. But now with 1.6, my first identified packet display...'''
date = "2011-06-10T14:12:00Z"
lastmod = "2013-02-19T11:21:00Z"
weight = 4515
keywords = [ "lua", "dissector", "post-dissector", "bug" ]
aliases = [ "/questions/4515" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lua Post Dissector from 1.4 breaks in 1.6](/questions/4515/lua-post-dissector-from-14-breaks-in-16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4515-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been building a post dissector in Lua for the last month, and have used pinfo.columns.protocol:set("G2S") to assign packets the G2S name in the Protocol column that I've identified as my application protocol. In V1.4.x, this worked just fine. But now with 1.6, my first identified packet displays G2S in the protocol column, but all subsequent packets continue to show HTTP/XML. When I look at these HTTP/XML packets, they are green highlighted, meaning WireShark has identified them as part of my protocol, and I find my G2S Protocol Post Dissector tree in the middle pane. So my protocol is being properly identified, and my Post Dissector is executing. But my setting of pinfo.columns.protocol is being ignored.</p><p>Has anyone else also seen this behavior? If others are seeing that it worked in 1.4.x and no longer does in 1.6, then I'll file this as a bug.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lua dissector post-dissector bug</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '11, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/6d70926a09a65b1329fb803549ab7205?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewbieBrian&#39;s gravatar image" /><p>NewbieBrian<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewbieBrian has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 10 Jun '11, 18:11</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4515" class="comments-container"></div><div id="comment-tools-4515" class="comment-tools"></div><div class="clear"></div><div id="comment-4515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4519"></span>

<div id="answer-container-4519" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4519-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just thought I'd point out that you can shorten</p><pre><code>pinfo.columns.protocol:set(&quot;G2S&quot;)</code></pre><p>to:</p><pre><code>pinfo.cols.protocol = &quot;G2S&quot;</code></pre><hr /><hr /><hr /><p>I just confirmed this behavior in 1.7.0 (Ubuntu 11.04, 64-bit), but it seems inconsistent in that it happens only when setting the column text inside an <code>if</code> block, as shown below. I agree you should file a bug.</p><p>Based on the sample <a href="http://wiki.wireshark.org/Lua/Dissectors#postdissectors">code</a> from the Wireshark wiki:</p><pre><code>-- trivial postdissector example
-- declare some Fields to be read
ip_src_f = Field.new(&quot;ip.src&quot;)
ip_dst_f = Field.new(&quot;ip.dst&quot;)
tcp_src_f = Field.new(&quot;tcp.srcport&quot;)
tcp_dst_f = Field.new(&quot;tcp.dstport&quot;)

-- declare our (pseudo) protocol
trivial_proto = Proto(&quot;trivial&quot;,&quot;Trivial Postdissector&quot;)

-- create the fields for our &quot;protocol&quot;
src_F = ProtoField.string(&quot;trivial.src&quot;,&quot;Source&quot;)
dst_F = ProtoField.string(&quot;trivial.dst&quot;,&quot;Destination&quot;)
conv_F = ProtoField.string(&quot;trivial.conv&quot;,&quot;Conversation&quot;,&quot;A Conversation&quot;)

-- add the field to the protocol
trivial_proto.fields = {src_F, dst_F, conv_F}

-- create a function to &quot;postdissect&quot; each frame
function trivial_proto.dissector(buffer,pinfo,tree)
    -- obtain the current values the protocol fields
    local tcp_src = tcp_src_f()
    local tcp_dst = tcp_dst_f()
    local ip_src = ip_src_f()
    local ip_dst = ip_dst_f()

    --###############################################################
    --# XXX: If we set the column here, the text always shows up
    --# properly in the Protocol column.
    --###############################################################
    --pinfo.cols.protocol = &quot;Trivial&quot;
    pinfo.cols.protocol:set(&quot;Trivial&quot;)

    if tcp_src then

       --###############################################################
       --# FIXME: But if we set the column here, the Protocol column
       --# is almost always not set to &quot;Trivial&quot; (or it&#39;s overwritten).
       --# The packets that do have &quot;Trivial&quot; in its Protocol column
       --# won&#39;t necessarily show it again when the pcap is reloaded.
       --###############################################################
       --pinfo.cols.protocol = &quot;Trivial&quot;
       pinfo.cols.protocol:set(&quot;Trivial&quot;)

       local subtree = tree:add(trivial_proto,&quot;Trivial Protocol Data&quot;)
       local src = tostring(ip_src) .. &quot;:&quot; tostring(tcp_src)
       local dst = tostring(ip_dst) .. &quot;:&quot; tostring(tcp_dst)
       local conv = src  .. &quot;-&gt;&quot; .. dst
       subtree:add(src_F,src)
       subtree:add(dst_F,dst)
       subtree:add(conv_F,conv)
    end
end
-- register our protocol as a postdissector
register_postdissector(trivial_proto)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 18:08</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-4519" class="comments-container"></div><div id="comment-tools-4519" class="comment-tools"></div><div class="clear"></div><div id="comment-4519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18746"></span>

<div id="answer-container-18746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18746-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is discussed in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6020">bug 6020</a>, and there's a patch attached to that bug to fix it as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-18746" class="comments-container"></div><div id="comment-tools-18746" class="comment-tools"></div><div class="clear"></div><div id="comment-18746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

