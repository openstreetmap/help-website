+++
type = "question"
title = "TCP reassembly and misordered frames"
description = '''Hi, I have created a dissector over TCP layer. Size of messages could vary a lot (from as little as 8 bytes to several Mbytes). Part of the network on which these messages are sent generates some packet error rate. Therefore, when I analyse the capture file, some messages part are misordered. Using ...'''
date = "2015-02-26T05:30:00Z"
lastmod = "2015-02-26T05:30:00Z"
weight = 40098
keywords = [ "tcp_dissect_pdus", "pdu", "tcp" ]
aliases = [ "/questions/40098" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP reassembly and misordered frames](/questions/40098/tcp-reassembly-and-misordered-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40098-score" class="post-score" title="current number of votes">1</div><span id="post-40098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have created a dissector over TCP layer. Size of messages could vary a lot (from as little as 8 bytes to several Mbytes). Part of the network on which these messages are sent generates some packet error rate. Therefore, when I analyse the capture file, some messages part are misordered. Using the tcp_dissect_pdus helps a lot to handle this, but, in some cases, messages are missing. This occurs when the misorder TCP fragment contains start of a new message.</p><p>Following is a quick summary that tries to explain what I am seeing:</p><ol><li>Frame x : start of msg 1 Frame x+1</li><li>Frame x+1 : missing, received later</li><li>Frame x+2 : end of msg2 + start of msg3</li><li>Frame x+1 : end of msg1 + start of msg2 --&gt; msg1 is dissected</li><li>Frame x+3 : end of msg3 --&gt; msg3 is dissected</li></ol><p>Unfortunately, I am working on a quite old version of wireshark (1.8.3).</p><p>Has anyone had this kind of problem and found a solution ?</p><p>Following is the dissector part that deals with pdu re-assembly (sorry, it is quite long). Each message is preceded by a header that will contain a magic number (to identify the protocol) and the message length.</p><pre><code>static const MYPROTO_MAGIC myProtoMagic = {xx, xx, xx, xx};
static guint get_myproto_message_len(packet_info *pinfo,
                                     tvbuff_t    *tvb,
                                     int          offset)
{
    guint l_len = 0;
    MYPROTO_MAGIC HeadPattern;
    guint i;

    for (i= 0; i &lt; sizeof(MYPROTO_MAGIC); i++)
        HeadPattern[i] = g_htonl(myProtoMagic[i]);

    //Check frame is a MYPROTO one, otherwise dismiss it
    if(tvb_memeql(tvb, offsetof(MYPROTO_HEAD, headPatternA), (const guint8 *) HeadPattern, sizeof(MY_PROTO_MAGIC)) == 0)
        l_len = tvb_get_ntohl(tvb, offset + offsetof(MYPROTO_HEAD, msgTotalSizeUI));
    else l_len = 0;

    return (l_len);
}

static int dissect_myproto_tcp(tvbuff_t     *tvb,
                               packet_info  *pinfo,
                               proto_tree   *tree)
{
    guint len = tvb_length(tvb);
    int ret = TRUE;
    MYPROTO_MAGIC HeadPattern;
    guint i;

    //Check packet is a MYPROTO ones
    // if tvb length is too short for comparison, consider frame as a MYPROTO ones,
    // but new comparison should be performed while retrieving PDU length
    //The following checks are performed :
    // - Frame length (sizeUI field should be large enough to contain MYPROTO header and trailer)
    // - Head pattern (used to identify MYPROTO frames) --&gt; Check the biggest possible part of this pattern
    for (i= 0; i&lt; sizeof(HeadPattern); i++)
        HeadPattern[i] = g_htonl(myProtoMagic[i]);

    if ((len &gt; offsetof(MYPROTO_HEAD, headPatternAUI)) AND (len &gt;= (offsetof(MYPROTO_HEAD, msgTotalSizeUI) + sizeof(guint))))
    {
        guint comparison_len = len - offsetof(MYPROTO_HEAD, headPatternAUI);

        if (comparison_len &gt; sizeof(HeadPattern))
            comparison_len = sizeof(HeadPattern);

        if (tvb_memeql(tvb, offsetof(MYPROTO_HEAD, headPatternAUI), (const guint8 *) HeadPattern, comparison_len) != 0)
            ret = FALSE;
    }
    else if (len &gt;= (offsetof(MYPROTO_HEAD, msgTotalSizeUI) + sizeof(guint)))
    {
        if (tvb_get_ntohl(tvb, offsetof(MYPROTO_HEAD, msgTotalSizeUI)) &lt; (sizeof(MYPROTO_HEAD) + sizeof(MYPROTO_TRAIL)))
            ret = FALSE;
    }

    if (ret != FALSE)
    {
        tcp_dissect_pdus(tvb, pinfo, tree, TRUE, sizeof(MYPROTO_HEAD), get_myproto_message_len, dissect_myproto);
        return ret;
    }
    else
    {
        /* Start of tvb does not match a MYPROTO message, try to find another MYPROTO marker in tvb */
        tvbuff_t * tvbHead = tvb_new_real_data((const guint8 *) HeadPattern, 4, 4);
        gint offset = tvb_find_tvb(tvb, tvbHead, 0);

        if (offset == -1) /* No MYPROTO header found --&gt; return */
            return FALSE;
        else
        {
            gint l_len, l_remain;
            tvbuff_t * tv;

            offset -= offsetof(MYPROTO_HEAD, headPattern);
            l_len = tvb_get_ntohl(tvb, offset + offsetof(MYPROTO_HEAD, msgTotalSizeUI));
            l_remain = tvb_length_remaining(tvb, offset);
            tv = tvb_new_subset(tvb, offset, l_len &gt; l_remain ? -1 : l_len, l_len &gt; l_remain ? -1 : l_len);

            tcp_dissect_pdus(tv, pinfo, tree, TRUE, sizeof(MYPROTO_HEAD), get_myproto_message_len, dissect_myproto);
            return TRUE;
        }
    }
}</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_dissect_pdus" rel="tag" title="see questions tagged &#39;tcp_dissect_pdus&#39;">tcp_dissect_pdus</span> <span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '15, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/6e2e06936e7e5026a548a5683da51ced?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baronju&#39;s gravatar image" /><p><span>baronju</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baronju has no accepted answers">0%</span></p></div></div><div id="comments-container-40098" class="comments-container"></div><div id="comment-tools-40098" class="comment-tools"></div><div class="clear"></div><div id="comment-40098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

