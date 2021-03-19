+++
type = "question"
title = "&quot;undefined symbol ssl_print_data&quot; when starting Wireshark"
description = '''I just finished building wireshark from the source with a pluggable dissector by following these steps. When I start wireshark from the command line I get the following message. &quot;Couldn&#x27;t load module /usr/local/lib/wireshark/plugins/1.11.3/PluggableDissectorSourceFilename.so: /usr/local/lib/wireshar...'''
date = "2014-06-16T11:15:00Z"
lastmod = "2014-06-28T11:43:00Z"
weight = 33869
keywords = [ "wireshark", "dissector", "startup", "undefined", "plugin" ]
aliases = [ "/questions/33869" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# ["undefined symbol ssl\_print\_data" when starting Wireshark](/questions/33869/undefined-symbol-ssl_print_data-when-starting-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33869-score" class="post-score" title="current number of votes">0</div><span id="post-33869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just finished building wireshark from the source with a pluggable dissector by following <a href="http://stackoverflow.com/questions/4905846/how-do-i-compile-this-plugin">these steps</a>. When I start wireshark from the command line I get the following message.</p><p>"Couldn't load module /usr/local/lib/wireshark/plugins/1.11.3/PluggableDissectorSourceFilename.so: /usr/local/lib/wireshark/plugins/1.11.3/PluggableDissectorSourceFilename.so: undefined symbol: ssl_print_data"</p><p><strong>ssl_print-data</strong> is a function that is called several times in the pluggable dissector source code PlugableDissector.c. It is defined in <a href="http://www.wireshark.org/docs/wsar_html/epan/packet-ssl-utils_8h_source.html">this header file</a> which I copied it and included it to my wireshark folder without any changes.</p><p>This error message does not prevent wireshark from running. A quiet similar question has been asked previously but I didn't get <a href="http://ask.wireshark.org/questions/23914/couldnt-load-moduleundefined-symbol">how they resolved it</a>. Any suggestions or hints for the possible cause/s for this problem and/or solution/s to get rid off this message?</p><p><strong>Update:</strong> I still have the same error even with 1.10.8 version. When I removed the sentences that use the <strong>ssl_print_data</strong> function from my dissector source code, Wireshark loaded without that error message.However, this is defiantly not a solution that I will go with because I do need to use that specific function. Any suggestions?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-undefined" rel="tag" title="see questions tagged &#39;undefined&#39;">undefined</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '14, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jun '14, 19:55</strong> </span></p></div></div><div id="comments-container-33869" class="comments-container"></div><div id="comment-tools-33869" class="comment-tools"></div><div class="clear"></div><div id="comment-33869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33873"></span>

<div id="answer-container-33873" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33873-score" class="post-score" title="current number of votes">0</div><span id="post-33873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To limit the filling of the namespace with all kinds of function names, most of which are never linked against, only function names which carry a specific prefix get published as external interface for the module. When you want to make use of a function that does not have this prefix you should add it, then the build system will handle the actual publication. The prefix in question is WS_DLL_PUBLIC, so you should add that to the function in packet-ssl-utils.h. Note that this does not make your plugin compatible with released versions of Wireshark, since these do not carry the prefix for this function. Also the 1.11 series (or any odd numbered minor version number) signifies an unmaintained development snapshot, see <a href="http://wiki.wireshark.org/Development/ReleaseNumbers">Release Numbers</a>. We are about to release 1.12, the new maintained branch. You might want to work off of that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '14, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-33873" class="comments-container"><span id="33874"></span><div id="comment-33874" class="comment"><div id="post-33874-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. I did add WS_DLL_PUBLIC to the function as following: WS_DLL_PUBLIC void ssl_print_data(const gchar <em>name, const guchar</em> data, size_t len);</p><p>and then make -C plugins, Wireshark I still get the same message!</p><p>Note: the function in the header file has already extern keywords, so it should be accessible from any other source file so why do I need to include WS_DLL_PUBLIC ?</p></div><div id="comment-33874-info" class="comment-info"><span class="comment-age">(16 Jun '14, 15:31)</span> <span class="comment-user userinfo">flora</span></div></div><span id="33961"></span><div id="comment-33961" class="comment"><div id="post-33961-score" class="comment-score"></div><div class="comment-text"><p>You will have to remake the library exporting the function that is now marked as WS_DLL_PUBLIC as well as your plugin.</p></div><div id="comment-33961-info" class="comment-info"><span class="comment-age">(19 Jun '14, 10:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="34196"></span><div id="comment-34196" class="comment"><div id="post-34196-score" class="comment-score"></div><div class="comment-text"><p>May you explain in more details how can I remark the WS_DLL_PUBLIC and the plugin?</p><p>I'm still having the same issue even after I reinstalled Wireshark 1.10.8</p></div><div id="comment-34196-info" class="comment-info"><span class="comment-age">(25 Jun '14, 16:37)</span> <span class="comment-user userinfo">flora</span></div></div><span id="34209"></span><div id="comment-34209" class="comment"><div id="post-34209-score" class="comment-score"></div><div class="comment-text"><p>The library that now export the function your plugin requires will have to be rebuilt (libwireshark.so??) and that library used in your installation along with your plugin. Reinstalling Wireshark 1.10.8 will simply reuse the original library that doesn't export the function.</p></div><div id="comment-34209-info" class="comment-info"><span class="comment-age">(26 Jun '14, 03:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="34260"></span><div id="comment-34260" class="comment"><div id="post-34260-score" class="comment-score"></div><div class="comment-text"><p>I added the prefix as suggested and rebuild it and it works just fine now. Thank you all for your help and explanations.</p></div><div id="comment-34260-info" class="comment-info"><span class="comment-age">(28 Jun '14, 11:43)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-33873" class="comment-tools"></div><div class="clear"></div><div id="comment-33873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33954"></span>

<div id="answer-container-33954" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33954-score" class="post-score" title="current number of votes">0</div><span id="post-33954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please refer to <a href="http://ask.wireshark.org/questions/25201/undefined-reference-to-tvb_bcd_dig_to_ep_str">this topic</a>, I'm not sure but maybe it could help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '14, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div></div><div id="comments-container-33954" class="comments-container"><span id="34204"></span><div id="comment-34204" class="comment"><div id="post-34204-score" class="comment-score"></div><div class="comment-text"><p>I don't think the undefined wireshark function has to do with what is in here. In deed, I've already updated to the new APIs. Thank you for your suggestion anyway :)</p></div><div id="comment-34204-info" class="comment-info"><span class="comment-age">(25 Jun '14, 19:44)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-33954" class="comment-tools"></div><div class="clear"></div><div id="comment-33954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

