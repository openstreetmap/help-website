+++
type = "question"
title = "maps with less data ?"
description = '''I would like to use OpenStreetMaps for a touristic panel, but there is too much information on it. Is there a way to click away too much info (like street names, buildings, etc....)'''
date = "2014-06-24T15:33:00Z"
lastmod = "2014-06-25T06:31:00Z"
weight = 34277
keywords = [ "deleteinfo" ]
aliases = [ "/questions/34277" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [maps with less data ?](/questions/34277/maps-with-less-data)

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
<span id="post-34277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34277-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to use OpenStreetMaps for a touristic panel, but there is too much information on it. Is there a way to click away too much info (like street names, buildings, etc....)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-deleteinfo" rel="tag" title="see questions tagged &#39;deleteinfo&#39;">deleteinfo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '14, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/07660b0400f70b099fd173458dc135b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iBeaken&#39;s gravatar image" />
<p><span>iBeaken</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iBeaken has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34277" class="comments-container">
<span id="34278"></span>
<div id="comment-34278" class="comment">
<div id="post-34278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you tried looking at one of the other layers (the Mapquest Open one, for example)?</p>
</div>
<div id="comment-34278-info" class="comment-info">
<span class="comment-age">(24 Jun '14, 16:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34279"></span>
<div id="comment-34279" class="comment">
<div id="post-34279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have, but I would like to have a map with less data. example : I would like to get rid of the names of the shops... and some street names. But it doesn't seem possible ?</p>
</div>
<div id="comment-34279-info" class="comment-info">
<span class="comment-age">(24 Jun '14, 16:25)</span> <span class="comment-user userinfo">iBeaken</span>
</div>
</div>
</div>
<div id="comment-tools-34277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34277-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="34280"></span>

<div id="answer-container-34280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34280-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The question is quite common and has been answered many times. What you want to do is not "remove data", but instead "display only what I want"</p>
<p>For a small area one of the best ways to do that is to use maperitive <a href="http://maperitive.net/">http://maperitive.net/</a> and modify one of the existing styles to do what you want, a bit more involved would be doing the same with TileMill.</p>
<p>A roughly generalized work flow is</p>
<pre><code>OSM data -&gt; renderer -&gt; output
                ^
                |
             map style</code></pre>
<p>Essentially what you are asking for is a point and click editor for a map style file, which I believe currently does not exist in OSM space.</p>
<p>A potential workaround might be to get the area you are interested in as SVG file (use the share button on openstreetmap.org) and edit that with your faviourite editor (for example Inkscape). I wouldn't however recommend that for anything except a small area.</p>
<p>In no circumstances should you try to remove data from the OSM database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '14, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '14, 00:21</strong> </span></p>
</div>
</div>
<div id="comments-container-34280" class="comments-container">
<span id="34288"></span>
<div id="comment-34288" class="comment">
<div id="post-34288-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have looked at all the different ways of 'display only what I want' - Maperitive is for PC (I'm using Mac), others involve coding (which I don't do), others just don't work or give text files with code...</p>
<p>If the question comes up regularly, isn't there a simple software that does the trick ?</p>
<p>Isn't there a way in OSM to 'simply' click out (google earth style) all the unnecessary info and get the 'basic map' ?</p>
</div>
<div id="comment-34288-info" class="comment-info">
<span class="comment-age">(24 Jun '14, 20:03)</span> <span class="comment-user userinfo">iBeaken</span>
</div>
</div>
<span id="34292"></span>
<div id="comment-34292" class="comment">
<div id="post-34292-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>unfortunately not, because OpenStreepMap is just a simple database with geographic data.</p>
<p>All the layout on openstreetmap.org is just one possibility among many how to display that data.</p>
<p>Maybe you can try <a href="http://umap.openstreetmap.fr">http://umap.openstreetmap.fr</a> ... it is said to be the most google-like OSM web service in these days.</p>
</div>
<div id="comment-34292-info" class="comment-info">
<span class="comment-age">(24 Jun '14, 21:45)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="34296"></span>
<div id="comment-34296" class="comment">
<div id="post-34296-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@iBeaken</span> I've expanded the answer a bit see above</p>
</div>
<div id="comment-34296-info" class="comment-info">
<span class="comment-age">(25 Jun '14, 00:18)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="34299"></span>
<div id="comment-34299" class="comment">
<div id="post-34299-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@iBeaken</span> "others involve coding" neither Maperitive nor TileMill requires programming (both require editing quite simple text files).</p>
</div>
<div id="comment-34299-info" class="comment-info">
<span class="comment-age">(25 Jun '14, 06:29)</span> <span class="comment-user userinfo">Bulwersator</span>
</div>
</div>
</div>
<div id="comment-tools-34280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34280-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34281"></span>

<div id="answer-container-34281" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34281-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please enter "own style" in the search box og this FAQ site.</p>
<p>There have been similar Questions and hints about your aim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '14, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-34281" class="comments-container">
&#10;</div>
<div id="comment-tools-34281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34281-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34298"></span>

<div id="answer-container-34298" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34298-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Companies like Mapbox or Cloudmade allows their customers to personalize their webmap. Tilemill shouldn't necessitate coding.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '14, 05:37</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-34298" class="comments-container">
&#10;</div>
<div id="comment-tools-34298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34298-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34300"></span>

<div id="answer-container-34300" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34300-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You may be more happy with Humanitaran layer - see <a href="http://www.openstreetmap.org/#map=13/50.2939/18.8325&amp;layers=H">http://www.openstreetmap.org/#map=13/50.2939/18.8325&amp;layers=H</a></p>
<p>It was designed as base layer for additional markers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '14, 06:31</strong></p>
<img src="https://secure.gravatar.com/avatar/fd2f7303e92334ed1eef75268aed7611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulwersator&#39;s gravatar image" />
<p><span>Bulwersator</span><br />
<span class="score" title="468 reputation points">468</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulwersator has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-34300" class="comments-container">
&#10;</div>
<div id="comment-tools-34300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34300-form-container" class="comment-form-container">
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

