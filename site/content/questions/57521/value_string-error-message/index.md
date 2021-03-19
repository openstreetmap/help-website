+++
type = "question"
title = "value_string error message"
description = '''Hi, I am trying to write my own dissector and so far it works pretty well. However, I am using value_string but it does not work as expected. By studying other dissectors, I see that most value_string arrays look like the following: static const value_string foo[] = {  {1, &quot;One&quot;},  {2, &quot;Two&quot;},  {0, ...'''
date = "2016-11-21T05:54:00Z"
lastmod = "2016-11-21T06:18:00Z"
weight = 57521
keywords = [ "dissector", "value_string", "ft_string" ]
aliases = [ "/questions/57521" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [value\_string error message](/questions/57521/value_string-error-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57521-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to write my own dissector and so far it works pretty well. However, I am using value_string but it does not work as expected. By studying other dissectors, I see that most value_string arrays look like the following:</p><pre><code>static const value_string foo[] = {
    {1, &quot;One&quot;},
    {2, &quot;Two&quot;},
    {0, NULL} };</code></pre><p>Instead of having integers as the value, I want to have characters, example:</p><pre><code>static const value_string foo2[] = {
    {&#39;A&#39;, &quot;One&quot;},
    {&#39;B&#39;, &quot;Two&quot;},
    {0, NULL} };</code></pre><p>My header field is the following:</p><pre><code>{ &amp;hf_field, /* supposed to be ampersand */
{ &quot;Field&quot;, &quot;proto.field&quot;, FT_STRING, STR_ASCII, VALS(foo2),0x00, NULL, HFILL }}</code></pre><p>The idea behind having FT_STRING is that it should show the char value from foo2. However, this does not work. I get the following error message</p><p>"Err Field 'FIELDNAME' has a 'strings' value but is of type FT_STRING (which is not allowed to have strings)"</p><p>If I change from "FT_STRING, STR_ASCII" to "FT_UINT8, BASE_DEC" it works but it shows the ascii decimal value (example 65 instead of 'A').</p><p>Is there a way I can accomplish this? As previously mentioned, all dissectors I have studied only have integers as their values and not chars. Does that mean my idea is not possible?</p><p>I also want to point out that I read <a href="https://ask.wireshark.org/questions/889/creating-a-filter-to-filter-on-a-text-label-based-on-a-uint64">this</a> which to me makes it sound like the value_string stuff does not support FT_STRING.</p></div><div id="question-tags" class="tags-container tags">dissector value_string ft_string</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '16, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/ea2079f8254c72aba204dd5d028063ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hokosha&#39;s gravatar image" /><p>hokosha<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hokosha has no accepted answers">0%</span></p></div></div><div id="comments-container-57521" class="comments-container"></div><div id="comment-tools-57521" class="comment-tools"></div><div class="clear"></div><div id="comment-57521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57526"></span>

<div id="answer-container-57526" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57526-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Indeed value_string arrays are designed to match a value (understand a number) and associate with it a string. FT_STRING is designed for fields containing a string, and cannot work with value_string arrays.</p><p>What you can eventually do is to use either the proto_tree_add_uint_format_value or proto_tree_add_string_format_value function to fully control the display. Note that it will not impact the filter content. Have a look at doc/README.dissector for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '16, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-57526" class="comments-container"><span id="57531"></span><div id="comment-57531" class="comment"><div id="post-57531-score" class="comment-score"></div><div class="comment-text"><p>You may also want to check out another type of value_string called a string_string. Unfortunately it seems this isn't yet supported in hf's (i.e., there's no VALS*() macro to allow your string_string to be put in the hf) but it should help...</p><p>(I wonder why string_string's aren't supported in hf's...)</p></div><div id="comment-57531-info" class="comment-info"><span class="comment-age">(21 Nov '16, 08:20)</span> JeffMorriss ♦</div></div><span id="57694"></span><div id="comment-57694" class="comment"><div id="post-57694-score" class="comment-score"></div><div class="comment-text"><p>Note that master tree now supports a FT_CHAR, that could be used in this case:</p><p>"FT_CHAR An 8-bit ASCII character. It's treated similarly to an FT_UINT8, but is displayed as a C-style character constant."</p></div><div id="comment-57694-info" class="comment-info"><span class="comment-age">(29 Nov '16, 03:24)</span> Pascal Quantin</div></div></div><div id="comment-tools-57526" class="comment-tools"></div><div class="clear"></div><div id="comment-57526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

