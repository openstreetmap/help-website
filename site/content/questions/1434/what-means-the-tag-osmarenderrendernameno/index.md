+++
type = "question"
title = "What means the tag &quot;osmarender:renderName=no&quot; ?"
description = '''I find sometimes this tag attached to highways. I interpret this tag as a hint for the Osmarender rendering application. Even though it is not really tagging for the renderer, I found some cases where a highway is split just to not display the name on some part of the street. Is that acceptable to a...'''
date = "2010-11-03T18:50:00Z"
lastmod = "2011-02-27T15:57:00Z"
weight = 1434
keywords = [ "name", "osmarender" ]
aliases = [ "/questions/1434" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [What means the tag "osmarender:renderName=no" ?](/questions/1434/what-means-the-tag-osmarenderrendernameno)

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
<span id="post-1434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1434-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I find sometimes this tag attached to highways. I interpret this tag as a hint for the <a href="https://wiki.openstreetmap.org/wiki/Osmarender">Osmarender</a> rendering application. Even though it is not really <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>, I found some cases where a highway is split just to not display the name on some part of the street. Is that acceptable to add tags helping rendering and is it correct to split an OSM way just to improve the rendering results ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-osmarender" rel="tag" title="see questions tagged &#39;osmarender&#39;">osmarender</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '10, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '11, 14:52</strong> </span></p>
</div>
</div>
<div id="comments-container-1434" class="comments-container">
<span id="1437"></span>
<div id="comment-1437" class="comment">
<div id="post-1437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please specify, is what correct?: - your interpretation "I interpret this tag..." or - special tagging using the the tag in question</p>
<p>I would be nervous about a question re "correct" tagging because from my initial reading about OSM concepts I understand that there are helpful conventions but no such thing as "incorrect" tagging.</p>
</div>
<div id="comment-1437-info" class="comment-info">
<span class="comment-age">(03 Nov '10, 20:24)</span> <span class="comment-user userinfo">Screentoosmall</span>
</div>
</div>
</div>
<div id="comment-tools-1434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1434-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="1439"></span>

<div id="answer-container-1439" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1439-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pieren has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes this tag is used to tell osmarender to not render the name for this object. Interestingly enough not only osmarender observes this tag but mapnik does too. However it should only be used as a very last resort as OpenStreetMap is not primarily focused on the creation of nice looking map tiles but on the collection of a database containing geographical informations.</p>
<p>In my opinion this tag should only be used in local copies of OpenStreetMap data which you tweak for rendering and never be uploaded to the main database.</p>
<p>Splitting ways to suppress name tags is a form of "tagging for the renderer" and should be avoided.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '10, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-1439" class="comments-container">
<span id="1448"></span>
<div id="comment-1448" class="comment">
<div id="post-1448-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>mapnik doesn't know this tag. I've searched the code for both the stylesheets and osm2pgsql, and neither of them mention the tag anywhere.</p>
</div>
<div id="comment-1448-info" class="comment-info">
<span class="comment-age">(04 Nov '10, 10:07)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-1439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1439-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1435"></span>

<div id="answer-container-1435" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1435-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It not even tag for render, it's tagging for one renderer !</p>
<p>There is no relay hint in OSM tagging schema for renderer. But OSM is not a place where fan of each renderer can add tag for it favorite engine. OSM data base is a geographic data base.</p>
<p>You can even found some svg conversion hint like svg:bezier key...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '10, 19:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0ca0ed82dfebe8539147e56d695aecfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frodrigo&#39;s gravatar image" />
<p><span>frodrigo</span><br />
<span class="score" title="674 reputation points">674</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frodrigo has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-1435" class="comments-container">
<span id="1443"></span>
<div id="comment-1443" class="comment">
<div id="post-1443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is actually wrong as mapnik knows about this tag too.</p>
</div>
<div id="comment-1443-info" class="comment-info">
<span class="comment-age">(04 Nov '10, 08:40)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="3413"></span>
<div id="comment-3413" class="comment">
<div id="post-3413-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>as Andy Allan stated above: Mapnik doesn't interpret this tag (I confirm this as I checked as well). On the other hand, telling the "renderer" that a way should be converted to a curve (svg:bezier) has few to do with rendering, it is besides the rendering a general statement that a way is curved instead of being polygonal (so it is actually a map datum), the only thing to criticize in this context might be the naming of the tag.</p>
</div>
<div id="comment-3413-info" class="comment-info">
<span class="comment-age">(27 Feb '11, 15:57)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-1435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1435-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3383"></span>

<div id="answer-container-3383" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3383-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-3383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can see how this tag may be useful in certain, limited and specific contexts. For example, complex intersections on two-way roads that have ramps or teapot handles, which would result in many breaks in ways to contain the turn restrictions that Osmarender would otherwise try to label.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '11, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-3383" class="comments-container">
&#10;</div>
<div id="comment-tools-3383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3383-form-container" class="comment-form-container">
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

