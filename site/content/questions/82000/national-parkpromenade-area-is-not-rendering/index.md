+++
type = "question"
title = "National Park/Promenade Area is not rendering."
description = '''Hello dear mappers, I join from Turkey. 5 weeks ago, I mapped a national park (actually more of a promenade/picnic aimed, modified forestry) called &#x27;&#x27;Sultangazi Kent Ormanı (Promenade Forest)&#x27;&#x27; and &#x27;&#x27;Mimar Sinan Kent Ormanı(Promenade Forest)&#x27;&#x27; located in İstanbul/Sultangazi, which has the change set...'''
date = "2021-09-29T11:50:00Z"
lastmod = "2021-09-29T18:54:00Z"
weight = 82000
keywords = [ "#renderingfail" ]
aliases = [ "/questions/82000" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [National Park/Promenade Area is not rendering.](/questions/82000/national-parkpromenade-area-is-not-rendering)

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
<span id="post-82000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82000-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello dear mappers,</p>
<p>I join from Turkey. 5 weeks ago, I mapped a national park (actually more of a promenade/picnic aimed, modified forestry) called ''Sultangazi Kent Ormanı (Promenade Forest)'' and ''Mimar Sinan Kent Ormanı(Promenade Forest)'' located in İstanbul/Sultangazi, which has the change set number of #1099503735.</p>
<p>When I checked my changeset after; then realized that Mimar Sinan one is rendering in the map normally, while Sultangazi one is only accesible by ''Show specifitations''. I assumed this problem may born because of my wrong tagging, so I tried to fix it by updating the tags 1 week later in change set #110975035.</p>
<p>However, this was not the solution. I did not touch the area since then, and now I wanted to get a helping hand from the experienced pals from here. Thanking you from now on.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-#renderingfail" rel="tag" title="see questions tagged &#39;#renderingfail&#39;">#renderingfail</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '21, 11:50</strong></p>
<img src="https://secure.gravatar.com/avatar/03c57068566d8dd97d5fab0a5219ef88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="em1nk&#39;s gravatar image" />
<p><span>em1nk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="em1nk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82000" class="comments-container">
&#10;</div>
<div id="comment-tools-82000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82000-form-container" class="comment-form-container">
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

<span id="82001"></span>

<div id="answer-container-82001" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82001-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the problem is the way Sultangazi Kent Ormanı is drawn. There are at least 3 different way objects: <a href="https://www.openstreetmap.org/way/974795068">https://www.openstreetmap.org/way/974795068</a> (the main one) <a href="https://www.openstreetmap.org/way/975250100">https://www.openstreetmap.org/way/975250100</a> <a href="https://www.openstreetmap.org/way/975250102">https://www.openstreetmap.org/way/975250102</a></p>
<p>Renderers generally won't understand just from the name that these are in fact a single boundary of a single object - you need to make the main way into a single closed way with no gaps.</p>
<p>(You could also add all the ways into a single multipolygon "relation". This is often done for complex boundaries such as national parks, e.g. <a href="https://www.openstreetmap.org/relation/287245">https://www.openstreetmap.org/relation/287245</a> ). But there would probably not be a big gain here where you have already mapped almost the whole boundary as a single way).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '21, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '21, 14:32</strong> </span></p>
</div>
</div>
<div id="comments-container-82001" class="comments-container">
<span id="82002"></span>
<div id="comment-82002" class="comment">
<div id="post-82002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Much appreciated it, thanks a lot.</p>
</div>
<div id="comment-82002-info" class="comment-info">
<span class="comment-age">(29 Sep '21, 18:40)</span> <span class="comment-user userinfo">em1nk</span>
</div>
</div>
<span id="82003"></span>
<div id="comment-82003" class="comment">
<div id="post-82003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just uploaded a changeset about fixing the issue with your guide. <a href="https://www.openstreetmap.org/changeset/111880742#map=15/41.1095/28.9135">https://www.openstreetmap.org/changeset/111880742#map=15/41.1095/28.9135</a></p>
<p>Much appreciated it, thanks a lot.</p>
</div>
<div id="comment-82003-info" class="comment-info">
<span class="comment-age">(29 Sep '21, 18:54)</span> <span class="comment-user userinfo">em1nk</span>
</div>
</div>
</div>
<div id="comment-tools-82001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82001-form-container" class="comment-form-container">
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

