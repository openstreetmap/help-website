+++
type = "question"
title = "How to hide all labels of OSM"
description = '''Hi everyone. Now I&#x27;m using Openlayers to integrate Openstreetmap into my web. Besides, I want to hide/remove all the labels on map(country,city,road,lake....). How can I do that without establishing my own Web Map Server? Thank you every much !'''
date = "2015-01-28T18:24:00Z"
lastmod = "2015-01-28T19:50:00Z"
weight = 40664
keywords = [ "nolabels", "style", "hide", "label" ]
aliases = [ "/questions/40664" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to hide all labels of OSM](/questions/40664/how-to-hide-all-labels-of-osm)

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
<span id="post-40664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40664-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone. Now I'm using Openlayers to integrate Openstreetmap into my web. Besides, I want to hide/remove all the labels on map(country,city,road,lake....). How can I do that without establishing my own Web Map Server? Thank you every much !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nolabels" rel="tag" title="see questions tagged &#39;nolabels&#39;">nolabels</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-hide" rel="tag" title="see questions tagged &#39;hide&#39;">hide</span> <span class="post-tag tag-link-label" rel="tag" title="see questions tagged &#39;label&#39;">label</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '15, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/47f7403c08fb9de3f0c16294c794747e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snowangel912&#39;s gravatar image" />
<p><span>snowangel912</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snowangel912 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '15, 19:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40664" class="comments-container">
&#10;</div>
<div id="comment-tools-40664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40664-form-container" class="comment-form-container">
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

<span id="40665"></span>

<div id="answer-container-40665" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40665-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately you can't, because the labels are rendered into the tiles that you're displaying.</p>
<p>Unless you can find a public source of tiles without labels, of course ... which turned out to be rather simpler than expected (see comment below). Here's an example:</p>
<p><a href="http://c.tiles.wmflabs.org/osm-no-labels/10/549/335.png">http://c.tiles.wmflabs.org/osm-no-labels/10/549/335.png</a></p>
<p>You should be able to figure out everything you need from that.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '15, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '15, 19:52</strong> </span></p>
</div>
</div>
<div id="comments-container-40665" class="comments-container">
<span id="40667"></span>
<div id="comment-40667" class="comment">
<div id="post-40667-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Well, a public source are those <a href="http://mc.bbbike.org/mc/?lon=13.368594&amp;lat=52.459748&amp;zoom=10&amp;num=2&amp;mt0=osm-no-labels&amp;mt1=mapnik&amp;marker=">"no labels" tiles</a> from wmflabs.org (Wikimedia).</p>
<p>I guess it is okay to use them for a small private website, but please check their(!) tile usage policy (example: <span>osm.org's tile usage policy</span>) if you plan to use them with more than a few accesses. Also check under which license they are distributed (in any case you need to attribute OSM <span>correctly</span>, too)</p>
</div>
<div id="comment-40667-info" class="comment-info">
<span class="comment-age">(28 Jan '15, 19:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40668"></span>
<div id="comment-40668" class="comment">
<div id="post-40668-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>you can also do a keyword search on this FAQ site about "label", "no label" or "without label" ... there are some topics.</p>
</div>
<div id="comment-40668-info" class="comment-info">
<span class="comment-age">(28 Jan '15, 19:18)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="40669"></span>
<div id="comment-40669" class="comment">
<div id="post-40669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> thanks - I had no idea those still existed, I thought that the WM labs stuff (like the multilanguage stuff, which found a new home) had all gone.</p>
</div>
<div id="comment-40669-info" class="comment-info">
<span class="comment-age">(28 Jan '15, 19:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40665-form-container" class="comment-form-container">
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

