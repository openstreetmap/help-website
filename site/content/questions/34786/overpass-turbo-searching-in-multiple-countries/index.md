+++
type = "question"
title = "Overpass Turbo searching in multiple Countries"
description = '''Hi I don&#x27;t get how I can tell Overpass Turbo that he shall search within more than one country. Using the wizard for germany only I got this.  http://overpass-turbo.eu/s/46G I tried different thinks but I couldn&#x27;t figure it out. In the documentation I couldn&#x27;t find how` to do it, too.'''
date = "2014-07-10T00:51:00Z"
lastmod = "2014-07-10T19:53:00Z"
weight = 34786
keywords = [ "overpass", "multiple", "overpass-turbo", "countries" ]
aliases = [ "/questions/34786" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo searching in multiple Countries](/questions/34786/overpass-turbo-searching-in-multiple-countries)

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
<span id="post-34786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34786-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I don't get how I can tell Overpass Turbo that he shall search within more than one country.</p>
<p>Using the wizard for germany only I got this. <a href="http://overpass-turbo.eu/s/46G">http://overpass-turbo.eu/s/46G</a></p>
<p>I tried different thinks but I couldn't figure it out. In the documentation I couldn't find how` to do it, too.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-countries" rel="tag" title="see questions tagged &#39;countries&#39;">countries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '14, 00:51</strong></p>
<img src="https://secure.gravatar.com/avatar/2b7524d13f78e89892e74a5a9baad782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hedaja&#39;s gravatar image" />
<p><span>Hedaja</span><br />
<span class="score" title="96 reputation points">96</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hedaja has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '19, 09:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-34786" class="comments-container">
&#10;</div>
<div id="comment-tools-34786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34786-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="34792"></span>

<div id="answer-container-34792" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34792-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-34792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hedaja has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't do this with the built-in query wizard in overpass turbo. But you can combine different areas if you manually tweak the Overpass query:</p>
<pre><code>&lt;!-- fetch area “germany” to search in --&gt;
&lt;id-query {{nominatimArea:germany}} into=&quot;area&quot;/&gt;</code></pre>
<p>In your query, this defines the area to search in. Here it is "germany".</p>
<p>Using the <code>&lt;union&gt;</code> statement you can combine multiple such areas into one. (Note that the final result of the union has to be named "area" for the later <code>&lt;area-query&gt;</code>s to work.)</p>
<pre><code>&lt;union into=&quot;area&quot;&gt;
  &lt;id-query {{nominatimArea:germany}} /&gt;
  &lt;id-query {{nominatimArea:austria}} /&gt;
  &lt;id-query {{nominatimArea:switzerland}} /&gt;
&lt;/union&gt;</code></pre>
<p>Here is a working example: <a href="http://overpass-turbo.eu/s/46Y">http://overpass-turbo.eu/s/46Y</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '14, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-34792" class="comments-container">
<span id="34809"></span>
<div id="comment-34809" class="comment">
<div id="post-34809-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Very nice! If not done yet, will try to add that feature to OSM Wiki.</p>
</div>
<div id="comment-34809-info" class="comment-info">
<span class="comment-age">(10 Jul '14, 19:53)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-34792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34792-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34789"></span>

<div id="answer-container-34789" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34789-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try this query: <a href="http://overpass-turbo.eu/s/46U">http://overpass-turbo.eu/s/46U</a> this uses the bounding box of the visual area, instead of the fixed area defined by id-query {{nominatimArea:germany and }} into="area"</p>
<p>in your query</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '14, 06:56</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-34789" class="comments-container">
<span id="34797"></span>
<div id="comment-34797" class="comment">
<div id="post-34797-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>thanks for you answer. But this isn't useful in this case because I wanted to count the number of charging_stations within Germany,Switzerland and Austria. Using bbox means I would get chargingstations in parts of the Czech Republic and other surrounding countries.</p>
</div>
<div id="comment-34797-info" class="comment-info">
<span class="comment-age">(10 Jul '14, 11:44)</span> <span class="comment-user userinfo">Hedaja</span>
</div>
</div>
</div>
<div id="comment-tools-34789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34789-form-container" class="comment-form-container">
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

