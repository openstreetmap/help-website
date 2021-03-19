+++
type = "question"
title = "Display successive data on one row when dissecting"
description = '''Hi Forum, I would like to know how dissect and display data in as successive fields on a single row using. My data N | followed by n bytes - ie 1001020304050607080910 I wish to dissect and display as  Count : 10 Values : [1,2,3,4,5,6,7,8,9,10]. The current dissector I am using   {&amp;amp;hf_count, {&quot;Co...'''
date = "2013-01-24T03:12:00Z"
lastmod = "2013-01-24T03:15:00Z"
weight = 17925
keywords = [ "dissector", "display" ]
aliases = [ "/questions/17925" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display successive data on one row when dissecting](/questions/17925/display-successive-data-on-one-row-when-dissecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17925-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Forum,</p><p>I would like to know how dissect and display data in as successive fields on a single row using.</p><p>My data N | followed by n bytes - ie 1001020304050607080910</p><p>I wish to dissect and display as Count : 10 Values : [1,2,3,4,5,6,7,8,9,10].</p><p>The current dissector I am using</p><pre><code>  {&amp;hf_count, {&quot;Count&quot;,  &quot;&quot;, FT_UINT8,    BASE_DEC,  NULL, 0x0, NULL, HFILL}},
  {&amp;hf_value,{&quot;Value&quot;, &quot;&quot;,  FT_UINT8,    BASE_DEC,   NULL, 0x0, NULL, HFILL}},
  proto_tree_add_item(...hf_count.)
  for loop {
       proto_tree_add_item(...hf_value.)
  }</code></pre><p>However, it shows the values on a separate row.<br />
</p><p>How set up the dissector to display the how I wish?</p><p>Thanks</p><p>Stuart</p></div><div id="question-tags" class="tags-container tags">dissector display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/e12bbe1b488f2a19cdf565465e260d19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StuieNorris&#39;s gravatar image" /><p>StuieNorris<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StuieNorris has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-17925" class="comments-container"></div><div id="comment-tools-17925" class="comment-tools"></div><div class="clear"></div><div id="comment-17925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17926"></span>

<div id="answer-container-17926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17926-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use the various <code>tvb_get_</code> routines, such as <code>tvb_get_guint8()</code>, to fetch the appropriate values from the tvbuff, and use <code>proto_tree_add_text()</code> to put in an entry into the protocol tree in whatever format you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17926" class="comments-container"></div><div id="comment-tools-17926" class="comment-tools"></div><div class="clear"></div><div id="comment-17926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

