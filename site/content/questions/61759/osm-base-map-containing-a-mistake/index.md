+++
type = "question"
title = "OSM base map containing a mistake?"
description = '''Hi, I&#x27;ve noticed a mistake on the OSM Standard base map.  In France, some regions merged on January 1st, 2016. It&#x27;s the case for Auvergne and Rhône-Alpes, which became Auvergne-Rhône-Alpes.  Back then, the modification was successfully carried out on the OSM Standard base map. However, a few days ag...'''
date = "2018-01-21T23:33:00Z"
lastmod = "2018-01-22T06:34:00Z"
weight = 61759
keywords = [ "regions", "problem", "basemap", "borders", "france" ]
aliases = [ "/questions/61759" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM base map containing a mistake?](/questions/61759/osm-base-map-containing-a-mistake)

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
<span id="post-61759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've noticed a mistake on the OSM Standard base map.</p>
<p>In France, some regions merged on January 1st, 2016. It's the case for Auvergne and Rhône-Alpes, which became Auvergne-Rhône-Alpes.</p>
<p>Back then, the modification was successfully carried out on the OSM Standard base map.</p>
<p>However, a few days ago, I noted that the region turned back to its prior status, i.e Auvergne and Rhône-Alpes, with a border between the two. Auvergne-Rhône-Alpes is the only French region affected by that problem on OSM.</p>
<p>Why? Is it possible to get those two regions merged again?</p>
<p>Thanks for your help.</p>
<p>Yours faithfully,</p>
<p>Marc</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regions" rel="tag" title="see questions tagged &#39;regions&#39;">regions</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-basemap" rel="tag" title="see questions tagged &#39;basemap&#39;">basemap</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '18, 23:33</strong></p>
<img src="https://secure.gravatar.com/avatar/89049f8295e5e3cf0b544307f4a3bfb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heaven656&#39;s gravatar image" />
<p><span>Heaven656</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heaven656 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61759" class="comments-container">
&#10;</div>
<div id="comment-tools-61759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61759-form-container" class="comment-form-container">
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

<span id="61760"></span>

<div id="answer-container-61760" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61760-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Auvergne-Rhône-Alpes region appears to be correctly mapped at the time of writing: <a href="https://www.openstreetmap.org/relation/3792877">https://www.openstreetmap.org/relation/3792877</a></p>
<p>The old regions carry a <code>boundary=administrative</code> and a <code>disused:admin_level</code> tag: <a href="https://www.openstreetmap.org/relation/8638">https://www.openstreetmap.org/relation/8638</a> , <a href="https://www.openstreetmap.org/relation/8655">https://www.openstreetmap.org/relation/8655</a> - this is the same with other regions that were combined 2 years ago. Details are best discussed on the French mailing list, <a href="https://lists.openstreetmap.org/listinfo/talk-fr">https://lists.openstreetmap.org/listinfo/talk-fr</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '18, 23:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '18, 06:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-61760" class="comments-container">
<span id="61761"></span>
<div id="comment-61761" class="comment">
<div id="post-61761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik,</p>
<p>First of all, thank you very much for your quick answer.</p>
<p>Actually, I checked your first link showing the basemap, and I maintain that the Auvergne-Rhône-Alpes region is the only one that contains an old, obsolete boundary: yes the name "Auvergne-Rhône-Alpes" appears, but the regions of Rhône-Alpes (around Lyon) and Auvergne (around Clermont-Ferrand) should be merged into a single unit, as it was a few days ago.</p>
<p>All the other newly-merged French regions appear correctly : Grand-Est, Bourgogne-Franche-Comté, Nouvelle-Aquitaine...</p>
<p><del>Your second link doesn't work,</del> but thanks to the third one, I might be able to contact the person who modified the map and to discuss the issue with him.</p>
<p>So, thank you very much for your help.</p>
<p>Best regards!</p>
</div>
<div id="comment-61761-info" class="comment-info">
<span class="comment-age">(22 Jan '18, 01:02)</span> <span class="comment-user userinfo">Heaven656</span>
</div>
</div>
<span id="61762"></span>
<div id="comment-61762" class="comment">
<div id="post-61762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta <a href="https://help.openstreetmap.org/users/14669/heaven656">@Heaven656</a>: fixed the second link - now it works.</p>
</div>
<div id="comment-61762-info" class="comment-info">
<span class="comment-age">(22 Jan '18, 06:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61760-form-container" class="comment-form-container">
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

