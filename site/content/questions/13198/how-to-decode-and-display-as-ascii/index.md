+++
type = "question"
title = "How to decode and display as ASCII?"
description = '''How would I edit my custom dissector to make it decode bytes and display them as ASCII rather than hex or dec or any of the standard formats?'''
date = "2012-07-31T14:13:00Z"
lastmod = "2012-08-06T10:16:00Z"
weight = 13198
keywords = [ "decode", "dissector", "ascii" ]
aliases = [ "/questions/13198" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode and display as ASCII?](/questions/13198/how-to-decode-and-display-as-ascii)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13198-score" class="post-score" title="current number of votes">0</div><span id="post-13198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How would I edit my custom dissector to make it decode bytes and display them as ASCII rather than hex or dec or any of the standard formats?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-ascii" rel="tag" title="see questions tagged &#39;ascii&#39;">ascii</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '12, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/f930b778c54e8c2d76dbcc36f76087ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bball2601&#39;s gravatar image" /><p><span>bball2601</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bball2601 has one accepted answer">50%</span></p></div></div><div id="comments-container-13198" class="comments-container"></div><div id="comment-tools-13198" class="comment-tools"></div><div class="clear"></div><div id="comment-13198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13202"></span>

<div id="answer-container-13202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13202-score" class="post-score" title="current number of votes">0</div><span id="post-13202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ASCII <em>is</em> a standard format - use a field of type <code>FT_STRING</code> or <code>FT_UINT_STRING</code> or <code>FT_STRINGZ</code>, with an encoding of <code>ENC_ASCII</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '12, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-13202" class="comments-container"><span id="13269"></span><div id="comment-13269" class="comment"><div id="post-13269-score" class="comment-score"></div><div class="comment-text"><p>I had tried that...when I used field types FT_STRING and FT_STRINGZ, nothing is displayed, and when I use FT_UNIT_STRING, I get an error saying: [Dissector bug, protocol PFCP: proto.c:1115: failed assertion "DISSECTOR_ASSERT_NOT_REACHED"]</p><p>I'm not sure if I possibly did something wrong. Here is my code dealing with this.</p><p>{ &amp;hf_pfcp_ipAddressStr, { "PFCP IP Address String", "pfcp.ipAddressStr", FT_UINT_STRING, BASE_NONE, NULL, 0, NULL, HFILL } },</p><p>proto_tree_add_item(pfcp_tree, hf_pfcp_ipAddressStr, tvb, offset, 15, ENC_ASCII); offset += 15;</p></div><div id="comment-13269-info" class="comment-info"><span class="comment-age">(01 Aug '12, 09:39)</span> <span class="comment-user userinfo">bball2601</span></div></div><span id="13274"></span><div id="comment-13274" class="comment"><div id="post-13274-score" class="comment-score"></div><div class="comment-text"><p>OK, this is a bit confusing. FT_UINT_STRING is for "counted" strings, where the string has an integral count of characters, followed by the characters. The length you specify is the length in <code>proto_tree_add_item()</code> is the length of the <em>count</em> in bytes, and it has to be between 1 and 4 bytes. In addition, you have to specify the byte-order of the count (<code>ENC_ASCII|ENC_BIG_ENDIAN</code> or <code>ENC_ASCII|ENC_LITTLE_ENDIAN</code>), <em>and</em> to do the <code>offset += N;</code> you'd have to fetch the count yourself and add it to the offset.</p><p>So what format is the string in?</p></div><div id="comment-13274-info" class="comment-info"><span class="comment-age">(01 Aug '12, 09:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="13276"></span><div id="comment-13276" class="comment"><div id="post-13276-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry I'm new to all of this, what do you mean by "what format is the string in"? And I believe the field type I'm going to be wanting to use is FT_STRING, if that makes any difference.</p></div><div id="comment-13276-info" class="comment-info"><span class="comment-age">(01 Aug '12, 10:07)</span> <span class="comment-user userinfo">bball2601</span></div></div><span id="13278"></span><div id="comment-13278" class="comment"><div id="post-13278-score" class="comment-score"></div><div class="comment-text"><p>Is it:</p><ul><li><p>15 bytes of ASCII characters, and always 15 bytes long?</p></li><li><p>0 to 15 bytes of ASCII characters, padded at the end with NULs (bytes with a value of 0);</p></li><li><p>an arbitrary number of ASCII characters, with a NUL at the end (so that it's not always 15 bytes long);</p></li><li><p>a 1-to-4-byte count of characters, followed by that number of ASCII characters (so that it's not always 15 bytes long);</p></li><li><p>something else?</p></li></ul></div><div id="comment-13278-info" class="comment-info"><span class="comment-age">(01 Aug '12, 10:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="13288"></span><div id="comment-13288" class="comment"><div id="post-13288-score" class="comment-score"></div><div class="comment-text"><p>Its 15 bytes of ASCII, always being 15 bytes. Its supposed to represent an IP address in the 000.000.000.000 format, each byte representing a digit or a period, always making it 15 bytes.</p></div><div id="comment-13288-info" class="comment-info"><span class="comment-age">(01 Aug '12, 11:09)</span> <span class="comment-user userinfo">bball2601</span></div></div><span id="13291"></span><div id="comment-13291" class="comment not_top_scorer"><div id="post-13291-score" class="comment-score"></div><div class="comment-text"><p>So 127.0.0.1 would be represented as 127.000.000.001?</p><p>OK, then what <em>should</em> work is</p><pre><code>{ &amp;hf_pfcp_ipAddressStr, { &quot;PFCP IP Address String&quot;, &quot;pfcp.ipAddressStr&quot;, FT_STRING, BASE_NONE, NULL, 0, NULL, HFILL } },</code></pre><p>and</p><pre><code>proto_tree_add_item(pfcp_tree, hf_pfcp_ipAddressStr, tvb, offset, 15, ENC_ASCII); offset += 15;</code></pre><p>If that doesn't work, file a bug - and attach a sample capture that exhibits the problem and your dissector code, if possible, as that would make it a <em>lot</em> easier to debug.</p></div><div id="comment-13291-info" class="comment-info"><span class="comment-age">(01 Aug '12, 11:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="13400"></span><div id="comment-13400" class="comment not_top_scorer"><div id="post-13400-score" class="comment-score"></div><div class="comment-text"><p>I finally got it working. The packets I was using I had individually created with another program, and it seems I created them wrong. Once I tested it with a proper packet, it decoded properly.</p><p>Thanks for all your help.</p></div><div id="comment-13400-info" class="comment-info"><span class="comment-age">(06 Aug '12, 10:16)</span> <span class="comment-user userinfo">bball2601</span></div></div></div><div id="comment-tools-13202" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-13202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

