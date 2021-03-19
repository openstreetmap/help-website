+++
type = "question"
title = "add_dissector problem"
description = '''Hello, I installed openflow plugin in wireshark, I followed some commands and packet_openflow.so was genereted and I copied it in wiresharklib folder, but I have an error:undefined symbol:dissector_add I try to modify packet_openflow.c by adding  #define NO_STRINGS NULL and  ***_add_uint() But I hav...'''
date = "2016-06-10T17:09:00Z"
lastmod = "2016-06-10T19:39:00Z"
weight = 53353
keywords = [ "openflow" ]
aliases = [ "/questions/53353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [add\_dissector problem](/questions/53353/add_dissector-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53353-score" class="post-score" title="current number of votes">0</div><span id="post-53353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I installed openflow plugin in wireshark, I followed some commands and packet_openflow.so was genereted and I copied it in wiresharklib folder, but I have an error:undefined symbol:dissector_add I try to modify packet_openflow.c by adding</p><pre><code>#define NO_STRINGS NULL</code></pre>and<pre><code>***_add_uint()</code></pre>But I haven't any results! Please , can you help me?</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-openflow" rel="tag" title="see questions tagged &#39;openflow&#39;">openflow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '16, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/36eaeee981d38eff5881890e7bdc560d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dija%20Ais-%C5%82&#39;s gravatar image" /><p><span>Dija Ais-ł</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dija Ais-ł has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '16, 00:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-53353" class="comments-container"><span id="53354"></span><div id="comment-53354" class="comment"><div id="post-53354-score" class="comment-score"></div><div class="comment-text"><p>Try using a newer version of wireshark which has openflow support built in. Or use the plugin with the version it was created with</p></div><div id="comment-53354-info" class="comment-info"><span class="comment-age">(10 Jun '16, 19:39)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-53353" class="comment-tools"></div><div class="clear"></div><div id="comment-53353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

