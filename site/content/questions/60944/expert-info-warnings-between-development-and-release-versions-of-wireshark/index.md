+++
type = "question"
title = "Expert Info Warnings between development and release versions of Wireshark"
description = '''I am using development version 2.3.0 and release version 2.2.5 of Wireshark in development of a C dissector (on the same system). Referring back to https://ask.wireshark.org/questions/60224/difference-between-proto_tree_add_item-and-proto_tree_add_uint , I currently have a warning for using the wron...'''
date = "2017-04-21T06:13:00Z"
lastmod = "2017-04-21T07:25:00Z"
weight = 60944
keywords = [ "development", "c", "dissector", "expert-info" ]
aliases = [ "/questions/60944" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Expert Info Warnings between development and release versions of Wireshark](/questions/60944/expert-info-warnings-between-development-and-release-versions-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60944-score" class="post-score" title="current number of votes">0</div><span id="post-60944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using development version 2.3.0 and release version 2.2.5 of Wireshark in development of a C dissector (on the same system). Referring back to <a href="https://ask.wireshark.org/questions/60224/difference-between-proto_tree_add_item-and-proto_tree_add_uint">https://ask.wireshark.org/questions/60224/difference-between-proto_tree_add_item-and-proto_tree_add_uint</a> , I currently have a warning for using the wrong FT_UINT for a field.</p><p>The code in question:</p><p>#define PROTO_MEMORY_WRITE_ADDRESS_LEN 8</p><pre><code>    proto_tree_add_item(proto_tree, hf_proto_memory_write_address, tvb, offset, PROTO_MEMORY_WRITE_ADDRESS_LEN, ENC_LITTLE_ENDIAN);
    offset += PROTO_MEMORY_WRITE_ADDRESS_LEN;

    {&amp;hf_proto_memory_write_address,
        {&quot;Memory Write Address&quot;, &quot;proto.memory_write_address&quot;, FT_UINT64, BASE_DEC, NULL, 0,
            NULL, HFILL }</code></pre><p>In the development version the memory write address displays with no errors. In the release version (copied generated .dll to plugins folder) the error is "Trying to fetch a signed integer with length 8." I have a similar issue in a nearly identical field - 8 bytes - with the same errors. I tried switching to FT_UINT32 and the results switched. No error in the release version but the dev version obviously said that the FT_UINT was wrong.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '17, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/134bbb4fd9687f9718bb94d36c4b75fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brownfox&#39;s gravatar image" /><p><span>brownfox</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brownfox has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Apr '17, 06:14</strong> </span></p></div></div><div id="comments-container-60944" class="comments-container"></div><div id="comment-tools-60944" class="comment-tools"></div><div class="clear"></div><div id="comment-60944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60945"></span>

<div id="answer-container-60945" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60945-score" class="post-score" title="current number of votes">0</div><span id="post-60945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="brownfox has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark APIs are not guaranteed to (and are often never) backward compatible between major releases. So you cannot compile your plugin with Wireshark 2.3.0 source code and expect it to work with 2.2.5 without recompilation. If you want your plugin to be compatible with various major versions (here 2.2.X vs 2.3.0), you have to compile the library twice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '17, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-60945" class="comments-container"><span id="60946"></span><div id="comment-60946" class="comment"><div id="post-60946-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that makes sense. I'll switch my development source code.</p></div><div id="comment-60946-info" class="comment-info"><span class="comment-age">(21 Apr '17, 07:25)</span> <span class="comment-user userinfo">brownfox</span></div></div></div><div id="comment-tools-60945" class="comment-tools"></div><div class="clear"></div><div id="comment-60945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

