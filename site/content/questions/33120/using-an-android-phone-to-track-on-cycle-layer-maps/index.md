+++
type = "question"
title = "Using an Android phone to track on Cycle Layer maps"
description = '''An going to Turkey and want to walk around hills. No local maps - best I can find is the cycle layer OSM map, so I an to download the cycle layer map from OSM and then be able to see my GPS position on my Galaxy S Mini. Every App I try has no cycle layer maps or the ability for me to load up my own ...'''
date = "2014-05-12T19:26:00Z"
lastmod = "2014-05-12T22:35:00Z"
weight = 33120
keywords = [ "android", "cyclelayer", "offlinemap" ]
aliases = [ "/questions/33120" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using an Android phone to track on Cycle Layer maps](/questions/33120/using-an-android-phone-to-track-on-cycle-layer-maps)

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
<span id="post-33120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33120-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>An going to Turkey and want to walk around hills. No local maps - best I can find is the cycle layer OSM map, so I an to download the cycle layer map from OSM and then be able to see my GPS position on my Galaxy S Mini. Every App I try has no cycle layer maps or the ability for me to load up my own OSM export. What App can I use?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-cyclelayer" rel="tag" title="see questions tagged &#39;cyclelayer&#39;">cyclelayer</span> <span class="post-tag tag-link-offlinemap" rel="tag" title="see questions tagged &#39;offlinemap&#39;">offlinemap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '14, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a1d64ea66c4eb0254484a073000dea12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stretchcj&#39;s gravatar image" />
<p><span>stretchcj</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stretchcj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33120" class="comments-container">
<span id="33121"></span>
<div id="comment-33121" class="comment">
<div id="post-33121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I understand you correctly you want to bulk download cycle layer tiles. You can't find applications doing this, because the <a href="http://thunderforest.com/terms/">terms of service of the cycle layer</a> don't allow bulk downloading without express written permission beforehand.</p>
</div>
<div id="comment-33121-info" class="comment-info">
<span class="comment-age">(12 May '14, 20:46)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33122"></span>
<div id="comment-33122" class="comment">
<div id="post-33122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's not exactly what I wanted to do - I only need a very small area and I have already exported the area I need using the export function on the website. What I wanted is an android app which can rende this .osm file and show my position using the phone's GPS.</p>
</div>
<div id="comment-33122-info" class="comment-info">
<span class="comment-age">(12 May '14, 20:52)</span> <span class="comment-user userinfo">stretchcj</span>
</div>
</div>
<span id="33123"></span>
<div id="comment-33123" class="comment">
<div id="post-33123-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is again not very clear to me ;) You talk about the cycle layer (which are pictures) and then you say you have an osm file (which is raw data).</p>
<p>If you have raw data, then you can use several tools from <a href="http://osmand.net/">OsmAnd</a> to <a href="https://code.google.com/p/osmand/wiki/HowToPrepareYourOwnDataToUseOffline">create your own map</a>. You can of course also simply use their offline map of Turkey.</p>
<p>P.S. Have a look at the related questions to the right.</p>
</div>
<div id="comment-33123-info" class="comment-info">
<span class="comment-age">(12 May '14, 21:09)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33124"></span>
<div id="comment-33124" class="comment">
<div id="post-33124-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>OsmAnd can do that. Start with the free version (only 10 map downloads allowed). You should be able to directly load the vector file for Turkey from the app. If not, it is available from <a href="http://download.osmand.net/rawindexes/">http://download.osmand.net/rawindexes/</a> (you'll need to be able to copy the .obf file to the osmand directory on your SD card if you do it manually).</p>
<p>In OsmAnd you can select several renderings including cycle map. If you download the appropriate SRTM files and get the contour module you can display contour levels which I find useful when hiking.</p>
</div>
<div id="comment-33124-info" class="comment-info">
<span class="comment-age">(12 May '14, 21:13)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="33125"></span>
<div id="comment-33125" class="comment not_top_scorer">
<div id="post-33125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cartinus - to be honest I don't know what I have exported - I was displaying the cycle layer map at the time and then clicked the export button and a 4Mb .osm file was created - i assumed that it was a cycle layer map.</p>
<p>stf - I tried OsmAnd and I could only download the country map for Turkey - it only seemed to be a road map - it had no contours (and that plus the tracks is exactly what i wanted). I could only download their maps - not my own. Where can I find the STM files? Where is the Contour Module?</p>
</div>
<div id="comment-33125-info" class="comment-info">
<span class="comment-age">(12 May '14, 21:23)</span> <span class="comment-user userinfo">stretchcj</span>
</div>
</div>
<span id="33126"></span>
<div id="comment-33126" class="comment not_top_scorer">
<div id="post-33126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please go to <a href="https://code.google.com/p/osmand/wiki/HowToArticles">the OsmAnd wiki I linked to before</a> and read the sections: "First Steps in OsmAnd" and "How To Display Contour Lines and Hillshades"</p>
</div>
<div id="comment-33126-info" class="comment-info">
<span class="comment-age">(12 May '14, 21:39)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33127"></span>
<div id="comment-33127" class="comment">
<div id="post-33127-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>stf - - have downloaded OsmAnd and the plug in - plus the Turkey map and the Contour map for Mugla (took a while to figure out which one I needed!), but now can see the area I'll be in with contours and GPS tracking - excellent - many thanks.</p>
</div>
<div id="comment-33127-info" class="comment-info">
<span class="comment-age">(12 May '14, 22:35)</span> <span class="comment-user userinfo">stretchcj</span>
</div>
</div>
</div>
<div id="comment-tools-33120" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33120-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

