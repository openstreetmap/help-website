+++
type = "question"
title = "Disable protocol dissection in tshark?"
description = '''Is there a hidden parameter I can use with tshark to disable the dissection of some protocol? Sure, I can edit the disabled protocols file, but I&#x27;m wondering if there&#x27;s a more &quot;dynamic&quot; way to disable a protocol. Thanks!'''
date = "2011-08-09T22:45:00Z"
lastmod = "2011-08-10T09:13:00Z"
weight = 5613
keywords = [ "disable", "tshark" ]
aliases = [ "/questions/5613" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Disable protocol dissection in tshark?](/questions/5613/disable-protocol-dissection-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5613-score" class="post-score" title="current number of votes">0</div><span id="post-5613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a hidden parameter I can use with tshark to disable the dissection of some protocol? Sure, I can edit the disabled protocols file, but I'm wondering if there's a more "dynamic" way to disable a protocol.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/9b7b5e633f7836289c2fc6c3934bffaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r0u1i&#39;s gravatar image" /><p><span>r0u1i</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r0u1i has no accepted answers">0%</span></p></div></div><div id="comments-container-5613" class="comments-container"></div><div id="comment-tools-5613" class="comment-tools"></div><div class="clear"></div><div id="comment-5613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5624"></span>

<div id="answer-container-5624" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5624-score" class="post-score" title="current number of votes">0</div><span id="post-5624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="r0u1i has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's no tshark "hidden parameter" to disable dissection of a protocol.</p><p>tshark does have an option to only show packet details for a list of specified protocols but this is quite different than enabling a set of protocols. (That is: dissection takes place as per the enabled/disabled list, but the details for just the specified protocols (and those riding on same) are printed).</p><pre><code>-O &lt;protocols&gt;           Only show packet details of these protocols, comma
                           separated</code></pre><p>If I had a need to do this dynamically w/o making changes to tshark, I suspect I'd end up doing some scripting to create a disabled protocols file on-the-fly (and storing it in the right place) before invoking tshark.</p><p>If you think an option to specify a list of disabled protocols (or maybe a list of enabled protocols) might be a generally useful feature to include in tshark, feel free to provide a patch (or request an enhancement) at bugs.wireshark.org. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '11, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Aug '11, 09:05</strong> </span></p></div></div><div id="comments-container-5624" class="comments-container"><span id="5625"></span><div id="comment-5625" class="comment"><div id="post-5625-score" class="comment-score"></div><div class="comment-text"><p>Please note that the -O option only has effect on which protocols get expanded in the -V output.</p></div><div id="comment-5625-info" class="comment-info"><span class="comment-age">(10 Aug '11, 09:13)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5624" class="comment-tools"></div><div class="clear"></div><div id="comment-5624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

