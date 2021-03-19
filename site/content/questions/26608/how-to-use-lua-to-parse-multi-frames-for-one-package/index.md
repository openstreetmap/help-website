+++
type = "question"
title = "How to use lua to parse multi frames for one package?"
description = '''I want to write a lua plugin to parse my private protocol. In my protocol, a package size often bigger then MTU, so I need parse many TCP frames for one package.'''
date = "2013-11-01T02:48:00Z"
lastmod = "2013-11-01T05:46:00Z"
weight = 26608
keywords = [ "lua" ]
aliases = [ "/questions/26608" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use lua to parse multi frames for one package?](/questions/26608/how-to-use-lua-to-parse-multi-frames-for-one-package)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26608-score" class="post-score" title="current number of votes">0</div><span id="post-26608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write a lua plugin to parse my private protocol. In my protocol, a package size often bigger then MTU, so I need parse many TCP frames for one package.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '13, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/1be7ca86b5f03e4b3e54351ea3d570fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhang&#39;s gravatar image" /><p><span>zhang</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhang has no accepted answers">0%</span></p></div></div><div id="comments-container-26608" class="comments-container"></div><div id="comment-tools-26608" class="comment-tools"></div><div class="clear"></div><div id="comment-26608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26613"></span>

<div id="answer-container-26613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26613-score" class="post-score" title="current number of votes">0</div><span id="post-26613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the first few comments in the Wiki</p><blockquote><p><a href="http://wiki.wireshark.org/Lua/Dissectors">http://wiki.wireshark.org/Lua/Dissectors</a><br />
</p></blockquote><p>Then there some samples, that show how it works. <code>pinfo.desegment_len</code> is the key (see also Wiki).</p><blockquote><p><a href="http://delog.wordpress.com/2013/05/21/dealing-with-segmented-data-in-a-wireshark-dissector-written-in-lua/">http://delog.wordpress.com/2013/05/21/dealing-with-segmented-data-in-a-wireshark-dissector-written-in-lua/</a><br />
<a href="http://blog.roisu.org/english-create-a-wireshark-dissector-with-lua/">http://blog.roisu.org/english-create-a-wireshark-dissector-with-lua/</a><br />
<a href="http://stackoverflow.com/questions/13138088/how-do-i-reassemble-tcp-packet-in-lua-dissector">http://stackoverflow.com/questions/13138088/how-do-i-reassemble-tcp-packet-in-lua-dissector</a><br />
<a href="https://github.com/reverbrain/elliptics/blob/master/wireshark/elliptics.lua">https://github.com/reverbrain/elliptics/blob/master/wireshark/elliptics.lua</a><br />
</p></blockquote><p>If you search google for <strong>lua "desegment_len"</strong> you'll probably find more samples.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '13, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26613" class="comments-container"></div><div id="comment-tools-26613" class="comment-tools"></div><div class="clear"></div><div id="comment-26613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

