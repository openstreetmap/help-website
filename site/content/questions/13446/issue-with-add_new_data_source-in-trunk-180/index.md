+++
type = "question"
title = "issue with add_new_data_source() in trunk 1.8.0"
description = '''When I try to add dissectors that is not octet-aligned, I found as long as add the following highlighted code the contents of &quot;Hex&quot; view is disappeared. Does anyone know if this is an existing known issue for trunk 1.8.0?  ...  next_tvb = tvb_new_octet_aligned(tvb, offset, tbs[i]);  add_new_data_sou...'''
date = "2012-08-07T18:38:00Z"
lastmod = "2012-08-07T18:38:00Z"
weight = 13446
keywords = [ "1.8.0", "add_new_data_source", "trunk" ]
aliases = [ "/questions/13446" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [issue with add\_new\_data\_source() in trunk 1.8.0](/questions/13446/issue-with-add_new_data_source-in-trunk-180)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13446-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I try to add dissectors that is not octet-aligned, I found as long as add the following highlighted code the contents of "Hex" view is disappeared. Does anyone know if this is an existing known issue for trunk 1.8.0?</p><pre><code>  ...
  next_tvb = tvb_new_octet_aligned(tvb, offset, tbs[i]);
  add_new_data_source(pinfo, next_tvb, &quot;MyProt PDU&quot;); // add this line of code the HEX view is disappeared
  call_dissector(my_handle, next_tvb, pinfo, tree);</code></pre></div><div id="question-tags" class="tags-container tags">1.8.0 add_new_data_source trunk</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '12, 18:38</strong></p><img src="https://secure.gravatar.com/avatar/3f941a275463946999dbd0130888c455?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tools_hpp&#39;s gravatar image" /><p>tools_hpp<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tools_hpp has no accepted answers">0%</span></p></div></div><div id="comments-container-13446" class="comments-container"></div><div id="comment-tools-13446" class="comment-tools"></div><div class="clear"></div><div id="comment-13446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

