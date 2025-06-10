+++
type = "question"
title = "How to display embedded map and display &quot;relation&quot; boundary line"
description = '''[I have tried searching using google and the search option - I promise] I wish to embed an Open Streetmap Map into my website (which is easy using LeafletJS), and then I want to display the boundary for a &quot;relation&quot; you have stored. Looking at the xml I can see the relation is made up of multiple &#x27;w...'''
date = "2023-05-01T16:30:00Z"
lastmod = "2023-05-02T07:59:00Z"
weight = 87202
keywords = [ "node", "map", "relation", "embded", "way" ]
aliases = [ "/questions/87202" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to display embedded map and display "relation" boundary line](/questions/87202/how-to-display-embedded-map-and-display-relation-boundary-line)

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
<span id="post-87202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>[I have tried searching using google and the search option - I promise]</p>
<p>I wish to embed an Open Streetmap Map into my website (which is easy using LeafletJS), and then I want to display the boundary for a "relation" you have stored. Looking at the xml I can see the relation is made up of multiple 'ways' and for each 'way' I could seek to download a 'node'. From here I could traverse the xml and locate each GPS co-ord and then add it programatically to the map using Leaflet but this seems (to me) overcomplicated. Is this what is generally done or is there a blindingly obvious programatic way that I have not seen? I can imagine this question should be directed here or to the Leaflet folks -so apologies if this is a wrong posting</p>
<p>Howard</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-embded" rel="tag" title="see questions tagged &#39;embded&#39;">embded</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '23, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/3ccaa086f4a9b8ace6ce6a04413653a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hjp23&#39;s gravatar image" />
<p><span>hjp23</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hjp23 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87202" class="comments-container">
<span id="87207"></span>
<div id="comment-87207" class="comment">
<div id="post-87207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unrelated to getting the Relation into Leaflet, if you're planning on using tiles from the "default" style then there's an associated usage policy linked to from the <a href="https://www.openstreetmap.org/copyright">copyright page</a>.</p>
</div>
<div id="comment-87207-info" class="comment-info">
<span class="comment-age">(01 May '23, 22:33)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-87202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87202-form-container" class="comment-form-container">
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

<span id="87206"></span>

<div id="answer-container-87206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87206-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you only want to use a single relation statically, and don't need updates then you can download the data <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/GeoJSON">in GeoJSON format</a> from <a href="https://overpass-turbo.eu/">Overpass Turbo</a>. I think Leaflet then allows you to use GeoJSON layers if you store it on your site somewhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '23, 22:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-87206" class="comments-container">
<span id="87209"></span>
<div id="comment-87209" class="comment">
<div id="post-87209-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I must admit that when I went to Overpass I scratched my head as to how to find the "relation" from OSM - but a quick question with ChatGPT led to the following Overpass query</p>
<p>[out:json]; relation(9456324); (._;&gt;;); out;</p>
<p>which then allowed me to download the GPS points as you describe. Perfect!</p>
</div>
<div id="comment-87209-info" class="comment-info">
<span class="comment-age">(02 May '23, 07:59)</span> <span class="comment-user userinfo">hjp23</span>
</div>
</div>
</div>
<div id="comment-tools-87206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87206-form-container" class="comment-form-container">
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

