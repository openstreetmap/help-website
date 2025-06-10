+++
type = "question"
title = "How to setup Localised maps"
description = '''I&#x27;m currently looking into using OSM as a replacement for Google maps. I&#x27;ve setup a vanilla tile-server using Postgres, Mapnik &amp;amp; OpenLayers, but still have one major obstacle to overcome, localisation. I want to be able to offer a map where the user (or app) can specify which set of name transla...'''
date = "2012-04-07T19:19:00Z"
lastmod = "2012-04-07T21:29:00Z"
weight = 11796
keywords = [ "osm2pgsql", "mapnik", "localization" ]
aliases = [ "/questions/11796" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to setup Localised maps](/questions/11796/how-to-setup-localised-maps)

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
<span id="post-11796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11796-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently looking into using OSM as a replacement for Google maps. I've setup a vanilla tile-server using Postgres, Mapnik &amp; OpenLayers, but still have one major obstacle to overcome, localisation.</p>
<p>I want to be able to offer a map where the user (or app) can specify which set of name translations they need. I've searched online for this, and have seen the experimental locale maps, but was wondering what i need to do to get this running on my local server.</p>
<p>I've looked at the imported postgres db structure and see that this has only a name it, which i assume is the default. I've used osm2pgsql to import the data, so it's presumably this step where i would need to specify which locale i would like to over-ride the default name if it exists.</p>
<p>If i wanted to offer maps with 4 translations, would i really need to setup 4 x full planet_osm databases, or is there a more optimal way of setting this up?</p>
<p>Any help much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-localization" rel="tag" title="see questions tagged &#39;localization&#39;">localization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '12, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/9ef4e665e6e82f6b5f08952ff8c69d23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Perrin&#39;s gravatar image" />
<p><span>John Perrin</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Perrin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11796" class="comments-container">
&#10;</div>
<div id="comment-tools-11796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11796-form-container" class="comment-form-container">
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

<span id="11797"></span>

<div id="answer-container-11797" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11797-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could create map tiles with no names on them. Then create overlays with the names on in each language you want to display. It would be possible to extend it too. Displaying overlays of mostly transparent tiles with names on using OpenLayers (or LeafletJS) is straightforward.</p>
<p>The planet_osm database could be created with osm2pgsql to have all four names in a single database and render the respective name onto the respective tile layer or overlay layer. You will need to modify the import style to include the translations you want to import.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '12, 20:48</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-11797" class="comments-container">
&#10;</div>
<div id="comment-tools-11797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11797-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11798"></span>

<div id="answer-container-11798" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11798-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You do not have to have a database for each language. You can specify the database scheme in the <em>.style</em> file that osm2pgsql uses. So you can have several name columns in the table, one for each language.</p>
<p>You can also have the lables in a transparant overlay to save the renderer having to render the same features for different languages. One example of this is at <a href="http://toolserver.org/~osm/locale/">toolserver.org</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '12, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11798" class="comments-container">
<span id="11800"></span>
<div id="comment-11800" class="comment">
<div id="post-11800-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, after looking into the style file on the wiki i found the following page: <a href="http://wiki.openstreetmap.org/wiki/Regionalisedmap">http://wiki.openstreetmap.org/wiki/Regionalisedmap</a></p>
<p>This mirrors what you and ChrisH are saying, i'll look into this further. Do you know if there any example mapnik style-sheets that just render names?</p>
</div>
<div id="comment-11800-info" class="comment-info">
<span class="comment-age">(07 Apr '12, 21:29)</span> <span class="comment-user userinfo">John Perrin</span>
</div>
</div>
</div>
<div id="comment-tools-11798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11798-form-container" class="comment-form-container">
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

