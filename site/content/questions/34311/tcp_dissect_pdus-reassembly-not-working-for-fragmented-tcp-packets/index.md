+++
type = "question"
title = "tcp_dissect_pdus reassembly not working for fragmented TCP packets"
description = '''Hi, I&#x27;m trying to get a protocol dissector plugin to work on custom wireshark build.As mentioned, in the wireshark documentation I&#x27;m using tcp_dissect_pdus for this.In my protocol (over TCP) the 6th and 7th bytes denote the payload length so minimumn bytes needed would be 7 for the getcallpmedmessag...'''
date = "2014-07-01T02:14:00Z"
lastmod = "2014-07-03T08:33:00Z"
weight = 34311
keywords = [ "tcp_dissect_pdus" ]
aliases = [ "/questions/34311" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp\_dissect\_pdus reassembly not working for fragmented TCP packets](/questions/34311/tcp_dissect_pdus-reassembly-not-working-for-fragmented-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34311-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to get a protocol dissector plugin to work on custom wireshark build.As mentioned, in the wireshark documentation I'm using <code>tcp_dissect_pdus</code> for this.In my protocol (over TCP) the 6th and 7th bytes denote the payload length so minimumn bytes needed would be 7 for the <code>getcallpmedmessagelen()</code> method. In network trace (I force simulate fragmentation by reducing MTU size on my linux card),I see both cases ,i.e,fragmented TCP packets and clubbed packets (multiple TCP packets in 1 packet). But my dissector is able to decode clubebd packets and shows them in the same protocol tree (in wireshark display) but fragmented packets are never shown (just prints in column info : "TCP segment of a reassembled PDU"). But if I don't force fragmentation, i.e, if the packets are sent without fragmentation, then the same dissector code works just fine (showing proper info in wireshark display)</p><p>Here is my code snippet. Please guide if I'm missing something or is this a problem with <code>tcp_dissect_pdus()</code> API, still.</p><pre><code>/* determine PDU length of protocol */
static guint get_callpmed_message_len(packet_info *pinfo, tvbuff_t *tvb, int offset)
{    
    guint len = (guint)tvb_get_letohs(tvb, offset+5);   
    return len;
}

//Top level dissector
static void dissect_callpmed(tvbuff_t* tvb, packet_info* pinfo, proto_tree* tree)
{
    tcp_dissect_pdus(tvb, pinfo, tree, TRUE, 7,get_kodiakcallpmed_message_len,   
                     dissect_ActualMethod,NULL);
    //return 0;
}

//Actual dissector routine
static int dissect_ActualMethod(tvbuff_t* tvb, packet_info* pinfo, proto_tree* tree, void* data)
{
    proto_item* kodiakcallpmed_item = NULL;
    proto_tree* kodiakcallpmed_tree = NULL;
    guint32 aLength = tvb_length(tvb);

    if((aLength == 0) || (aLength &gt; 3000))
        return -1;

    //Set protocol name in PROTOCOL column
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, PROTO_TAG_callpmed);

    /* Clear out stuff in the info column */
    col_clear(pinfo-&gt;cinfo,COL_INFO);

    if (tree) 
    {
            .... //Dissecting logic
    }
}</code></pre></div><div id="question-tags" class="tags-container tags">tcp_dissect_pdus</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '14, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/39863ff3d77fd9fdb36522366580eef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="puneet30&#39;s gravatar image" /><p>puneet30<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="puneet30 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jul '14, 02:47</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34311" class="comments-container"><span id="34313"></span><div id="comment-34313" class="comment"><div id="post-34313-score" class="comment-score"></div><div class="comment-text"><p>Presumably you either meant</p><pre><code>static guint get_kodiakcallpmed_message_len(packet_info *pinfo, tvbuff_t *tvb, int offset)
{
    ...
}</code></pre><p>or you meant</p><pre><code>    tcp_dissect_pdus(tvb, pinfo, tree, TRUE, 7, get_callpmed_message_len,   
                     dissect_ActualMethod,NULL);</code></pre></div><div id="comment-34313-info" class="comment-info"><span class="comment-age">(01 Jul '14, 02:50)</span> Guy Harris ♦♦</div></div><span id="34361"></span><div id="comment-34361" class="comment"><div id="post-34361-score" class="comment-score"></div><div class="comment-text"><p>Looks like a legitimate bug, I was able to reproduce it by splitting the TCP payload of a git capture using <a href="https://git.lekensteyn.nl/peter/wireshark-notes/tree/crafted-pkt/replay-chunks.py">https://git.lekensteyn.nl/peter/wireshark-notes/tree/crafted-pkt/replay-chunks.py</a></p></div><div id="comment-34361-info" class="comment-info"><span class="comment-age">(02 Jul '14, 12:45)</span> Lekensteyn</div></div><span id="34380"></span><div id="comment-34380" class="comment"><div id="post-34380-score" class="comment-score"></div><div class="comment-text"><p>Actually, it works fine for me. The script had an error which dropped data. OP, can you provide more details? Like a network capture, your wireshark version and dissector code?</p></div><div id="comment-34380-info" class="comment-info"><span class="comment-age">(03 Jul '14, 03:57)</span> Lekensteyn</div></div></div><div id="comment-tools-34311" class="comment-tools"></div><div class="clear"></div><div id="comment-34311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34388"></span>

<div id="answer-container-34388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34388-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe your IPv4 preference to <em>"Reassemble fragmented IPv4 datagrams"</em> is disabled?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '14, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-34388" class="comments-container"></div><div id="comment-tools-34388" class="comment-tools"></div><div class="clear"></div><div id="comment-34388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

