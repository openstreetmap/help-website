+++
type = "question"
title = "Couldn&#x27;t load module/undefined symbol"
description = '''I&#x27;m currently making a plugin based on the rmt-norm dissector by following the instructions in the README.plugins and I have been able to successfully build the plugin but when I go to start wireshark I get the following message:  &quot;Couldn&#x27;t load module /products/wireshark/plugins/1.8.6/newnorm.so: p...'''
date = "2013-08-21T09:09:00Z"
lastmod = "2013-09-11T12:09:00Z"
weight = 23914
keywords = [ "1.8.6", "norm", "undefined", "module", "linux" ]
aliases = [ "/questions/23914" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Couldn't load module/undefined symbol](/questions/23914/couldnt-load-moduleundefined-symbol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23914-score" class="post-score" title="current number of votes">0</div><span id="post-23914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm currently making a plugin based on the rmt-norm dissector by following the instructions in the README.plugins and I have been able to successfully build the plugin but when I go to start wireshark I get the following message:</p><p>"Couldn't load module /products/wireshark/plugins/1.8.6/newnorm.so: products/wireshark-1.8.6/lib/wireshark/plugins/1.8.6/newnorm.so: undefined symbol: newnorm_ext_parse".<br />
</p><p>I'm using the code found in epan/dissectors/packet-rmt-norm.c and its subsequent header files but I haven't changed anything except for the naming (i.e. rmt_norm to new_norm)<br />
</p><p>I've tried putting newnorm_ext_parse in the epan/libwireshark.def file as suggested in previous post but it still tells me that its an undefined symbol.<br />
</p><p>I am fairly new to Linux so any suggestions would be much appreciated.</p><p>I'm using wireshark 1.8.6 and a SUSE Linux OS.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-1.8.6" rel="tag" title="see questions tagged &#39;1.8.6&#39;">1.8.6</span> <span class="post-tag tag-link-norm" rel="tag" title="see questions tagged &#39;norm&#39;">norm</span> <span class="post-tag tag-link-undefined" rel="tag" title="see questions tagged &#39;undefined&#39;">undefined</span> <span class="post-tag tag-link-module" rel="tag" title="see questions tagged &#39;module&#39;">module</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/64a2be75a7a31bf1ba580e40acc8dab3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Torbett&#39;s gravatar image" /><p><span>Torbett</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Torbett has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-23914" class="comments-container"></div><div id="comment-tools-23914" class="comment-tools"></div><div class="clear"></div><div id="comment-23914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="24351"></span>

<div id="answer-container-24351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24351-score" class="post-score" title="current number of votes">1</div><span id="post-24351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're trying to access a symbol in libwireshark from a plugin then you'll need to add that symbol to the list of symbols exported by the library. You can do that by adding it to the <code>epan/libwireshark.def</code> file.</p><p>(That file exists and is used in Wireshark 1.8 but the method of selecting which symbols are exported changed in 1.10 and later.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '13, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></p></div></div><div id="comments-container-24351" class="comments-container"><span id="24352"></span><div id="comment-24352" class="comment"><div id="post-24352-score" class="comment-score"></div><div class="comment-text"><p>For the record: On March 1, 2013 in trunk SVN #47992, a change was made so that symbols which are to be exported should be declared using WS_DLL_PUBLIC. (libwireshark.def is no longer used).</p><p>For example (from epan/column.h)</p><pre><code>...
#include &quot;ws_symbol_export.h&quot;
...
WS_DLL_PUBLIC
const gchar         *col_format_to_string(const gint);
...</code></pre></div><div id="comment-24352-info" class="comment-info"><span class="comment-age">(04 Sep '13, 09:25)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-24351" class="comment-tools"></div><div class="clear"></div><div id="comment-24351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23925"></span>

<div id="answer-container-23925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23925-score" class="post-score" title="current number of votes">0</div><span id="post-23925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>Couldn't load module /products/wireshark/plugins/1.8.6/newnorm.so: products/wireshark-1.8.6/lib/wireshark/plugins/1.8.6/newnorm.so: undefined symbol: newnorm_ext_parse</code></p><p>I'm using the code found in epan/dissectors/packet-rmt-norm.c and its subsequent header files but I haven't changed anything except for the naming (i.e. rmt_norm to new_norm)</p></blockquote><p>Did you rename <code>rmt_norm</code> to <code>new_norm</code> or did you rename <code>rmt_norm</code> to <code>newnorm</code>? If you renamed <code>rmt_norm</code> to <code>new_norm</code>, it sounds as if you made a mistake in one place and either renamed <code>rmt_norm</code> to <code>newnorm</code> or, in new code, used <code>newnorm</code> rather than <code>new_norm</code>.</p><p>If so, then fix the places where you used <code>newnorm</code> to use <code>new_norm</code> instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23925" class="comments-container"><span id="23930"></span><div id="comment-23930" class="comment"><div id="post-23930-score" class="comment-score"></div><div class="comment-text"><p>Thanks for you reply. I don't think that is the problem. I went through all the naming to check and I don't believe that's the case. Any other suggestions?</p></div><div id="comment-23930-info" class="comment-info"><span class="comment-age">(21 Aug '13, 13:55)</span> <span class="comment-user userinfo">Torbett</span></div></div><span id="23933"></span><div id="comment-23933" class="comment"><div id="post-23933-score" class="comment-score"></div><div class="comment-text"><p>Make sure that the routine named <code>newnorm_ext_parse</code> (not <code>new_norm_ext_parse</code>) actually exists in your code and, if it doesn't, either make it exist (note: there is no <code>rmt_norm_ext_parse</code> routine in the Wireshark source; in particular, it's not in <code>epan/dissectors/packet-rmt-norm.c</code>) or stop calling it (for example, try calling <code>new_norm_ext_parse</code> instead, if <em>that</em> routine exists).</p></div><div id="comment-23933-info" class="comment-info"><span class="comment-age">(21 Aug '13, 14:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-23925" class="comment-tools"></div><div class="clear"></div><div id="comment-23925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24588"></span>

<div id="answer-container-24588" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24588-score" class="post-score" title="current number of votes">0</div><span id="post-24588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you both for your advice. I ended up abandoning the plugin route and instead I grep-ed for packet-rmt-norm and put my rendition of the protocol wherever the original was located and now it works just fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '13, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/64a2be75a7a31bf1ba580e40acc8dab3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Torbett&#39;s gravatar image" /><p><span>Torbett</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Torbett has no accepted answers">0%</span></p></div></div><div id="comments-container-24588" class="comments-container"></div><div id="comment-tools-24588" class="comment-tools"></div><div class="clear"></div><div id="comment-24588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

