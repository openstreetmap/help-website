+++
type = "question"
title = "Wireshark crashes when using g_free()"
description = '''I&#x27;m working on developing a Wireshark dissector that includes a UAT. I&#x27;m getting an error that I&#x27;m not sure how to fix or even look for information that helps with fixing it. When I run Wireshark, it starts normally. However, when I open a dump file that uses my own dissector it crashes reporting a ...'''
date = "2015-01-02T16:36:00Z"
lastmod = "2015-01-13T18:20:00Z"
weight = 38858
keywords = [ "core", "crash", "dump", "wireshark" ]
aliases = [ "/questions/38858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes when using g\_free()](/questions/38858/wireshark-crashes-when-using-g_free)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38858-score" class="post-score" title="current number of votes">0</div><span id="post-38858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on developing a Wireshark dissector that includes a UAT. I'm getting an error that I'm not sure how to fix or even look for information that helps with fixing it. When I run Wireshark, it starts normally. However, when I open a dump file that uses my own dissector it crashes reporting a long message in the terminal ended with the following:</p><pre><code>7fc2e49ac000-7fc2e49c7000 r-xp 00000000 08:01 2491310                    /home/flora/wireshark_with_my_dissector/wsutil/.libs/libwsutil.so.4.0.0
7fc2e49c7000-7fc2e4bc6000 ---p 0001b000 08:01 2491310                    /home/flora/wireshark_with_my_dissector/wsutil/.libs/libwsutil.so.4.0.0
7fc2e4bc6000-7fc2e4bc7000 r--p 0001a000 08:01 2491310                    /home/flora/wireshark_with_my_dissector/wsutil/.libs/libwsutil.so.4.0.0Aborted (core dumped)</code></pre><p>By using printif statements, I found that Wireshark seems to be crashing at a function called <strong><code>g_free()</code></strong>. This function is called by <code>my_dissector_key_free()</code> which is called in function: <code>**</code>g_hash_table_foreach(my_dissector_key_hash, my_dissector_key_free, NULL);<code>**</code> when parsing the uat I've created to be used with my dissector.</p><p>Any idea what this error could be about? what is wsutil? what does any line of the output (for example the following line) could mean</p><pre><code>/home/flora/wireshark_with_my_dissector/wsutil/.libs/libwsutil.so.4.0.0
7fc2e4bc6000-7fc2e4bc7000 r--p 0001a000 08:01 2491310</code></pre><p>In case it matters, I'm developing in Linux (Ubuntu).</p><p>Thank you. flora.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-core" rel="tag" title="see questions tagged &#39;core&#39;">core</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '15, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '15, 19:11</strong> </span></p></div></div><div id="comments-container-38858" class="comments-container"><span id="38861"></span><div id="comment-38861" class="comment"><div id="post-38861-score" class="comment-score"></div><div class="comment-text"><p>How did you allocate the memory been freed with g_free()? Is it using g_malloc or another function?</p></div><div id="comment-38861-info" class="comment-info"><span class="comment-age">(02 Jan '15, 23:58)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="38862"></span><div id="comment-38862" class="comment"><div id="post-38862-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your comments Pascal. It is a hash table that I declared as static GHashTable *my_dissector_key_hash = NULL;</p><p>and then I wanted to free it by using g_free() before creating a hash by using my_dissector_key_hash = g_hash_table_new() which is described in this link <a href="https://developer.gnome.org/glib/stable/glib-Hash-Tables.html#g-hash-table-new">https://developer.gnome.org/glib/stable/glib-Hash-Tables.html#g-hash-table-new</a></p></div><div id="comment-38862-info" class="comment-info"><span class="comment-age">(03 Jan '15, 00:45)</span> <span class="comment-user userinfo">flora</span></div></div><span id="38863"></span><div id="comment-38863" class="comment"><div id="post-38863-score" class="comment-score"></div><div class="comment-text"><p>No this g_free call is presumably for the elements of the hash table, and not the hash table itself (as you are using g_hash_table_foreach). So how are you allocating the elements put in the hash table (through the g_hash_table_insert function call)?</p></div><div id="comment-38863-info" class="comment-info"><span class="comment-age">(03 Jan '15, 02:01)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="38868"></span><div id="comment-38868" class="comment"><div id="post-38868-score" class="comment-score"></div><div class="comment-text"><p>Oh sorry I misunderstood it. I'm using g_malloc() for the allocation.</p></div><div id="comment-38868-info" class="comment-info"><span class="comment-age">(03 Jan '15, 18:02)</span> <span class="comment-user userinfo">flora</span></div></div><span id="38871"></span><div id="comment-38871" class="comment"><div id="post-38871-score" class="comment-score">1</div><div class="comment-text"><p>OK then g_free should work. If you get a crash, it means that you are corrupting your hash table; or trying to free a parameter that was not dynamically allocated (could be either the key itself or associated value, but according to what you shared earlier it seems to be the key). You should carefully reread your code and use a debugger to step in (instead of using printf).</p></div><div id="comment-38871-info" class="comment-info"><span class="comment-age">(04 Jan '15, 01:35)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="39104"></span><div id="comment-39104" class="comment not_top_scorer"><div id="post-39104-score" class="comment-score"></div><div class="comment-text"><p>works perfect thanks.</p></div><div id="comment-39104-info" class="comment-info"><span class="comment-age">(13 Jan '15, 18:18)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-38858" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-38858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39105"></span>

<div id="answer-container-39105" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39105-score" class="post-score" title="current number of votes">0</div><span id="post-39105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Pascal's last comments helped me to understand the problem and to solve it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '15, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-39105" class="comments-container"></div><div id="comment-tools-39105" class="comment-tools"></div><div class="clear"></div><div id="comment-39105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

