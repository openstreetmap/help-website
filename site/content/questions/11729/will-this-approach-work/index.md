+++
type = "question"
title = "Will this approach work ?"
description = '''Hi,  I want my dissector to get called when there is some specific pattern of dest mac , for that i am using eth heuristic dissector and my data which i want to dissect is last 12 bytes of IP payload.For this i am calling eth_dissector and then i am calculating exact location of my data and hence di...'''
date = "2012-06-06T22:33:00Z"
lastmod = "2012-06-06T22:33:00Z"
weight = 11729
keywords = [ "heuristics", "plugin", "wireshark" ]
aliases = [ "/questions/11729" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Will this approach work ?](/questions/11729/will-this-approach-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11729-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I want my dissector to get called when there is some specific pattern of dest mac , for that i am using eth heuristic dissector and my data which i want to dissect is last 12 bytes of IP payload.For this i am calling eth_dissector and then i am calculating exact location of my data and hence dissecting it. I need to know if this is right approach ?</p><pre><code>guint16 length , offs;
length = tvb_get_guint16(tvb,16);
offs = 14 + length - 12;
call_dissector(eth_dissector, tvb, pinfo, tree);
            if (tree) {

                    ti = proto_tree_add_item(tree, proto_extl2, tvb, offs,-1, TRUE);
                    l2_tree = proto_item_add_subtree(ti, ett_extl2);
                    -----------------------
                    -------------------------
                    Dissection continues..</code></pre></div><div id="question-tags" class="tags-container tags">heuristics plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '12, 22:33</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11729" class="comments-container"></div><div id="comment-tools-11729" class="comment-tools"></div><div class="clear"></div><div id="comment-11729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

