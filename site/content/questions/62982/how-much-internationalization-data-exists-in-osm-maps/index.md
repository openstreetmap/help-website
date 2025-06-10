+++
type = "question"
title = "How much internationalization data exists in OSM maps?"
description = '''Hi, I work at Wikimedia. We&#x27;re about to launch a project that, among other things, will let users display maps on Wikipedia and other wiki projects in the local language of the wiki (instead of the language of the territory mapped). But our maps are based on OSM, so what our users will actually see ...'''
date = "2018-04-11T23:42:00Z"
lastmod = "2018-04-12T07:22:00Z"
weight = 62982
keywords = [ "internationalization", "language" ]
aliases = [ "/questions/62982" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How much internationalization data exists in OSM maps?](/questions/62982/how-much-internationalization-data-exists-in-osm-maps)

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
<span id="post-62982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62982-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I work at Wikimedia. We're about to <a href="https://www.mediawiki.org/wiki/Map_improvements_2018">launch a project</a> that, among other things, will let users display maps on Wikipedia and other wiki projects in the local language of the wiki (instead of the language of the territory mapped). But our maps are based on OSM, so what our users will actually see will depend on how much internationalization data OSM has. I don't want to oversell this feature to our users and then have them be disappointed, so I am trying to figure out how extensively OSM maps are translated.</p>
<ul>
<li>In your experience, how much translation does OSM have? Is it just major city and country names and a few tourist attractions? Or does it go much further?</li>
<li>Is there any way to get a data readout on this? E.g., is there, perhaps, a dashboard someplace with stats or graphs?</li>
<li>Is there a way I can preview how various maps would look in a different language? Changing my "preferred language" setting on openstreetmap.org doesn't change the map display. I see that I can click on individual map features and look for translations, but this is time consuming. Is there a more general way? And is openstreetmap.org actually showing everything it has?</li>
</ul>
<p>Thanks so much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-internationalization" rel="tag" title="see questions tagged &#39;internationalization&#39;">internationalization</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '18, 23:42</strong></p>
<img src="https://secure.gravatar.com/avatar/566a85d0ce0e3d4f3fd84a60667cc657?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmatazzoni&#39;s gravatar image" />
<p><span>jmatazzoni</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmatazzoni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62982" class="comments-container">
&#10;</div>
<div id="comment-tools-62982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62982-form-container" class="comment-form-container">
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

<span id="62984"></span>

<div id="answer-container-62984" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62984-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-62984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One way to see what's available is to put a query like <code>name:en=*</code> into the <a href="http://overpass-turbo.eu/">Overpass Turbo</a> Wizard. That will show anything with an English name added in addition to the local name.</p>
<p>You can also <a href="http://overpass-turbo.eu/s/xOC">slightly modify</a> the query to be a little quicker (downloads the center of area features instead of the geometry). <a href="http://overpass-turbo.eu/s/xOD">Or use a catchall</a>.</p>
<p>For the most part there aren't all that many multilingual names. There's been a choice not to catalogue names that are just translations and transliterations and try to stick to names that are actually used in a language. So in areas where multiple languages are used, many objects will have several names, but in other areas it's likely that the name in the local language will be the only one available.</p>
<p>There's actually been quite a bit of work to add Wikidata ids to places with the idea that translations can then be pulled from the Wikidata entries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '18, 01:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '18, 02:48</strong> </span></p>
</div>
</div>
<div id="comments-container-62984" class="comments-container">
&#10;</div>
<div id="comment-tools-62984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62984-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62985"></span>

<div id="answer-container-62985" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62985-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-62985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Extending on what <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> wrote, it is important to note that we don't do translations in OSM data, at all. We do record if an object has different names in different languages, but we do not attempt to "translate" something into different languages. The same is true for machine-generated transliterations; we would only ever add transliterations that have their own standing as a name, but <em>not</em> auto-generated transliterations. Which does not mean that you cannot make a map that displays transliterations (suggested viewing: <a href="https://av.tib.eu/media/20287">https://av.tib.eu/media/20287</a> "Towards a more readable Openstreetmap based world map for westerners" by the guy who makes the openstreetmap.de map).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '18, 07:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62985" class="comments-container">
&#10;</div>
<div id="comment-tools-62985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62985-form-container" class="comment-form-container">
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

