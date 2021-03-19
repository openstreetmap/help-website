+++
type = "question"
title = "ascii value display"
description = '''how to display character value for a field in my protocol dissection ?i am getting the decimal value ,but want to convert to a character..plz explain'''
date = "2013-05-27T03:37:00Z"
lastmod = "2013-05-27T05:10:00Z"
weight = 21488
keywords = [ "ascii" ]
aliases = [ "/questions/21488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ascii value display](/questions/21488/ascii-value-display)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21488-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to display character value for a field in my protocol dissection ?i am getting the decimal value ,but want to convert to a character..plz explain</p></div><div id="question-tags" class="tags-container tags">ascii</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '13, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/afa04deca78e2ac8df31ecc4deea5bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajain&#39;s gravatar image" /><p>ajain<br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajain has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 May '13, 04:46</p></div></div><div id="comments-container-21488" class="comments-container"></div><div id="comment-tools-21488" class="comment-tools"></div><div class="clear"></div><div id="comment-21488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21489"></span>

<div id="answer-container-21489" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21489-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use FT_STRING field type. Here is an example taken from doc/README.developer:</p><pre><code>static hf_register_info hf[] = {
    {&amp;hf_cstring,
     {&quot;C String&quot;, &quot;c.string&quot;, FT_STRING, BASE_NONE, NULL, 0x0,
      NULL, HFILL}
     }
   };

/**
*   Dissect a buffer containing ASCII C strings.
*
*   @param  tvb     The buffer to dissect.
*   @param  pinfo   Packet Info.
*   @param  tree    The protocol tree.
**/
static void dissect_cstr(tvbuff_t * tvb, packet_info * pinfo, proto_tree * tree)
{
    guint offset = 0;
    while(offset &lt; tvb_reported_length(tvb)) {
        gint available = tvb_reported_length_remaining(tvb, offset);
        gint len = tvb_strnlen(tvb, offset, available);

        if( -1 == len ) {
            /* we ran out of data: ask for more */
            pinfo-&gt;desegment_offset = offset;
            pinfo-&gt;desegment_len = DESEGMENT_ONE_MORE_SEGMENT;
            return;
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
}</code></pre><p>See doc/README.developer or search for FT_STRING usage in the source code for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '13, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-21489" class="comments-container"></div><div id="comment-tools-21489" class="comment-tools"></div><div class="clear"></div><div id="comment-21489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

