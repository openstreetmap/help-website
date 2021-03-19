+++
type = "question"
title = "Is possible to export/save a wieshark file with colourized packets that have been filtered?"
description = '''Hi all,  In wireshark is possible to filter some packets and colorize them (i.e. put in &quot;Red&quot; all packets of a specific filter applied). My question is: Is it possible to save/export the wireshark file with all colourized filters that have been applied in order to see them again later? I know that i...'''
date = "2016-02-10T09:34:00Z"
lastmod = "2016-02-10T13:39:00Z"
weight = 50060
keywords = [ "filter", "coloringpetit" ]
aliases = [ "/questions/50060" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is possible to export/save a wieshark file with colourized packets that have been filtered?](/questions/50060/is-possible-to-exportsave-a-wieshark-file-with-colourized-packets-that-have-been-filtered)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50060-score" class="post-score" title="current number of votes">0</div><span id="post-50060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>In wireshark is possible to filter some packets and colorize them (i.e. put in "Red" all packets of a specific filter applied). My question is: Is it possible to save/export the wireshark file with all colourized filters that have been applied in order to see them again later? I know that is possible to export the filtered packets, but I want to export them with the colours.</p><p>Thank you in advacne.</p><p>Regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-coloringpetit" rel="tag" title="see questions tagged &#39;coloringpetit&#39;">coloringpetit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '16, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/08317d6cd999a98c43fd85807066c6d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nairda&#39;s gravatar image" /><p><span>Nairda</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nairda has no accepted answers">0%</span></p></div></div><div id="comments-container-50060" class="comments-container"></div><div id="comment-tools-50060" class="comment-tools"></div><div class="clear"></div><div id="comment-50060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50075"></span>

<div id="answer-container-50075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50075-score" class="post-score" title="current number of votes">0</div><span id="post-50075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The two things are independent. As you already know, you can use <code>File -&gt; Export Specified Packets</code> to save only packets shown by the display filter currently applied. And when in the coloring rules management window (<code>View -&gt; Coloring rules</code>), you can select rules from the list (click with Ctrl, Shift, or with both together works the way it usually does on lists) and then click <code>Export</code> to export the selected rules to a file.</p><p>The only exception from the rule is that if you haven't selected any rule and you press <code>Export</code>, all rules in the list are exported.</p><p><code>Import</code> of a previously exported rule used to create a duplicate, I don't know whether it is still the case, try with one of the rules you've created.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '16, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50075" class="comments-container"></div><div id="comment-tools-50075" class="comment-tools"></div><div class="clear"></div><div id="comment-50075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

