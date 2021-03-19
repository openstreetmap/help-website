+++
type = "question"
title = "not a valid display filter"
description = '''In 1.8.5, One of my protocol &quot;wimax-btsbts&quot; is not getting registered. If I try to apply filter &#x27;wimax-btsbts&#x27;, wireshark pop-ups a notification saying Wiax-btsbts is not a valid display filter. I have removed the below last lines : #ifndef ENABLE_STATIC G_MODULE_EXPORT void plugin_register(void)  {...'''
date = "2013-09-26T05:55:00Z"
lastmod = "2013-09-26T05:55:00Z"
weight = 25274
keywords = [ "lnk1169", "proto_register" ]
aliases = [ "/questions/25274" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [not a valid display filter](/questions/25274/not-a-valid-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25274-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In 1.8.5, One of my protocol "wimax-btsbts" is not getting registered. If I try to apply filter 'wimax-btsbts', wireshark pop-ups a notification saying Wiax-btsbts is not a valid display filter. I have removed the below last lines :</p><p><strong>#ifndef ENABLE_STATIC</strong></p><p>G_MODULE_EXPORT void</p><pre><code>plugin_register(void)</code></pre><p>{</p><pre><code>/*register the new protocol, protocol fields, and subtrees */
if (proto_btsBts == -1) { /* execute protocol initialization only once */
    proto_register_BTS_BTS();
}</code></pre><p>}</p><p>G_MODULE_EXPORT void</p><pre><code>plugin_reg_handoff(void){
    proto_reg_handoff_bts_bts();</code></pre><p>}</p><p><strong>#endif</strong></p><p>If I include above compile-time error fatal error LNK1169: one or more multiply defined symbols found occurs. It seems that proto_register never get hit during compilation.Where could be the probable issue?</p></div><div id="question-tags" class="tags-container tags">lnk1169 proto_register</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '13, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/dd64de546bcf7652a4faed163ff02df0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunshine&#39;s gravatar image" /><p>sunshine<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunshine has no accepted answers">0%</span></p></div></div><div id="comments-container-25274" class="comments-container"></div><div id="comment-tools-25274" class="comment-tools"></div><div class="clear"></div><div id="comment-25274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

