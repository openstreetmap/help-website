+++
type = "question"
title = "Is it possible to create my individual layer?"
description = '''Is it possible to create my own individual layer in OSM, where my partners and I can create objects like POIs and road paths? The created objects should be saved/locked from the unauthorized changes. Such layer could be visible (but not changeable) by every user of OSM. If I can`t lock the created s...'''
date = "2011-08-05T11:11:00Z"
lastmod = "2011-08-10T13:11:00Z"
weight = 6905
keywords = [ "lock", "layer" ]
aliases = [ "/questions/6905" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to create my individual layer?](/questions/6905/is-it-possible-to-create-my-individual-layer)

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
<span id="post-6905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6905-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to create my own individual layer in OSM, where my partners and I can create objects like POIs and road paths? The created objects should be saved/locked from the unauthorized changes. Such layer could be visible (but not changeable) by every user of OSM.</p>
<p>If I can`t lock the created street objects in general OSM network, is it possible to create my own thematic layer in which I will create the objects for the internal authorized changes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lock" rel="tag" title="see questions tagged &#39;lock&#39;">lock</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '11, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/9408e968b4ce3d8ccd727d1600981d77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnZem&#39;s gravatar image" />
<p><span>AnZem</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnZem has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '11, 12:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-6905" class="comments-container">
&#10;</div>
<div id="comment-tools-6905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6905-form-container" class="comment-form-container">
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

<span id="6906"></span>

<div id="answer-container-6906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6906-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-6906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't do this using the main OSM servers, but you can run your own servers to do this.</p>
<p>Everything in OpenStreetMap is editable by everyone, and if you have some data which you don't want to be edited by anyone else, it shouldn't go in the main OSM database.</p>
<p>What you can do is set up your own instance of the <a href="http://wiki.openstreetmap.org/wiki/The_Rails_Port">"Rails Port"</a>, the software running on the OSM servers and use the same editors and rendering tools as OSM.</p>
<p>Also, you need to consider OSM's licence, which says that if you publish anything made from a combination of your own data and OSM data, the whole work must be under OSM's license.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '11, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '11, 18:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-6906" class="comments-container">
&#10;</div>
<div id="comment-tools-6906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6914"></span>

<div id="answer-container-6914" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6914-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-6914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"my partners and I" suggests you might need a collaboration platform which might mean installing your own instance of <a href="http://wiki.openstreetmap.org/wiki/The_Rails_Port">the rails port</a> (fairly complicated)</p>
<p>A simpler small-scale solution might be to have a play around with <a href="http://wiki.openstreetmap.org/wiki/JOSM">JOSM</a>, which allows you to edit the data offline, and save your changes offline away from the main OSM database. You can also do this with separate layer of newly added data if you wish. That's all very easy, but then maybe the challenge comes with <em>using</em> that data.</p>
<p>Depending on what kind of "thematic layer" we're talking about You might achieve what you want with a web map display and some markers. If you want to see your new data on a rendered map then you've either got to share the data with the rest of us and see it rendered on OpenStreetMap, or run your own rendering software.</p>
<p>You know authorisation is overrated. Just share your data with OpenStreetMap. We promise not to break it :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '11, 16:14</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-6914" class="comments-container">
<span id="6999"></span>
<div id="comment-6999" class="comment">
<div id="post-6999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tank you, for the so quick answers!</p>
<p>I am absolutely inexperienced in the OSM service and will be very appreciative if you will explain me the answers (my questions in the letter body).</p>
<p>"my partners and I" suggests you might need a collaboration platform which might mean installing your own instance of the rails port (fairly complicated)" You mean that I have to organize my own web-server on which will be stored my own created road data and this layer will be independent from the OSM data, I will use the OSM only like the base reference map. Am I right?</p>
</div>
<div id="comment-6999-info" class="comment-info">
<span class="comment-age">(10 Aug '11, 13:11)</span> <span class="comment-user userinfo">AnZem</span>
</div>
</div>
<span id="7000"></span>
<div id="comment-7000" class="comment">
<div id="post-7000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"A simpler small-scale solution might be to have a play around with JOSM, which allows you to edit the data offline, and save your changes offline away from the main OSM database." As I understand, this solution can be used only for the internal usage on the one computer (offline)? But in my case, the data have to be updated by different organizations located in the different countries (online service). It will not be a problem if all OSM users will see my data; but only limited users should have the possibility to change the data.</p>
</div>
<div id="comment-7000-info" class="comment-info">
<span class="comment-age">(10 Aug '11, 13:11)</span> <span class="comment-user userinfo">AnZem</span>
</div>
</div>
<span id="7001"></span>
<div id="comment-7001" class="comment">
<div id="post-7001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"You can also do this with separate layer of newly added data if you wish. That's all very easy, but then maybe the challenge comes with using that data." Does it mean that I have the possibility to create my own internal layer with limited access directly on the OSM service? Or I have to make the some agreement with OSM owners to make such layer on their side? How do you think, which way is more realistic?</p>
</div>
<div id="comment-7001-info" class="comment-info">
<span class="comment-age">(10 Aug '11, 13:11)</span> <span class="comment-user userinfo">AnZem</span>
</div>
</div>
</div>
<div id="comment-tools-6914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6914-form-container" class="comment-form-container">
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

