+++
type = "question"
title = "Get subregions that city is parent of"
description = '''When using Nonimatim browser I can get this kind of view to a city, where also all the subregions to which a city is a parent of are listed (+many other interesting details): http://nominatim.openstreetmap.org/details.php?place_id=97761941 I&#x27;d like to be able to get this same list through Nominatim ...'''
date = "2013-01-25T14:04:00Z"
lastmod = "2013-01-28T09:28:00Z"
weight = 19340
keywords = [ "api", "nominatim", "parent" ]
aliases = [ "/questions/19340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get subregions that city is parent of](/questions/19340/get-subregions-that-city-is-parent-of)

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
<span id="post-19340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19340-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using Nonimatim browser I can get this kind of view to a city, where also all the subregions to which a city is a parent of are listed (+many other interesting details): <a href="http://nominatim.openstreetmap.org/details.php?place_id=97761941">http://nominatim.openstreetmap.org/details.php?place_id=97761941</a></p>
<p>I'd like to be able to get this same list through Nominatim API, but am unable to figure out how to do that. All API calls return just a very few details - so is this something that is not available through API? If this is so, is there some other way to get this data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-parent" rel="tag" title="see questions tagged &#39;parent&#39;">parent</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '13, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/5c42f5ddb4acad42a4aea8b471b94346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lari&#39;s gravatar image" />
<p><span>Lari</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lari has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19340" class="comments-container">
<span id="19388"></span>
<div id="comment-19388" class="comment">
<div id="post-19388-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems like there is no API call for this specific output, maybe because it was (initially) intended for debugging.</p>
</div>
<div id="comment-19388-info" class="comment-info">
<span class="comment-age">(28 Jan '13, 09:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19340-form-container" class="comment-form-container">
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

<span id="19378"></span>

<div id="answer-container-19378" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19378-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know whether Nominatim has an API call for this.</p>
<p>But to get the data, you can use [<a href="http://overpass-api.de/api/interpreter?data=rel%5Bname=Helsinki%5D;%3E;is_in;area._%5Badmin_level%5D;out;">http://overpass-api.de/api/interpreter?data=rel[name=Helsinki];&gt;;is_in;area._[admin_level];out;</a> ]<a href="http://overpass-api.de/api/interpreter?data=rel%5Bname=Helsinki%5D;%3E;is_in;area._%5Badmin_level%5D;out;">1</a> The returned XML contains all the administrative units that have a node inside Helsinki, including both suburbs and provinces, Finland and even the EU entry.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '13, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '13, 21:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-19378" class="comments-container">
<span id="19382"></span>
<div id="comment-19382" class="comment">
<div id="post-19382-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, but the list received through this url is not the same as what I get through the Nominatim url above. What I need is a hierarchical list or a tree through which I could build a structure which starts at the city level, and goes down to different city districts and to their sub-districts. Is there a way to get this?</p>
</div>
<div id="comment-19382-info" class="comment-info">
<span class="comment-age">(27 Jan '13, 21:47)</span> <span class="comment-user userinfo">Lari</span>
</div>
</div>
</div>
<div id="comment-tools-19378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19378-form-container" class="comment-form-container">
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

