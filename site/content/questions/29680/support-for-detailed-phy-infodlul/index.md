+++
type = "question"
title = "Support for detailed PHY info(DL/UL)"
description = '''Hi, I want to see detail PHY info which is given in structure mac_lte_info in packet-mac-lte.h. But I came to know that in packet-mac-lte.c : In function it&#x27;s by default disable. I want to use it, is it any other way? gboolean dissect_mac_lte_context_fields(struct mac_lte_info *p_mac_lte_info, tvbuf...'''
date = "2014-02-11T03:21:00Z"
lastmod = "2014-02-11T03:31:00Z"
weight = 29680
keywords = [ "mac-lte" ]
aliases = [ "/questions/29680" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Support for detailed PHY info(DL/UL)](/questions/29680/support-for-detailed-phy-infodlul)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29680-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I want to see detail PHY info which is given in structure mac_lte_info in packet-mac-lte.h.</p><p>But I came to know that in packet-mac-lte.c : In function it's by default disable. I want to use it, is it any other way?</p><pre><code>gboolean dissect_mac_lte_context_fields(struct mac_lte_info  *p_mac_lte_info, tvbuff_t *tvb,
                                        gint *p_offset)
{
    gint    offset = *p_offset;
    guint8  tag = 0;

    /* Read fixed fields */
    p_mac_lte_info-&gt;radioType = tvb_get_guint8(tvb, offset++);
    p_mac_lte_info-&gt;direction = tvb_get_guint8(tvb, offset++);

    /* TODO: currently no support for detailed PHY info... */
    if (p_mac_lte_info-&gt;direction == DIRECTION_UPLINK) {
        p_mac_lte_info-&gt;detailed_phy_info.ul_info.present = FALSE;
    }
    else {
        p_mac_lte_info-&gt;detailed_phy_info.dl_info.present = FALSE;
    }

    p_mac_lte_info-&gt;rntiType = tvb_get_guint8(tvb, offset++);

    /* Initialize RNTI with a default val
    ...</code></pre></div><div id="question-tags" class="tags-container tags">mac-lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/4091871c463c530445ea51fd3886f2e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajeev&#39;s gravatar image" /><p>Rajeev<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajeev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '14, 03:22</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29680" class="comments-container"></div><div id="comment-tools-29680" class="comment-tools"></div><div class="clear"></div><div id="comment-29680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29682"></span>

<div id="answer-container-29682" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29682-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since 22nd December last year support was added for detailed PHY info. See <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=9de6aa86197063a9e56f824217e727eb80b363cb">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=9de6aa86197063a9e56f824217e727eb80b363cb</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/4b31b42b2960269c605715bae6547459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinM&#39;s gravatar image" /><p>MartinM<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinM has 3 accepted answers">33%</span></p></div></div><div id="comments-container-29682" class="comments-container"><span id="29684"></span><div id="comment-29684" class="comment"><div id="post-29684-score" class="comment-score"></div><div class="comment-text"><p>Hi Martin, Thanks for reply. Yes carrier Id is working Fine. By your given reference i can still see same in packet-mac-lte.c<br />
/ <em>TODO: currently no support for detailed PHY info...</em> / if (p_mac_lte_info-&gt;direction == DIRECTION_UPLINK) { p_mac_lte_info-&gt;detailed_phy_info.ul_info.present = FALSE; } else { p_mac_lte_info-&gt;detailed_phy_info.dl_info.present = FALSE; } Or, am i doing something wrong ?</p></div><div id="comment-29684-info" class="comment-info"><span class="comment-age">(11 Feb '14, 03:46)</span> Rajeev</div></div><span id="29686"></span><div id="comment-29686" class="comment"><div id="post-29686-score" class="comment-score">1</div><div class="comment-text"><p>Rajeev, that comment/TODO is no longer in that version of the code at that revision onwards. Do you maybe have a svn/git conflict to resolve?</p></div><div id="comment-29686-info" class="comment-info"><span class="comment-age">(11 Feb '14, 04:50)</span> MartinM</div></div><span id="29688"></span><div id="comment-29688" class="comment"><div id="post-29688-score" class="comment-score">1</div><div class="comment-text"><p>As can be seen around line 1817- of the current version of the file <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-mac-lte.c;h=e18ed944473a88c3f50cf84af039cea6ad616c95;hb=HEAD">HERE</a>.</p></div><div id="comment-29688-info" class="comment-info"><span class="comment-age">(11 Feb '14, 05:20)</span> grahamb ♦</div></div><span id="29692"></span><div id="comment-29692" class="comment"><div id="post-29692-score" class="comment-score"></div><div class="comment-text"><p>Thank You Martin &amp; Graham.</p></div><div id="comment-29692-info" class="comment-info"><span class="comment-age">(11 Feb '14, 06:26)</span> Rajeev</div></div><span id="29697"></span><div id="comment-29697" class="comment not_top_scorer"><div id="post-29697-score" class="comment-score"></div><div class="comment-text"><p>@Rajeev</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-29697-info" class="comment-info"><span class="comment-age">(11 Feb '14, 06:51)</span> grahamb ♦</div></div><span id="29727"></span><div id="comment-29727" class="comment not_top_scorer"><div id="post-29727-score" class="comment-score"></div><div class="comment-text"><p>Hi Martin</p><p>I am using Wireshark Version 1.10.5, Released on 19-Dec-2013. And In released source code version wireshark-1.10.5 "\epan\dissectors\packet-mac-lte.c", code is not updated accordingly link given by Graham. Need to updated.</p><p>Please follow the link provided by Graham. Line 1896 : case MAC_LTE_PHY_TAG: -- is not included in wireshark-1.10.5.</p><p>Thank You</p></div><div id="comment-29727-info" class="comment-info"><span class="comment-age">(11 Feb '14, 21:10)</span> Rajeev</div></div><span id="29741"></span><div id="comment-29741" class="comment"><div id="post-29741-score" class="comment-score">1</div><div class="comment-text"><p>You need to take a 1.11.X development build as this code is not part of the stable 1.10.X branch. See <a href="http://www.wireshark.org/develop.html">http://www.wireshark.org/develop.html</a> for the various options to get the development branch source code.</p></div><div id="comment-29741-info" class="comment-info"><span class="comment-age">(12 Feb '14, 01:40)</span> Pascal Quantin</div></div></div><div id="comment-tools-29682" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-29682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

