+++
type = "question"
title = "How to retrieve Wireshark version during compilation"
description = '''Hi all, Anybody knows, how to get Wireshark version during compilation ? I am writing a dissector plugin, and I would like to be able to build this plugin under different version of Wireshark. The interface functions prototypes can differ in different version of Wireshark, so I would like to check i...'''
date = "2016-02-01T05:01:00Z"
lastmod = "2016-02-01T10:14:00Z"
weight = 49681
keywords = [ "dissector", "version", "plugin" ]
aliases = [ "/questions/49681" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to retrieve Wireshark version during compilation](/questions/49681/how-to-retrieve-wireshark-version-during-compilation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49681-score" class="post-score" title="current number of votes">0</div><span id="post-49681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Anybody knows, how to get Wireshark version during compilation ? I am writing a dissector plugin, and I would like to be able to build this plugin under different version of Wireshark. The interface functions prototypes can differ in different version of Wireshark, so I would like to check it during build, something like this:</p><pre><code>#if CURRENT_WIRESHARK_VERSION &gt;= VERSION(10,1,0)
...
#else
...
#endif</code></pre><p>Is it possible to get a version somehow?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '16, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/64c95b4ac4440bfb19c73c1431a0f33e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gralex&#39;s gravatar image" /><p><span>gralex</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gralex has no accepted answers">0%</span></p></div></div><div id="comments-container-49681" class="comments-container"></div><div id="comment-tools-49681" class="comment-tools"></div><div class="clear"></div><div id="comment-49681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49693"></span>

<div id="answer-container-49693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49693-score" class="post-score" title="current number of votes">2</div><span id="post-49693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should use the following preprocessor variables: VERSION_MAJOR, VERSION_MINOR, VERSION_MICRO</p><p>For example in my own plugins I use this kind of code:</p><pre><code>#if (VERSION_MAJOR &gt; 2) || ((VERSION_MAJOR == 2) &amp;&amp; (VERSION_MINOR &gt;= 1))
    sqnmbim_handle = create_dissector_handle(dissect_foo, proto_foo);
#else
    sqnmbim_handle = new_create_dissector_handle(dissect_foo, proto_foo);
#endif</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '16, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-49693" class="comments-container"><span id="49695"></span><div id="comment-49695" class="comment"><div id="post-49695-score" class="comment-score"></div><div class="comment-text"><p>Oops, <span>@Pascal Quantin</span> is correct, I forgot about the definitions in config.h, instead I looked for them on the compiler command line.</p></div><div id="comment-49695-info" class="comment-info"><span class="comment-age">(01 Feb '16, 10:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-49693" class="comment-tools"></div><div class="clear"></div><div id="comment-49693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49687"></span>

<div id="answer-container-49687" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49687-score" class="post-score" title="current number of votes">0</div><span id="post-49687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><del>Unfortunately for you there's no pre-processor definition of the build version. I guess one could be generated by the build systems, CMake and autotools. I suggest you file an enhancement request for this on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</del></p><p><strong>Edit:</strong> Ignore, the answer from <span><span>@Pascal Quantin</span></span> is the correct answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '16, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Feb '16, 14:59</strong> </span></p></div></div><div id="comments-container-49687" class="comments-container"></div><div id="comment-tools-49687" class="comment-tools"></div><div class="clear"></div><div id="comment-49687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

