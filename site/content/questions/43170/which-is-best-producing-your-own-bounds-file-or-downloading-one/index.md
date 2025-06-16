+++
type = "question"
title = "Which is best, producing your own bounds file or downloading one"
description = '''I am just starting to get to grips with how to produce maps using osmosis, mkgmap etc etc. does anyone have any information as to which is the best approach, should I produce my own bounds directory using osmosis and mkgmap or should I download one, are there pros and cons to each aspproach, if so w...'''
date = "2015-05-23T08:34:00Z"
lastmod = "2015-05-23T11:53:00Z"
weight = 43170
keywords = [ "boundaries", "mkgmap", "osmosis" ]
aliases = [ "/questions/43170" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which is best, producing your own bounds file or downloading one](/questions/43170/which-is-best-producing-your-own-bounds-file-or-downloading-one)

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
<span id="post-43170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43170-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am just starting to get to grips with how to produce maps using osmosis, mkgmap etc etc. does anyone have any information as to which is the best approach, should I produce my own bounds directory using osmosis and mkgmap or should I download one, are there pros and cons to each aspproach, if so what are they</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '15, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '15, 08:37</strong> </span></p>
</div>
</div>
<div id="comments-container-43170" class="comments-container">
<span id="43172"></span>
<div id="comment-43172" class="comment">
<div id="post-43172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure whether you mean using bounds to define a specific extract or different bounds for mkgmap tiles. Personally I just use splitter with default settings: although at one stage I thought tiles on OS Landranger boundaries would be useful (I had a Garmin with limited memory).</p>
</div>
<div id="comment-43172-info" class="comment-info">
<span class="comment-age">(23 May '15, 09:55)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="43173"></span>
<div id="comment-43173" class="comment">
<div id="post-43173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, well I am a little confused by the terminology from the documentation.</p>
<p>I started with the guide. <a href="https://wiki.openstreetmap.org/wiki/Mkgmap/help/How_to_create_a_map">How to make a map</a></p>
<p>This says "These tiles can be compiled into a map as-is, but the resultant map would lack addressing data (e.g. city or zip code). Addressing data comes from preprocessed bounds tiles, and you can either download them from navmaps.eu or create them yourself as described in Mkgmap/help/options#Using_preprocessed_bounds_for_the_address_index. Place the resultant files into a subdirectory named bounds. "</p>
<p>To me that implies that the bounds directory would contain more of an index than boundary definitions.</p>
</div>
<div id="comment-43173-info" class="comment-info">
<span class="comment-age">(23 May '15, 10:40)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
<span id="43175"></span>
<div id="comment-43175" class="comment">
<div id="post-43175-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This wiki information was outdated, boundary data can be downloaded from mkgmap.org or on the link to Lambertus site (see my answer). In your mkgmap parameters you have to add --bounds=bounds_20150206.zip to make it work.</p>
</div>
<div id="comment-43175-info" class="comment-info">
<span class="comment-age">(23 May '15, 11:53)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
</div>
<div id="comment-tools-43170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43170-form-container" class="comment-form-container">
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

<span id="43174"></span>

<div id="answer-container-43174" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43174-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>World wide boundary data for mkgmap is regularly updated by Lambertus, so not necessary to use osmosis (unless you need more recent or specific boundary data): <a href="http://osm2.pleiades.uni-wuppertal.de/bounds/">http://osm2.pleiades.uni-wuppertal.de/bounds/</a> or <a href="http://www.mkgmap.org.uk/download/mkgmap.html">http://www.mkgmap.org.uk/download/mkgmap.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '15, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '15, 11:53</strong> </span></p>
</div>
</div>
<div id="comments-container-43174" class="comments-container">
&#10;</div>
<div id="comment-tools-43174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43174-form-container" class="comment-form-container">
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

