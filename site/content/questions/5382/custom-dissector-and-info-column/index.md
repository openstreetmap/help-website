+++
type = "question"
title = "Custom dissector and info column"
description = '''Hi, I must admit I am very new to wireshark, but I have read a lot of material of the last few days and this problem has me stumped. I have written a custom dissector plugin to handle an XCP protocol. This consists of PDUs on TCP and I am using the tcp_dissect_pdus function to handle the reassembly ...'''
date = "2011-08-01T14:34:00Z"
lastmod = "2011-08-03T08:56:00Z"
weight = 5382
keywords = [ "reassembly", "dissector", "tcp" ]
aliases = [ "/questions/5382" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Custom dissector and info column](/questions/5382/custom-dissector-and-info-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5382-score" class="post-score" title="current number of votes">0</div><span id="post-5382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I must admit I am very new to wireshark, but I have read a lot of material of the last few days and this problem has me stumped.</p><p>I have written a custom dissector plugin to handle an XCP protocol. This consists of PDUs on TCP and I am using the tcp_dissect_pdus function to handle the reassembly of TCP packets to allow successful dissecting of my PDUs.</p><p>I want to add to the info (COL_INFO) column in the GUI the packets contained in the TCP packet (e.g. Packets: 0x1234 - 0x1240). This works as expected except when the TCP packet is reassembled and then I just get the first PDU packet number. What is really strange is that the other PDUs are correctly dissected and added to the tree view at the bottom. I've tried all manner of things to work out what is going on, but figure I need some expert help! ;-)</p><pre><code>static void dissect_xcp(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
     if (check_col(pinfo-&gt;cinfo, COL_PROTOCOL))
         col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, PROTO_TAG_XCP);

     /* Clear out stuff in the info column */
     if(check_col(pinfo-&gt;cinfo,COL_INFO)){
         col_clear(pinfo-&gt;cinfo,COL_INFO);
     }

     if (check_col(pinfo-&gt;cinfo, COL_INFO)) {
        col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;%d &gt; %d Packets:&quot;,
        pinfo-&gt;srcport, pinfo-&gt;destport);
     }

          tcp_dissect_pdus(tvb, pinfo, tree, TRUE, FRAME_HEADER_LEN,
                 get_xcp_message_len, dissect_xcp_message);
}

static void dissect_xcp_message(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
  proto_item *xcp_item = NULL;
  proto_item *xcp_sub_item = NULL;
  proto_tree *xcp_tree = NULL;
  proto_tree *xcp_header_tree = NULL;
  guint16 count = 0;
  guint16 status = 0;
  guint16 length = 0;
  // This is not a good way of dissecting packets.  The tvb length should
  // be sanity checked so we aren&#39;t going past the actual size of the buffer.
  tvb_memcpy(tvb, (guint8 *)&amp;length, offset, 2);

  xcpcount = tvb_get_guint8( tvb, 2 ); // Get the xcp ccounter
  xcpcount += (tvb_get_guint8( tvb, 3 ) * 256);

  if (check_col(pinfo-&gt;cinfo, COL_INFO)) {
      col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;[0x%X] &quot;,
      xcpcount);
  }

  if (tree)
  {
    // If there is a &quot;tree&quot; requested, we handle that request.
    guint16 counter = 0;
    xcp_item = proto_tree_add_item(tree, proto_xcp, tvb, 0, -1, FALSE);
    xcp_tree = proto_item_add_subtree(xcp_item, ett_xcp);
    xcp_header_tree = proto_item_add_subtree(xcp_item, ett_xcp);

    xcp_sub_item = proto_tree_add_item( xcp_tree, hf_xcp_header, tvb, offset, -1, FALSE );
    xcp_header_tree = proto_item_add_subtree(xcp_sub_item, ett_xcp);

    // Copy length data
    tvb_memcpy(tvb, (guint8 *)&amp;length, offset, 2);
    proto_tree_add_uint(xcp_header_tree, hf_xcp_length, tvb, 0, 0, length);

    tvb_memcpy(tvb, (guint8 *)&amp;counter, offset, 2);
    proto_tree_add_uint(xcp_header_tree, hf_xcp_counter, tvb, 0, 0, counter);
  }</code></pre><p>}</p><p>Any suggestions greatly appreciated!</p><p>I also want to add a PDU sequence check (i.e. packet numbers increase monotonically). This is what lead me to this problem in the first place, since I was getting failed sequence check on the reassembled TCP packets.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '11, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/61dcdb3dbf1e0d5b42ee3eb2ca528494?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tupperware&#39;s gravatar image" /><p><span>Tupperware</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tupperware has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '11, 16:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5382" class="comments-container"></div><div id="comment-tools-5382" class="comment-tools"></div><div class="clear"></div><div id="comment-5382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="5383"></span>

<div id="answer-container-5383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5383-score" class="post-score" title="current number of votes">1</div><span id="post-5383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TBH your code in <code>dissect_xcp_message()</code> is a bit of a mess. You are unnecessarily calling <code>tvb_memcpy()</code> rather than using <code>tvb_get_*()</code>, and not really using the power of <code>proto_tree_add_item()</code> to do all the work for you. You should read the section of the developers guide regarding basic dissection <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html#ChDissectDetails">here</a>.</p><p>As to your problem, I can't see a declaration of offset. That should be declared and initialised in <code>dissect_xcp_message()</code>, so that dissection of each message starts from the same point in the tvb. You are also missing an increment of offset as you extract items from the tvb.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '11, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5383" class="comments-container"><span id="5388"></span><div id="comment-5388" class="comment"><div id="post-5388-score" class="comment-score"></div><div class="comment-text"><p>And you don't need check_col() anymore.</p></div><div id="comment-5388-info" class="comment-info"><span class="comment-age">(01 Aug '11, 19:19)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-5383" class="comment-tools"></div><div class="clear"></div><div id="comment-5383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5390"></span>

<div id="answer-container-5390" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5390-score" class="post-score" title="current number of votes">1</div><span id="post-5390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With reassembly, your dissector isn't going to be called until TCP has enough data to hand off to your dissector as informed by <code>get_xcp_message_len()</code>. This means all the TCP fragments (except the last one) are just that - TCP fragments and they are not handed off to your dissector until reassembly is complete. You don't want to do any column manipulation in <code>dissect_xcp()</code>; save it for <code>dissect_xcp_message()</code>.</p><p>You may want to re-read <code>README.developer</code>, particularly section 2.7, again. You may also want to examine some of the dissectors that utilize <code>tcp_dissect_pdus()</code>, such as the one mentioned in <code>README.developer</code>, namely <code>packet-dns.c</code>. Notice the function that calls <code>tcp_dissect_pdus()</code> and how simple it is - it ONLY calls <code>tcp_dissect_pdus()</code> and nothing more.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '11, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5390" class="comments-container"></div><div id="comment-tools-5390" class="comment-tools"></div><div class="clear"></div><div id="comment-5390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5395"></span>

<div id="answer-container-5395" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5395-score" class="post-score" title="current number of votes">0</div><span id="post-5395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for your responses, much appreciated. I should have mentioned that the code has been hacked about a good few times to test out various theories which is why is looked a mess.</p><p>I have re-read the manula items you suggested, but I think maybe I need to clarify the issue a bit further. The reassembly of the packets is working as expected, but it is the calling of the dissect function that I don't quite follow.</p><p>Here is my code simplified a bit.</p><pre><code>static void dissect_xcp(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
 tcp_dissect_pdus(tvb, pinfo, tree, TRUE, FRAME_HEADER_LEN,
                 get_xcp_message_len, dissect_xcp_message);</code></pre><p>}</p><pre><code>static guint get_xcp_message_len(packet_info *pinfo, tvbuff_t *tvb, int offset){
guint16 length = 0;
tvb_memcpy(tvb, (guint8 *)&amp;length, offset, 2);

return (guint)(length + 4);  // length must include header as well as payload data length}

static void dissect_xcp_message(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree){
proto_item *xcp_item = NULL;
proto_item *xcp_sub_item = NULL;
proto_tree *xcp_tree = NULL;
proto_tree *xcp_header_tree = NULL;
guint16 count = 0;
guint16 length = 0;

if (check_col(pinfo-&gt;cinfo, COL_PROTOCOL))
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, PROTO_TAG_XCP);

xcpcount = tvb_get_guint8( tvb, 2 ); // Get the xcp ccounter
xcpcount += (tvb_get_guint8( tvb, 3 ) * 256);

if (check_col(pinfo-&gt;cinfo, COL_INFO)) {
    col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;[0x%X] &quot;,
    xcpcount);
}

if (tree)
{
    // If there is a &quot;tree&quot; requested, we handle that request.
    guint16 counter = 0;
    xcp_item = proto_tree_add_item(tree, proto_xcp, tvb, 0, -1, FALSE);
    xcp_tree = proto_item_add_subtree(xcp_item, ett_xcp);
    xcp_header_tree = proto_item_add_subtree(xcp_item, ett_xcp);

    xcp_sub_item = proto_tree_add_item( xcp_tree, hf_xcp_header, tvb, 0, -1, FALSE );
    xcp_header_tree = proto_item_add_subtree(xcp_sub_item, ett_xcp);

    // Copy length data
    tvb_memcpy(tvb, (guint8 *)&amp;length, 0, 2);
    proto_tree_add_uint(xcp_header_tree, hf_xcp_length, tvb, 0, 0, length);

    tvb_memcpy(tvb, (guint8 *)&amp;counter, 2, 2);
    proto_tree_add_uint(xcp_header_tree, hf_xcp_counter, tvb, 0, 0, counter);
}</code></pre><p>}</p><p>So this bit of code shows the packet numbers in the info column e.g. [0x1234] [0x1235] [0x1236] [0x1237] and in the detailed information I get a breakdown of each XCP packet (4 of them) arranged as XCP Protocol-&gt;Header-&gt;(Packet Length and Package Counter). This is exactly as I expected for some of the TCP packets.<br />
</p><p>However, on a packet which indicated [2 Reassembled TCP Segments xxxx] I only get the first packet number e.g. [0x1234]. In the detailed view at the bottom I get the 4 packets I expected.</p><p>I could probably live without the packet display in the info column, but when I tried to implement a packet counter check I saw the same issue when checking packet counters across TCP segments in that the packet counter I was checking against was the first one in the reassembled TCP segment rather than the last one.</p><p>Thanks</p><p>EDIT: I thought a picture might be useful to see the problem.</p><p>http://postimage.org/image/uih7wfc4/</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '11, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/61dcdb3dbf1e0d5b42ee3eb2ca528494?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tupperware&#39;s gravatar image" /><p><span>Tupperware</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tupperware has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '11, 04:56</strong> </span></p></div></div><div id="comments-container-5395" class="comments-container"><span id="5399"></span><div id="comment-5399" class="comment"><div id="post-5399-score" class="comment-score"></div><div class="comment-text"><p>First off, as grahamb already pointed out, stop using tvb_memcpy(). Use proto_tree_add_item() instead or where you really need to grab data, use the tvb endian-friendly accessors. Is XCP Big-Endian (BE) or Little-Endian (LE)? I assume BE. Try coding get_xcp_message_len() like this instead:</p><p>static guint get_xcp_message_len(packet_info <em>pinfo, tvbuff_t</em> tvb, int offset){return 4 + tvb_get_ntohs(tvb, offset);}</p><p>And if XCP is BE, xcpcount is being assigned wrong. Try this instead: xcpcount = tvb_get_ntohs(tvb, 2);</p><p>If it's LE, then use tvb_get_letohs() consistently throughout instead.</p></div><div id="comment-5399-info" class="comment-info"><span class="comment-age">(02 Aug '11, 08:08)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="5400"></span><div id="comment-5400" class="comment"><div id="post-5400-score" class="comment-score"></div><div class="comment-text"><p>Also, get rid of C++ comments and get rid of check_col().<br />
After all that's cleaned up, we can look into the column problem.</p></div><div id="comment-5400-info" class="comment-info"><span class="comment-age">(02 Aug '11, 08:08)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-5395" class="comment-tools"></div><div class="clear"></div><div id="comment-5395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5401"></span>

<div id="answer-container-5401" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5401-score" class="post-score" title="current number of votes">0</div><span id="post-5401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi cmaynard,</p><p>Thanks for your support. I've tidied up the code (hopefully) to your liking and removed any unecessary variables. The output is the same as described above and shown in the screenshot.</p><pre><code>static void dissect_xcp(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    tcp_dissect_pdus(tvb, pinfo, tree, TRUE, FRAME_HEADER_LEN,
                 get_xcp_message_len, dissect_xcp_message);
}

static guint get_xcp_message_len(packet_info *pinfo, tvbuff_t *tvb, int offset)
{    
    /* Get length data and extend to cover header info */
    return 4 + tvb_get_letohs(tvb, offset);
}

/* This method dissects fully reassembled messages */
static void dissect_xcp_message(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    proto_item *xcp_item = NULL;
    proto_item *xcp_sub_item = NULL;
    proto_tree *xcp_tree = NULL;
    proto_tree *xcp_header_tree = NULL;

    /* Identify XCP protocol */
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, PROTO_TAG_XCP);

    /* Extract XCP counter value */
    xcpcount = tvb_get_letohs(tvb, 2);

    /* Add packet counter to the info column */
    col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;[0x%X] &quot;,xcpcount);

    if (tree)
    {
        /* If there is a &quot;tree&quot; requested, we handle that request. */
        xcp_item = proto_tree_add_item(tree, proto_xcp, tvb, 0, -1, FALSE);
        xcp_tree = proto_item_add_subtree(xcp_item, ett_xcp);
        xcp_header_tree = proto_item_add_subtree(xcp_item, ett_xcp);
        xcp_sub_item = proto_tree_add_item( xcp_tree, hf_xcp_header, tvb, 0, -1, FALSE );
        xcp_header_tree = proto_item_add_subtree(xcp_sub_item, ett_xcp);

        /* Show length data in detail view */
        proto_tree_add_uint(xcp_header_tree, hf_xcp_length, tvb, 0, 0, tvb_get_letohs(tvb, 0));
        /* Show count data in detail view */
        proto_tree_add_uint(xcp_header_tree, hf_xcp_counter, tvb, 0, 0, xcpcount);
    }
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '11, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/61dcdb3dbf1e0d5b42ee3eb2ca528494?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tupperware&#39;s gravatar image" /><p><span>Tupperware</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tupperware has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-5401" class="comments-container"><span id="5402"></span><div id="comment-5402" class="comment"><div id="post-5402-score" class="comment-score"></div><div class="comment-text"><p>OK, so it's LE then. When you add items to the tree, be sure to use ENC_LITTLE_ENDIAN for the proto_tree_add_xyz() endian argument instead of FALSE as FALSE is actually synonymous with ENC_BIG_ENDIAN. For items where endian-ness is irrelevant, some folks prefer to use ENC_NA.</p><p>What is the value of FRAME_HEADER_LEN? Are you calling col_clear() anywhere?</p></div><div id="comment-5402-info" class="comment-info"><span class="comment-age">(02 Aug '11, 09:02)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="5404"></span><div id="comment-5404" class="comment"><div id="post-5404-score" class="comment-score"></div><div class="comment-text"><p>FRAME_HEADER_LEN is 2</p><p>I removed col_clear in this example to ensure I never lost any data from the info column.</p><p>Question is, how do the proto_tree_* calls get executed whilst col_append_fstr does not for the reassembled TCP packets? TCP packets which were not reassembled work as expected.</p></div><div id="comment-5404-info" class="comment-info"><span class="comment-age">(02 Aug '11, 09:51)</span> <span class="comment-user userinfo">Tupperware</span></div></div><span id="5406"></span><div id="comment-5406" class="comment"><div id="post-5406-score" class="comment-score"></div><div class="comment-text"><p>At this point, it would probably be better to move this over to the -dev mailing list. There, if you could supply your code and a sample capture file, I think it would be a lot easier to help you.</p><p>More critiques ... these are wrong: proto_tree_add_uint(xcp_header_tree, hf_xcp_length, tvb, 0, 0, tvb_get_letohs(tvb, 0));</p><p>proto_tree_add_uint(xcp_header_tree, hf_xcp_counter, tvb, 0, 0, xcpcount);</p><p>The length field should be 2, not 0 and the offset for xcpcount should be 2, not 0. But don't use proto_tree_add_uint() -&gt; use proto_tree_add_item() instead.</p></div><div id="comment-5406-info" class="comment-info"><span class="comment-age">(02 Aug '11, 10:10)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="5425"></span><div id="comment-5425" class="comment"><div id="post-5425-score" class="comment-score"></div><div class="comment-text"><p>Added it to the list :-)</p></div><div id="comment-5425-info" class="comment-info"><span class="comment-age">(03 Aug '11, 03:48)</span> <span class="comment-user userinfo">Tupperware</span></div></div><span id="5448"></span><div id="comment-5448" class="comment"><div id="post-5448-score" class="comment-score"></div><div class="comment-text"><p>And for anyone following this question, the thread is <a href="http://www.wireshark.org/lists/wireshark-dev/201108/msg00036.html">here</a>.</p></div><div id="comment-5448-info" class="comment-info"><span class="comment-age">(03 Aug '11, 08:56)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-5401" class="comment-tools"></div><div class="clear"></div><div id="comment-5401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

