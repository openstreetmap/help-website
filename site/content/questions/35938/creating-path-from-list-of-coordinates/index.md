+++
type = "question"
title = "Creating path from list of coordinates"
description = '''Is there any way to create paths from a list of coordinates directly, through editing the XML files, or otherwise? The KML data in rowmaps, contains public rights of way info and is released under the OS OpenData Licence. This path, for example, is assigned coordinate data {-1.92871,53.35826; -1.928...'''
date = "2014-08-18T07:37:00Z"
lastmod = "2014-08-19T06:59:00Z"
weight = 35938
keywords = [ "editing", "list", "coordinates" ]
aliases = [ "/questions/35938" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Creating path from list of coordinates](/questions/35938/creating-path-from-list-of-coordinates)

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
<span id="post-35938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35938-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way to create paths from a list of coordinates directly, through editing the XML files, or otherwise? The KML data in <a href="http://www.rowmaps.com/kmls/DY/">rowmaps</a>, contains public rights of way info and is released under the OS OpenData Licence. <a href="http://www.openstreetmap.org/way/8045826">This path</a>, for example, is assigned coordinate data {-1.92871,53.35826; -1.92859,53.35825; -1.92848,53.35821; -1.92834,53.35814; -1.92792,53.35784 -1.92787,53.35780;} in the KML file.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '14, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a56aacf4d1e927dcd675dfc85cb7e992?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="u003f&#39;s gravatar image" />
<p><span>u003f</span><br />
<span class="score" title="351 reputation points">351</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="u003f has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '14, 01:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35938" class="comments-container">
&#10;</div>
<div id="comment-tools-35938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35938-form-container" class="comment-form-container">
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

<span id="35975"></span>

<div id="answer-container-35975" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35975-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="u003f has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All copyright issues aside (but please be sure ...) and all ignoring the downsides of not surveying (if that would happen) …</p>
<p>… one simple option (without a intermediate KML step) to convert a <em>list of coordinates into a way</em> is to use the "Lat Lon Tool" (ctrl+shift+L) of the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/utilsplugin2">JOSM utilsplugin2</a>:</p>
<p>In the case of the example list above some preparation is needed:</p>
<ul>
<li>You would just need to convert the ";" into newlines as this tool expects each point in a new line (for example in a <span>text editor</span> find "<code>;</code>" replace by the escape sequence or regular expression "<code>\n</code>").</li>
<li>And it seems that you need to swap the coordinates (or append N and W)(e.g. by regular expression replacement ("<code>[^,]*),(.*$)</code>" → "<code>\2,\1</code>").</li>
</ul>
<p>Paste into the JOSM tool, select "way" and done.</p>
<p>The are likely many many more options. For example if you would do some simple scripting to create a OSM XML file manually.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '14, 00:59</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '14, 16:29</strong> </span></p>
</div>
</div>
<div id="comments-container-35975" class="comments-container">
&#10;</div>
<div id="comment-tools-35975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35975-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35940"></span>

<div id="answer-container-35940" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35940-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Given that you cannot use the data due to the license in the first place it doesn't seem to be a sensible question at this point in time, but yes, naturally it is possible to convert a list of coordinates to a way. However what you are proposing is an import, and you need to follow <a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines">http://wiki.openstreetmap.org/wiki/Import/Guidelines</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '14, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '14, 08:53</strong> </span></p>
</div>
</div>
<div id="comments-container-35940" class="comments-container">
<span id="35958"></span>
<div id="comment-35958" class="comment">
<div id="post-35958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Simon. No I don't think an import isn't what I would have wanted, I meant editing on a path-by-path basis. Whilst not applicable for this data, is there a guide for how to add a way using a coordinate list? Thus far, my edits have been high-level point-and-click, but would be more comfortable with a lower-level approach.</p>
</div>
<div id="comment-35958-info" class="comment-info">
<span class="comment-age">(18 Aug '14, 16:58)</span> <span class="comment-user userinfo">u003f</span>
</div>
</div>
<span id="35959"></span>
<div id="comment-35959" class="comment">
<div id="post-35959-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You seem to hinted that you have the list in kml format? If yes you can create gpx tracks from the data and trace them or potentially convert directly to an OSM way.</p>
<p>As SK53 has pointed out surveying by actually walking/whatever is better, not the least because then you can collect so much more additional information which in the end makes the difference between OSM and other sources.</p>
</div>
<div id="comment-35959-info" class="comment-info">
<span class="comment-age">(18 Aug '14, 18:25)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35940-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35981"></span>

<div id="answer-container-35981" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35981-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Potlatch 2 allows you to open a KML file as a <a href="http://wiki.openstreetmap.org/wiki/Potlatch_2/vector_background_layers">vector background layer</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '14, 06:59</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-35981" class="comments-container">
&#10;</div>
<div id="comment-tools-35981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35981-form-container" class="comment-form-container">
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

