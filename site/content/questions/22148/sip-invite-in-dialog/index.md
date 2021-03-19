+++
type = "question"
title = "SIP INVITE in-dialog"
description = '''Hi all, I&#x27;m tracing SIP calls, and sometimes I see INVITE messages indicated with &quot;in-dialog&quot;. What does that mean??? Reg, Gerben'''
date = "2013-06-19T02:35:00Z"
lastmod = "2013-06-19T04:21:00Z"
weight = 22148
keywords = [ "sip", "in-dialog", "invite" ]
aliases = [ "/questions/22148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SIP INVITE in-dialog](/questions/22148/sip-invite-in-dialog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm tracing SIP calls, and sometimes I see INVITE messages indicated with "in-dialog". What does that mean???</p><p>Reg,</p><p>Gerben</p></div><div id="question-tags" class="tags-container tags">sip in-dialog invite</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '13, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/ac649e2bf183a6d7e0cf217528e3bfad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glammertink&#39;s gravatar image" /><p>glammertink<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glammertink has no accepted answers">0%</span></p></div></div><div id="comments-container-22148" class="comments-container"></div><div id="comment-tools-22148" class="comment-tools"></div><div class="clear"></div><div id="comment-22148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22151"></span>

<div id="answer-container-22151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22151-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This indicator is added to the info column by Wireshark when it finds a "tag" added in one of the headers of an INVITE, SUBSCRIBE or REFER message.</p><p>Deducted from the following part of the sip dissector:</p><pre><code>                        parameter_offset = offset;
                        while (parameter_offset &lt; line_end_offset
                               &amp;&amp; (tvb_strneql(tvb, parameter_offset, &quot;tag=&quot;, 4) != 0))
                            parameter_offset++;

                        if ( parameter_offset &lt; line_end_offset ){ /* Tag found */
                            parameter_offset = parameter_offset + 4;
                            parameter_end_offset = tvb_find_guint8(tvb, parameter_offset,
                                                                   (line_end_offset - parameter_offset), &#39;;&#39;);
                            if ( parameter_end_offset == -1)
                                parameter_end_offset = line_end_offset;
                            parameter_len = parameter_end_offset - parameter_offset;
                            proto_tree_add_item(sip_element_tree, hf_sip_to_tag, tvb, parameter_offset,
                                                parameter_len, ENC_ASCII|ENC_NA);
                            item = proto_tree_add_item(sip_element_tree, hf_sip_tag, tvb, parameter_offset,
                                                       parameter_len, ENC_ASCII|ENC_NA);
                            PROTO_ITEM_SET_HIDDEN(item);

                            /* Tag indicates in-dialog messages, in case we have a INVITE, SUBSCRIBE or REFER, mark it */
                            switch (current_method_idx) {

                            case SIP_METHOD_INVITE:
                            case SIP_METHOD_SUBSCRIBE:
                            case SIP_METHOD_REFER:
                                col_append_str(pinfo-&gt;cinfo, COL_INFO, &quot;, in-dialog&quot;);
                                break;
                            }
                        }</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22151" class="comments-container"></div><div id="comment-tools-22151" class="comment-tools"></div><div class="clear"></div><div id="comment-22151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

