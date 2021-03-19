+++
type = "question"
title = "Wireshark dissector development - Reassembly tcp frames"
description = '''Just before starting, sorry for my english... i&#x27;m french. I&#x27;m developing (in C language) a wireshark dissector to dissect a specific protocol to the company (it&#x27;s owner of it) where I work but I have a problems when messages are several TCP frames ... I can not reassemble the messages when a message...'''
date = "2014-11-04T04:47:00Z"
lastmod = "2014-11-13T05:33:00Z"
weight = 37566
keywords = [ "reassembly", "dissector", "help", "tcp", "wireshark" ]
aliases = [ "/questions/37566" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark dissector development - Reassembly tcp frames](/questions/37566/wireshark-dissector-development-reassembly-tcp-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37566-score" class="post-score" title="current number of votes">0</div><span id="post-37566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just before starting, sorry for my english... i'm french.</p><p>I'm developing (in C language) a wireshark dissector to dissect a specific protocol to the company (it's owner of it) where I work but I have a problems when messages are several TCP frames ... I can not reassemble the messages when a message is broken into two different frames TCP, I can not reform it in one message...</p><p>I read the readme.dissector and try using two methods:</p><pre><code>First method:

    tcp_dissect_pdus(tvb, pinfo, tree, dns_desegment, 2,
                get_dns_pdu_len, dissect_dns_tcp_pdu, data);
            return tvb_captured_length(tvb);

Second method :

    guint offset = 0;
        while(offset &lt; tvb_reported_length(tvb)) {
            gint available = tvb_reported_length_remaining(tvb, offset);
            gint len = tvb_strnlen(tvb, offset, available);

            if( -1 == len ) {
                /* we ran out of data: ask for more */
                pinfo-&gt;desegment_offset = offset;
                pinfo-&gt;desegment_len = DESEGMENT_ONE_MORE_SEGMENT;
                return (offset + available);
            }

            col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;C String&quot;);

            len += 1; /* Add one for the &#39;\0&#39; */

            if (tree) {
                proto_tree_add_item(tree, hf_cstring, tvb, offset, len,
                    ENC_ASCII|ENC_NA);
            }
            offset += (guint)len;
        }

        /* if we get here, then the end of the tvb coincided with the end of a
           string. Happy days. */
        return tvb_captured_length(tvb);</code></pre><p>But impossible to reassemble the message, I do not understand why ... can you help me please? I hope you understand my problem ...: /</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '14, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/6e41ef358edbaa0233d30fbd5b41b4d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guillaume&#39;s gravatar image" /><p><span>Guillaume</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guillaume has no accepted answers">0%</span></p></div></div><div id="comments-container-37566" class="comments-container"><span id="37640"></span><div id="comment-37640" class="comment"><div id="post-37640-score" class="comment-score"></div><div class="comment-text"><p>Nobody can help me please ?</p></div><div id="comment-37640-info" class="comment-info"><span class="comment-age">(07 Nov '14, 01:53)</span> <span class="comment-user userinfo">Guillaume</span></div></div><span id="37641"></span><div id="comment-37641" class="comment"><div id="post-37641-score" class="comment-score"></div><div class="comment-text"><p>You're not really giving anyone a chance to help. You must describe in more detail what happens with the two methods, as they are both used successfully elsewhere in the code.</p><p>The first method is definitely the easiest as long as you have correctly created the <code>get_dns_pdu_len()</code> function. Have you tried debugging the code to check that function returns the expected value?</p></div><div id="comment-37641-info" class="comment-info"><span class="comment-age">(07 Nov '14, 02:48)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37646"></span><div id="comment-37646" class="comment"><div id="post-37646-score" class="comment-score"></div><div class="comment-text"><p>Thank grahamb for your answer!</p><p>I will try to explain you... So, my problem is to reassemble the packets between them. To illustrate this, see "picture1.png" (in the end of this message) which shows the packet number 8 should be following the packet number 6. As you can see the number 6 is malformed packet because its sequel is in the number 8 ... I can not get them together to make one cut and the entire message ...</p><p>To reach the result of "picture1.png" I'll put the code I use. "choixMessageASA" allows according to the header frame of the ASA (the protocol that I have to decode) to know what message travels :</p><p>if (tree) {</p><pre><code>    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;ASA&quot;);
    col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;Ceci est un test message ASA&quot;);
    ti = proto_tree_add_item(tree, proto_asa, tvb, 0, -1, ENC_NA);
    asa_tree = proto_item_add_subtree(ti, ett_asa);
    artrh = wmem_new(wmem_packet_scope(), struct artere_header);
    artrh-&gt;th_length = tvb_get_ntohs(tvb, offset);
    if(artrh-&gt;th_length &gt; tvb_length(tvb)){
        pinfo-&gt;desegment_offset = offset;
        pinfo-&gt;desegment_len = artrh-&gt;th_length - tvb_length(tvb);
        choixMessageASA(artrh, tvb, asa_tree, &amp;offset);
    } else {
        choixMessageASA(artrh, tvb, asa_tree, &amp;offset);
    }

}</code></pre><p>I hope you can help me :/</p><p>picture1.png : <img src="https://osqa-ask.wireshark.org/upfiles/picture1_VHv0ZuD.png" alt="alt text" /></p></div><div id="comment-37646-info" class="comment-info"><span class="comment-age">(07 Nov '14, 05:14)</span> <span class="comment-user userinfo">Guillaume</span></div></div><span id="37669"></span><div id="comment-37669" class="comment"><div id="post-37669-score" class="comment-score"></div><div class="comment-text"><p>Why don't you use tvb_dissect_pdus? It would be much simpler. The code should be something like this:</p><pre><code>static int dissect_asa_pdu(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data)
{
    tcp_dissect_pdus(tvb, pinfo, tree, TRUE, 2, get_asa_pdu_len, dissect_asa_pdu, data); 
    return tvb_captured_length(tvb);
}</code></pre><p>where get_asa_pdu_len() is:</p><pre><code>static guint get_asa_pdu_len(packet_info *pinfo _U_, tvbuff_t *tvb, int offset)
{
    return tvb_get_ntohs(tvb, offset);
}</code></pre></div><div id="comment-37669-info" class="comment-info"><span class="comment-age">(07 Nov '14, 13:07)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="37776"></span><div id="comment-37776" class="comment"><div id="post-37776-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer and sorry for my late reply ...</p><p>I tried the way you speak with tvb_dissect_pdus but the result is the same, I get the same thing as "picture1.png" I set in my previous message ... Do not you know how to meet the frames 6 and 8 (those of "picture1.png") and dissect the whole frame assembled?</p></div><div id="comment-37776-info" class="comment-info"><span class="comment-age">(12 Nov '14, 01:08)</span> <span class="comment-user userinfo">Guillaume</span></div></div><span id="37782"></span><div id="comment-37782" class="comment not_top_scorer"><div id="post-37782-score" class="comment-score"></div><div class="comment-text"><p>One small thing reassembly and code adding to columns shouldn't be under "if (tree) {" as allwas should be executed.</p></div><div id="comment-37782-info" class="comment-info"><span class="comment-age">(12 Nov '14, 04:10)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="37785"></span><div id="comment-37785" class="comment not_top_scorer"><div id="post-37785-score" class="comment-score"></div><div class="comment-text"><p>Thank you Anders for your answer but I do not know what you mean ... is it possible showing me what would be the code please?</p><p>You thought that because it gives me the same thing:</p><pre><code>col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;ASA&quot;);
col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;Ceci est un test message ASA&quot;);

ti = proto_tree_add_item(tree, proto_asa, tvb, 0, -1, ENC_NA);
asa_tree = proto_item_add_subtree(ti, ett_asa);

artrh = wmem_new(wmem_packet_scope(), struct artere_header);

artrh-&gt;th_length = tvb_get_ntohs(tvb, offset);

if(artrh-&gt;th_length &gt; tvb_length(tvb)){
    if (tree) {
       pinfo-&gt;desegment_offset = offset;
       pinfo-&gt;desegment_len = artrh-&gt;th_length - tvb_length(tvb);
       choixMessageASA(artrh, tvb, asa_tree, &amp;offset);
} else {
    if (tree) {
       choixMessageASA(artrh, tvb, asa_tree, &amp;offset);
    }
}</code></pre></div><div id="comment-37785-info" class="comment-info"><span class="comment-age">(12 Nov '14, 04:45)</span> <span class="comment-user userinfo">Guillaume</span></div></div><span id="37786"></span><div id="comment-37786" class="comment not_top_scorer"><div id="post-37786-score" class="comment-score"></div><div class="comment-text"><p>Higer up in the post before the code box you have</p><blockquote><p>if (tree) { if that's in your code and the code block is inside it - it's wrong. e.g the reassembly code must not be inside an if(tree) attement.</p></blockquote></div><div id="comment-37786-info" class="comment-info"><span class="comment-age">(12 Nov '14, 05:00)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="37789"></span><div id="comment-37789" class="comment not_top_scorer"><div id="post-37789-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, I did not understand what you meant! I succeeded to make it work according your advice, thank you!</p><p>Quick question, how can I customize the "length" column to display the length of the reassembled message and not the length of the normal message?</p></div><div id="comment-37789-info" class="comment-info"><span class="comment-age">(12 Nov '14, 05:51)</span> <span class="comment-user userinfo">Guillaume</span></div></div><span id="37790"></span><div id="comment-37790" class="comment not_top_scorer"><div id="post-37790-score" class="comment-score"></div><div class="comment-text"><p>Use something like <code>col_add_fstr(pinfo-&gt;cinfo, COL_PACKET_LENGTH, "%i", new_length);</code>, but be very careful about this, all Wireshark users and code expect the length column to contain the length of that frame, not reassembled length from subsequent frames. You would be better adding the length as a field in the packet tree and possibly in the "Info" column.</p></div><div id="comment-37790-info" class="comment-info"><span class="comment-age">(12 Nov '14, 06:13)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37807"></span><div id="comment-37807" class="comment not_top_scorer"><div id="post-37807-score" class="comment-score"></div><div class="comment-text"><p>The changes made to the hiqnet dissector <a href="https://code.wireshark.org/review/#/c/5267/1">here</a> show how simple it is to do reassembly when using tcp_dissect_pdus().</p></div><div id="comment-37807-info" class="comment-info"><span class="comment-age">(13 Nov '14, 01:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37817"></span><div id="comment-37817" class="comment not_top_scorer"><div id="post-37817-score" class="comment-score"></div><div class="comment-text"><p>I have already tried this method but I have two warnings during compilation :</p><ul><li><p><code>warning C4020: 'tcp_dissect_pdus' : too many actuals parameters</code> but if I remove the "data" parameter at the end of <code>tcp_dissect_pdu</code> the warning disappears...</p></li><li><p><code>warning C4013: 'tcp_captured_length' undefined; assuming extern returning int</code> while i imported the correct files...</p></li></ul><p>This is why I have not used this method even if it is faster :/</p></div><div id="comment-37817-info" class="comment-info"><span class="comment-age">(13 Nov '14, 04:38)</span> <span class="comment-user userinfo">Guillaume</span></div></div><span id="37819"></span><div id="comment-37819" class="comment not_top_scorer"><div id="post-37819-score" class="comment-score"></div><div class="comment-text"><p>Are you using an older version of source code, rather than trunk (or 1.12)?</p><p>The <code>dissector_data</code> parameter was added to <code>tcp_dissect_pdus</code> last year:</p><blockquote><code> commit 8081cf1d90397cbbb4404f9720595e1537ed5e14                                                     Author: Michael Mann &lt;[email protected]&gt;                                                         Date:   Sat Nov 9 17:46:28 2013 +0000      Add data parameter to tcp_dissect_pdus() as well as convert it to using "new" style dissectors.</code></blockquote><p>Did you actually use <code>tcp_captured_length</code> in your code or is that just a typo in your comment? It should be <code>tvb_captured_length</code> and that was added earlier this year:</p><blockquote><code> commit 22149c5523a77e642ec13d12064b2ccef29e51fb                                      Author: Evan Huus &lt;[email protected]&gt;                                                Date:   Sat Feb 22 08:39:57 2014 -0500      TVB API deprecations and cleanup                                                      - rename tvb_length and similar to tvb_captured_length and similar; leave              #defines in place for backwards-compat, but mark them clearly as deprecated in       code comments and in checkAPI                                                 </code></blockquote></div><div id="comment-37819-info" class="comment-info"><span class="comment-age">(13 Nov '14, 04:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37820"></span><div id="comment-37820" class="comment not_top_scorer"><div id="post-37820-score" class="comment-score"></div><div class="comment-text"><p>I use an an older version is why the <code>tcp_dissect_pdus</code> does not work with the data parameter! You're right!</p><p>For <code>tvb_captured_length</code> is a typo from me in my comment for the <code>tcp</code> .. Maybe the warning is there because I do not have the latest version of Wireshark.</p><p>Anyway, thank you all for your answers, it has been of great help!</p></div><div id="comment-37820-info" class="comment-info"><span class="comment-age">(13 Nov '14, 05:33)</span> <span class="comment-user userinfo">Guillaume</span></div></div></div><div id="comment-tools-37566" class="comment-tools"><span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a></div><div class="clear"></div><div id="comment-37566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

