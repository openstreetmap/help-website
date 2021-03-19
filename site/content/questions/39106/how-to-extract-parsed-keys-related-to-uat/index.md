+++
type = "question"
title = "How to extract parsed keys related to  UAT?"
description = '''I need to work with a hash table keys of type struct (something similar to the defined struct below). These keys are related to number of parsed values from a UAT in my protocol dissector. I used g_hash_table_get_keys_as_array () but I&#x27;m getting several errors and warnings : warning: old-style funct...'''
date = "2015-01-13T18:50:00Z"
lastmod = "2015-01-13T23:13:00Z"
weight = 39106
keywords = [ "glib", "hash_table", "uats", "wireshark" ]
aliases = [ "/questions/39106" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to extract parsed keys related to UAT?](/questions/39106/how-to-extract-parsed-keys-related-to-uat)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39106-score" class="post-score" title="current number of votes">0</div><span id="post-39106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to work with a hash table keys of type struct (something similar to the defined struct below). These keys are related to number of parsed values from a UAT in my protocol dissector. I used <a href="https://developer.gnome.org/glib/stable/glib-Hash-Tables.html#g-hash-table-lookup">g_hash_table_get_keys_as_array ()</a> but I'm getting several errors and warnings</p><pre><code>: warning: old-style function definition [-Wold-style-definition]
   : warning: implicit declaration of function &#39;g_hash_table_get_keys_as_array&#39; [-Wimplicit-function-declaration]
   : error: incompatible types when assigning to type &#39;struct key[]&#39; from type &#39;int&#39;
   : warning: variable &#39;keys_array&#39; set but not used [-Wunused-but-set-variable]</code></pre><p>I'm not sure why I'm getting these errors and not sure how to solve them. my guess that I'm not using the function in the proper way but again I'm not sure what I'm missing. I'd appreciate any hints that help me to better understand or solve the problem. my related code looks like the following:</p><pre><code>typedef struct _key {
  guint32 num;
  address address;
  guint id;
} key;

static void 
Working_with_hash_table_keys()
{
    key  keys_array[] = NULL; 
    keys_array=  (*key ) g_hash_table_get_keys_as_array(my_key_hash);

}</code></pre><p>Thank you. Flora</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-hash_table" rel="tag" title="see questions tagged &#39;hash_table&#39;">hash_table</span> <span class="post-tag tag-link-uats" rel="tag" title="see questions tagged &#39;uats&#39;">uats</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '15, 18:50</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jan '15, 18:52</strong> </span></p></div></div><div id="comments-container-39106" class="comments-container"></div><div id="comment-tools-39106" class="comment-tools"></div><div class="clear"></div><div id="comment-39106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39113"></span>

<div id="answer-container-39113" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39113-score" class="post-score" title="current number of votes">1</div><span id="post-39113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>g_hash_table_get_keys_as_array is only available starting from GLib 2.40. Given the warnings you get, I guess you have an older GLib release. So you should look at alternative methods.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '15, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39113" class="comments-container"></div><div id="comment-tools-39113" class="comment-tools"></div><div class="clear"></div><div id="comment-39113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

