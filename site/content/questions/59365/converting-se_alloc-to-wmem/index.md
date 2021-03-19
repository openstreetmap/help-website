+++
type = "question"
title = "Converting se_alloc() to wmem"
description = '''In my old plugin code(1.6), the following lines of codes has been used inside proto_register_myPlugin Routine to initialize Array to Zero. I know that se_alloc is invalid now and wmem_alloc should be used. I have tried different ways. It just isn&#x27;t working. Could someone please help me? Thanks msc_t...'''
date = "2017-02-13T04:43:00Z"
lastmod = "2017-02-13T07:43:00Z"
weight = 59365
keywords = [ "dissector", "wmem", "updateplugin", "custom" ]
aliases = [ "/questions/59365" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Converting se\_alloc() to wmem](/questions/59365/converting-se_alloc-to-wmem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59365-score" class="post-score" title="current number of votes">0</div><span id="post-59365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my old plugin code(1.6), the following lines of codes has been used inside proto_register_myPlugin Routine to initialize Array to Zero. I know that se_alloc is invalid now and wmem_alloc should be used. I have tried different ways. It just isn't working. Could someone please help me? Thanks</p><pre><code>msc_to_cmd_database = (void*) se_alloc(255 * (sizeof(proto_tree) + 1));
memset(msc_to_cmd_database, 0, 255 * (sizeof(proto_tree) + 1));

(in .h file _&gt;)
 static struct msc_to_cmd_relation_struct {
    guint8 ife_command;
 }*msc_to_cmd_database;</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wmem" rel="tag" title="see questions tagged &#39;wmem&#39;">wmem</span> <span class="post-tag tag-link-updateplugin" rel="tag" title="see questions tagged &#39;updateplugin&#39;">updateplugin</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '17, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p><span>xaheen</span><br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Feb '17, 09:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-59365" class="comments-container"><span id="59370"></span><div id="comment-59370" class="comment"><div id="post-59370-score" class="comment-score"></div><div class="comment-text"><p>Could you please clarify what is not working exactly? Are you triggering an assert because you are not using the right memory scope?</p></div><div id="comment-59370-info" class="comment-info"><span class="comment-age">(13 Feb '17, 06:35)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="59371"></span><div id="comment-59371" class="comment"><div id="post-59371-score" class="comment-score"></div><div class="comment-text"><p><span>@Pascal Quantin</span> I am upgrading the dissector for wireshark 2.2 I am supposed to use wmem, which I have used but it is not compiling and not even showing any error. What could be the wmem_alloc Version for the above code. Thanks for your Response</p></div><div id="comment-59371-info" class="comment-info"><span class="comment-age">(13 Feb '17, 06:43)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-59365" class="comment-tools"></div><div class="clear"></div><div id="comment-59365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59372"></span>

<div id="answer-container-59372" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59372-score" class="post-score" title="current number of votes">1</div><span id="post-59372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xaheen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Give a try to:</p><pre><code>msc_to_cmd_database = (struct msc_to_cmd_relation_struct*) wmem_alloc0(wmem_epan_scope(), 255 * (sizeof(proto_tree) + 1));</code></pre><p>But was this memory freed somewhere else in the code?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '17, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-59372" class="comments-container"><span id="59373"></span><div id="comment-59373" class="comment"><div id="post-59373-score" class="comment-score"></div><div class="comment-text"><p><span>@Pascal Quantin</span> wow! it worked! thanks. No, I havent freed the Memory. how do I do it?</p></div><div id="comment-59373-info" class="comment-info"><span class="comment-age">(13 Feb '17, 07:23)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="59374"></span><div id="comment-59374" class="comment"><div id="post-59374-score" class="comment-score"></div><div class="comment-text"><p>If it is not required to free the memory in your plugin, why allocate it dynamically and not define the array once for all?</p></div><div id="comment-59374-info" class="comment-info"><span class="comment-age">(13 Feb '17, 07:43)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-59372" class="comment-tools"></div><div class="clear"></div><div id="comment-59372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

