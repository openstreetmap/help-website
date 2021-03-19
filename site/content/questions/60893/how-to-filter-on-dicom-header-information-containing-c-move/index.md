+++
type = "question"
title = "How to filter on dicom header information containing C-MOVE..."
description = '''Hi, I have a network capture that contains DICOM data. In the Info column for a packet containing a DICOM header, I have the string: P-DATA, C-MOVE-RQ ID=1 My question is: Shouldn&#x27;t I be able to use the filter: dicom contains &quot;C-MOVE-RQ&quot; to show only packets that have a DICOM header containing that ...'''
date = "2017-04-19T11:00:00Z"
lastmod = "2017-04-19T12:07:00Z"
weight = 60893
keywords = [ "dicom", "filtering", "display_filter", "display-filter" ]
aliases = [ "/questions/60893" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter on dicom header information containing C-MOVE...](/questions/60893/how-to-filter-on-dicom-header-information-containing-c-move)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60893-score" class="post-score" title="current number of votes">0</div><span id="post-60893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a network capture that contains DICOM data.<br />
In the Info column for a packet containing a DICOM header, I have the string:<br />
P-DATA, C-MOVE-RQ ID=1</p><p>My question is: Shouldn't I be able to use the filter: dicom contains "C-MOVE-RQ" to show only packets that have a DICOM header containing that string? I would think the answer is yes. Yet, I can not use that filter to show only those packets. Any thoughts out there on this?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dicom" rel="tag" title="see questions tagged &#39;dicom&#39;">dicom</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-display_filter" rel="tag" title="see questions tagged &#39;display_filter&#39;">display_filter</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/80f108673181588448e72547e5d16f2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cpigz&#39;s gravatar image" /><p><span>cpigz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cpigz has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-60893" class="comments-container"><span id="60898"></span><div id="comment-60898" class="comment"><div id="post-60898-score" class="comment-score"></div><div class="comment-text"><p>One way I found that I could do something like what I'm looking for is to right-click on a DICOM packet -&gt; protocol preferences -&gt; Create subtrees for DICOM tags.</p><p>This enables me to use a display filter like: dicom.tag.value.str contains "MOVE"</p><p>Now I can see only packets related to a C-MOVE-RQ and the C-MOVE-RSP but this does not include the C-MOVE-DATA packets. So, this is closer to what I'm looking to do but still not perfect.</p></div><div id="comment-60898-info" class="comment-info"><span class="comment-age">(19 Apr '17, 11:51)</span> <span class="comment-user userinfo">cpigz</span></div></div></div><div id="comment-tools-60893" class="comment-tools"></div><div class="clear"></div><div id="comment-60893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60897"></span>

<div id="answer-container-60897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60897-score" class="post-score" title="current number of votes">1</div><span id="post-60897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The DICOM dissector doesn't provide a field for command values.</p><p>A workaround can be to use the hex bytes of the C-MOVE-RQ command (0x0021) in the display filter. Please be aware of the endianness of the capture. So a <code>dicom contains 21:00</code> should work.</p><p>If this lists too much packets prepending the hex bytes of the Unsigned Short can help.</p><p>=&gt; <code>dicom contains 02:00:00:00:21:00</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '17, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-60897" class="comments-container"><span id="60899"></span><div id="comment-60899" class="comment"><div id="post-60899-score" class="comment-score"></div><div class="comment-text"><p>Thanks! That is an interesting approach. I never even thought of that. However, this also means that a hex combination of 21:00 will be matched when "Presentation Context Reply" is present. This means I will also see all association accepts.</p><p>The filter: dicom.tag.value.str contains "MOVE"</p><p>seems to work a little better (its just missing the C-MOVE-Data packets).</p></div><div id="comment-60899-info" class="comment-info"><span class="comment-age">(19 Apr '17, 12:07)</span> <span class="comment-user userinfo">cpigz</span></div></div></div><div id="comment-tools-60897" class="comment-tools"></div><div class="clear"></div><div id="comment-60897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

