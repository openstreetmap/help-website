+++
type = "question"
title = "Constructing new tvbuff from other data"
description = '''Can anyone suggest any examples of dissectors that combine two tvbs together? because I need to remove some unwanted data before processing. Also, if I remove the unwanted data from the tvb and pass that off to say the eth dissector for further processing would the &quot;Packet Bytes&quot; window be updated w...'''
date = "2013-02-16T17:31:00Z"
lastmod = "2013-05-16T02:10:00Z"
weight = 18671
keywords = [ "tvbuff_t" ]
aliases = [ "/questions/18671" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Constructing new tvbuff from other data](/questions/18671/constructing-new-tvbuff-from-other-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18671-score" class="post-score" title="current number of votes">0</div><span id="post-18671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone suggest any examples of dissectors that combine two tvbs together? because I need to remove some unwanted data before processing. Also, if I remove the unwanted data from the tvb and pass that off to say the eth dissector for further processing would the "Packet Bytes" window be updated with the new tvb or will it display the previous one?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tvbuff_t" rel="tag" title="see questions tagged &#39;tvbuff_t&#39;">tvbuff_t</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '13, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/024c038a84faf77c618cfe43ee97ed64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StealthUE&#39;s gravatar image" /><p><span>StealthUE</span><br />
<span class="score" title="66 reputation points">66</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StealthUE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Feb '13, 20:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18671" class="comments-container"><span id="18673"></span><div id="comment-18673" class="comment"><div id="post-18673-score" class="comment-score"></div><div class="comment-text"><p>Combining two tvbuffs doesn't remove data in and of itself.</p><p>Do you mean "taking some data from one tvbuff and some data from another tvbuff, and combining them into a third tvbuff"?</p><p>Or do you mean "taking one tvbuff, removing some data from it, and putting that into another tvbuff"?</p></div><div id="comment-18673-info" class="comment-info"><span class="comment-age">(16 Feb '13, 19:19)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18674"></span><div id="comment-18674" class="comment"><div id="post-18674-score" class="comment-score"></div><div class="comment-text"><p>taking one tvbuff, removing some data from it, and putting that into another tvbuff</p></div><div id="comment-18674-info" class="comment-info"><span class="comment-age">(16 Feb '13, 19:50)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18675"></span><div id="comment-18675" class="comment"><div id="post-18675-score" class="comment-score"></div><div class="comment-text"><p>So are you removing data from the <em>middle</em> of a tvbuff, or just from the beginning or the end?</p></div><div id="comment-18675-info" class="comment-info"><span class="comment-age">(16 Feb '13, 20:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18676"></span><div id="comment-18676" class="comment"><div id="post-18676-score" class="comment-score"></div><div class="comment-text"><p>The data I'm removing will be in the middle of the tvbuff</p></div><div id="comment-18676-info" class="comment-info"><span class="comment-age">(16 Feb '13, 20:57)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="21172"></span><div id="comment-21172" class="comment"><div id="post-21172-score" class="comment-score"></div><div class="comment-text"><p>Hi <span>@guy</span>-harris Above you've asked if the question is "taking some data from one tvbuff and some data from another tvbuff, and combining them into a third tvbuff".</p><p>Actually, that is exactly the question I'm looking for an answer. (The only question I've posted few minutes ago.)</p><p>Could you please give an idea inside that post?</p></div><div id="comment-21172-info" class="comment-info"><span class="comment-age">(16 May '13, 01:53)</span> <span class="comment-user userinfo">barisalis</span></div></div><span id="21174"></span><div id="comment-21174" class="comment not_top_scorer"><div id="post-21174-score" class="comment-score"></div><div class="comment-text"><p><span>@barisalis</span>, see my answer in <a href="http://ask.wireshark.org/questions/21171/combine-ending-part-of-packet-with-starting-part-of-the-next-packet-to-dissect-later-on">your question</a></p></div><div id="comment-21174-info" class="comment-info"><span class="comment-age">(16 May '13, 02:10)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-18671" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-18671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18725"></span>

<div id="answer-container-18725" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18725-score" class="post-score" title="current number of votes">1</div><span id="post-18725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SYN-bit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Figured it out.. When returning the new_tvb I was trying to pass it back into the original tvb eg: tvb = escCharRemove(tvb, pinfo, len, esccharcount); which was causing it to crash it needed to passed into another tvbuff</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '13, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/024c038a84faf77c618cfe43ee97ed64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StealthUE&#39;s gravatar image" /><p><span>StealthUE</span><br />
<span class="score" title="66 reputation points">66</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StealthUE has one accepted answer">100%</span></p></div></div><div id="comments-container-18725" class="comments-container"></div><div id="comment-tools-18725" class="comment-tools"></div><div class="clear"></div><div id="comment-18725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18678"></span>

<div id="answer-container-18678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18678-score" class="post-score" title="current number of votes">1</div><span id="post-18678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Although complicated by various other aspects of the protocol the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-dnp.c?revision=47699&amp;view=markup">DNP3 dissector</a> handles something along these lines as Application Layer (AL) messages have a 16 bit CRC every 16 bytes (chunk). The dissector takes the chunks, checks the CRC, and if OK adds them to a new tvb.</p><p>Have a look at the code following the comment <code>/* extract the application layer data, validating the CRCs */</code> where <code>tmp</code> is the temporary buffer, <code>tmp_ptr</code> points into it, and each chunk is <code>memcpy()</code>'d into it. After all the chunks have been added and if all the CRC's are OK, a new tvb (<code>al_tvb</code>) is created containing the <code>tmp</code> buffer (using <code>tvb_new_child_real_data</code>).</p><p>As AL messages can be fragmented over many TCP or UDP packets, these tvb's are reassembled by the fragmentation code, and eventually end up in <code>next_tvb</code>. A separate hex pane window is created for this tvb using <code>add_new_data_source</code> and then the tvb is passed to the AL dissector in the call <code>dissect_dnp3_al()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '13, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18678" class="comments-container"><span id="18688"></span><div id="comment-18688" class="comment"><div id="post-18688-score" class="comment-score"></div><div class="comment-text"><p>thanks. I'll have a look through it</p></div><div id="comment-18688-info" class="comment-info"><span class="comment-age">(17 Feb '13, 14:58)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18692"></span><div id="comment-18692" class="comment"><div id="post-18692-score" class="comment-score"></div><div class="comment-text"><p>need help! ive posted the code i have so far as the next answer cause i couldn't fit it in as a comment.</p><p>this is what im trying to achieve data in: xx xx xx xx FE FF xx xx data out: xx xx xx xx FF xx xx</p></div><div id="comment-18692-info" class="comment-info"><span class="comment-age">(17 Feb '13, 18:33)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18693"></span><div id="comment-18693" class="comment"><div id="post-18693-score" class="comment-score"></div><div class="comment-text"><pre><code>static tvbuff_t* escCharRemove(tvbuff_t *tvb, packet_info *pinfo, guint data_len)
{
    tvbuff_t *new_tvb;
    int i;
    guint8 *tmp, *tmp_ptr;
    const guint8 *chk_ptr;
    int tmplen;

    tmp = g_malloc(data_len);
    tmp_ptr = tmp;

    tmplen = tvb_length(tvb)-1;
    for(i=0; i&lt;tmplen; i+=2)
    {
        if (tvb_get_guint8(tvb,i) == 0xFE &amp;&amp; (tvb_get_guint8(tvb,i+1) == 0xFF || tvb_get_guint8(tvb,i+1) == 0xFE))
        {
            chk_ptr  = tvb_get_ptr(tvb, 0, i-1);
            memcpy(tmp_ptr, chk_ptr, i-1);
            tmp_ptr += i-1;
            chk_ptr  = tvb_get_ptr(tvb, i+1, tvb_length(tvb));
            memcpy(tmp_ptr, chk_ptr, tvb_length(tvb) - (i + 1));
            tmp_ptr += tvb_length(tvb) - (i + 1);
        }
    }
    new_tvb = tvb_new_child_real_data(tvb, tmp, (guint) (tmp_ptr-tmp), (gint) (tmp_ptr-tmp));
    tvb_set_free_cb(new_tvb, g_free);

    add_new_data_source(pinfo, new_tvb, &quot;New message&quot;);
    free(tmp_ptr);

    return new_tvb;
}</code></pre></div><div id="comment-18693-info" class="comment-info"><span class="comment-age">(17 Feb '13, 18:33)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18696"></span><div id="comment-18696" class="comment"><div id="post-18696-score" class="comment-score"></div><div class="comment-text"><p>data in: xx xx xx xx FE FF xx xx data out: xx xx xx xx FF xx xx</p><p>wireshark just crashes. Im guessing im accessing an illegal part of memory but im unable to find the error. Any help on this would be greatly appreciated as im stuck</p></div><div id="comment-18696-info" class="comment-info"><span class="comment-age">(17 Feb '13, 22:19)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18721"></span><div id="comment-18721" class="comment"><div id="post-18721-score" class="comment-score"></div><div class="comment-text"><p>len is equal to the length of the data without the extra bytes and esccharcount is the amount of extra bytes</p><pre><code>static tvbuff_t* escCharRemove(tvbuff_t *tvb, packet_info *pinfo, gint len, gint esccharcount) /*Removes the extra FE bytes of data*/
{
    tvbuff_t *new_tvb;
    int offset = 0;
    int i;
    guint8 *tmp, *tmp_ptr;
    const guint8 *chk_ptr;
    gint totlen;

    totlen = len + esccharcount;
    tmp = g_malloc(len);
    tmp_ptr = tmp;

    for(i=0; i&lt;totlen; i++)
    {
        if (tvb_get_guint8(tvb,i) == 0xFE &amp;&amp; (tvb_get_guint8(tvb,i+1) == 0xFF || tvb_get_guint8(tvb,i+1) == 0xFE))
        {
            chk_ptr  = tvb_get_ptr(tvb, offset, i-1);
            memcpy(tmp_ptr, chk_ptr, i-1);
            tmp_ptr += i;
            offset = i + 1;
        }
    }
    new_tvb = tvb_new_child_real_data(tvb, tmp, (guint) (tmp_ptr-tmp), (gint) (tmp_ptr-tmp));
    tvb_set_free_cb(new_tvb, g_free);

    add_new_data_source(pinfo, new_tvb, &quot;New message&quot;);

    return new_tvb;
}</code></pre><p>its still giving me problems...deforming packets and crashing wireshark and displaying a memory map in the terminal</p></div><div id="comment-18721-info" class="comment-info"><span class="comment-age">(18 Feb '13, 14:50)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18723"></span><div id="comment-18723" class="comment not_top_scorer"><div id="post-18723-score" class="comment-score"></div><div class="comment-text"><p>I adjusted the size I was using in g_malloc to g_malloc(len * sizeof(int)) and now Im not getting memory issues but every packet that contains the extra data becomes malformed and the extra data is still displayed in the "Packet Bytes" window</p></div><div id="comment-18723-info" class="comment-info"><span class="comment-age">(18 Feb '13, 15:36)</span> <span class="comment-user userinfo">StealthUE</span></div></div></div><div id="comment-tools-18678" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-18678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

