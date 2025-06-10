+++
type = "question"
title = "JOSM MapPaint style that shows/renders the age/&quot;last modified&quot; for objects?"
description = '''I&#x27;m looking at an area and I see some roughly drawn buildings, and I&#x27;m going through them one by one seeing which I can improve. Many were mapped in 2011, and we have better aerial imagery now. However I have to manually open up the history window to confirm this. It would be much easier if I could ...'''
date = "2017-01-16T20:27:00Z"
lastmod = "2017-04-11T21:46:00Z"
weight = 54088
keywords = [ "josm", "map_paint_style" ]
aliases = [ "/questions/54088" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM MapPaint style that shows/renders the age/"last modified" for objects?](/questions/54088/josm-mappaint-style-that-showsrenders-the-agelast-modified-for-objects)

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
<span id="post-54088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking at an area and I see some roughly drawn buildings, and I'm going through them one by one seeing which I can improve. Many were mapped in 2011, and we have better aerial imagery now. However I have to manually open up the history window to confirm this.</p>
<p>It would be much easier if I could enable a MapPaint style in JOSM which would render how old an object is. Some little text on/beside objects which shows the age/year of last modification.</p>
<p>Does such a JOSM style exist?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-map_paint_style" rel="tag" title="see questions tagged &#39;map_paint_style&#39;">map_paint_style</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '17, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Dec '18, 15:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-54088" class="comments-container">
&#10;</div>
<div id="comment-tools-54088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54088-form-container" class="comment-form-container">
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

<span id="54090"></span>

<div id="answer-container-54090" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54090-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>workaround: what about using Time-dependent JOSM search parameters? see <a href="https://wiki.openstreetmap.org/wiki/JOSM/Search_function#Time-dependent">https://wiki.openstreetmap.org/wiki/JOSM/Search_function#Time-dependent</a></p>
<p>Search for <code>type:node timestamp:/2012-01-01</code> and see which nodes are selected then. I guess that with some advanced syntax one also could only search nodes which belong to a building.</p>
<p>The list of available map styles is at <a href="https://josm.openstreetmap.de/wiki/Styles">https://josm.openstreetmap.de/wiki/Styles</a> (or inside your JOSM).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '17, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jan '17, 20:57</strong> </span></p>
</div>
</div>
<div id="comments-container-54090" class="comments-container">
&#10;</div>
<div id="comment-tools-54090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54090-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55569"></span>

<div id="answer-container-55569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55569-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no mappaint style. Afaik it is not possible to read the timestamp via mapcss atm. However you could try this plugin: <a href="https://github.com/Rub21/osm-obj-info">https://github.com/Rub21/osm-obj-info</a> It displays the timestamp of the selected object.</p>
<p>Note that this is always the date when the object was last modified. You can't see the date of first creation as this would require to download the full history of every object. (Which is done when displaying the history window CTRL+H)</p>
<p>Also note that if someone adjusts the shape of a building usually only the nodes are touched and this will not be reflected in the history of the way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '17, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/b904d75b8ea950f64710d2a8303cead7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klumbumbus&#39;s gravatar image" />
<p><span>Klumbumbus</span><br />
<span class="score" title="543 reputation points">543</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klumbumbus has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-55569" class="comments-container">
<span id="55570"></span>
<div id="comment-55570" class="comment">
<div id="post-55570-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, a bit hacky mappaint style could be realized via the josm serch function, e.g.:</p>
<p>way[JOSM_search("timestamp:/2013")] { width: 3; color: red; }</p>
<p>display all ways with old last modification date in red. could be extended for nodes too. for mapcss syntax see <a href="https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation">https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation</a></p>
</div>
<div id="comment-55570-info" class="comment-info">
<span class="comment-age">(11 Apr '17, 21:46)</span> <span class="comment-user userinfo">Klumbumbus</span>
</div>
</div>
</div>
<div id="comment-tools-55569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55569-form-container" class="comment-form-container">
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

