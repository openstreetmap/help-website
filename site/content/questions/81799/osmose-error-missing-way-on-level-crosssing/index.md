+++
type = "question"
title = "Osmose error &quot;Missing way on level crosssing&quot;"
description = '''I get Osmose errors: &quot;Missing way on level crosssing&quot;. But I can&#x27;t find any errors. There is a road crossing the railway on the same node, which is tagged &quot;railway=level_crossing&quot;. Exemples:  n21619940 w48980273, n4813150648 w48674965, n318444322 w206601940 Any ideas why?'''
date = "2021-09-17T21:58:00Z"
lastmod = "2021-09-20T09:06:00Z"
weight = 81799
keywords = [ "osmose" ]
aliases = [ "/questions/81799" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmose error "Missing way on level crosssing"](/questions/81799/osmose-error-missing-way-on-level-crosssing)

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
<span id="post-81799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81799-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I get Osmose errors: "Missing way on level crosssing".</p>
<p>But I can't find any errors. There is a road crossing the railway on the same node, which is tagged "railway=level_crossing".</p>
<p>Exemples: n21619940 w48980273, n4813150648 w48674965, n318444322 w206601940</p>
<p>Any ideas why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmose" rel="tag" title="see questions tagged &#39;osmose&#39;">osmose</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '21, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '21, 21:59</strong> </span></p>
</div>
</div>
<div id="comments-container-81799" class="comments-container">
<span id="81802"></span>
<div id="comment-81802" class="comment">
<div id="post-81802-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, it is a bit difficult to try to find something now that you have played around with those nodes already. Better leave the objects untouched for a while when you ask such questions.</p>
</div>
<div id="comment-81802-info" class="comment-info">
<span class="comment-age">(18 Sep '21, 20:17)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81803"></span>
<div id="comment-81803" class="comment">
<div id="post-81803-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I understand this. If I get such errors again, I will post them here.</p>
<p>I have tested to unglue the railway, road and the crossing, and the glue everything back on the same node. And I'm now waiting see if the errors come back.</p>
</div>
<div id="comment-81803-info" class="comment-info">
<span class="comment-age">(18 Sep '21, 21:12)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
<span id="81815"></span>
<div id="comment-81815" class="comment">
<div id="post-81815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I now have a new example of this error:</p>
<p><a href="https://www.openstreetmap.org/#map=19/59.50733/16.00168">https://www.openstreetmap.org/#map=19/59.50733/16.00168</a> n3847978760, w48980273</p>
</div>
<div id="comment-81815-info" class="comment-info">
<span class="comment-age">(20 Sep '21, 08:35)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
<span id="81817"></span>
<div id="comment-81817" class="comment">
<div id="post-81817-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That example seems to be a mixture of tagging foe a level crossing (allowing vehicles and pedestrians to cross from one side of the railway to the other) and a pedestrian crossing (allowing pedestrians to pass from one side of the road to the other). What is highway=crossing intended to refer to? It seems unlikely that there would be a marked pedestrian crossing literally on the railway tracks.</p>
</div>
<div id="comment-81817-info" class="comment-info">
<span class="comment-age">(20 Sep '21, 09:06)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-81799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81799-form-container" class="comment-form-container">
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

<span id="81816"></span>

<div id="answer-container-81816" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81816-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Msiipola has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is anything wrong. It seems to be a false warning from Osmose. Actually, there is already a <a href="https://github.com/osm-fr/osmose-backend/issues/1327">ticket</a> about this on Osmose's Github repository.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '21, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81816" class="comments-container">
&#10;</div>
<div id="comment-tools-81816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81816-form-container" class="comment-form-container">
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

