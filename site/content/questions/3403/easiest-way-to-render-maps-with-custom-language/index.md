+++
type = "question"
title = "Easiest way to render maps with custom language?"
description = '''I&#x27;m looking to make maps for printing, but would need to have all names in english since some of our staff don&#x27;t read arabic. I&#x27;ve looked around online, but I haven&#x27;t found any (sufficiently easy) way of achieving this, and would really appreciate some pointers on which way to go. I&#x27;ve dabbled with ...'''
date = "2011-02-27T08:48:00Z"
lastmod = "2011-02-27T20:05:00Z"
weight = 3403
keywords = [ "maperetive", "rendering", "language" ]
aliases = [ "/questions/3403" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Easiest way to render maps with custom language?](/questions/3403/easiest-way-to-render-maps-with-custom-language)

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
<span id="post-3403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3403-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking to make maps for printing, but would need to have all names in english since some of our staff don't read arabic.</p>
<p>I've looked around online, but I haven't found any (sufficiently easy) way of achieving this, and would really appreciate some pointers on which way to go.</p>
<p>I've dabbled with different renderers, but the only one I've achieved a decent worklflow with is Maperetive. I run WinXP and have little experience with nix-commandline environments.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maperetive" rel="tag" title="see questions tagged &#39;maperetive&#39;">maperetive</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '11, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/df2fd17be9ca696157dcaa547d6ca98e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="riyaah&#39;s gravatar image" />
<p><span>riyaah</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="riyaah has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3403" class="comments-container">
&#10;</div>
<div id="comment-tools-3403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3403-form-container" class="comment-form-container">
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

<span id="3418"></span>

<div id="answer-container-3418" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3418-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="riyaah has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You say you've tried Maperitive, but you don't explain why it didn't fit your needs. Making Maperitive render English names is really quite simple: add a new line in the default rules (under the "properties" section):</p>
<pre><code>text : @any([[name:en]], int_name, name)</code></pre>
<p>(make sure it's a tab indent and not spaces). This will ensure English names will be used as default ones (but you can override this in any rule later). If English name is not defined, it will look for international name or a default name (which would probably be in Arabic).</p>
<p><a href="http://maperitive.net/docs/manual/Properties/Text.html"></a><a href="http://maperitive.net/docs/manual/Properties/Text.html"></a><a href="http://maperitive.net/docs/manual/Properties/Text.html">http://maperitive.net/docs/manual/Properties/Text.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '11, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '11, 19:36</strong> </span></p>
</div>
</div>
<div id="comments-container-3418" class="comments-container">
<span id="3419"></span>
<div id="comment-3419" class="comment">
<div id="post-3419-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To improve this, you could additionally render int_name if name:en is empty.</p>
</div>
<div id="comment-3419-info" class="comment-info">
<span class="comment-age">(27 Feb '11, 17:32)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="3421"></span>
<div id="comment-3421" class="comment">
<div id="post-3421-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I don't know why I didn't see this in the Maperetive book, I looked around for quite a while!</p>
</div>
<div id="comment-3421-info" class="comment-info">
<span class="comment-age">(27 Feb '11, 17:54)</span> <span class="comment-user userinfo">riyaah</span>
</div>
</div>
<span id="3428"></span>
<div id="comment-3428" class="comment">
<div id="post-3428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@dieterdreist</span> good suggestion, I've updated my answer</p>
</div>
<div id="comment-3428-info" class="comment-info">
<span class="comment-age">(27 Feb '11, 19:37)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
</div>
<div id="comment-tools-3418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3418-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3429"></span>

<div id="answer-container-3429" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3429-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option would be to preprocess the data using <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> with the <a href="http://wiki.openstreetmap.org/wiki/Osmosis/TagTransform">TagTransform</a> plugin. eg you could write rules to copy anything in the name:en or int_name tag to the name tag.</p>
<p>This can output in .osm format, which you can then use as input for any of the usual rendering software (Maperitive, Mapnik, Mkgmap etc), and you don't have to change any of the rendering rules.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '11, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-3429" class="comments-container">
&#10;</div>
<div id="comment-tools-3429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3416"></span>

<div id="answer-container-3416" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3416-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can tell you for mapnik: simply update your tables. First overwrite the name field in your database with int_name if it is not empty, this is a fallback:</p>
<p>UPDATE planet_osm_point SET name=int_name WHERE int_name IS NOT NULL;</p>
<p>then overwrite again with name:en where present:</p>
<p>UPDATE planet_osm_point SET name="name:en" WHERE "name:en" IS NOT NULL;</p>
<p>in order to be able to do this, you will have to add int_name and name:en before importing to standard.style in your osm2pgsql-folder. If you want to keep the original name field content you would have to make a copy of the column before (but your question doesn't sound like). Repeat this command for all 4 relevant tables (point, polygon, line, roads). Afterwards you might want to delete the now obsolete columns name_int and name:en to save space.</p>
<p>This procedure is the simplest (especially if you are not planning to apply diffs) but of course you could also modify your rendering rules for every occurence of name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '11, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-3416" class="comments-container">
<span id="3422"></span>
<div id="comment-3422" class="comment">
<div id="post-3422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Personally, I would tend to add views using CASE WHEN or COALESCE statements (e.g., CREATE VIEW osm_planet_way_nameen AS SELECT a.*, CASE WHEN ... FROM osm_planet_way). It is not hugely difficult to d global search and replace for this type of change in the mapnik XML. I would also use the hstore option on osm2pgsql to make all tags available during the load. In this way the data can be refreshed without having to repeat DML statements like UPDATE.</p>
</div>
<div id="comment-3422-info" class="comment-info">
<span class="comment-age">(27 Feb '11, 18:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-3416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3416-form-container" class="comment-form-container">
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

