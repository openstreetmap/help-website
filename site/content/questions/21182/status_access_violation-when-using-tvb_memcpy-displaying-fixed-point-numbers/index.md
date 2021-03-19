+++
type = "question"
title = "STATUS_ACCESS_VIOLATION when using tvb_memcpy / Displaying Fixed Point Numbers"
description = '''I have an issue where the information I&#x27;m trying to display a fixed point number from the message. However, the way the message is sent is that the value is basically a short int (signed 16 bit int) multiplied by 10^-2. Since there are no accessors to pull a 16 bit signed int from the buffer I used ...'''
date = "2013-05-16T06:15:00Z"
lastmod = "2013-05-16T10:46:00Z"
weight = 21182
keywords = [ "tvb_memcpy", "fixedpoint" ]
aliases = [ "/questions/21182" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [STATUS\_ACCESS\_VIOLATION when using tvb\_memcpy / Displaying Fixed Point Numbers](/questions/21182/status_access_violation-when-using-tvb_memcpy-displaying-fixed-point-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21182-score" class="post-score" title="current number of votes">0</div><span id="post-21182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an issue where the information I'm trying to display a fixed point number from the message. However, the way the message is sent is that the value is basically a short int (signed 16 bit int) multiplied by 10^-2. Since there are no accessors to pull a 16 bit signed int from the buffer I used tvb_memcpy to place the bits into a gint16 variable. Then I cast that as a gfloat and multiply by 0.01. Whenever I do this, I see an error in the tree at this section that says</p><p>"[Dissector bug, protocol MY_PROTOCOL: STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address".</p><p>Am I missing something curcial, or is there a better way to do this? Any suggestions would be greatly appreciated. Here is the code for this part:</p><pre><code>    // declared at the beginning of the dissect function
    gint16 *val_short = 0;
    gfloat val_float = 0;     
    .
    .
    .
    //within the switch that handles message type
    case 10:
       tvb_memcpy(tvb, (guint8*)&amp;val_short, offset, 2);
       val_float = ((gfloat)(*val_short)) * (gfloat)0.01;
       proto_tree_add_float(my_protocol_tree, hf_my_protocol_x_value, tvb, offset, 2, val_float);</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tvb_memcpy" rel="tag" title="see questions tagged &#39;tvb_memcpy&#39;">tvb_memcpy</span> <span class="post-tag tag-link-fixedpoint" rel="tag" title="see questions tagged &#39;fixedpoint&#39;">fixedpoint</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '13, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/cd2062d7ed21eb7908017d9011ec4c3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gaax&#39;s gravatar image" /><p><span>Gaax</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gaax has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 May '13, 06:16</strong> </span></p></div></div><div id="comments-container-21182" class="comments-container"></div><div id="comment-tools-21182" class="comment-tools"></div><div class="clear"></div><div id="comment-21182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21184"></span>

<div id="answer-container-21184" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21184-score" class="post-score" title="current number of votes">1</div><span id="post-21184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gaax has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The invalid memory access is because you didn't allocate any memory for val_short. You have a pointer pointing to NULL and you're trying to copy into it.</p><p>But: why not use tvb_get_ntohs() or tvb_get_letohs() (depending on the endianism of the 16 bits)? Sure they returned an unsigned value but if you store the result in a signed variable, well, it'll be treated as signed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '13, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-21184" class="comments-container"><span id="21188"></span><div id="comment-21188" class="comment"><div id="post-21188-score" class="comment-score"></div><div class="comment-text"><p>Ok, I kind of feel stupid but hey, I'm learning lol.</p><p>I tried doing it using tvb_get_ntohs() and it worked perfectly! I just had to cast the return value as a gint16 (simply storing it into a gint16 wasn't enough apparantly).</p><p>Before this, I also tried allocating the memory space for that pointer and doing it the way I had originally planned but it just returned zero every time. For the sake of learning, if you (or anyone) could tell me how to do it properly using the pointer, I'd be truly grateful.</p></div><div id="comment-21188-info" class="comment-info"><span class="comment-age">(16 May '13, 10:26)</span> <span class="comment-user userinfo">Gaax</span></div></div><span id="21189"></span><div id="comment-21189" class="comment"><div id="post-21189-score" class="comment-score"></div><div class="comment-text"><p>No worries, we are all (hopefully) learning all the time. :-)</p><p>Something like this would probably be a good way to do it (no need for a pointer):</p><pre><code>gint16 val_short;
[...]
tvb_memcpy(tvb, (guint8*)&amp;val_short, offset, 2);</code></pre><p>If you really want to use a pointer then:</p><pre><code>gint16 *val_short;
val_short = g_malloc(sizeof(gint16));
[...]
tvb_memcpy(tvb, (guint8*)val_short, offset, 2); &lt;&lt; note the lack of &quot;&amp;&quot; since val_short is already a pointer</code></pre></div><div id="comment-21189-info" class="comment-info"><span class="comment-age">(16 May '13, 10:39)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="21190"></span><div id="comment-21190" class="comment"><div id="post-21190-score" class="comment-score"></div><div class="comment-text"><p>Aha, ok I get it now. Thanks!</p></div><div id="comment-21190-info" class="comment-info"><span class="comment-age">(16 May '13, 10:46)</span> <span class="comment-user userinfo">Gaax</span></div></div></div><div id="comment-tools-21184" class="comment-tools"></div><div class="clear"></div><div id="comment-21184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

