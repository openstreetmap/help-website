+++
type = "question"
title = "OSM on iOS for Nepal"
description = '''Hi! I am working on an app ( https://github.com/maxvonhippel/Chetawani ) designed to deliver useful OSM information and accurate news to people in Nepal. I have no idea how to parse OSM data (I have been told it is an XML format?) to an MKMapView and at the moment am just presenting the map itself a...'''
date = "2015-04-28T19:43:00Z"
lastmod = "2015-04-28T20:54:00Z"
weight = 42648
keywords = [ "xml", "xcode", "ios", "notes", "iphone" ]
aliases = [ "/questions/42648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM on iOS for Nepal](/questions/42648/osm-on-ios-for-nepal)

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
<span id="post-42648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42648-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am working on an app ( <a href="https://github.com/maxvonhippel/Chetawani">https://github.com/maxvonhippel/Chetawani</a> ) designed to deliver useful OSM information and accurate news to people in Nepal. I have no idea how to parse OSM data (I have been told it is an XML format?) to an MKMapView and at the moment am just presenting the map itself as a web view. Anyone have any suggestions RE how I could get the XML data, refreshing regularly, and present it as an overlay on my map? Just looking for a point in the right direction, not full code or anything. Thanks!</p>
<p>EDIT: To be more specific, I want to overlay date from <a href="https://www.openstreetmap.org/relation/184633#map=10/27.7042/85.5581&amp;layers=HN">THIS</a> map onto an MKMapView. Yes there is an Open Street Map app, but I am trying to make an app which has a toolset of different features for aid workers in Nepal, including but not limited to the map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-xcode" rel="tag" title="see questions tagged &#39;xcode&#39;">xcode</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span> <span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '15, 19:43</strong></p>
<img src="https://secure.gravatar.com/avatar/25a5030413189c7d62561085191fe966?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaxvH&#39;s gravatar image" />
<p><span>MaxvH</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaxvH has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '15, 20:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42648" class="comments-container">
<span id="42649"></span>
<div id="comment-42649" class="comment">
<div id="post-42649-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>could you please describe your idea in more words? What do you mean with "overlay on my map"? You want to overlay OSM data (which? all?) on your map (which map? based on which data?)? Isn't there already a useful <span>iOS OSM app</span>?</p>
</div>
<div id="comment-42649-info" class="comment-info">
<span class="comment-age">(28 Apr '15, 20:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42650"></span>
<div id="comment-42650" class="comment">
<div id="post-42650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to overlay this data: <a href="https://www.openstreetmap.org/relation/184633#map=10/27.7042/85.5581&amp;layers=HN">https://www.openstreetmap.org/relation/184633#map=10/27.7042/85.5581&amp;layers=HN</a> Including pins and the info you get when you tap on a pin, onto an MKMapView for iOS for on and offline use (refreshes when online). Yes there is an app but I am making something else- including access to the OSM humanitarian map of Nepal is just a feature of my project.</p>
</div>
<div id="comment-42650-info" class="comment-info">
<span class="comment-age">(28 Apr '15, 20:16)</span> <span class="comment-user userinfo">MaxvH</span>
</div>
</div>
<span id="42651"></span>
<div id="comment-42651" class="comment">
<div id="post-42651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, thanks for the addition. Sorry, still not clear to me. And what do you mean by "date from THIS map"? The map in total? Okay, you say "the map itself as a web view", which means that you have this map (the Humanitarian map) already? But, what else? Offline? Or do you want to render an own map like the Humanitarian map?</p>
<p>Okay, do you only want the notes (the markers/pins)?</p>
</div>
<div id="comment-42651-info" class="comment-info">
<span class="comment-age">(28 Apr '15, 20:20)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42653"></span>
<div id="comment-42653" class="comment">
<div id="post-42653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hhaha let me further clarify :) I want to take the pins from the humanitarian map, with their notes, and parse them and present them on an MKMapView. So for example, there is a note on the web map that says something like"bridge destroyed, under construction" and has the date and name of poster. I'd like to have a pin on my map that, when tapped, presents a little popup with that information. So the problem is parsing the humanitarian notes people put up and presenting them natively on iOS on a map view. Also to be clear I only want the map of the region shown in my link.</p>
</div>
<div id="comment-42653-info" class="comment-info">
<span class="comment-age">(28 Apr '15, 20:24)</span> <span class="comment-user userinfo">MaxvH</span>
</div>
</div>
<span id="42654"></span>
<div id="comment-42654" class="comment">
<div id="post-42654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>okay, thanks. :-) I hope we get to some good understanding in the end. See my answer below how to get the "notes". I am myself not aware of MKMapView, maybe others can help here more, after all that clarification.</p>
</div>
<div id="comment-42654-info" class="comment-info">
<span class="comment-age">(28 Apr '15, 20:28)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42655"></span>
<div id="comment-42655" class="comment not_top_scorer">
<div id="post-42655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thanks! I will take a look at your links tonight and see what I can do. MKMapView is just the map view Apple provides in Xcode for iOS :)</p>
</div>
<div id="comment-42655-info" class="comment-info">
<span class="comment-age">(28 Apr '15, 20:29)</span> <span class="comment-user userinfo">MaxvH</span>
</div>
</div>
</div>
<div id="comment-tools-42648" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-42648-form-container" class="comment-form-container">
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

<span id="42652"></span>

<div id="answer-container-42652" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42652-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is the basis of all OSM-based maps: <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">https://wiki.openstreetmap.org/wiki/Planet.osm</a> - one representation is in a XML format, yes. Maps get <a href="https://wiki.openstreetmap.org/wiki/Rendering">rendered</a> from this data, also the "Humanitarian" map. If you want only data for a class of features <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> is often used.</p>
<p>For info on the OSM notes (the markers in your links, <em>what you seem to want</em>) see <a href="https://wiki.openstreetmap.org/wiki/Notes">https://wiki.openstreetmap.org/wiki/Notes</a> (there is an API and a download option similar to the planet). Note that those "OSM notes" are not "humanitarian notes".</p>
<p>Also see <a href="https://wiki.openstreetmap.org/wiki/About">https://wiki.openstreetmap.org/wiki/About</a> in general.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '15, 20:22</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '15, 20:42</strong> </span></p>
</div>
</div>
<div id="comments-container-42652" class="comments-container">
<span id="42656"></span>
<div id="comment-42656" class="comment">
<div id="post-42656-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want OSM notes you might find <a href="https://github.com/SomeoneElseOSM/Notes01">https://github.com/SomeoneElseOSM/Notes01</a> useful. It's designed to produce a GPX file that a Garmin can read, but I suspect many other platforms could read the GPX files it produces too (or they could be converted using something like GPSBabel).</p>
</div>
<div id="comment-42656-info" class="comment-info">
<span class="comment-age">(28 Apr '15, 20:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42652-form-container" class="comment-form-container">
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

