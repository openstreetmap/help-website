+++
type = "question"
title = "fragment_head  is not returning any Value"
description = '''Hi, While doing Reassembly in my dissector  fragment_head *fd_head;  i have assigned. After declaring table   fd_head = fragment_add_seq_next(&amp;amp;mte_reassembly_table,next_tvb, offset_payload, pinfo, 0, NULL, 28, TRUE );   if (fd_head != NULL){  col_append_fstr(pinfo-&amp;gt;cinfo, COL_INFO, &quot; MTE segm...'''
date = "2014-12-08T03:14:00Z"
lastmod = "2014-12-08T03:14:00Z"
weight = 38426
keywords = [ "fragment", "head", "reassemble" ]
aliases = [ "/questions/38426" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [fragment\_head is not returning any Value](/questions/38426/fragment_head-is-not-returning-any-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38426-score" class="post-score" title="current number of votes">0</div><span id="post-38426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>While doing Reassembly in my dissector</p><p>fragment_head *fd_head; i have assigned. After declaring table</p><pre><code>  fd_head = fragment_add_seq_next(&amp;mte_reassembly_table,next_tvb, offset_payload, pinfo, 0, NULL,  28, TRUE );

 if (fd_head != NULL){
     col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; MTE segment of a reassembled PDU&quot;);
    } else {

           col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; Something Wrong&quot;);

   }</code></pre><p>next_tvb is a originnal TVB and offset_payload is Not a Zero . seq id set to 0 and data is NULL and 28 is the length and more_frags set true.</p><p>Iam always getting the colinfo as Something Wrong. i have tried using fragment_add_seq_check, fragment_add_seq but still same. Can anyone help me why iam not getting the fd_head?</p><p>My table initialization all ok. comparesd with other dissectors.??</p><p>Please Help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragment" rel="tag" title="see questions tagged &#39;fragment&#39;">fragment</span> <span class="post-tag tag-link-head" rel="tag" title="see questions tagged &#39;head&#39;">head</span> <span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '14, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Dec '14, 21:45</strong> </span></p></div></div><div id="comments-container-38426" class="comments-container"></div><div id="comment-tools-38426" class="comment-tools"></div><div class="clear"></div><div id="comment-38426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

