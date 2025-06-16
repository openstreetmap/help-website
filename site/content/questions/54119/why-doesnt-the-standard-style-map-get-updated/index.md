+++
type = "question"
title = "Why doesn&#x27;t the standard style map get updated?"
description = '''Please check out this view on a region in Paraguay: https://www.openstreetmap.org/#map=12/-22.6569/-60.1694 This view is several weeks old. Many many chnages and additions have been made since then, but although zoom levels &amp;lt;= 11 get updated within a minute or so, nothing happens to zoom levels of...'''
date = "2017-01-17T18:28:00Z"
lastmod = "2017-01-18T20:48:00Z"
weight = 54119
keywords = [ "rendering", "updates", "mapnik" ]
aliases = [ "/questions/54119" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why doesn't the standard style map get updated?](/questions/54119/why-doesnt-the-standard-style-map-get-updated)

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
<span id="post-54119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54119-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please check out this view on a region in Paraguay: <a href="https://www.openstreetmap.org/#map=12/-22.6569/-60.1694">https://www.openstreetmap.org/#map=12/-22.6569/-60.1694</a></p>
<p>This view is several weeks old. Many many chnages and additions have been made since then, but although zoom levels &lt;= 11 get updated within a minute or so, nothing happens to zoom levels of &gt;= 12, even after weeks.</p>
<p>This is not a chache problem, as I have tried it on many computers and browsers, same result.</p>
<p>Also, adding /dirty as recommended here has not shown any effect: <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated?">https://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated?</a></p>
<p>Any idea?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '17, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/5f5d99b38973b2f5f0a322f6695ff1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DerGuteDiktator&#39;s gravatar image" />
<p><span>DerGuteDiktator</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DerGuteDiktator has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '17, 20:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-54119" class="comments-container">
&#10;</div>
<div id="comment-tools-54119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54119-form-container" class="comment-form-container">
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

<span id="54122"></span>

<div id="answer-container-54122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54122-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-54122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A quick check shows that the tiles correspond to the underlying map data here, so either it is an issue with local caching or with the tile cache Paraquay is served from.</p>
<p>You can find the cache serving you with <a href="http://a.tile.openstreetmap.org/cgi-bin/debug">http://a.tile.openstreetmap.org/cgi-bin/debug</a> (run it for a, b and c), if it is really an issue you need to report it to our operations group: <a href="https://github.com/openstreetmap/operations">https://github.com/openstreetmap/operations</a></p>
<p>Re-reading your question, it may be that you had the zooms the wrong way around. If yoou are having issues with zoom levels lower and including 12 (in other words 0-12) the issue is due to low zoom tiles being bulk rendered.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '17, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '17, 22:06</strong> </span></p>
</div>
</div>
<div id="comments-container-54122" class="comments-container">
<span id="54148"></span>
<div id="comment-54148" class="comment">
<div id="post-54148-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for replying.</p>
<p>Yes, I mixed up the "direction" of zoom levels; the issue is with levels 0-12, 13 to 19 are doing fine. Sorry for the red herring.</p>
<p>What do you mean by "low zoom tiles being bulk rendered" - I understand this is done less regularly, but can it really last more than a month? And if so, why does the /dirty tweak not show any effect?</p>
</div>
<div id="comment-54148-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 18:01)</span> <span class="comment-user userinfo">DerGuteDiktator</span>
</div>
</div>
<span id="54150"></span>
<div id="comment-54150" class="comment">
<div id="post-54150-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Normally the low zoom tile update runs early in the month, however that may have not happened this month and the last update been post the last style change on the 24th December.</p>
</div>
<div id="comment-54150-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 20:48)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54122-form-container" class="comment-form-container">
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

