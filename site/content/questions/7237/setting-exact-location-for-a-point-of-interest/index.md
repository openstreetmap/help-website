+++
type = "question"
title = "Setting exact location for a Point of Interest"
description = '''On holiday, I marked with my Garmin some points of interest - ancient monuments, associated car parking. I&#x27;ve added one of these to Open Streetmap. Surely I should be able to use the coordinates recorded on the Garmin to set the exact location of my POI but I can&#x27;t see how to do it. Help, please? Da...'''
date = "2011-08-21T12:12:00Z"
lastmod = "2018-08-03T15:52:00Z"
weight = 7237
keywords = [ "point", "exact", "location", "interest", "poi" ]
aliases = [ "/questions/7237" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Setting exact location for a Point of Interest](/questions/7237/setting-exact-location-for-a-point-of-interest)

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
<span id="post-7237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7237-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On holiday, I marked with my Garmin some points of interest - ancient monuments, associated car parking.</p>
<p>I've added one of these to Open Streetmap. Surely I should be able to use the coordinates recorded on the Garmin to set the exact location of my POI but I can't see how to do it.</p>
<p>Help, please?</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span> <span class="post-tag tag-link-exact" rel="tag" title="see questions tagged &#39;exact&#39;">exact</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-interest" rel="tag" title="see questions tagged &#39;interest&#39;">interest</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '11, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/3407c124dac612d0b9f046f50bf63c6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flightmaker&#39;s gravatar image" />
<p><span>flightmaker</span><br />
<span class="score" title="226 reputation points">226</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flightmaker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7237" class="comments-container">
&#10;</div>
<div id="comment-tools-7237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7237-form-container" class="comment-form-container">
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

<span id="7238"></span>

<div id="answer-container-7238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7238-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The JOSM editor has an option called "add node" in the "tools" menu that lets you specify an exact location for a new node, but you cannot move an existing node to an exact location (other than manually moving it and watching the coordinate display while you do).</p>
<p>It is possible to work around this using the following procedure (in JOSM):</p>
<ul>
<li>load OSM data for region of interest</li>
<li>move existing node just a little</li>
<li>save data as .osm file, close JOSM</li>
<li>open .osm file in text editor, find node (search for "action='modify'"), change location in XML, save file</li>
<li>open JOSM, load file from disk, upload to OSM.</li>
</ul>
<p>Another, slightly less complicated, option is to use the <a href="http://wiki.openstreetmap.org/wiki/RawEditor">OSM Raw Editor</a> (which will nonetheless require that you edit XML code by hand, but it does so in a browser window).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '11, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7238" class="comments-container">
<span id="7239"></span>
<div id="comment-7239" class="comment">
<div id="post-7239-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Also keep in mind that it doesn't make sense to move the node if it is already correct within a meter or two. Your GPS is most likely no more precise than that.</p>
</div>
<div id="comment-7239-info" class="comment-info">
<span class="comment-age">(21 Aug '11, 13:05)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-7238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7238-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7240"></span>

<div id="answer-container-7240" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7240-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you've marked waypoints on your Garmin, and you upload the trace to OSM, you can also add the waypoints to OSM directly in the Potlatch 2 online editor. Have a look at <a href="http://www.openstreetmap.org/user/SomeoneElse/traces/1056198">this trace</a> - if you edit the area and zoom in you'll see an orange dot where a waypoint was marked in the middle. To convert it to a node, "alt-click" on it, select "advanced" mode in Potlatch and add any necessary tags (and remove any Garmin ones that don't belong in OSM, such as "cmt" and "extensions").</p>
<p>With Potlatch 2, this works provided the node isn't under an existing OSM way</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '11, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-7240" class="comments-container">
<span id="7246"></span>
<div id="comment-7246" class="comment">
<div id="post-7246-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah interesting. Potlatch 1 used to ignore any waypoints contained within GPX files. This is quite a useful feature.</p>
</div>
<div id="comment-7246-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 05:24)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
<span id="7251"></span>
<div id="comment-7251" class="comment">
<div id="post-7251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Potlatch 1 doesn't ignore waypoints for me - trying editing the "this trace" link above with it and you'll see an orange dot for the waypoint.</p>
<p>Potlatch 1 actually has a couple of advantages over Potlatch 2 as far as waypoint handling goes - see trac 3669 and <a href="http://help.openstreetmap.org/questions/2355/waypoint-handling-in-potlatch-2">http://help.openstreetmap.org/questions/2355/waypoint-handling-in-potlatch-2</a></p>
</div>
<div id="comment-7251-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 10:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7240-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7242"></span>

<div id="answer-container-7242" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7242-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your garmin can be set to lat long degrees mode (etrex can) the marks recorded will be easy to plot in potlach 2. In edit mode there is an "option box" drop down menu box to show the lat long of mouse pointer which you tick. this works ok for the odd point but the answers above are neater for bigger jobs. For best accuracy the etrex and some other models can average the point with a number of readings. you can also view the error on the screen in some modes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '11, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-7242" class="comments-container">
<span id="7372"></span>
<div id="comment-7372" class="comment">
<div id="post-7372-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That one works for me, for what I need to do at this time. Nice to see that another way point I marked with my Garmin exactly agrees with the POI placed on the map by another user.</p>
</div>
<div id="comment-7372-info" class="comment-info">
<span class="comment-age">(28 Aug '11, 10:53)</span> <span class="comment-user userinfo">flightmaker</span>
</div>
</div>
</div>
<div id="comment-tools-7242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7242-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65113"></span>

<div id="answer-container-65113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With JOSM, which is the best editor, you can relocate any existing node with JOSM&gt;Tools&gt;Move Node</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '18, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/6abea2df2074c337b7ef787d1cc80028?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A_Pirard&#39;s gravatar image" />
<p><span>A_Pirard</span><br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A_Pirard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65113" class="comments-container">
&#10;</div>
<div id="comment-tools-65113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65113-form-container" class="comment-form-container">
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

