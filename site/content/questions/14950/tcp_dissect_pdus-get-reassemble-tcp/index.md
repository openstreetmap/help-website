+++
type = "question"
title = "[closed] tcp_dissect_pdus. get reassemble TCP"
description = '''Hi,  I&#x27;m using  tcp_dissect_pdus(tvb, pinfo, tree, TRUE, FRAME_HEADER_LEN,  get_foo_message_len, dissect_foo_message) to reassemble split TCP Packets in my own dissector. However, I cannot get the full TCP packet. In the dissect_foo_message, I do nothing first, just get the full TCP context by using...'''
date = "2012-10-11T23:56:00Z"
lastmod = "2012-10-15T07:37:00Z"
weight = 14950
keywords = [ "reassemble", "tcp" ]
aliases = [ "/questions/14950" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] tcp\_dissect\_pdus. get reassemble TCP](/questions/14950/tcp_dissect_pdus-get-reassemble-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14950-score" class="post-score" title="current number of votes">0</div><span id="post-14950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using</p><p><em>tcp_dissect_pdus(tvb, pinfo, tree, TRUE, FRAME_HEADER_LEN, get_foo_message_len, dissect_foo_message)</em></p><p>to reassemble split TCP Packets in my own dissector. However, I cannot get the full TCP packet. In the <em>dissect_foo_message</em>, I do nothing first, just get the full TCP context by using:</p><pre><code>data_len = tvb_length(tvb);
sprintf(str, &quot;%s\n&quot;, tvb_get_string(tvb, 122, data_len));</code></pre><p>the context in str is truncated.</p><p>I'm confused, according to the tutorial, I should get the full TCP packet in the dissect_foo_message, right? Help!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/f1e82e9d684047b8c41f89a4163b8863?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razygon&#39;s gravatar image" /><p><span>razygon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razygon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>15 Oct '12, 07:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-14950" class="comments-container"><span id="14964"></span><div id="comment-14964" class="comment"><div id="post-14964-score" class="comment-score">1</div><div class="comment-text"><p>We'll need to see a bit more of your code. How are you determining the actual length of the PDU in <code>get_foo_message_len()</code> ?</p><p><code>dissect_foo_message()</code> will be handed a tvb of whatever length is returned by <code>get_foo_message_len()</code></p></div><div id="comment-14964-info" class="comment-info"><span class="comment-age">(12 Oct '12, 06:48)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="15010"></span><div id="comment-15010" class="comment"><div id="post-15010-score" class="comment-score"></div><div class="comment-text"><pre><code>void proto_reg_handoff_dataparse(void)
{
    dataparse_handle = create_dissector_handle(dissect_dataparse, proto_dataparse);
    dissector_add_uint(&quot;tcp.port&quot;, dataparse_PORT, dataparse_handle); 
    **`//so the tvb only include data, no package headers, right?`**

}
static guint get_dataparse_message_len(packet_info *pinfo, tvbuff_t *tvb, int offset)
{
    return 2000;
}
static void dissect_dataparse_message(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    int ip_len = 0;
    int data_len = 0;
    char *str;

    FILE *stream;

    if ((stream = fopen(filename,&quot;a&quot;)) ==NULL)
    {
        return;
    }

    data_len = tvb_length(tvb);
    str = (char *)malloc(data_len);
    sprintf(str, &quot;%s\n&quot;, tvb_get_string(tvb, 0, 2000));
    fwrite(str, strlen(str), 1, stream);        
    if(stream != NULL)
    fclose(stream);</code></pre><p>}</p></div><div id="comment-15010-info" class="comment-info"><span class="comment-age">(15 Oct '12, 02:54)</span> <span class="comment-user userinfo">razygon</span></div></div><span id="15011"></span><div id="comment-15011" class="comment"><div id="post-15011-score" class="comment-score"></div><div class="comment-text"><p>Hi Bill, I didn't finish the code, now i'm testing the function tcp_dissect_pdus() to check whether it works. But i try to give specific code in the below comment. besides that I have two questions: 1. I cannot get the len in advance, for the protocol didn't give it... is there any other way to get it? 2. for test, i set the return value of get_foo_message_len fixed, like 2000. but the data i get is not consecutive? confused...</p></div><div id="comment-15011-info" class="comment-info"><span class="comment-age">(15 Oct '12, 02:58)</span> <span class="comment-user userinfo">razygon</span></div></div><span id="15018"></span><div id="comment-15018" class="comment"><div id="post-15018-score" class="comment-score"></div><div class="comment-text"><p>[ This type of discussion is best done on <span class="__cf_email__" data-cfemail="a2d5cbd0c7d1cac3d0c98fc6c7d4e2">[email protected]</span><a href="http://wireshark.org">wireshark.org</a> mailing list.</p><p>So: I'm taking the liberty of "closing" this question in favor of continuing the discussion on wireshark-dev; I'll post a reply shortly on wireshark-dev.</p><p>See <a href="https://www.wireshark.org/lists/">https://www.wireshark.org/lists/</a> to subscribe to the list. ]</p></div><div id="comment-15018-info" class="comment-info"><span class="comment-age">(15 Oct '12, 07:37)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-14950" class="comment-tools"></div><div class="clear"></div><div id="comment-14950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "(Discussion to continue on wireshark-dev mailing list)." by Bill Meier 15 Oct '12, 07:38

</div>

</div>

</div>

