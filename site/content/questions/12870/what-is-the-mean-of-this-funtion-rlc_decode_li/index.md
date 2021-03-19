+++
type = "question"
title = "what is  the mean of this funtion: rlc_decode_li?"
description = '''In UMTS, lub_decoder,MAC to RLC,there is a cipher/decipher process. I have to find this process.But I can&#x27;t find code in wireshark,just a function:rlc_decode_li,maybe this a cipher?? follow is the code in wireshark. pos = fpinf-&amp;gt;cur_tb; if (rlcinf-&amp;gt;ciphered[pos] == TRUE &amp;amp;&amp;amp; rlcinf-&amp;gt;d...'''
date = "2012-07-19T19:31:00Z"
lastmod = "2012-07-19T19:31:00Z"
weight = 12870
keywords = [ "decipher", "cipher", "rlc_decode_li" ]
aliases = [ "/questions/12870" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what is the mean of this funtion: rlc\_decode\_li?](/questions/12870/what-is-the-mean-of-this-funtion-rlc_decode_li)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12870-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In UMTS, lub_decoder,MAC to RLC,there is a cipher/decipher process. I have to find this process.But I can't find code in wireshark,just a function:rlc_decode_li,maybe this a cipher?? follow is the code in wireshark.</p><pre><code>pos = fpinf-&gt;cur_tb;
if (rlcinf-&gt;ciphered[pos] == TRUE &amp;&amp; rlcinf-&gt;deciphered[pos] == FALSE) {
    proto_tree_add_text(tree, tvb, 0, -1,
        &quot;Cannot dissect RLC frame because it is ciphered&quot;);
    return;
}  
num_li = rlc_decode_li(RLC_AM, tvb, pinfo, tree, li, MAX_LI);
if (num_li == -1) return; /* something went wrong */
offs += num_li;</code></pre></div><div id="question-tags" class="tags-container tags">decipher cipher rlc_decode_li</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '12, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p>smilezuzu<br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jul '12, 19:32</p></div></div><div id="comments-container-12870" class="comments-container"></div><div id="comment-tools-12870" class="comment-tools"></div><div class="clear"></div><div id="comment-12870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

