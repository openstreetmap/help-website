+++
type = "question"
title = "WS version 1.02 patched make: *** [all] Error 2"
description = '''Hey im trying to install a version of ws with a patched applied already, but when i get to the MAKE command i get the error below. I am running Ubuntu 11.10 and i believe all have all the dependencies installed. Is there a way to check for the dependencies that are needed? Any help would be great. A...'''
date = "2012-09-06T04:15:00Z"
lastmod = "2012-09-06T07:09:00Z"
weight = 14081
keywords = [ "make", "1.0.2", "error" ]
aliases = [ "/questions/14081" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WS version 1.02 patched make: \*\*\* \[all\] Error 2](/questions/14081/ws-version-102-patched-make-all-error-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14081-score" class="post-score" title="current number of votes">0</div><span id="post-14081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey im trying to install a version of ws with a patched applied already, but when i get to the MAKE command i get the error below. I am running Ubuntu 11.10 and i believe all have all the dependencies installed. Is there a way to check for the dependencies that are needed? Any help would be great. And the patch is for P25 radio from the op25-dev yahoo group. I do have a current version installed and running. Is that the problem?</p><pre><code>read  -L/usr/local/lib wiretap/.libs/libwiretap.so /usr/lib/i386-linux-gnu/libgmodule-2.0.so -lrt /usr/lib/i386-linux-gnu/libglib-2.0.so -lm -lpcap -lz -pthread
wiretap/.libs/libwiretap.so: undefined reference to `g_direct_hash&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_list_append&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_malloc&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_free&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_hash_table_remove&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_str_equal&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_hash_table_lookup&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_assertion_message_expr&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_array_new&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_strup&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_hash_table_new&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_array_prepend_vals&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_direct_equal&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_ptr_array_add&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_strdup_printf&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_ptr_array_new&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_array_append_vals&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_hash_table_insert&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_log&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_hash_table_destroy&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_list_free&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_str_hash&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_strdown&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_realloc&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_memdup&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_malloc0&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_strdup&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_snprintf&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_ptr_array_free&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_assertion_message&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_hash_table_foreach_remove&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_hash_table_foreach&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_strndup&#39;
wiretap/.libs/libwiretap.so: undefined reference to `g_list_foreach&#39;
collect2: ld returned 1 exit status
make[2]: *** [randpkt] Error 1
make[2]: Leaving directory `/home/allan/wireshark/1.0.2-patched&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/allan/wireshark/1.0.2-patched&#39;
make: *** [all] Error 2
[email protected]:~/wireshark/1.0.2-patched$</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-1.0.2" rel="tag" title="see questions tagged &#39;1.0.2&#39;">1.0.2</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '12, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/797ce906ac269681f7467e9cd73ed060?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajs007&#39;s gravatar image" /><p><span>ajs007</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajs007 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '12, 04:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-14081" class="comments-container"><span id="14083"></span><div id="comment-14083" class="comment"><div id="post-14083-score" class="comment-score"></div><div class="comment-text"><p>1.02 is very old and unsupported, and as you haven't provided the patch it's somewhat hard for others to test.</p><p>Could you try a supported version of Wireshark?</p></div><div id="comment-14083-info" class="comment-info"><span class="comment-age">(06 Sep '12, 04:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="14084"></span><div id="comment-14084" class="comment"><div id="post-14084-score" class="comment-score"></div><div class="comment-text"><p>I understand what you're saying about it being an old version. I have tried unsuccessfully to patch a supported version with no success. I tried to follow the instructions on <a href="http://op25.osmocom.org/I/wiki/WireSharkPage">http://op25.osmocom.org/I/wiki/WireSharkPage</a></p><p>The latest patch available is for 1.6.5 at <a href="http://op25.osmocom.org/wiki/browser/trunk/wireshark/patches/wireshark-1.6.5.patch">http://op25.osmocom.org/wiki/browser/trunk/wireshark/patches/wireshark-1.6.5.patch</a></p></div><div id="comment-14084-info" class="comment-info"><span class="comment-age">(06 Sep '12, 04:38)</span> <span class="comment-user userinfo">ajs007</span></div></div><span id="14085"></span><div id="comment-14085" class="comment"><div id="post-14085-score" class="comment-score"></div><div class="comment-text"><p>I would think you'll have more luck with the 1.6.5 patch using a supported version of Wireshark, even if the current version is 1.6.10.</p><p>First check you can build the plain 1.6.5 version of Wireshark, then apply the patch and try to build again as per the osmocon instructions.</p><p>If that fails then you can post the results here, but you're more likely to get support on the osmocon forums as it's their patch.</p></div><div id="comment-14085-info" class="comment-info"><span class="comment-age">(06 Sep '12, 04:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="14086"></span><div id="comment-14086" class="comment"><div id="post-14086-score" class="comment-score"></div><div class="comment-text"><p>Ok the thanks for that. I have tried the osmocom forums with no answer. haha a real noob question but on the instructions page i dont understand the line (cd wireshark &amp;&amp; patch -p1 &lt; ../patches/wireshark-1.6.5.patch)</p></div><div id="comment-14086-info" class="comment-info"><span class="comment-age">(06 Sep '12, 04:57)</span> <span class="comment-user userinfo">ajs007</span></div></div><span id="14087"></span><div id="comment-14087" class="comment"><div id="post-14087-score" class="comment-score"></div><div class="comment-text"><p>It's 2 commands joined into one; <code>cd wireshark</code> means to change into the wireshark sources directory and <code>patch -p1 &lt; ../patches/wireshark-1.6.5.path</code> means that the patch in the file specified is to be applied to the current directory.</p><p>If your wireshark source directory, and\or the path to your patch file from that directory are different, then you'll have to adjust the command(s) accordingly. You can separate out the commands into two separate entries if you wish, just lose the <code>&amp;&amp;</code> that joins them, e.g.</p><p><code>Prompt&gt;cd path/to/wireshark_sources Prompt&gt;patch -p1 &lt; path/to/patchfile</code></p></div><div id="comment-14087-info" class="comment-info"><span class="comment-age">(06 Sep '12, 05:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="14089"></span><div id="comment-14089" class="comment not_top_scorer"><div id="post-14089-score" class="comment-score"></div><div class="comment-text"><p>ok i shall try that soon. Will a new version interfere with the old one as i have 1.8.2 installed now. How do i un-install that?</p></div><div id="comment-14089-info" class="comment-info"><span class="comment-age">(06 Sep '12, 05:49)</span> <span class="comment-user userinfo">ajs007</span></div></div><span id="14091"></span><div id="comment-14091" class="comment not_top_scorer"><div id="post-14091-score" class="comment-score"></div><div class="comment-text"><p>I wouldn't install it just now. Run it from the directory you've built it in. I've never "installed" it on Ubuntu so I can't answer that question but presumably you can use the same method you used to install it.</p><p>You can get conflicts between contents of config files and plugin directories between versions.</p></div><div id="comment-14091-info" class="comment-info"><span class="comment-age">(06 Sep '12, 07:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-14081" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-14081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

