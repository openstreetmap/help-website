+++
type = "question"
title = "tags-filter with multiple filter expressions not working as expected?"
description = '''I am trying to get all main railway tracks from an .osm.pbf file. My command looks like this: osmium tags-filter austria-latest.osm.pbf railway=rail railway:track_type=main service!=yard service!=siding -o rails_in_austria.osm.pbf My expectation was that osmium will match the file against all four f...'''
date = "2021-12-25T13:29:00Z"
lastmod = "2021-12-25T17:25:00Z"
weight = 82894
keywords = [ "tags-filter" ]
aliases = [ "/questions/82894" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tags-filter with multiple filter expressions not working as expected?](/questions/82894/tags-filter-with-multiple-filter-expressions-not-working-as-expected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82894-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get all main railway tracks from an .osm.pbf file. My command looks like this:</p>
<p><code>osmium tags-filter austria-latest.osm.pbf railway=rail railway:track_type=main service!=yard service!=siding -o rails_in_austria.osm.pbf</code></p>
<p>My expectation was that osmium will match the file against all four filter expressions sequentially similar to a logical &amp; operator. Somehow this doesn't seem to happen as my result contains entries that e.g. do not contain any railway attribute.</p>
<p>The man page for osmium-tags-filter says:</p>
<p><code>The filter expressions specified in a file and/or on the command line are matched in the order they are given. To achieve best performance, put expressions expected to match more often first.</code></p>
<p>I'm stuck here, maybe more experienced users can help?</p>
<p>In QGis my filter works with following SQL filter expression:</p>
<p><code>"other_tags" LIKE '%"railway:track_type"=&gt;"main"%' AND "other_tags" NOT LIKE '%"service"=&gt;"yard"%' AND "other_tags" NOT LIKE '%"service"=&gt;"siding"%'</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tags-filter" rel="tag" title="see questions tagged &#39;tags-filter&#39;">tags-filter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Dec '21, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2aeb3aa74f0a2230126218578524e9b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pato3&#39;s gravatar image" />
<p><span>pato3</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pato3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82894" class="comments-container">
&#10;</div>
<div id="comment-tools-82894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82894-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="82896"></span>

<div id="answer-container-82896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first sentence of the man page should make things clear: "Get objects matching at least one of the specified expressions from the input and write them to the output." So the expressions are ORed together. You can not do general AND expressions. Sometimes what you want can be done using inverted expressions and the -i option. Or you run Osmium several times, once each with the expressions you want ANDed.</p>
<p>Generally <code>osmium tags-filter</code> is more suited to to a rough filtering (in your case the <code>railway=rail</code>) which will reduce the data from "huge amounts of data" to "manageable amount of data" quickly. Then just use any other kind of specialized processing you want to do with whatever tool suits you best.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '21, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-82896" class="comments-container">
&#10;</div>
<div id="comment-tools-82896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82896-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

