+++
type = "question"
title = "GPSMid, changing language of Israel map?"
description = '''Hello, i have installed GPSMid with a map of Israel on my phone (Nokia N78). As far as i don&#x27;t speak (and can&#x27;t even read much) Hebrew, i would like to change the language of the map to English, like here: http://toolserver.org/~osm/locale/en.html?zoom=9&amp;amp;lat=31.87056&amp;amp;lon=34.9942&amp;amp;layers=B...'''
date = "2011-09-26T21:06:00Z"
lastmod = "2011-09-26T23:33:00Z"
weight = 8160
keywords = [ "internationalization", "map", "gpsmid", "language" ]
aliases = [ "/questions/8160" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [GPSMid, changing language of Israel map?](/questions/8160/gpsmid-changing-language-of-israel-map)

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
<span id="post-8160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8160-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i have installed GPSMid with a map of Israel on my phone (Nokia N78). As far as i don't speak (and can't even read much) Hebrew, i would like to change the language of the map to English, like here:</p>
<p><a href="http://toolserver.org/~osm/locale/en.html?zoom=9&amp;lat=31.87056&amp;lon=34.9942&amp;layers=BT">http://toolserver.org/~osm/locale/en.html?zoom=9&amp;lat=31.87056&amp;lon=34.9942&amp;layers=BT</a></p>
<p>In the maps XML source, the english tags are existent, but by default, GPSMid only shows Hebrew tags.</p>
<p>How can i switch to english tags?</p>
<p>Thank you, barny</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-internationalization" rel="tag" title="see questions tagged &#39;internationalization&#39;">internationalization</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-gpsmid" rel="tag" title="see questions tagged &#39;gpsmid&#39;">gpsmid</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '11, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/cca17c3aa60dfbe668405c9c687f8fb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barny2507&#39;s gravatar image" />
<p><span>barny2507</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barny2507 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8160" class="comments-container">
&#10;</div>
<div id="comment-tools-8160" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8160-form-container" class="comment-form-container">
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

<span id="8162"></span>

<div id="answer-container-8162" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8162-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="barny2507 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To change the language, you need to use OSM2GpsMid to build a GpsMid midlet yourself, using a customised style file. See the page on the GpsMid wiki for <a href="http://sourceforge.net/apps/mediawiki/gpsmid/index.php?title=Style-File_Documentation">Style-File Documentation</a>.</p>
<p>Basically, you can get a copy of the default GpsMid style, then open it in a text editor. The name for each object is set with the <code>namekey</code> tag. In the standard style, this will be something like <code>&lt;namekey tag = "name"/&gt;</code>, which means it will use the <code>name</code> tag from the OSM data, ie the default/local name. To change this to use English language names, you will have to change it to <code>&lt;namekey tag = "name:en"/&gt;</code>. So you can use the find and replace in your text editor to change all of these. You may also want to specify something for the <code>namefallback</code> tag, so it will just display the default name if the object isn't tagged with an English language name.</p>
<p>You then you have to modify your OSM2GpsMid properties file to tell it to use your modified style file. See <a href="http://sourceforge.net/apps/mediawiki/gpsmid/index.php?title=Properties_file">Properties file</a>. Basically add line that says something like <code>style-file = mystyle.xml</code>. Or just use the OSM2GpsMid GUI, and choose the option for "Load custom style file"</p>
<p>Then run OSM2GpsMid, using the GUI if you want, see instructions at <a href="http://sourceforge.net/apps/mediawiki/gpsmid/index.php?title=Getting_started">Getting started</a>. And use it to produce your midlet, which you can then load onto your phone. And you should have a map with English language names.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '11, 23:33</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-8162" class="comments-container">
&#10;</div>
<div id="comment-tools-8162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8162-form-container" class="comment-form-container">
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

