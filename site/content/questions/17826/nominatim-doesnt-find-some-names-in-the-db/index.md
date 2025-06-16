+++
type = "question"
title = "nominatim doesn&#x27;t find some names in the DB"
description = '''Hello I hope you can help me with this.  I have nominatim V2 installed on a machine, and upload some OSM data that I created, so good, but I not understand why not search for all data. For example, in the database I have a polygon type &quot;place state&quot; with name: &quot;Antioquia&quot; but the search does not fin...'''
date = "2012-11-20T21:43:00Z"
lastmod = "2012-11-27T16:59:00Z"
weight = 17826
keywords = [ "search", "nominatim" ]
aliases = [ "/questions/17826" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim doesn't find some names in the DB](/questions/17826/nominatim-doesnt-find-some-names-in-the-db)

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
<span id="post-17826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17826-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I hope you can help me with this.</p>
<p>I have nominatim V2 installed on a machine, and upload some OSM data that I created, so good, but I not understand why not search for all data.</p>
<p>For example, in the database I have a polygon type "place state" with name: "Antioquia" but the search does not find, on the contrary the "place state" "valle del cauca" if found, then, nominatim not search all the names of the DB.</p>
<p>Example "Valle del cauca": <a href="http://201.245.166.77/nominatim/search?q=valle+del+cauca&amp;format=xml">http://201.245.166.77/nominatim/search?q=valle+del+cauca&amp;format=xml</a></p>
<p>Example for "antioquia" state: <a href="http://201.245.166.77/nominatim/search?q=antioquia&amp;format=xml">http://201.245.166.77/nominatim/search?q=antioquia&amp;format=xml</a></p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '12, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/8151a2cd9f1041f10b62d8ca446d3b2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alveniz&#39;s gravatar image" />
<p><span>alveniz</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alveniz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '12, 10:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-17826" class="comments-container">
&#10;</div>
<div id="comment-tools-17826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17826-form-container" class="comment-form-container">
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

<span id="17853"></span>

<div id="answer-container-17853" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17853-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The official nominatim instance finds both <a href="http://nominatim.openstreetmap.org/search.php?q=valle+del+cauca">valle de cauca</a> and <a href="http://nominatim.openstreetmap.org/search.php?q=Antioquia">antioquia</a>, so the problem must be with your setup.</p>
<p>The first thing that springs to mind is that the data for that region is not properly loaded. Can you find other placenames near (or in) Antioquia ? Does your data extract emcompass the whole of Antioquia, plus some margin ? Can you setup a slippymap using you data and verify that Antioquia gets rendered ? Does the data import procedure report some errors ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '12, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-17853" class="comments-container">
<span id="17869"></span>
<div id="comment-17869" class="comment">
<div id="post-17869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello</p>
<p>Thanks for the reply, and excuse my English.</p>
<ol>
<li><p>Yes, I find places in "Antioquia", example: the city of <a href="http://201.245.166.77/nominatim/search?q=envigado&amp;format=xml">Envigado</a>, the County of <a href="http://201.245.166.77/nominatim/search?q=sabaneta&amp;format=xml">Sabaneta</a>, but no details of Antioquia state.</p></li>
<li><p>In the database there is a state "Antioquia", attached images with table and the polygon in gvSIG.</p></li>
</ol>
<p><img src="/upfiles/screenshot_1.png" alt="alt text" /></p>
<p><img src="/upfiles/screenshot2.png" alt="alt text" /></p>
</div>
<div id="comment-17869-info" class="comment-info">
<span class="comment-age">(21 Nov '12, 17:02)</span> <span class="comment-user userinfo">alveniz</span>
</div>
</div>
<span id="17878"></span>
<div id="comment-17878" class="comment">
<div id="post-17878-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to check the placex table for your data. If it is in the place table but not in placex, then your geometry is broken. In that case, the table import_polygon_error will contain an entry that tells you where the error is.</p>
</div>
<div id="comment-17878-info" class="comment-info">
<span class="comment-age">(21 Nov '12, 20:58)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="18034"></span>
<div id="comment-18034" class="comment">
<div id="post-18034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Lonvia, I check the placex table, My placex is 50% the size of place, and the table import_polygon_error is empty. I do not think either geometry, because if I import only that state there is no error. Do you have another idea?</p>
</div>
<div id="comment-18034-info" class="comment-info">
<span class="comment-age">(27 Nov '12, 16:59)</span> <span class="comment-user userinfo">alveniz</span>
</div>
</div>
</div>
<div id="comment-tools-17853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17853-form-container" class="comment-form-container">
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

