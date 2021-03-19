+++
type = "question"
title = "[TAP] Tap listener: request for documentation ressources"
description = '''Hi, I am currently working on a tap listener and I am struggling on how to get (reassembled) packet informations from it, using a tap listener. I would like to extract the following information:  tapped protocol payload (without using the &quot;Frame&quot; data source if possible) protocol tree named field Do...'''
date = "2015-09-21T08:20:00Z"
lastmod = "2015-09-22T07:22:00Z"
weight = 46020
keywords = [ "listener", "packet_info", "tap", "tcp", "plugin" ]
aliases = [ "/questions/46020" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[TAP\] Tap listener: request for documentation ressources](/questions/46020/tap-tap-listener-request-for-documentation-ressources)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46020-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am currently working on a tap listener and I am struggling on how to get (reassembled) packet informations from it, using a tap listener.</p><p>I would like to extract the following information:</p><ol><li>tapped protocol payload (without using the "Frame" data source if possible)</li><li>protocol tree named field</li><li>Documentation/Guide on how to use packet_info/epan_dissect_t ? (I have read README.* and source files but it is still hard to catch)</li></ol><hr /><p>Tap listener callback I have access to.</p><pre><code>static gboolean my_tap_listener_packet(void *tapdata, packet_info *pinfo, epan_dissect_t *edt, const void *tcp);</code></pre><hr /><p>Example of TCP tree I would like to access named field (no necessary with the name).</p><pre><code>Source Port: 443 (443)
Destination Port: 57189 (57189)
[Stream index: 0]
[TCP Segment Len: 0]
Sequence number: 152    (relative sequence number)
Acknowledgment number: 939    (relative ack number)
Header Length: 20 bytes
.... 0000 0001 0000 = Flags: 0x010 (ACK)
Window size value: 254
[Calculated window size: 65024]
[Window size scaling factor: 256]
Checksum: 0x0b60 [correct]
Urgent pointer: 0
[SEQ/ACK analysis]
    [This is an ACK to the segment in frame: 17]
    [The RTT to ACK the segment was: 0.000140000 seconds]
    [iRTT: 0.000577000 seconds]</code></pre><hr /><p>Any help or link to documentations (even a README section I would have missed) would be appreciated.</p><p>Regards,</p></div><div id="question-tags" class="tags-container tags">listener packet_info tap tcp plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '15, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/a6754cdcb165ca0e2928c9927244d8ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewUser2&#39;s gravatar image" /><p>NewUser2<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewUser2 has no accepted answers">0%</span></p></div></div><div id="comments-container-46020" class="comments-container"></div><div id="comment-tools-46020" class="comment-tools"></div><div class="clear"></div><div id="comment-46020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46053"></span>

<div id="answer-container-46053" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46053-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So finaly I got something to access protocol layer and the corresponding data (using bad practice for now since I am using tvbuff struct field directly, but I did not found an other way to do this simply). I will update this answer with news on this.</p><p>Working on accessing named field.</p><hr /><p>Part of the Code:</p><pre><code># define LOG_PREFIX &quot;[TAP Listener plugin] =&gt; &quot;##__FUNCTION__##&quot;(): &quot;
void    pretty_print_edt_tree(epan_dissect_t const *edt)
{
    proto_node  *node;

    if (edt &amp;&amp; edt-&gt;tree)
    {
        node = edt-&gt;tree-&gt;first_child;
        while (node)
        {
            if (node-&gt;finfo)
            {
                if (node-&gt;finfo-&gt;hfinfo)
                    printf(LOG_PREFIX&quot;Node name: %s\n&quot;, node-&gt;finfo-&gt;hfinfo-&gt;name);
                if (node-&gt;finfo-&gt;ds_tvb)
                    hex_dump(&amp;node-&gt;finfo-&gt;ds_tvb-&gt;real_data[node-&gt;finfo-&gt;start], node-&gt;finfo-&gt;length, 8, 0);
            }
            node = node-&gt;next;
            printf(LOG_PREFIX&quot;Going to next node\n&quot;);
        }
    }
}

//gboolean(*packet)(void *tapdata, packet_info *pinfo, epan_dissect_t *edt, const void *data)
static gboolean tap_packet(void *tapdata, packet_info *pinfo, epan_dissect_t *edt, const void *ssl)
{
  pretty_print_edt_tree(edt);
  return (0);
}

// TL_REQUIRES_PROTO_TREE and TL_REQUIRES_COLUMNS were used to register the tap listener</code></pre><hr /><p>Output:</p><pre><code>[TAP Listener plugin] =&gt; pretty_print_edt_tree(): Node name: Ethernet^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000000:   08 00 27 0e e4 14 08 00   ..&#39;.....^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000008:   27 00 44 90 08 00         &#39;.D...^M$
^M$
[TAP Listener plugin] =&gt; pretty_print_edt_tree(): Going to next node^M$
[TAP Listener plugin] =&gt; pretty_print_edt_tree(): Node name: Internet Protocol Version 4^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000000:   45 00 00 84 73 7d 40 00   E...s}@.^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000008:   80 06 95 3f c0 a8 38 01   ...?..8.^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000010:   c0 a8 38 65               ..8e^M$
^M$
[TAP Listener plugin] =&gt; pretty_print_edt_tree(): Going to next node^M$
[TAP Listener plugin] =&gt; pretty_print_edt_tree(): Node name: Transmission Control Protocol^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000000:   01 bb df 78 a2 57 49 c1   ...x.WI.^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000008:   c9 17 ac be 50 18 01 00   ....P...^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000010:   33 be 00 00 16 03 01 00   3.......^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000018:   57 02 00 00 53 03 01 56   W...S..V^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000020:   01 62 4e 09 09 09 09 09   .bN.....^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000028:   09 09 09 09 09 09 09 09   ........^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000030:   09 09 09 09 09 09 09 09   ........^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000038:   09 09 09 09 09 09 09 20   ........^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000040:   64 f6 ec 95 c2 79 dd 76   d....y.v^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000048:   6f a5 03 ff 94 49 f1 70   o....I.p^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000050:   85 88 df 99 d3 f8 ce 1b   ........^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000058:   aa b0 a4 bc 80 ed e3 c9   ........^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000060:   00 35 00 00 0b ff 01 00   .5......^M$
[TAP Listener plugin] =&gt; hex_dump(): 0x000068:   01 00 00 0b 00 02 01 00   ........^M$</code></pre><hr /></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '15, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/a6754cdcb165ca0e2928c9927244d8ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewUser2&#39;s gravatar image" /><p>NewUser2<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewUser2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '15, 07:24</p></div></div><div id="comments-container-46053" class="comments-container"></div><div id="comment-tools-46053" class="comment-tools"></div><div class="clear"></div><div id="comment-46053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

